# SC2 Hatch Timer 🐣

A simple timer for Zerg hatcheries in *StarCraft 2*, featuring a GUI and sound alerts.

---

## 🛠️ Project Setup (What We Did Together)

### 1. **Initial GitHub Repository Setup**
- Created a new repository on GitHub.
- Configured the remote (`origin`) and linked it to the local project.
- Fixed authentication issues (SSH/HTTPS setup).

### 2. **File Management**
- Moved `Timer.py` from `.venv/` to the project root (to avoid ignoring it in Git).
- Added a `.gitignore` file to exclude:
  - Virtual environments (`.venv/`, `venv/`).
  - IDE configurations (`.idea/`, `.vscode/`).
  - Compiled Python files (`__pycache__/`, `*.pyc`).

### 3. **Git Workflow**
- Renamed the default branch from `master` to `main` (modern best practice).
- Added, committed, and pushed `Timer.py` to GitHub:
  ```bash
  git add Timer.py
  git commit -m "Add Timer.py (main script)"
  git push origin main

