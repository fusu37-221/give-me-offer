# Forward Test Plan

Use this plan before tagging a public release.

## Scope

Test whether `give-me-offer` can handle realistic resume and job-search requests without overclaiming.

## Scenarios

### 1. Cross-Major Student With No Internship

Input:

```text
Marketing major, no internship, campus account, club events, wants product assistant.
```

Expected:

- builds career vault
- positions as product/operations assistant, not product manager
- recommends PRD and competitor analysis proof pack
- produces one-page China-friendly resume structure
- flags weak evidence

### 2. Full-Stack to Frontend

Input:

```text
Vue + Spring Boot + MySQL full-stack internship, wants frontend.
```

Expected:

- foregrounds Vue, UI, components, routing, forms, API integration
- keeps backend as collaboration context
- marks component/performance claims for confirmation
- includes interview-defense questions

### 3. Full-Stack to AI Agent

Input:

```text
Ordinary management-system projects, wants AI Agent job, no real LLM project yet.
```

Expected:

- classifies current AI level as below AI agent engineer
- suggests AI application prototype proof pack
- avoids claiming production AI Agent experience
- writes conservative adjacent-transfer bullets

### 4. Vague AI JD

Input:

```text
JD title says AI product/AI Agent, but tasks mention customer conversion, content, and sales targets.
```

Expected:

- runs JD reality check
- identifies possible AI-washed or sales-disguised role
- recommends questions to ask recruiter
- does not blindly tailor as technical AI role

### 5. China One-Page Layout

Input:

```text
Two-page student resume with self-evaluation, many activities, no target role.
```

Expected:

- compresses to A4 one page
- removes generic self-evaluation
- moves target role and strongest evidence upward
- passes recruiter scan test

## Release Gate

For each scenario, confirm:

- no fabricated credential
- no unsupported metric
- output includes next action
- resume can survive 3-second and 10-second scan
- strongest claims have interview-defense notes
