---
name: security-reviewer
description: >
  Scan the working tree or git diff for hardcoded secrets — API keys, tokens,
  private keys, connection strings, cloud credentials — across common
  providers. Reports file:line with the masked match. Pure Claude Code, no signup.
user-invocable: true
argument-hint: ""
license: Apache-2.0
metadata:
  author: Quality-Max
  version: "1.0"
  category: security
---

# Secret Scan

Catch a leaked credential before it lands in git history. No signup required.

## Prerequisites

- **None.** Pure Claude Code — works in any repo, no MCP required.

## Patterns

| Provider / type     | Signature |
|---------------------|-----------|
| AWS access key      | `AKIA[0-9A-Z]{16}` |
| AWS secret key      | 40-char base64 near `aws_secret` |
| Google API key      | `AIza[0-9A-Za-z\-_]{35}` |
| GitHub token        | `ghp_`, `gho_`, `ghs_`, `github_pat_` |
| Slack token         | `xox[baprs]-` |
| Stripe              | `sk_live_`, `rk_live_` |
| OpenAI / Anthropic  | `sk-`, `sk-ant-` |
| Private key block   | `-----BEGIN (RSA \|EC \|OPENSSH \|PGP )?PRIVATE KEY-----` |
| JWT                 | `eyJ[A-Za-z0-9_-]+\.eyJ[A-Za-z0-9_-]+\.` |
| Connection string   | `(postgres\|mysql\|mongodb(\+srv)?\|redis)://[^ ]*:[^ @]*@` |
| Generic assignment  | `(password\|passwd\|secret\|token\|api[_-]?key)\s*[:=]\s*['"][^'"]{8,}` |

## Triage

- **Real secret** → BLOCKER. Recommend: remove, rotate the credential, move to env/secret store.
- **Placeholder / example** → note as ignored.
- **Already committed** → flag that rotation is needed regardless of removal.

## Output

```
## Secret Scan — git diff (staged + unstaged)

**2 real secrets, 1 placeholder ignored**

### BLOCKER
- `backend/config.py:14` — Stripe live key `sk_l…` hardcoded.
  Rotate it now and load from env.

### Ignored (placeholders)
- `README.md:42` — `api_key = "your-key-here"` — example text.
```
