#!/usr/bin/env python3
"""
自动检查并安装 openai/skills 仓库中新增的 curated skills。
由 auto-update 技能调度，可由 cron automation 定期调用。
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import urllib.error
import urllib.request

# ── 配置 ──────────────────────────────────────────────
DEFAULT_REPO = "openai/skills"
DEFAULT_PATH = "skills/.curated"
DEFAULT_REF = "main"


# ── GitHub API 工具 ───────────────────────────────────
def _github_request(url: str, user_agent: str) -> bytes:
    headers = {"User-Agent": user_agent}
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        headers["Authorization"] = f"token {token}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        return resp.read()


def _github_api_contents_url(repo: str, path: str, ref: str) -> str:
    return f"https://api.github.com/repos/{repo}/contents/{path}?ref={ref}"


# ── 技能操作 ──────────────────────────────────────────
def _codex_home() -> str:
    return os.environ.get("CODEX_HOME", os.path.expanduser("~/.codex"))


def _installed_skills() -> set[str]:
    """返回当前已安装的所有 skill 名称集合（包括 .system 目录）。"""
    root = os.path.join(_codex_home(), "skills")
    if not os.path.isdir(root):
        return set()
    return {name for name in os.listdir(root) if os.path.isdir(os.path.join(root, name))}


def _list_curated_skills(repo: str, path: str, ref: str) -> list[str]:
    """从 GitHub 获取 curated 技能列表。"""
    api_url = _github_api_contents_url(repo, path, ref)
    try:
        payload = _github_request(api_url, "codex-auto-update")
    except urllib.error.HTTPError as exc:
        print(f"[错误] 无法获取技能列表: HTTP {exc.code}", file=sys.stderr)
        return []
    data = json.loads(payload.decode("utf-8"))
    if not isinstance(data, list):
        print("[错误] 技能列表返回格式异常", file=sys.stderr)
        return []
    return sorted(item["name"] for item in data if item.get("type") == "dir")


def _install_skill(skill_name: str) -> bool:
    """安装单个 curated skill。返回 True 表示安装成功。"""
    installer = os.path.join(
        _codex_home(),
        "skills",
        ".system",
        "skill-installer",
        "scripts",
        "install-skill-from-github.py",
    )
    if not os.path.isfile(installer):
        print(f"[错误] 找不到安装脚本: {installer}", file=sys.stderr)
        return False

    result = subprocess.run(
        [
            sys.executable,
            installer,
            "--repo", DEFAULT_REPO,
            "--path", f"{DEFAULT_PATH}/{skill_name}",
        ],
        capture_output=True,
        text=True,
    )
    if result.returncode == 0:
        return True

    # 如果提示"已存在"，也算成功（幂等）
    if "already exists" in result.stderr.lower():
        return True

    print(f"  └─ 安装失败: {result.stderr.strip()}")
    return False


# ── 主逻辑 ────────────────────────────────────────────
def main() -> int:
    print("=" * 54)
    print("  Auto Update - 技能自动更新")
    print("  检查 openai/skills 仓库中的最新 curated skills")
    print("=" * 54)

    # 1. 获取远程技能列表
    print("\n[1/4] 获取 curated 技能列表...")
    curated = _list_curated_skills(DEFAULT_REPO, DEFAULT_PATH, DEFAULT_REF)
    if not curated:
        print("  └─ 未获取到技能列表，退出。")
        return 1
    print(f"  └─ 共发现 {len(curated)} 个 curated skills")

    # 2. 获取已安装列表
    print("\n[2/4] 获取本地已安装技能列表...")
    installed = _installed_skills()
    print(f"  └─ 已安装 {len(installed)} 个技能")

    # 3. 找出需要安装的技能
    print("\n[3/4] 对比并识别新技能...")
    to_install = [s for s in curated if s not in installed]
    if not to_install:
        print("  └─ ✓ 所有 curated skills 已是最新，无需更新。")
        return 0
    print(f"  └─ 发现 {len(to_install)} 个未安装的技能：")
    for name in to_install:
        print(f"      - {name}")

    # 4. 安装
    print("\n[4/4] 开始安装...")
    success_count = 0
    fail_count = 0
    for idx, name in enumerate(to_install, start=1):
        print(f"  [{idx}/{len(to_install)}] 安装: {name}")
        if _install_skill(name):
            print(f"  └─ ✓ 安装成功")
            success_count += 1
        else:
            fail_count += 1

    # 报告
    print("\n" + "=" * 54)
    print("  更新报告")
    print("=" * 54)
    print(f"  ✓ 成功安装: {success_count} 个")
    if fail_count > 0:
        print(f"  ✗ 安装失败: {fail_count} 个")
    print(f"  ℹ 已最新:   {len(curated) - len(to_install)} 个")
    print("=" * 54)

    if fail_count > 0:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
