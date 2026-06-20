# codex-auto-update

## 仓库说明
Codex Auto Update 技能的增强版，额外包含 Claude Code 自定义技能包。

## 目录结构

| 路径 | 说明 |
|------|------|
| `SKILL.md` | Codex 原版 auto-update 技能 |
| `scripts/check_and_install.py` | Codex 版更新脚本 |
| `auto-update-task.xml` | Windows 计划任务配置 |
| `claude-skills/` | Claude Code 自定义技能包 |
| `claude-skills/auto-update/` | Claude Code 版自动更新器 |
| `claude-skills/music-creator/` | AI 辅助音乐创作助手 |
| `claude-skills/zh-code-review/` | 中文代码审查助手 |

## 技能开发规范

- 每个 skill 必须包含 `SKILL.md` + 可选 `plugin.json`
- `SKILL.md` 头部必须包含 `name` 和 `description` 字段
- 中英文双语优先
- 新增技能放在 `claude-skills/<skill-name>/` 目录下

