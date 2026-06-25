# give-me-offer

`give-me-offer` is an open-source Codex Skill for targeted resumes, career positioning, job-transition strategy, and credible application-material generation.

It is designed for students, graduate students, cross-major candidates, entry-level applicants, and experienced workers who want to pivot into a related or hotter role such as frontend, AI application, AI agent, product, operations, data, or industry-specific junior positions.

## What It Does

- Turns real experience into role-specific resume language.
- Rewrites existing resumes for a target JD.
- Helps candidates choose realistic target roles.
- Supports direct-fit, adjacent-transfer, and entry-switch scenarios.
- Maintains an evidence boundary so enhancement does not become fabrication.
- Builds a reusable career-vault inventory from scattered candidate history.
- Provides industry and transition playbooks for common career-switch routes.
- Defaults to clean China-facing one-page A4 resumes for early-career candidates unless context requires otherwise.
- Adds recruiter-scan, proof-pack, interview-defense, and AI-skill-level checks.
- Supports JD reality checks and channel-specific application snippets.
- Suggests portfolio projects and short gap-closing plans.
- Gives profile-photo guidance when the target market uses resume photos.

## Repository Layout

```text
skills/give-me-offer/       Codex Skill package
docs/                       Project notes and design docs
assets/                     Repository-level assets
outputs/                    Final deliverables
logs/                       Project logs
```

## Skill Package

The installable Skill lives in:

```text
skills/give-me-offer
```

The root repository files support GitHub collaboration; the Skill folder itself stays concise so Codex can load it efficiently.

## Included Skill Resources

- `references/career-vault.md`: structured inventory for candidate assets.
- `references/industry-playbooks.md`: common transition routes and positioning patterns.
- `references/resume-examples.md`: fictional before/after rewrite examples.
- `references/forward-test-prompts.md`: prompts for validating future revisions.
- `references/layout-standards.md`: one-page, ATS/parser-friendly, China-facing layout rules.
- `references/case-library.md`: fictional complete cases for common applicant profiles.
- `references/recruiter-scan-test.md`: 3-second, 10-second, and 30-second recruiter scan audit.
- `references/proof-pack.md`: portfolio and evidence materials for weak or switching resumes.
- `references/interview-defense.md`: follow-up question and claim downgrade workflow.
- `references/ai-skill-levels.md`: AI skill expression levels from tool user to model specialist.
- `references/jd-reality-check.md`: detects inflated, vague, AI-washed, or sales-disguised JDs.
- `references/application-channels.md`: adapts content for PDF, BOSS/direct chat, email, online fields, LinkedIn, SOE/public-sector, and academic CVs.
- `references/quality-gates.md`: final truthfulness, fit, scanability, parser, interview, and proof-plan gates.

## Core Philosophy

Enhance honestly:

- Strengthen what is true.
- Translate adjacent experience conservatively.
- Mark uncertain numbers and ownership for confirmation.
- Never invent degrees, employers, internships, certificates, awards, papers, production results, user counts, or revenue.

## Status

Initial scaffold and first working draft.

## License

MIT.
