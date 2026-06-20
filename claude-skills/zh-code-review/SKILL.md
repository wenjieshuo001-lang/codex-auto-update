---
name: zh-code-review
description: "中文代码审查助手 — 用中文进行专业的代码审查，特别适合国内开发团队使用"
metadata:
  version: 1.0.0
  author: "wenjieshuo001-lang"
---

# 中文代码审查 (Zh Code Review)

## 概述

针对中文开发者团队的代码审查 skill。和标准 code-review 不同：

- **中文输出** — 审查报告、建议、评论全部使用中文
- **国内技术栈熟悉** — 对阿里/腾讯/华为云、微信小程序、Vue/React 等国内主流技术栈有深度认知
- **中文命名规范** — 理解拼音命名、中文注释等国内常见实践，并给出改进建议

## 审查维度

每个审查覆盖以下维度：

| 维度 | 说明 |
|------|------|
| 正确性 | 逻辑错误、边界条件、并发问题 |
| 安全性 | SQL注入、XSS、敏感信息泄露 |
| 性能 | 不必要的计算、N+1查询、内存泄漏 |
| 可维护性 | 代码结构、命名、注释质量 |
| 最佳实践 | 是否符合该语言/框架的社区规范 |

## 使用方法

- 单个文件审查：`review this file`
- PR 差异审查：`review these changes`
- 全量项目审查：`review this project`

## 技术栈支持

- 前端: Vue/React/微信小程序/Uni-app
- 后端: Spring Boot/Flask/Django/Express
- 移动端: Flutter/React Native/Android/iOS
- 数据库: MySQL/PostgreSQL/Redis/MongoDB
- 云服务: 阿里云/腾讯云/华为云/AWS

