# GitHub Publish Checklist

## Current Local State

- Local repository initialized.
- Default branch renamed to `main`.
- Initial commit exists.
- `give-me-offer` installed to the active Codex Skill directory.
- No remote repository is configured yet.
- GitHub CLI (`gh`) was not found locally.

## Recommended Repository Settings

Repository name:

```text
give-me-offer
```

Description:

```text
Codex Skill for targeted resumes, career switching, job-description matching, proof packs, and interview-defensible application materials.
```

Visibility:

```text
Public
```

Topics:

```text
codex-skill resume career job-search ats campus-recruiting career-switch ai-agent
```

## Manual GitHub Steps

1. Open GitHub and create a new repository named `give-me-offer`.
2. Do not initialize with README, license, or `.gitignore`; this repository already has them.
3. Copy the remote URL.
4. In this project directory, run:

```bash
git remote add origin https://github.com/fusu37-221/give-me-offer.git
git push -u origin main
```

## Post-Push Checks

- README renders correctly.
- `skills/give-me-offer/SKILL.md` renders correctly.
- Issue template appears.
- PR template appears.
- License is detected as MIT.
- No personal candidate materials are committed.
- No `__pycache__`, `tmp`, or generated outputs are committed.

## First Release

Suggested tag:

```text
v0.1.0-draft
```

Suggested title:

```text
give-me-offer v0.1.0-draft
```

Use `RELEASE_NOTES.md` as the release body.
