---
name: give-me-offer
description: Targeted resume, career-positioning, job-transition, recruiter-scan, proof-pack, interview-defense, AI-skill-leveling, and application-material strategy for students, graduate students, cross-major applicants, entry-level candidates, and experienced workers changing roles. Use when the user asks to create, rewrite, tailor, audit, beautify, or translate a resume/CV; match experience to a job description; reposition campus, research, internship, full-stack, frontend, AI agent, product, operations, data, e-commerce, or career-switch experience; produce Chinese or English resumes; review ATS/parser fit; suggest realistic target roles; plan portfolio projects; or generate professional profile-photo guidance. Also trigger on Chinese-language requests about jianli, qiuzhi, xiaozhao, shezhao, tiaocao, zhuanhang, zhuangang, gangwei pipei, runse jianli, meihua jianli, zhengjianzhao, zhiye zhao, or gei wo offer.
---

# Give Me Offer

## Purpose

Help candidates turn real experience into targeted, credible application materials and job-search strategy. Optimize for employability, role fit, ATS readability, interview defensibility, and honest enhancement.

## Operating Principles

1. Start from the candidate's actual experience and target intent.
2. Tailor the resume to the target role instead of making a generic resume.
3. Translate adjacent experience into role language without fabricating credentials.
4. Separate facts, conservative inferences, and user-confirmation-needed claims.
5. Preserve interview defensibility: every bullet should be explainable by the candidate.
6. Default to one-page ATS/parser-friendly resumes for students, graduate students, early-career candidates, and ordinary career switchers unless seniority, academic CV needs, or a required application format calls for more.
7. Keep the candidate's preference primary; suggest hotter or easier-fit roles only as options, not as a forced path.

## Workflow

### 1. Classify the Request

Choose the primary mode:

- **Resume from scratch**: user has experiences but no resume.
- **Resume rewrite**: user has an existing resume.
- **JD tailoring**: user provides a target job description or role.
- **Career switch**: target role differs from major or work history.
- **Role discovery**: user is unsure what to apply for.
- **Photo/profile material**: user wants professional headshot or profile presentation.
- **Review only**: user asks for critique, risk audit, or ATS check.

If essential inputs are missing, proceed with a lightweight intake instead of asking many questions. Ask for the target role/JD, candidate background, and desired language first.

### 2. Build the Experience Inventory

Convert raw history into structured evidence:

```text
Experience:
Context:
Actions:
Tools/skills:
Outcome:
Evidence:
Target-role relevance:
Risk level:
Missing confirmation:
```

For students and cross-major candidates, include courses, course projects, competitions, student work, lab work, volunteer work, clubs, self-study projects, GitHub/portfolio items, internships, part-time work, and capstones.

### 3. Analyze the Target Role

Extract from the JD or target role:

- business domain
- hard skills
- tools/platforms
- soft skills
- seniority signals
- repeated keywords
- must-have vs nice-to-have requirements
- likely screening concerns

When the role is current or trend-sensitive, search the web before making strong claims about the market.

### 4. Choose the Positioning Strategy

Use one:

- **Direct-fit**: candidate already matches the role. Emphasize depth and achievements.
- **Adjacent-transfer**: candidate has related skills. Translate experience into target-role language.
- **Entry-switch**: candidate lacks direct experience. Emphasize learning velocity, adjacent projects, portfolio, and realistic junior positioning.
- **Specialist pivot**: candidate has broad experience and wants narrower positioning, such as full-stack to frontend or full-stack to AI agent.
- **Role-discovery**: compare several realistic target directions.

For role-specific guidance, read `references/role-playbooks.md`. For detailed route patterns across industries, read `references/industry-playbooks.md`.

### 5. Apply the Evidence Boundary

Before writing final bullets, classify each claim:

- **Green**: true and supported. Strengthen directly.
- **Yellow**: reasonable transfer from real experience. Use conservative phrasing.
- **Orange**: plausible but needs user confirmation. Mark as "confirm before use".
- **Red**: do not write. This includes fake degrees, companies, internships, certificates, papers, awards, revenue, user counts, rankings, or production impact.

For detailed rules, read `references/evidence-boundary.md`. When the user has scattered history or multiple targets, build a reusable asset inventory with `references/career-vault.md`.

### 6. Produce the Deliverable

Deliver the artifact the user needs:

- Chinese resume
- English resume
- bilingual resume content
- rewritten bullet list
- JD-match report
- ATS audit
- target-role recommendation matrix
- gap-closing plan
- portfolio project plan
- profile-photo prompt/advice
- channel-specific application snippets
- JD reality check
- final quality-gate checklist
- recruiter scan test
- proof-pack recommendation
- interview-defense plan
- AI skill-level classification

