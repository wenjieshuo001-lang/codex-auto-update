---
name: auto-update
description: 自动检查并安装 openai/skills 仓库中新增的 curated skills 和 plugins。定期运行可保持技能库最新，自动获取社区新发布的技能。
---

# Auto Update - 自动更新流行技能和插件

## 概述

自动检查 [openai/skills](https://github.com/openai/skills) 仓库的 curated 列表，对比当前已安装的技能，
自动安装所有尚未安装的技能。同时也会检查是否有可用的插件更新。

## 执行流程

1. **获取 curated 技能列表**：调用 GitHub API 获取 `openai/skills` 仓库 `skills/.curated` 目录下的所有技能
2. **对比已安装列表**：读取 `$CODEX_HOME/skills` 目录下的已安装技能
3. **安装新增技能**：使用 skill-installer 的安装脚本安装所有尚未安装的 curated 技能
4. **输出报告**：列出本次新安装的技能

## 使用方式

### 手动运行

在对话中发送 `$auto-update` 即可触发。

### 自动化运行

配合 Codex 自动化系统定时运行，通过 `automation_update` 工具设置每日或每半小时的 cron 任务。

### 报告格式

运行完成后输出：
- 本次新安装的技能列表
- 已是最新的技能列表（已安装且无更新）
- 安装失败的技能及原因
