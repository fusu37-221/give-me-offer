# Career Vault

Use this file when the user has scattered experience, no resume, multiple target roles, or repeated job-search sessions.

## Purpose

Build a reusable inventory of the candidate's real assets. Tailor resumes by selecting and rewriting from this vault instead of inventing new claims.

## Asset Schema

```text
asset_id:
title:
type: education | course | project | internship | work | research | competition | campus | certificate | portfolio
time:
organization:
raw_description:
candidate_role:
actions:
tools:
domain:
outcome:
evidence:
evidence_level: A | B | C | D
target_roles:
transferable_skills:
risk_notes:
confirm_before_use:
```

## Evidence Levels

- **A**: externally verifiable, such as certificate, award page, publication, internship proof, repository, deployed product, transcript, or official record.
- **B**: internally verifiable, such as screenshots, project report, course artifact, presentation, supervisor confirmation, or event record.
- **C**: self-reported but plausible and interview-defensible.
- **D**: weak, vague, or risky. Use only after clarification, or keep out of the resume.

## Vault Workflow

1. Extract all candidate experiences without judging them too early.
2. Normalize each item into the schema.
3. Assign evidence level and target-role relevance.
4. Merge duplicates.
5. For each target role, select the strongest 5-8 assets.
6. Convert selected assets into resume bullets with the evidence boundary.

## Target-Role Asset Selection

Prioritize assets that match:

- target role tasks
- tools and hard skills
- business or research domain
- proof strength
- recentness
- interview defensibility

Downgrade assets that are prestigious but irrelevant.

## Candidate Follow-Up Questions

Ask short questions only for high-value missing facts:

- Was this project deployed, demoed, graded, published, or used by anyone?
- Which part did you personally complete?
- What tools did you actually use hands-on?
- Are there any numbers you can verify?
- Do you have a link, screenshot, report, certificate, or repository?

## Output Format

When helpful, return:

```text
Strongest assets:
Role-specific assets:
Claims needing confirmation:
Assets to omit:
Portfolio gaps:
```
