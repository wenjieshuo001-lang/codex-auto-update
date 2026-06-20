---
name: claude-auto-update
description: "Claude Code 版自动技能更新器 — 检查并安装最新的热门 skills 和 plugins，让你的 Claude Code 始终保持最新能力"
metadata:
  source: adapted-from-codex-auto-update
  version: 1.0.0
---

# Claude Code 自动技能更新器

基于 [codex-auto-update](https://github.com/wenjieshuo001-lang/codex-auto-update) 的创意，为 Claude Code 量身打造。

## 功能

- 自动检查 \[[claude-skills|skill-creator]] 社区的最新热门 skills
- 通过 `/plugin marketplace update` 刷新市场索引
- 自动安装新增的官方和社区插件
- 输出详细的更新报告

## 工作流程

1. **刷新市场索引** — 调用 `claude plugin marketplace update` 更新所有已添加市场
2. **获取最新插件列表** — 对比当前已安装的插件
3. **安装新插件** — 自动安装尚未安装的热门插件
4. **生成报告** — 列出新增、已最新、失败的插件

## 使用方法

在 Claude Code 中触发本技能，或通过 `/loop` 定时执行。

## 依赖

- Claude Code 环境
- `gh` CLI (已认证)
- 网络连接

## 相关技能

- [[plugin-dev]] — 创建自己的插件
- [[skill-creator]] — 创建自己的 skill
- [[hookify]] — 自动化钩子

