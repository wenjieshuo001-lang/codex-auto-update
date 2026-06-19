# Codex Auto Update Skill

自动检查并安装 [openai/skills](https://github.com/openai/skills) 仓库中新增的 curated skills。支持手动触发 (`$auto-update`) 和 Windows 计划任务自动运行。

## 功能

- 自动获取 `openai/skills` 仓库的 curated 技能列表
- 对比本地已安装技能，自动安装新增的
- 输出详细的安装报告（成功/失败/已是最新）

## 安装方式

### 方式一：通过 Codex 技能安装目录

```bash
git clone https://github.com/wenjieshuo001-lang/codex-auto-update.git \
  $HOME/.codex/skills/auto-update
```

### 方式二：通过 skill-installer

```bash
python scripts/install-skill-from-github.py \
  --repo wenjieshuo001-lang/codex-auto-update \
  --path .
```

## 使用方法

### 手动运行

在 Codex 对话中输入 `$auto-update` 即可触发检查和安装。

### 自动运行（Windows 计划任务）

仓库附带了计划任务 XML 模板 `auto-update-task.xml`，导入方法：

```bash
schtasks /create /tn "Codex Auto Update Skills" /xml auto-update-task.xml /f
```

任务包含两个触发器：

- **每天 10:00** 定时执行
- **系统空闲超过 15 分钟** 时自动触发

## 技术细节

- 核心脚本：`scripts/check_and_install.py`
- 使用 GitHub API 获取 curated 列表
- 复用 skill-installer 的安装脚本进行安装
- 幂等设计：已安装的技能不会重复安装
