# give-me-offer

`give-me-offer` 是一个面向中文求职者的 Codex Skill，用来帮助学生、研究生、跨专业求职者、转岗者和有一定工作经验的社招候选人，基于真实经历生成更匹配目标岗位的简历和求职材料。

它不是简单的“简历润色模板”，而是一个求职策略 Skill：先分析经历和岗位，再做岗位化表达、证据边界控制、HR 快速扫描、面试防爆和作品集补强建议。

## 适合谁使用

- 没写过简历的本科生、研究生、应届生
- 专业和目标岗位只算“沾边”的跨专业求职者
- 有项目/校园经历但不知道怎么写成岗位语言的人
- 有简历但想针对某个 JD 优化的人
- 全栈转前端、全栈转 AI Agent、科研转企业、文科转运营/产品等转岗者
- 想做一页中文简历、BOSS 直聊开场、网申字段、邮件投递材料的人

## 它能做什么

- 从零整理经历，生成中文/英文/双语简历内容
- 根据目标岗位或 JD 改写简历
- 把校园、科研、课程、社团、实习、项目经历翻译成岗位语言
- 默认生成国内企业更容易阅读的一页 A4 简历
- 检查 ATS/解析友好性和 HR 3 秒/10 秒快速扫描效果
- 识别“AI 包装岗”“销售伪装成产品/运营”“膨胀初级岗”等 JD 风险
- 给出作品集/证明材料补强方案
- 对强 bullet 做面试追问和降级措辞检查
- 对 AI 能力做 L1-L5 分级，避免把“会用 AI 工具”夸成“AI Agent 工程师”
- 给出证件照/职业照风格建议

## 核心原则

真实美化，不造假：

- 真实做过的事情，可以写得更清楚、更职业化
- 相邻经历可以保守转译成岗位语言
- 数字、规模、成果、个人贡献必须能确认
- 不虚构学历、公司、实习、证书、奖项、论文、上线成果、用户数、营收等信息
- 每条强表述都应该能在面试里讲清楚

## 项目结构

```text
skills/give-me-offer/       Codex Skill 本体
docs/                       项目说明、测试报告、发布清单
assets/                     仓库级素材
outputs/                    最终交付物，占位目录
logs/                       项目日志
```

## Skill 本体

可安装的 Skill 位于：

```text
skills/give-me-offer
```

其中：

- `SKILL.md`：Skill 入口和主流程
- `references/`：证据边界、转岗路线、排版标准、JD 检查、面试防爆等细分手册
- `assets/templates/`：一页中文简历、ATS 中文/英文模板
- `scripts/`：轻量检查脚本

## 重要模块

- `references/evidence-boundary.md`：真实美化和禁止造假边界
- `references/career-vault.md`：职业资产库，把零散经历结构化
- `references/layout-standards.md`：国内一页 A4 简历排版标准
- `references/jd-reality-check.md`：JD 真实性和岗位包装识别
- `references/recruiter-scan-test.md`：HR 3 秒/10 秒/30 秒扫描测试
- `references/proof-pack.md`：作品集/证明材料补强方案
- `references/interview-defense.md`：面试追问防爆
- `references/ai-skill-levels.md`：AI 能力分级表达
- `references/application-channels.md`：BOSS、邮件、网申、LinkedIn、国企/公职等投递通道适配
- `references/quality-gates.md`：最终交付质量门

## 当前状态

`0.1.0-draft`：本地可用、已完成核心 Skill 结构和 GitHub 首次发布准备。

后续重点：补更多行业路线、更多完整中文案例、真实新会话触发测试和持续迭代。

## 许可证

MIT License。