# ⚖️ Cipher Court: Escape to Justice

[![Unity](https://img.shields.io/badge/Unity-6000.3.21f1%20LTS-black?logo=unity)](https://unity.com/)
[![Render Pipeline](https://img.shields.io/badge/Render%20Pipeline-URP-blue)](https://unity.com/srp/universal-render-pipeline)
[![Backend](https://img.shields.io/badge/Backend-FastAPI%20%2F%20SQLite%203-green?logo=python)](https://fastapi.tiangolo.com/)
[![Platform](https://img.shields.io/badge/Platform-Windows%20x64%20%7C%20WebGL-red)](https://github.com/)

**Cipher Court: Escape to Justice** is an advanced 3D first-person forensic investigation, cryptographic puzzle, and escape-room video game developed using **Unity 6 (6000.3.21f1 LTS)** and the **Universal Render Pipeline (URP)** with a persistent **Python event logging & telemetry backend**.

---

## 🏛️ Project Overview

Players step into the shoes of a forensic legal investigator unraveling a high-stakes judicial conspiracy across 6 interconnected investigation rooms:

1. **Level 1 — Investigation Office:** Caesar cipher cryptanalysis on a confidential case dossier (`JUSTICE`).
2. **Level 2 — Cyber Security Hub:** Hardware USB drive inspection and terminal authentication (`COURT2026`).
3. **Level 3 — Forensic Evidence Vault:** Crime scene evidence markers and combination safe cracking (`472`).
4. **Level 4 — Underground Archive:** Chronological library query and date-coded archive retrieval (`427`).
5. **Level 5 — Case Files & Affidavits:** Witness deposition cross-examination and contradiction detection (`315`).
6. **Level 6 — Grand Courtroom / Final Verdict:** Perjury detection under oath, elevated judge platform confrontation, and dynamic escape door routing (Option `2`).

---

## 📁 Repository Structure

```
├── Assets/                      # Unity Source Assets, Models, Prefabs & Textures
│   ├── Editor/                  # Editor scripts (Build tools, Visual polishers)
│   ├── Scenes/                  # All 8 core gameplay scenes (MainMenu to Level 6)
│   ├── Scrpits/                 # C# Gameplay, Player, UI & Telemetry Scripts
│   │   ├── Core/                # GameManager singleton lifecycle
│   │   ├── Interaction/         # Interactive clues, flash drives, markers
│   │   ├── Player/              # Character controller & mouse look
│   │   ├── Puzzle/              # Cryptographic puzzle engines
│   │   ├── Systems/             # CipherCourtDatabase telemetry, timers, exits
│   │   └── UI/                  # Menus, overlays, and keypad displays
│   └── Settings/                # URP Graphics & Volume profiles
├── Backend/                     # Dual-Mode Telemetry & Audit Web Server
│   ├── main.py                  # FastAPI + PostgreSQL production API
│   ├── server.py                # Zero-dependency multi-threaded SQLite server & live dashboard
│   ├── schema.sql               # Database schema definition
│   ├── requirements.txt         # Python dependencies
│   ├── Dockerfile               # Container deployment configuration
│   └── docker-compose.yml       # Multi-service container stack
├── Packages/                    # Unity Package Manager manifest & lock
├── ProjectSettings/             # Unity project, tag, input, and build configurations
├── Builds/                      # Compiled release executables
│   ├── CipherCourt_Windows_x64/ # Native Windows 64-bit Standalone (.exe)
│   └── CipherCourt_WebGL/       # HTML5 / WebAssembly browser build
├── DEPLOYMENT_GUIDE.md          # Complete deployment, build & architecture manual
├── Play_CipherCourt.bat         # 1-click standalone desktop launcher
├── Play_With_Backend.bat        # 1-click game + backend + dashboard launcher
└── Launch_Online_WebGL.bat      # 1-click WebGL server & global tunnel launcher
```

---

## 🚀 Quick Start

### 1. Play Standalone (Windows 64-bit)
Double-click `Play_With_Backend.bat` or `Play_CipherCourt.bat` in the root folder, or run:
```cmd
Builds\CipherCourt_Windows_x64\CipherCourt.exe
```

### 2. Run the Telemetry Server & Dashboard
```cmd
cd Backend
python server.py
```
Open **[http://127.0.0.1:8000](http://127.0.0.1:8000)** in your browser for the real-time audit log dashboard.

### 3. Open in Unity Editor
- Requires **Unity 6 (6000.3.21f1 LTS)** with Universal Render Pipeline (URP).
- Open **Unity Hub** -> **Add project from disk** -> Select this repository folder.

---

## ⌨️ Controls & In-Game Telemetry

- **W, A, S, D:** Movement
- **Mouse:** 360° First-Person Camera
- **Left Click:** Inspect dossiers, examine evidence, interact with keypads
- **F1 Key:** Toggle the in-engine Live Telemetry & Database HUD overlay

---

## 📜 Academic Attribution

- **Author / Candidate:** Sahil Kate (CS-9012)
- **Degree:** Bachelor of Technology (B.Tech) in Computer Science & Engineering
- **Dissertation Documentation:** Comprehensive 70+ page report and test matrix included in root.
