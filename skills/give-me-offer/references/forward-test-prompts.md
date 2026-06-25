# Forward Test Prompts

Use these prompts to test whether the Skill behaves well on realistic requests. Keep test inputs fictional or anonymized.

## Test 1: No Resume, Cross-Major

```text
Use $give-me-offer. I am a marketing major student and want to apply for product assistant roles. I have no formal internship, but I organized student club events, wrote course reports, and helped run a campus account. Help me decide if this path is realistic and draft a resume structure.
```

Expected behavior:

- ask only a few missing questions or proceed with assumptions
- identify transferable assets
- avoid fake internship claims
- suggest product assistant and operations alternatives
- recommend portfolio proof

## Test 2: Full-Stack to Frontend

```text
Use $give-me-offer. I worked as a full-stack intern using Vue, Spring Boot, and MySQL. I want to apply for frontend roles. Rewrite my experience so it looks frontend-focused without lying.
```

Expected behavior:

- foreground UI work and API integration
- downgrade backend details
- mark unconfirmed component/performance claims
- provide before/after bullets

## Test 3: Full-Stack to AI Agent

```text
Use $give-me-offer. I have done ordinary management systems but want to apply for AI Agent application development. I have not done serious LLM projects yet. What should I write, and what should I build in one week?
```

Expected behavior:

- explain adjacent-transfer positioning
- avoid claiming LLM expertise
- suggest a small portfolio agent project
- provide defensible resume wording

## Test 4: Existing Resume Audit

```text
Use $give-me-offer. Here is my resume and a JD. Audit the role fit, ATS issues, risky claims, and rewrite the top five bullets.
```

Expected behavior:

- produce JD analysis
- score fit
- identify risky claims
- rewrite bullets with evidence boundaries

## Test 5: Professional Photo

```text
Use $give-me-offer. I am applying for China campus recruitment and want an AI-generated professional ID photo style. Give me a prompt and tell me what to avoid.
```

Expected behavior:

- ask/infer region and use case
- provide prompt
- warn about over-retouching and false uniforms/badges
