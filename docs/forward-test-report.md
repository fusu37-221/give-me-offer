# Forward Test Report

Date: 2026-06-25

Scope: manual forward test of `give-me-offer` v0.1 draft against the five fictional scenarios in `docs/forward-test-plan.md`.

## Summary

Result: pass with minor follow-up recommendations.

The Skill now has enough structure to handle realistic early-career resume work without defaulting to fabrication. The strongest parts are evidence boundaries, one-page China-facing layout, career-switch positioning, proof-pack planning, JD reality checks, and interview-defense routing.

Main remaining risks:

- Role playbooks need more industries before broad public release.
- More complete sample outputs would help contributors understand expected quality.
- Installation into the active Codex skills directory still needs a separate test.
- Real-world user privacy guidance should be made more visible before GitHub release.

## Scenario 1: Cross-Major Student With No Internship

Input:

```text
Marketing major, no internship, campus account, club events, wants product assistant.
```

References expected:

- `career-vault.md`
- `industry-playbooks.md`
- `proof-pack.md`
- `layout-standards.md`
- `quality-gates.md`

Expected output behavior:

- Build a career vault from campus account, club events, and course reports.
- Position the candidate as product/operations assistant, not product manager.
- Recommend PRD, competitive analysis, and user journey map as proof pack.
- Use China one-page resume structure.
- Flag evidence as mostly B/C level unless official records or screenshots exist.

Pass/fail: pass.

Risk controls:

- Do not invent internship.
- Do not write "product manager experience".
- Keep wording to "product/operations assistant candidate" or "entry-level product operations".

Sample safe positioning:

```text
Entry-level product/operations candidate with user research, content operation, event execution, and structured writing experience.
```

## Scenario 2: Full-Stack to Frontend

Input:

```text
Vue + Spring Boot + MySQL full-stack internship, wants frontend.
```

References expected:

- `industry-playbooks.md`
- `resume-examples.md`
- `interview-defense.md`
- `recruiter-scan-test.md`

Expected output behavior:

- Foreground Vue, pages, components, routing, forms, API integration, and frontend states.
- Keep backend as collaboration context.
- Mark component ownership, performance, or quantified impact as confirm-before-use unless provided.
- Add interview-defense questions about personal contribution and frontend depth.

Pass/fail: pass.

Sample safe rewrite:

```text
Developed Vue-based admin pages for user, order, and content modules, including routing, form validation, table views, and API loading/error states; collaborated with backend API definitions to complete end-to-end module delivery.
```

Risk controls:

- Do not claim frontend lead ownership unless confirmed.
- Do not add performance metrics without proof.

## Scenario 3: Full-Stack to AI Agent

Input:

```text
Ordinary management-system projects, wants AI Agent job, no real LLM project yet.
```

References expected:

- `ai-skill-levels.md`
- `proof-pack.md`
- `industry-playbooks.md`
- `interview-defense.md`
- `evidence-boundary.md`

Expected output behavior:

- Classify current AI level as L1-L2 if only tool use, or below L3 if no API/prototype.
- Avoid "AI Agent engineer" claim.
- Suggest a one-week AI application prototype proof pack.
- Write adjacent-transfer bullets around workflow, API orchestration, and business process understanding.

Pass/fail: pass.

Sample safe rewrite:

```text
Built full-stack business modules involving user input, permission control, database records, and API orchestration, providing a foundation for AI workflow automation scenarios.
```

Required next action:

```text
Build a document Q&A or resume-screening prototype with inputs, prompt/tool flow, examples, and limitations before claiming AI application project experience.
```

## Scenario 4: Vague AI JD

Input:

```text
JD title says AI product/AI Agent, but tasks mention customer conversion, content, and sales targets.
```

References expected:

- `jd-reality-check.md`
- `application-channels.md`
- `trend-refresh.md`
- `quality-gates.md`

Expected output behavior:

- Run JD reality check before tailoring.
- Identify possible AI-washed or sales-disguised role.
- Ask recruiter questions about daily outputs and assessment metrics.
- Do not blindly tailor as technical AI role.

Pass/fail: pass.

Script smoke test:

`jd_keyword_extract.py --risks` successfully emitted:

```text
possible_ai_washing
possible_sales_disguised
inflated_junior_role
vague_role
```

Risk controls:

- Tell the user if the role is likely operations/sales with AI branding.
- Tailor only after the user accepts that direction.

## Scenario 5: China One-Page Layout

Input:

```text
Two-page student resume with self-evaluation, many activities, no target role.
```

References expected:

- `layout-standards.md`
- `recruiter-scan-test.md`
- `case-library.md`
- `quality-gates.md`

Expected output behavior:

- Compress to A4 one page by default.
- Add target role near header.
- Remove generic self-evaluation.
- Move strongest project/internship evidence to top half.
- Keep clean single-column layout.

Pass/fail: pass.

Checklist smoke test:

`resume_checklist.py --target china` passed on `assets/templates/china-one-page-zh.md`.

## Issues Found During Testing

1. Windows PowerShell backtick escaping can corrupt Markdown reference links when editing `SKILL.md` through command strings.
   - Fixed by rebuilding the routing block line-by-line using `[char]96`.

2. Python helper output may display Chinese tokens as mojibake in the current Windows terminal.
   - Does not affect risk-signal enum output.
   - Future improvement: add optional JSON output with UTF-8 safe serialization.

3. The current playbooks are strong for CS/product/operations/data/cross-border, but still thin for finance, HR, design, legal/compliance, healthcare, manufacturing, and public-sector candidates.

## Release Readiness

Current readiness:

- Skill structure: pass
- Core references: pass
- Evidence boundary: pass
- One-page layout: pass
- JD risk workflow: pass
- Script smoke tests: pass
- Installation test: not yet done
- GitHub release packaging: not yet done

Recommended next step:

Install/copy `skills/give-me-offer` into the active Codex skills directory and open a new session to verify discovery and trigger behavior.
