# Release Notes

## 0.1.0-draft

Initial local draft of `give-me-offer`, a Codex Skill for targeted resumes and job-search strategy.

### Added

- Core `give-me-offer` Skill package under `skills/give-me-offer`.
- Evidence-boundary workflow for truthful resume enhancement.
- Career-vault structure for reusable candidate assets.
- China-facing one-page A4 resume layout standard.
- ATS/parser-friendly Chinese and English templates.
- Domestic one-page Chinese resume template.
- Role and industry playbooks for common transitions:
  - full-stack to frontend
  - full-stack to AI Agent / AI application
  - non-CS to product assistant
  - operations/new media/e-commerce
  - research to industry/data/product
  - cross-border e-commerce
- JD reality-check workflow for inflated, vague, AI-washed, or sales-disguised job posts.
- Recruiter 3-second / 10-second / 30-second scan test.
- Proof-pack recommendations for portfolio and evidence building.
- Interview-defense workflow for strong resume bullets.
- AI skill levels from L1 tool user to L5 model/platform specialist.
- Application channel adaptation for PDF, BOSS/direct chat, email, online fields, LinkedIn, SOE/public-sector forms, and academic CVs.
- Quality gates for final resume and application package review.
- Helper scripts:
  - `jd_keyword_extract.py`
  - `resume_checklist.py`
- GitHub community files:
  - `README.md`
  - `CONTRIBUTING.md`
  - `CODE_OF_CONDUCT.md`
  - `GOVERNANCE.md`
  - issue and PR templates

### Validated

- `quick_validate.py` passes for the Skill package.
- Helper scripts compile with Python.
- Forward-test report covers five fictional scenarios.
- Installed copy validated at `C:\Users\15938\.codex\skills\give-me-offer`.

### Known Gaps

- Needs more full industry playbooks before public v1.0.
- Needs new-session verification that `$give-me-offer` appears in the active Skill list.
- Needs remote GitHub repository creation and push.
- GitHub CLI was not found on the local machine during release preparation.
