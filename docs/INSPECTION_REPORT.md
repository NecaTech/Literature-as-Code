# 🕵️ Inspection Report: Literature as Code Framework
**Date**: 2025-12-09
**Auditor**: AntiGravity (Agent)

## 🚨 Critical Findings

### 1. The "Single Source of Truth" is Missing
- **Issue**: `03_MANUSCRIPT/01_drafts/sommaire.md` does not exist.
- **Impact**: `manage.py sync` fails. The Agent (me) cannot track chapter progress (`Draft`, `Review`, `Done`).
- **Fix**: Run `manage.py init` or manually restore `sommaire.md` from `_SYSTEM/defaults/templates/`.

### 2. "Drafting" Automation Gap
- **Issue**: `_SYSTEM/automation/build_chapter.py` exists but is **not exposed** in `manage.py`.
- **Impact**: `HOWTO.md` (UC-04) instructs the user to *manually* copy-paste prompts into an LLM. This breaks the flow and ignores existing automation code.
- **Fix**: Implement `manage.py build` (or `write`) that calls `build_chapter.py`.

### 3. Missing `inspect` Command
- **Issue**: The user ran `/inspect`, but `manage.py inspect` does not verify the system state programmatically.
- **Impact**: Self-correction is currently manual (Agent-driven) rather than System-driven (Script-driven).
- **Fix**: Add `command_inspect` to `manage.py` to check for file existence (`sommaire.md`, templates) and configuration validity.

### 4. Missing Templates
- **Issue**: `HOWTO.md` references `tpl_location.md` as "(à créer)".
- **Fix**: Create `_SYSTEM/defaults/templates/tpl_location.md`.

---

## 🧠 Cognitive Workflow Analysis

The current workflow forces a **Context Switch** that kills creativity:
1.  **Terminal**: `manage.py assemble` (Left Brain / Structure)
2.  **Browser**: Copy Prompt -> Paste to LLM -> Wait -> Copy Result (Friction / Distraction)
3.  **IDE**: Paste to `chXX.md` -> Save (Administrative)
4.  **Terminal**: `manage.py lint` (Left Brain / Critique)

**Proposed "Flow State" Architecture**:
The goal is to stay in the **Creative Console** (IDE/Terminal).
- **New Command**: `manage.py draft ch01 --auto`
    - Assembles context.
    - Sends to LLM API (requires API Key config).
    - Streams text directly into `03_MANUSCRIPT/01_drafts/ch01.md`.
    - Auto-runs Linter.
- **Result**: The author triggers creation and watches the chapter appear, then immediately switches to **Editing** (Right Brain).

---

## 🛠 Recommended Action Plan

### Phase 1: Repair (Immediate)
- [ ] **Restoration**: Re-run logic to generate `sommaire.md`.
- [ ] **Templates**: Create `tpl_location.md`.

### Phase 2: Automation (High Value)
- [ ] **Manage.py**: Expose `build_chapter.py` via `manage.py draft`.
- [ ] **Config**: Add `config.yaml` or `.env` for LLM API keys (needed for automated drafting).

### Phase 3: Consolidate
- [ ] **Self-Diagnostics**: Implement `python manage.py inspect` code-side.

---
**Verification**:
Run `python manage.py init` to see if it restores `sommaire.md` without overwriting existing work, or if we need a specific `repair` command.
