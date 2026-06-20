#!/bin/bash
# ============================================================
# Claude Code 自动技能更新器
# 基于 codex-auto-update 思路，适配 Claude Code 生态
# ============================================================

set -euo pipefail

echo "=============================================="
echo "  Claude Code Auto Update - 技能自动更新"
echo "=============================================="

# 配置
MARKETPLACES=(
  "claude-plugins-official"
  "agent-toolkit"
  "claude-code-workflows"
  "oaustegard-claude-skills"
  "neurofoo-agent-skills"
  "sorawit-w"
)

# 1. 更新市场索引
echo ""
echo "[1/4] 刷新市场索引..."
for mp in "${MARKETPLACES[@]}"; do
  echo "  └─ 更新: $mp"
  claude plugin marketplace update "$mp" 2>/dev/null || true
done
echo "  └─ ✓ 市场索引已刷新"

# 2. 获取已安装列表
echo ""
echo "[2/4] 获取当前已安装插件..."
INSTALLED=$(claude plugin list 2>/dev/null | grep -c "enabled" || echo 0)
echo "  └─ 当前已启用: $INSTALLED 个插件"

# 3. 获取可更新列表
echo ""
echo "[3/4] 检查可用更新..."
UPDATES=$(claude plugin update --check 2>/dev/null || echo "暂无可用更新")
echo "  └─ $UPDATES"

# 4. 安装推荐的官方插件
echo ""
echo "[4/4] 安装推荐插件..."
RECOMMENDED=(
  "code-review@claude-plugins-official"
  "feature-dev@claude-plugins-official"
  "security-guidance@claude-plugins-official"
  "commit-commands@claude-plugins-official"
)
for plugin in "${RECOMMENDED[@]}"; do
  echo "  └─ 安装: $plugin"
  claude plugin install "$plugin" -s user 2>/dev/null || true
done

echo ""
echo "=============================================="
echo "  ✓ 更新完成！"
echo "  使用 /plugin 查看所有已安装插件"
echo "=============================================="

