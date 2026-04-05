---
name: buddy
description: >
  Dev server launcher for Claude Code. Use this skill whenever the user wants to
  start, detect, or manage dev servers in their project. Triggers on: "/buddy",
  "start my dev server", "run the app", "launch the frontend/backend", "start
  development", "boot up the project", "get the servers running", or any request
  to start, detect, or configure local development servers. Also triggers when
  the user asks what servers are available or how to run the project.
---

# Buddy — Dev Server Launcher

Your job is to detect the project's dev servers, maintain `.claude/launch.json` as a persistent config, and start whichever servers the user wants using `preview_start`.

## Step 1: Detect dev servers

Scan the project root for these files (read them if they exist):

| File | What to look for |
|------|-----------------|
| `package.json` | `scripts` field — look for `dev`, `start`, `serve`, `preview`, and any script that runs a server |
| `Makefile` | Targets like `dev`, `run`, `serve`, `start` |
| `Procfile` | Each line is a named process (e.g. `web: node server.js`) |
| `docker-compose.yml` / `docker-compose.yaml` | Each service with a `ports` mapping |
| `vite.config.*` | Implies `npm run dev` / `vite` on port 5173 |
| `next.config.*` | Implies `npm run dev` / `next dev` on port 3000 |
| `nuxt.config.*` | Implies `npm run dev` / `nuxt dev` on port 3000 |
| `manage.py` | Django — implies `python manage.py runserver` on port 8000 |
| `pyproject.toml` / `requirements.txt` | May contain FastAPI/Flask/uvicorn hints |
| `Cargo.toml` | Rust — look for `[[bin]]` with serve/axum/actix hints |
| `go.mod` | Go — may imply `go run .` |

For each detected server, extract or infer:
- **name**: a short human-readable label (e.g. "Frontend", "API", "Django")
- **runtimeExecutable**: the bare command (`npm`, `yarn`, `python`, `node`, `go`, `cargo`, etc.)
- **runtimeArgs**: the arguments as an array (e.g. `["run", "dev"]`, `["manage.py", "runserver"]`)
- **port**: the port number if determinable, otherwise omit or set to `null`

## Step 2: Load and merge `.claude/launch.json`

Check if `.claude/launch.json` exists.

- **If it exists**: read it. Merge newly detected servers into it — keep existing entries unchanged, add new ones that aren't already listed (match by `name` or by `runtimeExecutable` + `runtimeArgs`).
- **If it doesn't exist**: create `.claude` directory if needed, then write a fresh `launch.json`.

Schema:
```json
{
  "version": "0.0.1",
  "configurations": [
    {
      "name": "Frontend",
      "runtimeExecutable": "npm",
      "runtimeArgs": ["run", "dev"],
      "port": 3000
    }
  ]
}
```

If nothing was detected and no `launch.json` exists, ask the user:
> "I couldn't find any server configs automatically. Can you describe your dev servers? (e.g. 'npm run dev on port 3000, and python manage.py runserver on port 8000')"
Then build `launch.json` from their answers.

Always save the final merged config back to `.claude/launch.json`.

## Step 3: Ask which servers to start

Present the available configurations clearly:

```
Found these dev servers:

  1. Frontend   — npm run dev          (port 3000)
  2. API        — python manage.py runserver  (port 8000)

Which would you like to start? (e.g. "1 2", "all", "just the frontend")
```

Wait for the user's response.

## Step 4: Start selected servers

For each server the user selected, call the `preview_start` MCP tool. Pass the configuration fields directly — `name`, `runtimeExecutable`, `runtimeArgs`, and `port` (if set).

After starting, confirm which servers are running and on what ports.

## Tips

- If the user says "all", start everything in `configurations`.
- If a `launch.json` already exists and covers everything, skip straight to Step 3 — no need to re-scan unless the user asks.
- Keep `launch.json` tidy: don't add duplicate entries on repeated runs.
- If `preview_start` isn't available in the current environment, tell the user clearly and show them the commands to run manually instead.
