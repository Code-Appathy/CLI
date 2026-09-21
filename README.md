# UbuntuCLIApp

UbuntuCLIApp is a PC-side support application/project for using Codex comfortably inside an Ubuntu CLI environment running in a container, while operating that environment remotely from a smartphone.

## Current environment

- PC runs an Ubuntu CLI environment inside a container.
- Smartphone remotely operates the Ubuntu CLI using an SSH terminal app.
- Codex is intended to be used from the Ubuntu CLI.
- This repository is the handoff point between smartphone-side planning and PC-side implementation.

## Primary goal

Make Codex in Ubuntu CLI comfortable to use from both PC and smartphone, with minimal friction when sending development instructions, switching projects, and handing work between environments.

## Core concepts

1. **Ubuntu CLI / Codex workspace**
   - Treat the Ubuntu container as the main execution environment.
   - Make starting Codex, selecting a project, checking status, and resuming work simple.

2. **Smartphone-first remote operation**
   - Optimize common operations for an SSH terminal on a smartphone.
   - Reduce long command entry and repetitive typing.
   - Provide short commands, menus, aliases, scripts, or a lightweight web UI where useful.

3. **Project / chat handoff**
   - Allow instructions prepared on the smartphone to be delivered to the Ubuntu CLI/Codex workflow.
   - Investigate integration with other Codex app chats/workspaces on the PC.
   - Prefer direct CLI integration when officially supported; otherwise use safe handoff mechanisms such as files, GitHub, clipboard/queue files, or local APIs.

4. **GitHub as persistent handoff storage**
   - Repository: Code-Appathy/CLI
   - Specifications, implementation notes, setup procedures, and Codex handoff instructions live here.
   - Do not store secrets, tokens, SSH private keys, or machine-specific credentials.

## Initial functional scope

### Phase 1
- Detect/check the Ubuntu CLI environment.
- Check whether Codex is installed and available.
- Start/resume Codex with short smartphone-friendly commands.
- Select a local project/repository.
- Send prepared instruction text to the Codex workflow.
- Show concise status/output suitable for a phone screen.
- Provide setup and recovery commands.

### Phase 2
- Instruction inbox/queue for smartphone -> Ubuntu CLI.
- Project presets and recent-project selection.
- Reusable prompt templates.
- Session/history metadata for handoff.
- Optional lightweight local web UI optimized for smartphone screens.

### Phase 3
- Explore supported integration with the PC Codex app and its other chats/workspaces.
- If direct cross-chat writing is not supported by an official interface, do not depend on UI automation or undocumented internal data. Use a documented handoff layer instead.
- Support two-way handoff where feasible: smartphone -> Ubuntu CLI/Codex and Codex/PC -> smartphone-visible status.

## Architecture direction

```text
Smartphone
  |
  | SSH terminal / future phone web UI
  v
PC
  |
  +-- Ubuntu container
        |
        +-- UbuntuCLIApp helper
        |     +-- command/menu layer
        |     +-- project selector
        |     +-- instruction inbox
        |     +-- status/history
        |
        +-- Codex CLI
              |
              +-- target project repositories

GitHub (Code-Appathy/CLI)
  ^
  |
  +-- specifications / handoff docs / implementation history
```

## Design principles

- Smartphone operation must require as little typing as possible.
- Ubuntu CLI remains usable without the GUI.
- Prefer documented/stable interfaces over screen automation.
- Keep project source repositories separate from the UbuntuCLIApp control layer.
- Commands that modify/delete files or execute dangerous operations must remain explicit.
- Never commit credentials or authentication secrets.

## Open technical investigation

Before implementing direct Codex-app/chat integration, verify what officially supported interfaces are available in the current Codex desktop/CLI environment. The desired UX is to prepare an instruction on the smartphone and send it directly into the appropriate Codex workflow, but the implementation must depend on supported interfaces actually available on the PC.

## Next design steps

1. Inventory the current Ubuntu container, SSH access, Codex CLI installation, and PC Codex app workflow.
2. Define the smartphone -> UbuntuCLIApp command flow.
3. Design the instruction inbox/queue.
4. Define project/session identifiers and handoff format.
5. Investigate supported Codex CLI/desktop integration.
6. Build the minimum CLI helper.
7. Add a smartphone-sized local web UI only where it improves the SSH workflow.
