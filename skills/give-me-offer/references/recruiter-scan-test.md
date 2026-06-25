# Recruiter Scan Test

Use this file when auditing whether a resume can survive fast human screening and AI-assisted initial review.

## Purpose

Recruiters often make an initial keep/reject decision quickly. A strong resume should communicate the candidate's target, baseline fit, and strongest proof within seconds.

## Three-Layer Scan

### 3-second test

The reader should immediately see:

- name and contact path
- target role
- school/degree or current role
- core technical/business direction
- one clear signal of fit

Fail conditions:

- no target role
- decorative header hides core facts
- contact info is buried
- the resume looks like a poster, not a business document

### 10-second test

The reader should quickly find:

- strongest project or internship
- role-relevant skills
- target keywords from the JD
- one concrete outcome or proof
- whether the candidate is campus, entry-level, switcher, or experienced

Fail conditions:

- strongest evidence starts in the lower half of the page
- projects read like class names without actions
- skills are a long unordered pile
- target-role fit is implied but not obvious

### 30-second test

The reader should be able to answer:

- why this candidate may fit the role
- what they personally did
- what evidence supports the claims
- what to ask in the interview

Fail conditions:

- all bullets are generic responsibilities
- claims are impressive but hard to verify
- the resume creates more suspicion than interest

## Output Format

```text
3-second result:
10-second result:
30-second result:
Top scan blockers:
Highest-impact layout fix:
Highest-impact content fix:
Keep/reject risk:
```

## China-Facing One-Page Checks

For campus, graduate, entry-level, and ordinary social recruitment:

- target role appears near the header
- education and skills are easy to locate
- 2 strongest projects/internships appear before weaker activities
- section headings use familiar names
- bullets are compact and aligned
- one accent color at most
- no large self-evaluation block

## Rewrite Priority

If the scan fails, fix in this order:

1. target role and header clarity
2. section order
3. first project/internship bullets
4. skills grouping
5. spacing and visual hierarchy
6. removal of weak or decorative content
