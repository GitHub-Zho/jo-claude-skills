---
name: writing-chinese-tech-resumes
description: Use when creating, rewriting, tailoring, or visually rebuilding a Chinese technical resume for software, AI, algorithm, research, Agent, LLM, multimodal, AIGC, search, or recommendation roles, especially when source resumes conflict, key technical detail risks being compressed, or DOCX/PDF layout must match a reference.
---

# 中文技术简历生成

## 核心原则

先让事实准确、技术链路完整、阅读层级清楚，再优化篇幅。两页是优先目标，不是内容上限；绝不为了把一条经历压成 1–2 行而删除判断候选人能力所需的方法、机制或结果。

## 工作流

1. 建立事实母表。逐份读取简历、证明材料和用户说明，标记“已验证 / 有冲突 / 待核验”。未经证实的技术栈、指标、奖项和项目性质不得写入。
2. 建立岗位证据映射。按目标岗位排序能力，并将每项能力映射到经历、项目或成果；没有证据时不要堆关键词。
3. 先写完整内容版。使用“任务或问题 → 方法与关键机制 → 可验证结果或工程产出”的结构。复杂项目可使用 2–4 行段落或多条要点，保留模型、数据、流程、系统边界、个人贡献和取舍。
4. 再做相关性删减。优先删除重复、空泛和低相关内容；不得先删关键机制。按 [内容与取舍](references/content-and-selection.md) 执行。
5. 建立视觉系统。若有参考 PDF，先测量页面、版心、字号、颜色、字重、段距和日期坐标，再重建样式。按 [视觉系统](references/visual-system.md) 执行。
6. 生成可编辑 DOCX，并渲染为 PDF/逐页图片。以完整信息块分页，禁止标题孤行和无意义的硬换行。
7. 按 [交付检查](references/qa-checklist.md) 完成内容、视觉、PDF、ATS 和跨页验证后再交付。

## 不可妥协项

- 保持单栏、可选择文本和自然阅读顺序；不要用侧栏、文本框、技能条或图标代替文字。
- 页面安全区优先使用节属性中的真实上下页边距；普通空行不得承担页面留白。只有已确认转换器不遵守页边距时，才为导出副本使用单个、可测量的兼容留白段落。
- 使用真实存在且具备 Regular/Bold 字重的中文字体；不得依赖仿粗体。
- 日期使用固定在正文版心右边界的右对齐制表位，不使用空格或页面最大制表位推齐。
- 中文与英文之间的空格由文本本身控制；生成 DOCX 时关闭 Word 的自动中西文/数字间距。
- 当两页无法同时容纳必要证据与舒适字号时，允许三页；先说明取舍，不得静默删减。
- 所有指标和事实都必须能追溯到来源；冲突信息保留为待确认项。

## 模板资源

- 新建事实母表时复制 [事实母表模板](assets/FACT_PROFILE.template.md)。
- 复刻或新建版式时复制 [视觉档案模板](assets/VISUAL_PROFILE.template.md)。