When generating a resume, prefer sections in this order:

```text
Name and Contact
Target Title / Summary (optional, short)
Education
Skills
Experience / Projects / Research
Internship or Work Experience
Leadership / Activities
Awards / Certificates
```

For experienced candidates, place work experience before education unless the education is more relevant.

## Layout Default

For China-facing campus recruitment, graduate recruitment, early-career resumes, and ordinary social recruitment, default to a clean A4 one-page resume. Use a restrained business-document style: single column, strong section hierarchy, compact bullets, conventional headings, limited color, and no decorative charts or skill bars. Allow two pages only for senior specialists, academic CV needs, or applications that explicitly require detailed records.

## Resume Writing Rules

- Write bullets with action, scope, method, and result.
- Use numbers only when supplied or explicitly confirmed.
- Avoid inflated generic words such as "excellent", "strong", "responsible for many", "significantly improved" without evidence.
- Replace weak campus phrasing with work-facing language.
- Keep each bullet concise and scannable.
- Avoid dense tables, text boxes, headers/footers containing key details, and overly decorative layouts for ATS resumes.
- Use role keywords naturally; do not keyword-stuff.
- For English resumes, use direct action verbs and US-friendly formatting when applicable.
- For Chinese resumes, keep the language concrete, compact, and job-market native.

## Career Switch Guidance

When the user's major or prior role is only partly related to the target job:

1. Acknowledge the mismatch internally; do not overexplain it in the resume.
2. Identify transferable skills, adjacent tasks, tools, and domain knowledge.
3. Reorder sections to put target-relevant evidence first.
4. Use "participated in", "supported", "implemented", "built", "analyzed", or "coordinated" according to actual ownership.
5. Recommend one or two fast portfolio projects if the resume lacks proof.
6. Prepare an interview explanation for the transition.

Examples:

- Full-stack to frontend: emphasize UI modules, componentization, state management, API integration, performance, design collaboration.
- Full-stack to AI agent: emphasize workflow automation, API orchestration, data flow, tool invocation, prompt/RAG prototypes, business process understanding.
- Non-CS to operations/product: emphasize user research, content/data analysis, process coordination, communication, and measurable project work.

## Trend Awareness

This skill should evolve with the job market. For hot roles or uncertain trends, search recent job posts or credible labor-market sources before giving trend claims. Use `references/trend-refresh.md` when updating role playbooks or giving market-sensitive advice.

## Profile Photo Guidance

Use `references/profile-photo.md` when the user asks for resume photos, professional headshots, AI-generated ID photos, Chinese resume photos, US-style headshots, or industry-specific image style.

## Reference Routing

- Read `references/evidence-boundary.md` for truthfulness, enhancement, and risk-control decisions.
- Read `references/role-playbooks.md` for target-role repositioning and transition maps.
- Read `references/industry-playbooks.md` for common industry and cross-major routes.
- Read `references/career-vault.md` when turning scattered history into reusable candidate assets.
- Read `references/resume-examples.md` when producing before/after rewrites or needing fictional patterns.
- Read `references/workflow-playbook.md` for intake forms, output formats, and scoring rubrics.
- Read `references/trend-refresh.md` for market-update workflow.
- Read `references/jd-reality-check.md` when the user provides a vague, inflated, AI-heavy, or suspicious JD.
- Read `references/application-channels.md` when adapting resume content for BOSS/direct chat, email, online application fields, LinkedIn, SOE/public-sector forms, or academic CVs.
- Read `references/profile-photo.md` for professional image and photo prompt guidance.
- Read `references/forward-test-prompts.md` only when validating or extending the skill.
- Read `references/layout-standards.md` when creating or auditing resume layout, especially for China-facing resumes.
- Read `references/case-library.md` when needing full fictional cases or stable examples.
- Read `references/recruiter-scan-test.md` when auditing whether a resume survives 3-second, 10-second, and 30-second screening.
- Read `references/proof-pack.md` when a candidate needs portfolio or evidence materials to support a weak resume.
- Read `references/interview-defense.md` after writing strong bullets or aggressive role-tailored claims.
- Read `references/ai-skill-levels.md` before writing AI, AIGC, RAG, or AI Agent claims.
- Read `references/quality-gates.md` before final delivery of a resume, role strategy, or application package.

Use assets in `assets/templates/` only when the user wants a full resume draft in a template-like Markdown structure. Prefer `assets/templates/china-one-page-zh.md` for China-facing one-page resumes.
