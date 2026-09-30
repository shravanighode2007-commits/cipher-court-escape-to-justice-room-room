# ⚖️ Cipher Court: Escape to Justice

[![Unity 6](https://img.shields.io/badge/Unity-6000.3.21f1%20LTS-black?logo=unity)](https://unity.com/)
[![Universal Render Pipeline](https://img.shields.io/badge/Render%20Pipeline-URP-blue)](https://unity.com/)
[![Python Backend](https://img.shields.io/badge/Backend-Python%203.12%20%7C%20FastAPI%20%7C%20SQLite-yellow?logo=python)](https://python.org/)
[![WebGL Live](https://img.shields.io/badge/Deployment-Live%20WebGL%20%7C%20Cloudflare-orange?logo=cloudflare)](https://observed-choice-entry-civilization.trycloudflare.com)
[![Platform](https://img.shields.io/badge/Target-Windows%20x64%20%7C%20WebAssembly-green)](#)

A 3D first-person investigation, forensic evidence synthesis, and courtroom escape experience developed in **Unity 6 LTS (6000.3.21f1)** using the **Universal Render Pipeline (URP)** with a live Python telemetry microservice and SQL audit backend.

---

## 🌐 Live Playable Online Demo

Play directly in your browser with zero installation on PC, Mac, iPad, or Chromebook:
* **🌍 Public Live URL:** [https://observed-choice-entry-civilization.trycloudflare.com](https://observed-choice-entry-civilization.trycloudflare.com)
* **🎮 Local WebGL Host:** `http://localhost:8085`
* **📊 Live Telemetry Dashboard:** `http://localhost:8000`

---

## 🔍 Game Synopsis

In *Cipher Court: Escape to Justice*, the player assumes the role of a forensic legal detective investigating a high-stakes judicial conspiracy. Players traverse 6 sequentially locked, physically-based sectors, gathering physical forensic clues, breaking cryptographic ciphers, and presenting evidence in court under oath:

1. **Level 1 — Crime Scene Investigation:** Search a cordoned office, inspect physical crime scene markers, and retrieve the classified dossier.
2. **Level 2 — Forensic Cyber Terminal:** Discover the hardware USB key and crack the terminal authentication hash (`COURT2026`).
3. **Level 3 — Steganographic Legal Archive:** Operate the antique rotor cipher wheel and decrypt the Caesar shift key (`JUSTICE`).
4. **Level 4 — Underground Archival Records:** Decouple medical examiner timestamps and crack the 3-digit combination safe (`427`).
5. **Level 5 — Sworn Affidavits & Case Files:** Cross-reference financial ledgers, detect invoice discrepancies (`315`), and unlock the courtroom doors.
6. **Level 6 — Grand Courtroom / Final Verdict:** Face the judicial bench, cross-examine sworn witness depositions, detect perjury under oath, and trigger the judicial gavel to escape.
7. **End Stage — Mission Debriefing:** Real-time clearance rating, deduction accuracy metrics, and forensic case summary certificate.

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                   CIPHER COURT ARCHITECTURE                 │
└─────────────────────────────────────────────────────────────┘

 [ Presentation Tier - Unity 6 URP / WebGL ]
   ├── First-Person Locomotion & Raycast Detection (d <= 2.5m)
   ├── 8 Scene Lifecycle Orchestration (MainMenu -> GameComplete)
   ├── Responsive Canvas Scaler (1920x1080, Match = 0.5)
   └── TextMeshPro Multi-Channel SDF Typography Atlases
         │
         ├── GameManager.cs (In-Memory Singleton Lifecycle)
         └── CipherCourtDatabase (JSON Telemetry Client)
               │
               ▼ HTTP POST (JSON Payloads)
 [ Network Ingress & Edge Proxy Tier ]
   ├── High-Performance Static WebGL HTTP Server (Port 8085)
   │     └── Strict MIME Types & Cross-Origin Isolation (COOP / COEP)
   └── Cloudflare Edge Tunnel Daemon (cloudflared.exe, HTTP/2 + TLS)
         │
         ▼
 [ Telemetry & Persistence Backend (Port 8000) ]
   ├── Option A: Zero-Dependency Embedded SQLite Microservice (server.py)
   │     └── Built-in Dark-Themed Live Web Dashboard at http://localhost:8000
   └── Option B: Enterprise Cloud Container Stack (FastAPI + PostgreSQL 15)
```

---

## 🚀 Quick Launch (Windows)

The repository includes convenient 1-click batch scripts in the project root:

| Launcher Script | Action |
| :--- | :--- |
| **`Launch_Online_WebGL.bat`** | Starts WebGL server, backend daemon, and Cloudflare global edge tunnel; opens browser automatically. |
| **`Play_With_Backend.bat`** | Starts the Python telemetry server, opens the live web audit dashboard, and launches `CipherCourt.exe`. |
| **`Play_CipherCourt.bat`** | Launches the standalone desktop game in offline mode (caches telemetry locally to `cipher_court_database.json`). |

---

## 📂 Repository Directory Tree

```text
e:/vyt/
├── Assets/
│   ├── CipherCourtPolish/          # PBR materials, custom shaders, screenshots, and diagrams
│   │   ├── Backgrounds/            # Gameplay interface screenshots
│   │   ├── Materials/              # PBR shaders (Walnut, Marble, Brass)
│   │   └── UploadedDiagrams/       # Official UML, ER, and WBS diagram assets
│   ├── Scenes/                     # All 8 sequential gameplay scenes
│   │   ├── MainMenu.unity          # Level 0: Authentication gateway
│   │   ├── Level1_Investigation.unity # Level 1: Crime scene sleuthing
│   │   ├── Level2_Computer.unity   # Level 2: Cyber forensics terminal
│   │   ├── Level3_Evidence.unity   # Level 3: Steganographic Caesar cipher
│   │   ├── Level4_Archive.unity    # Level 4: Archival safe keypad
│   │   ├── Level5_Statements.unity # Level 5: Sworn affidavits deliberation
│   │   ├── Level6_Courtroom.unity  # Level 6: Grand courtroom verdict
│   │   └── GameComplete.unity      # Level 7: Victory debriefing
│   ├── Scrpits/                    # C# gameplay and system scripts
│   │   ├── Core/                   # GameManager.cs singleton
│   │   ├── Interaction/            # Raycast and item collection scripts
│   │   ├── Player/                 # PlayerMovement.cs and MouseLook.cs
│   │   ├── Puzzle/                 # CipherPuzzle.cs, EvidencePuzzle.cs, Keypads
│   │   ├── Systems/                # LevelTimer.cs, LevelExit.cs, Database.cs
│   │   └── UI/                     # MainMenuManager.cs, GameCompleteManager.cs
│   └── TextMesh Pro/               # SDF typography fonts and assets
├── Backend/                        # Full-stack Python persistence service
│   ├── cipher_court.db             # Local SQLite 3 audit database
│   ├── main.py                     # FastAPI cloud microservice
│   ├── schema.sql                  # PostgreSQL 15 DDL migration script
│   └── server.py                   # Zero-dependency HTTP REST server and dashboard
├── Builds/                         # Output build targets
│   ├── CipherCourt_WebGL/          # WebAssembly / HTML5 production bundle
│   └── CipherCourt_Windows_x64/    # Standalone 64-bit Windows executable
├── cloudflared.exe                 # Cloudflare global edge tunnel daemon
├── deploy_online.py                # 1-Click live online deployment orchestrator
├── serve_webgl.py                  # Static HTTP server with Cross-Origin headers
├── blackbook_builder.py            # Master two-pass dissertation compiler
├── Cipher_Court_Project_Report.docx # Complete 117-page dissertation report
├── Cipher_Court_Project_Report.pdf  # Final compiled dissertation PDF
└── LIVE_URL.txt                    # Auto-generated public Cloudflare live URL
```

---

## 📑 Academic Documentation

Complete academic blackbook dissertation reports generated according to university capstone guidelines:
* **Word Dissertation Document:** [`Cipher_Court_Project_Report.docx`](./Cipher_Court_Project_Report.docx) *(117 Pages)*
* **PDF Dissertation Document:** [`Cipher_Court_Project_Report.pdf`](./Cipher_Court_Project_Report.pdf) *(117 Pages)*

---

## 📜 License & Acknowledgements

Developed as a Major Academic Capstone Project for the Department of Computer Science & Engineering. Built with Unity 6 LTS, Python Software Foundation, and Cloudflare.
