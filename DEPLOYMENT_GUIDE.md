# Cipher Court: Escape to Justice — Deployment & Architecture Guide

**Project Title:** Cipher Court – Escape to Justice  
**Engine:** Unity 6 (6000.3.21f1 LTS) | Universal Render Pipeline (URP)  
**Backend:** Python 3 (FastAPI / HTTP Server + SQLite / PostgreSQL)  
**Target Platform:** WebGL (Live Browser Online) + Windows Standalone (x64)  
**Candidate / Author:** Sahil Kate (CS-9012)  

---

## 🌐 0. LIVE ONLINE WEBGL PLAYABLE DEPLOYMENT

The game is compiled to WebGL (WebAssembly / HTML5) and deployed live online over a secure Cloudflare global edge tunnel. Anyone on any browser (Chrome, Edge, Firefox, Safari) on PC, Mac, iPad, or Chromebook can play immediately with zero installation:

- **🌍 Public Live URL:** `https://observed-choice-entry-civilization.trycloudflare.com`
- **🎮 Local Host URL:** `http://localhost:8085`
- **📊 Backend Dashboard:** `http://localhost:8000`
- **1-Click Online Launcher:** Double-click `Launch_Online_WebGL.bat` in the project root.
- **Underlying Scripts:**
  - `serve_webgl.py`: Static HTTP server configured with proper `application/wasm`, `application/octet-stream` MIME types and Cross-Origin isolation headers.
  - `deploy_online.py`: Manages the WebGL server, backend telemetry server, and Cloudflare tunnel daemon.

---

## 1. System Architecture Overview

Cipher Court combines a high-fidelity 3D first-person forensic escape game with a persistent event telemetry backend:

```
┌─────────────────────────────────────────────────────────────┐
│                   CIPHER COURT ARCHITECTURE                 │
└─────────────────────────────────────────────────────────────┘

 [ Player Client (Unity 6 URP x64 Standalone) ]
   │
   ├── Core Systems (GameManager, LevelTimer, LevelExit)
   ├── 6 Forensic Levels & Puzzle Engines (Levels 1 to 6)
   ├── UI & Post-Processing (URP Volume, Glassmorphic HUD)
   └── CipherCourtDatabase Client (Singleton Telemetry)
         │
         ├── Local Persistence: cipher_court_database.json (Disk Cache)
         ├── In-Game Telemetry HUD: Press [F1] anytime during gameplay
         └── Real-Time HTTP Post: JSON Payloads to Backend API
               │
               ▼
 [ Telemetry & Audit Backend (Port 8000) ]
   ├── Choice A: Zero-Dependency SQLite Server (Backend/server.py)
   │     └── Built-in Live Dark-Themed Web Dashboard at http://localhost:8000
   └── Choice B: Production Cloud Stack (Backend/main.py + PostgreSQL)
         └── Containerized via Docker / Docker Compose
```

---

## 2. Standalone Windows x64 Game Deployment

The standalone build produces a fully self-contained directory that requires no Unity installation to play:

### Build Output Directory:
`Builds/CipherCourt_Windows_x64/`
- `CipherCourt.exe` — Main executable
- `UnityPlayer.dll` — Unity 6 runtime engine library
- `CipherCourt_Data/` — Compiled scenes, assets, textures, and bytecode

### Quick Launch Options (Root Directory):
1. **`Play_With_Backend.bat` (Recommended):**  
   Automatically launches the background telemetry server, opens the live audit log dashboard in your default web browser, and launches `CipherCourt.exe`.
2. **`Play_CipherCourt.bat`:**  
   Launches the game standalone. If the backend is not running, the game gracefully caches all events locally without any gameplay interruptions.

### Gameplay Controls:
- **W, A, S, D:** Walk forward, backward, strafe left, strafe right
- **Mouse:** Look around (360° first-person view)
- **Left Mouse Click:** Interact with clues, keypads, and submit answers
- **[F1] Key:** Toggle the in-game Live Database & Event Log Overlay

---

## 3. Backend Deployment

### Option A: Local Zero-Dependency Server (Recommended for Evaluation)
No third-party packages required — uses standard Python libraries (`http.server`, `sqlite3`, `socketserver`):
```cmd
cd Backend
python server.py
```
Or double-click `Backend/run_backend.bat`.  
- **Web Dashboard:** [http://127.0.0.1:8000](http://127.0.0.1:8000)  
- **Health Check:** [http://127.0.0.1:8000/health](http://127.0.0.1:8000/health)  
- **API Endpoint:** `POST /game-events`, `GET /game-events`

### Option B: Docker Container Deployment
Deploy anywhere with Docker in a single command:
```bash
cd Backend
docker compose up -d --build
```

### Option C: Enterprise Cloud Deployment (FastAPI + PostgreSQL)
For hosting on Render, Railway, AWS, or Heroku:
```bash
cd Backend
pip install -r requirements.txt
export DATABASE_URL="postgresql://user:password@host:5432/cipher_court"
python -m uvicorn main:app --host 0.0.0.0 --port 8000
```

---

## 4. End-to-End Investigation Walkthrough & Solutions

| Sector | Scene Name | Forensic Evidence | Puzzle Mechanism | Solution Code | Exit Result |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Level 1** | `Level1_Investigation` | Classified Dossier | Caesar Cipher Shift (+3) | `JUSTICE` | Motor Door opens up |
| **Level 2** | `Level2_Computer` | Hardware USB Flash Drive | Terminal Authentication | `COURT2026` | Security Gate raises |
| **Level 3** | `Level3_Evidence` | Crime Scene Markers A, B, C | Evidence Locker Lock Code | `472` | Vault Door unlocks |
| **Level 4** | `Level4_Archive` | Microfilm Archives 1974/1992 | Chronological Date Query | `427` | Records Gate opens |
| **Level 5** | `Level5_CaseFiles` | Witness Depositions 1, 2, 3 | Cross-Examination Synthesis | `315` | Jury Door unlocks |
| **Level 6** | `Level6_FinalVerdict` | Sworn Testimony Under Oath | Perjury Detection Confrontation | Option `2` | Escape Door unlocks |
| **End** | `GameComplete` | Case Solved Certificate | Telemetry Finalization | — | Final Victory Screen |

---

## 5. Verification Checklist

- [x] All 8 scenes compiled into Standalone Windows 64-bit build.
- [x] Automated batch build script integrated (`CipherCourtBuilder.cs`).
- [x] Dual backend support: SQLite + Web Dashboard and FastAPI + PostgreSQL.
- [x] CORS and multi-threading enabled for telemetry server.
- [x] 1-Click launcher scripts created (`Play_CipherCourt.bat`, `Play_With_Backend.bat`).
- [x] Dockerfile and Docker Compose configurations ready for cloud hosting.
- [x] Full dissertation, Black Book reports, and test execution logs verified.
