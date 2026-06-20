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
---

# 🎯 Claude Code Skills 扩展包

除了原有的 Codex auto-update 功能外，本仓库还包含了适用于 **Claude Code** 的自定义技能。

## 目录结构

```
claude-skills/
├── auto-update/          # Claude Code 版自动更新器
│   ├── SKILL.md          #  技能定义
│   ├── plugin.json       #  插件清单
│   └── scripts/          #  更新脚本
├── music-creator/        # AI 辅助音乐创作助手
│   └── SKILL.md
└── zh-code-review/       # 中文代码审查助手
    └── SKILL.md
```

## Claude Code 技能说明

### 🔄 claude-auto-update
Claude Code 版自动技能更新器。自动检查并安装最新的热门插件和 skills。

```bash
# 手动触发更新
bash claude-skills/auto-update/scripts/claude-update.sh
```

### 🎵 music-creator
AI 辅助音乐创作助手。用 AI 生成灵感，通过**实质性的手工改编**（改和弦、旋律、歌词、编曲）创作真正的原创作品。

> ⚠️ **原则声明**：本技能坚持"AI 辅助人工创作"，不鼓励将 AI 输出直接冒充原创。

### 📝 zh-code-review
面向国内开发团队的中文代码审查助手。支持 Vue/React/小程序/Spring Boot/Flask 等主流技术栈，审查报告全部使用中文输出。

## 安装 Claude Code 技能

```bash
# 方法1：复制到 Claude Code 技能目录
cp -r claude-skills/* ~/.claude/skills/

# 方法2：通过 CLI 安装具体技能
claude plugin install claude-auto-update@wenjieshuo001-lang
```

## 贡献

欢迎提交 PR 增加更多实用的 Claude Code 技能！请确保：

1. 遵循 `SKILL.md` 标准格式
2. 包含完整的 metadata 头部
3. 中英文双语文档更佳
