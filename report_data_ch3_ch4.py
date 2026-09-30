# Chapter 3 & 4 content for Cipher Court Dissertation
# Complete integration of User-Specified SRS & UML Diagrams
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

def add_chapter_3_and_4(doc, helpers):
    add_ch = helpers['add_chapter_heading']
    add_sec = helpers['add_sec_heading']
    add_subsec = helpers['add_subsec_heading']
    add_p = helpers['add_body_p']
    add_bullet = helpers['add_bullet_p']
    add_code = helpers['add_code_block']
    add_fig = helpers['add_image_figure']
    set_cell_background = helpers['set_cell_background']
    set_cell_margins = helpers['set_cell_margins']
    set_table_borders = helpers['set_table_borders']
    NAVY = helpers['NAVY']
    STEEL = helpers['STEEL']

    # =========================================================================
    # CHAPTER 3: SOFTWARE REQUIREMENTS SPECIFICATION (SRS)
    # =========================================================================
    add_ch("Software Requirements Specification (SRS)", "3")

    add_p(
        "Project Title: Cipher Court – Escape to justice room\n"
        "Candidate Investigators: Shravani Laxman Ghode (Roll No.: 9022) and Sahil Kate (Roll No.: CS-9012)\n"
        "Academic Year: 2026–2027 | Department of Computer Science & Engineering",
        bold_prefix="Project Credentials & Identification:"
    )
    add_p(
        "This Software Requirements Specification (SRS) establishes the formal foundational requirements for 'Cipher Court – Escape to justice room'. "
        "It specifies the system scope across visual front-end interfaces, real-time backend C# game logic, programming languages, functional requirements, "
        "non-functional constraints, and integrated development requirements needed to construct, verify, and maintain the application in Unity 6 URP."
    )

    # 3.1 Front End & Backend Demarcation
    add_sec("Architectural Scope: Front End and Backend Demarcation", "3.1")
    add_subsec("1. Front End Architecture", "3.1.1")
    add_p(
        "The front end is the visual and interactive part of the game through which the player experiences the 3D environment "
        "and communicates with the system. Key front-end modules and visual presentation layers encompass:"
    )
    add_bullet("Unity 3D game scenes for the courtroom/escape-room environment.")
    add_bullet("3D character/player controller with smooth first-person camera movement.")
    add_bullet("Interactive doors, locks, files, computers, documents and other objects.")
    add_bullet("Main Menu, Gameplay UI, Pause Menu and Completion/Game Over UI.")
    add_bullet("Code-entry and puzzle interfaces with real-time feedback.")
    add_bullet("Clue and hint display systems.")
    add_bullet("Timer and objective indicators with dynamic TextMeshPro typography.")
    add_bullet("Lighting, textures, animations and audio presentation.")

    add_subsec("2. Backend Architecture", "3.1.2")
    add_p(
        "The backend/game logic manages player actions, puzzle validation, game state and progression. For the Unity implementation, "
        "this logic is primarily handled by C# scripts inside the Unity project:"
    )
    add_bullet("Player movement and interaction management via character kinematics and raycasting.")
    add_bullet("Puzzle and cipher validation algorithms.")
    add_bullet("Code and password checking mechanisms.")
    add_bullet("Door/area unlocking logic and physical slerp rotation controllers.")
    add_bullet("Clue and hint management services.")
    add_bullet("Timer and objective management engines.")
    add_bullet("Game-state and progression management.")
    add_bullet("Scene loading and asynchronous transition control.")
    add_bullet("Audio and event-trigger management subsystems.")

    # 3.2 Languages
    add_sec("Languages & Technology Stack", "3.2")
    add_p("The project leverages specialized programming languages and shader scripts tailored for interactive real-time 3D simulation. Table 3.1 defines their specific use and operational roles:")

    t_lang = doc.add_table(rows=4, cols=3)
    t_lang.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_lang.autofit = False
    set_table_borders(t_lang)

    lang_headers = ["Language", "Use", "Role"]
    lang_widths = [Inches(1.8), Inches(1.8), Inches(2.9)]

    for j, h in enumerate(lang_headers):
        cell = t_lang.cell(0, j)
        cell.width = lang_widths[j]
        set_cell_background(cell, "102C57")
        set_cell_margins(cell, top=70, bottom=70, left=60, right=60)
        p = cell.paragraphs[0]
        run = p.add_run(h)
        run.font.name = "Times New Roman"
        run.font.size = Pt(8.5)
        run.font.bold = True
        run.font.color.rgb = RGBColor(255, 255, 255)

    lang_data = [
        ("C#", "Unity scripts", "Player controls, interactions, puzzles, UI and game logic"),
        ("HLSL/Shader code (where required)", "Unity rendering", "Visual/material effects when custom shaders are used"),
        ("HTML/CSS/JavaScript (optional fallback)", "Web-based prototype", "Rapid web prototype preview, cross-platform demonstration, and web documentation"),
    ]

    for i, row_data in enumerate(lang_data):
        row = t_lang.rows[i + 1]
        for j, val in enumerate(row_data):
            cell = row.cells[j]
            cell.width = lang_widths[j]
            if (i % 2) == 1:
                set_cell_background(cell, "F7F9FB")
            set_cell_margins(cell, top=50, bottom=50, left=60, right=60)
            p = cell.paragraphs[0]
            run = p.add_run(val)
            run.font.name = "Times New Roman"
            run.font.size = Pt(8)
            if j == 0:
                run.font.bold = True

    # 3.3 Functional Requirements
    add_sec("Functional Requirements Specification (FR-01 to FR-20)", "3.3")
    add_p("Functional requirements delineate the explicit capabilities, behaviors, and interactive transformations provided by Cipher Court. Table 3.2 details the twenty core functional requirements:")

    t_fr = doc.add_table(rows=21, cols=3)
    t_fr.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_fr.autofit = False
    set_table_borders(t_fr)

    fr_headers = ["ID", "Requirement", "Priority"]
    fr_widths = [Inches(1.0), Inches(4.5), Inches(1.0)]

    for j, h in enumerate(fr_headers):
        cell = t_fr.cell(0, j)
        cell.width = fr_widths[j]
        set_cell_background(cell, "102C57")
        set_cell_margins(cell, top=70, bottom=70, left=60, right=60)
        p = cell.paragraphs[0]
        run = p.add_run(h)
        run.font.name = "Times New Roman"
        run.font.size = Pt(8.5)
        run.font.bold = True
        run.font.color.rgb = RGBColor(255, 255, 255)

    fr_data = [
        ("FR-01", "The system shall allow the player to start a new game from the main menu.", "High"),
        ("FR-02", "The system shall display a 3D courtroom/escape-room environment to the player.", "High"),
        ("FR-03", "The system shall allow the player to move the character within the game environment.", "High"),
        ("FR-04", "The system shall allow the player to interact with doors, files, documents, computers, locks, clues and other designated objects.", "High"),
        ("FR-05", "The system shall provide cipher-based puzzles that the player must solve to progress through the game.", "High"),
        ("FR-06", "The system shall provide clues related to the cipher puzzles.", "High"),
        ("FR-07", "The system shall allow the player to enter answers or codes using an interactive interface.", "High"),
        ("FR-08", "The system shall validate the code entered by the player and indicate whether it is correct or incorrect.", "High"),
        ("FR-09", "The system shall unlock the corresponding door, locker or game area when the correct code is entered.", "High"),
        ("FR-10", "The system shall maintain the current game progress during gameplay.", "High"),
        ("FR-11", "The system shall maintain the current game progress during gameplay.", "High"),
        ("FR-12", "The system shall provide a timer to track the player's progress.", "Medium"),
        ("FR-13", "The system shall provide hints when the player requests assistance.", "Medium"),
        ("FR-14", "The system shall display appropriate messages for successful and unsuccessful interactions.", "Medium"),
        ("FR-15", "The system shall provide a pause menu containing Resume, Restart and Exit options.", "Medium"),
        ("FR-16", "The system shall display a completion message when the player successfully solves all required puzzles.", "High"),
        ("FR-17", "The system shall allow the player to restart the game.", "Medium"),
        ("FR-18", "The system shall provide sound effects and background audio for important game events.", "Low"),
        ("FR-19", "The system shall detect completion of required objectives and trigger the final game sequence.", "High"),
        ("FR-20", "The system shall provide an exit option to leave the game.", "Low"),
    ]

    for i, row_data in enumerate(fr_data):
        row = t_fr.rows[i + 1]
        for j, val in enumerate(row_data):
            cell = row.cells[j]
            cell.width = fr_widths[j]
            if (i % 2) == 1:
                set_cell_background(cell, "F7F9FB")
            set_cell_margins(cell, top=45, bottom=45, left=60, right=60)
            p = cell.paragraphs[0]
            run = p.add_run(val)
            run.font.name = "Times New Roman"
            run.font.size = Pt(8)
            if j == 0:
                run.font.bold = True
            if j == 2:
                run.font.bold = True
                if val == "High":
                    run.font.color.rgb = RGBColor(160, 20, 20)

    # 3.4 Non-Functional Requirements
    add_sec("Non-Functional Requirements Specification (NFR-01 to NFR-15)", "3.4")
    add_p("Non-functional requirements specify the performance benchmarks, usability criteria, security parameters, and architectural quality standards. Table 3.3 presents the formal non-functional requirements:")

    t_nfr = doc.add_table(rows=15, cols=3)
    t_nfr.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_nfr.autofit = False
    set_table_borders(t_nfr)

    for j, h in enumerate(fr_headers):
        cell = t_nfr.cell(0, j)
        cell.width = fr_widths[j]
        set_cell_background(cell, "35598E")
        set_cell_margins(cell, top=70, bottom=70, left=60, right=60)
        p = cell.paragraphs[0]
        run = p.add_run(h)
        run.font.name = "Times New Roman"
        run.font.size = Pt(8.5)
        run.font.bold = True
        run.font.color.rgb = RGBColor(255, 255, 255)

    nfr_data = [
        ("NFR-01", "The game should provide smooth and acceptable response time during normal gameplay and player interactions.", "High"),
        ("NFR-02", "The system should provide a simple, clear and user-friendly game interface.", "High"),
        ("NFR-03", "The system shall restrict access to game-development and configuration features to authorized developers.", "High"),
        ("NFR-04", "The system shall maintain consistency of game states, puzzle states and player progress during gameplay.", "High"),
        ("NFR-05", "The game should be modular and maintainable so that new puzzles, rooms, clues and features can be added easily.", "High"),
        ("NFR-06", "The system should provide stable gameplay without frequent crashes or unexpected termination.", "High"),
        ("NFR-07", "The 3D environment should load within an acceptable time on the target computer.", "Medium"),
        ("NFR-08", "Player controls should respond accurately to keyboard and mouse input.", "High"),
        ("NFR-09", "Puzzle validation should provide immediate feedback after the player submits an answer.", "High"),
        ("NFR-10", "The system should provide appropriate response feedback after the player submits an answer.", "Medium"),
        ("NFR-12", "The game should maintain consistent behaviour on supported Windows systems.", "High"),
        ("NFR-13", "The system should allow game assets, scripts, scenes and UI components to be updated independently where practical.", "Medium"),
        ("NFR-14", "The system should minimize unnecessary memory and processing usage during gameplay.", "Medium"),
        ("NFR-15", "The system should provide appropriate error messages when invalid codes or unsupported interactions are attempted.", "Medium"),
    ]

    for i, row_data in enumerate(nfr_data):
        row = t_nfr.rows[i + 1]
        for j, val in enumerate(row_data):
            cell = row.cells[j]
            cell.width = fr_widths[j]
            if (i % 2) == 1:
                set_cell_background(cell, "F7F9FB")
            set_cell_margins(cell, top=45, bottom=45, left=60, right=60)
            p = cell.paragraphs[0]
            run = p.add_run(val)
            run.font.name = "Times New Roman"
            run.font.size = Pt(8)
            if j == 0:
                run.font.bold = True
            if j == 2:
                run.font.bold = True
                if val == "High":
                    run.font.color.rgb = RGBColor(160, 20, 20)

    # 3.5 Integrated Development Requirements
    add_sec("Integrated Development Requirements (IDR-01 to IDR-10)", "3.5")
    add_p("Integrated Development Requirements describe the engineering tools, folder topologies, version control, and development environments needed to build, test, and maintain Cipher Court. Table 3.4 outlines these requirements:")

    t_idr = doc.add_table(rows=9, cols=3)
    t_idr.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_idr.autofit = False
    set_table_borders(t_idr)

    for j, h in enumerate(fr_headers):
        cell = t_idr.cell(0, j)
        cell.width = fr_widths[j]
        set_cell_background(cell, "102C57")
        set_cell_margins(cell, top=70, bottom=70, left=60, right=60)
        p = cell.paragraphs[0]
        run = p.add_run(h)
        run.font.name = "Times New Roman"
        run.font.size = Pt(8.5)
        run.font.bold = True
        run.font.color.rgb = RGBColor(255, 255, 255)

    idr_data = [
        ("IDR-01", "The project shall be developed using Unity Hub and a supported Unity 3D Editor version selected for the project.", "High"),
        ("IDR-02", "C# shall be used for Unity gameplay and system scripts.", "High"),
        ("IDR-03", "A suitable code editor such as Visual Studio or Visual Studio Code shall be used for C# development.", "Medium"),
        ("IDR-04", "The project shall be organized into separate folders for Scenes, Scripts, Prefabs, Materials, Models, UI and Audio.", "High"),
        ("IDR-07", "Game assets shall be integrated into the Unity project and tested for compatibility and performance.", "Medium"),
        ("IDR-08", "The project shall be tested for player movement, interaction, puzzle validation, scene transitions and completion conditions.", "High"),
        ("IDR-09", "Development shall use versioned project backups or version control where available to reduce the risk of losing source files.", "Medium"),
        ("IDR-10", "The final build shall be tested on the target Windows computer before project submission.", "High"),
    ]

    for i, row_data in enumerate(idr_data):
        row = t_idr.rows[i + 1]
        for j, val in enumerate(row_data):
            cell = row.cells[j]
            cell.width = fr_widths[j]
            if (i % 2) == 1:
                set_cell_background(cell, "F7F9FB")
            set_cell_margins(cell, top=45, bottom=45, left=60, right=60)
            p = cell.paragraphs[0]
            run = p.add_run(val)
            run.font.name = "Times New Roman"
            run.font.size = Pt(8)
            if j == 0:
                run.font.bold = True
            if j == 2:
                run.font.bold = True
                if val == "High":
                    run.font.color.rgb = RGBColor(160, 20, 20)

    # 3.6 Detailed Use Case Specifications
    add_sec("Detailed Use Case Specifications", "3.6")
    add_p("To provide formal software engineering rigor, core functional requirements are elaborated into standardized Use Case Specifications detailing actors, preconditions, normal flows, and postconditions:")

    add_subsec("Use Case UC-01: Spatial Clue Raycast and Inspection", "3.6.1")
    add_bullet("Primary Actor: Player Investigator.")
    add_bullet("Preconditions: Player is spawned in a playable level; character controller is active; cursor is locked in center.")
    add_bullet("Trigger: Player centers viewport reticle over a 3D interactable object within 2.5 meters.")
    add_bullet("Main Success Scenario:\n1. Player moves camera so forward vector intersects evidence collider.\n2. PlayerInteraction raycast hits collider with Layer 'Interactable'.\n3. Reticle interpolates scale from 1.0x to 1.35x and changes color to Cyan (#00E5FF).\n4. Prompt text '[E] Inspect Evidence' appears on HUD.\n5. Player presses KeyCode.E.\n6. System invokes IInteractable.Interact() and displays evidence inspection modal.")
    add_bullet("Alternative / Exception Flows: If distance > 2.5m, raycast fails to reach; reticle remains white; no prompt displayed. If object is behind a wall, Physics.Raycast terminates at the intervening occluder collider.")
    add_bullet("Postconditions: Player enters inspection sub-state; clue ID is marked as discovered.")

    add_subsec("Use Case UC-03: Keypad Numerical Code Input and Validation", "3.6.2")
    add_bullet("Primary Actor: Player Investigator.")
    add_bullet("Preconditions: Player is standing in front of Level 1 keypad console.")
    add_bullet("Trigger: Player presses interactive digit buttons (0–9) on the electronic keypad.")
    add_bullet("Main Success Scenario:\n1. Player clicks or presses key on digit button.\n2. Keypad script appends digit to `currentInput` buffer.\n3. Display screen updates with current buffer (e.g. '1 0 1 _').\n4. Audio source plays button click sound effect.\n5. Upon 4th digit entry, system executes `ValidateKeypadCode()`.\n6. Buffer matches '1011'. Display screen flashes 'ACCESS GRANTED' in green.\n7. Door motor initiates slerp rotation; exit passage is cleared.")
    add_bullet("Alternative / Exception Flows: If entered code does not match '1011', display screen flashes 'INVALID KEY' in red; error buzzer plays; buffer resets after 1.2s delay.")
    add_bullet("Postconditions: Keypad transitions to solved state; door collider disabled.")

    add_subsec("Use Case UC-08: Courtroom Final Verdict Delivery", "3.6.3")
    add_bullet("Primary Actor: Player Investigator.")
    add_bullet("Preconditions: Player has traversed through Levels 1–5, possessing all evidence tokens; spawned in Grand Courtroom.")
    add_bullet("Trigger: Player steps up to the judicial podium and selects the final indictment prompt.")
    add_bullet("Main Success Scenario:\n1. Courtroom dialogue system presents summary of evidence items.\n2. Player presents evidence demonstrating conspirator's guilt.\n3. Verdict engine evaluates proposition against evidence truth table.\n4. Truth verified: Judge strikes gavel three times (audio SFX triggered).\n5. Verdict banner displays 'VERDICT: GUILTY BEYOND REASONABLE DOUBT'.\n6. Grand exit bronze doors open, revealing exit trigger to GameComplete.")
    add_bullet("Alternative / Exception Flows: If player presents incorrect evidence, judge reprimands counsel; player is prompted to re-examine court records.")
    add_bullet("Postconditions: Game progresses to victory state; `FinalLevelExit` triggers.")

    # 3.7 Operational Environment & Feasibility
    add_sec("Operational Environment Specifications and Feasibility Study", "3.7")
    add_p("The operational environment specifications for development and target client deployment are defined below:")

    t_hw = doc.add_table(rows=6, cols=3)
    t_hw.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_hw.autofit = False
    set_table_borders(t_hw)
    hw_headers = ["Hardware Component", "Minimum Deployment Specification", "Development Workstation Specification"]
    hw_widths = [Inches(2.0), Inches(2.2), Inches(2.3)]
    for j, h in enumerate(hw_headers):
        cell = t_hw.cell(0, j)
        cell.width = hw_widths[j]
        set_cell_background(cell, "102C57")
        set_cell_margins(cell, top=70, bottom=70, left=60, right=60)
        p = cell.paragraphs[0]
        run = p.add_run(h)
        run.font.name = "Times New Roman"
        run.font.size = Pt(8.5)
        run.font.bold = True
        run.font.color.rgb = RGBColor(255, 255, 255)

    hw_data = [
        ("Central Processor (CPU)", "Intel Core i5-4460 / AMD FX-6300 (4 Cores)", "Intel Core i7-13700H / AMD Ryzen 7 7840HS (16 Cores)"),
        ("System Memory (RAM)", "8 GB DDR3 / DDR4 System RAM", "32 GB DDR5 High-Speed Dual Channel RAM"),
        ("Graphics Processor (GPU)", "NVIDIA GeForce GTX 960 / AMD Radeon R9 280", "NVIDIA GeForce RTX 4060 Laptop GPU (8 GB GDDR6)"),
        ("Storage Subsystem", "2.5 GB Free Disk Space (HDD supported)", "1 TB NVMe PCIe 4.0 SSD (Read: 5000 MB/s)"),
        ("Display / Resolution", "1280x720 (720p HD) @ 60 Hz", "1920x1080 (1080p FHD) / 2560x1440 (QHD) @ 144 Hz"),
    ]
    for i, row_data in enumerate(hw_data):
        row = t_hw.rows[i + 1]
        for j, val in enumerate(row_data):
            cell = row.cells[j]
            cell.width = hw_widths[j]
            if (i % 2) == 1:
                set_cell_background(cell, "F7F9FB")
            set_cell_margins(cell, top=50, bottom=50, left=60, right=60)
            p = cell.paragraphs[0]
            run = p.add_run(val)
            run.font.name = "Times New Roman"
            run.font.size = Pt(8)
            if j == 0:
                run.font.bold = True

    add_bullet("Technical Feasibility: High. Unity 6 URP provides production-proven first-person kinematic controllers, robust raycast query APIs (Physics.Raycast), and optimized PBR shader execution.")
    add_bullet("Operational Feasibility: Excellent. The game requires zero proprietary hardware peripherals, running smoothly on standard commercial PC keyboards and mice.")
    add_bullet("Economic Feasibility: Zero Capital Outlay. The entire software stack was engineered using free educational licenses (Unity Personal, Visual Studio Community, Git).")
    add_bullet("Schedule Feasibility: Completed on Schedule. The project was successfully executed across Agile milestones culminating in verified standalone PC builds.")

    doc.add_page_break()

    # =========================================================================
    # CHAPTER 4: SYSTEM DESIGN AND ARCHITECTURE (UML DIAGRAMS)
    # =========================================================================
    add_ch("System Design and Architecture", "4")

    add_sec("High-Level Layered System Architecture", "4.1")
    add_p(
        "To achieve modularity, high cohesion, and low coupling, the software architecture of Cipher Court is organized into "
        "a five-tier hierarchical model:"
    )
    add_bullet("Tier 1: Presentation & URP Rendering Layer: Handles camera viewport rendering, URP Lit PBR materials, directional and point light calculations, post-processing volumetric bloom, and occlusion culling bounds.")
    add_bullet("Tier 2: Gameplay & Puzzle Controller Layer: Encapsulates level-specific logic modules (Level1KeypadPuzzle, Level2BallisticsPuzzle, Level3CipherPuzzle, Level4LockerPuzzle, Level5EvidencePresentation, Level6VerdictPuzzle) which inherit from common abstract puzzle state interfaces.")
    add_bullet("Tier 3: Interaction & Physics Kinematics Layer: Houses the PlayerController kinematic equations, CharacterController collision volumes, and the distance-bounded PlayerInteraction raycasting engine.")
    add_bullet("Tier 4: State Machine & Scene Management Layer: Governs global application lifecycle states (MainMenu -> Level1 -> ... -> Level6 -> GameComplete), persistent game flags, audio source routing, and safe asynchronous scene loading.")
    add_bullet("Tier 5: Resilient UI & EventSystem Layer: Manages dynamic Canvas rendering, TextMeshPro typography, dynamic button listener attachment, and mouse cursor locking safety guarantees.")

    add_sec("Game Lifecycle and State Machine Architecture", "4.2")
    add_p("The application lifecycle is modeled as a deterministic Finite State Machine (FSM) spanning MainMenu, Exploration, PuzzleInspection, PuzzleSolved, Transition, and GameComplete states.")

    # 4.3 Unified Modeling Language (UML) Diagrams
    add_sec("Unified Modeling Language (UML) Diagrams", "4.3")
    add_p(
        "To provide rigorous software engineering representation across structural, behavioral, and architectural viewpoints, "
        "the software design of Cipher Court is formally modeled through the complete official suite of Unified Modeling Language "
        "(UML 2.5) diagrams and behavioral event matrices:"
    )

    # 4.3.1 Event Table
    add_subsec("1. Event Table", "4.3.1")
    add_p(
        "The Event Table specifies the stimulus-response dynamics of the game engine, identifying event triggers, primary actors, "
        "system actions, and concrete gameplay outcomes across all investigation and trial phases. Table 4.1 outlines these events:"
    )

    t_evt = doc.add_table(rows=11, cols=5)
    t_evt.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_evt.autofit = False
    set_table_borders(t_evt)

    evt_headers = ["Event ID", "Event / Trigger", "Actor", "System Response / Action", "Outcome"]
    evt_widths = [Inches(0.8), Inches(1.5), Inches(0.7), Inches(2.2), Inches(1.3)]

    for j, h in enumerate(evt_headers):
        cell = t_evt.cell(0, j)
        cell.width = evt_widths[j]
        set_cell_background(cell, "102C57")
        set_cell_margins(cell, top=60, bottom=60, left=50, right=50)
        p = cell.paragraphs[0]
        run = p.add_run(h)
        run.font.name = "Times New Roman"
        run.font.size = Pt(8)
        run.font.bold = True
        run.font.color.rgb = RGBColor(255, 255, 255)

    evt_data = [
        ("E-01", "Player starts the game.", "Player", "System loads the game introduction, storyline, objectives and instructions.", "Investigation begins."),
        ("E-02", "Player enters the investigation area.", "Player", "System loads the investigation environment and available interactive objects.", "Player can explore the area."),
        ("E-03", "Player interacts with a clue/evidence object.", "Player", "System displays the relevant clue, message, document or evidence information.", "Clue is examined and recorded."),
        ("E-04", "Player selects a cipher puzzle.", "Player", "System displays the cipher puzzle and instructions.", "Player can attempt the puzzle."),
        ("E-05", "Player submits a cipher answer.", "Player", "System validates the submitted answer.", "Correct/incorrect result is displayed."),
        ("E-06", "Player requests a hint.", "Player", "System displays an available hint for the current challenge.", "Player receives assistance."),
        ("E-07", "Player identifies suspicious information.", "Player", "System records the selected clue/decision and provides appropriate feedback.", "Investigation progress is updated."),
        ("E-08", "Player makes an investigation decision.", "Player", "System evaluates the decision and updates the player's progress/score.", "Next challenge or consequence is determined."),
        ("E-09", "Player completes the required challenge(s).", "Player", "System updates the level/stage status and unlocks the next stage when requirements are satisfied.", "Player progresses to the next stage."),
        ("E-10", "Player completes the investigation.", "Player", "System calculates the final result based on completed challenges, score and decisions.", "Final Justice/Outcome is displayed."),
    ]

    for i, row_data in enumerate(evt_data):
        row = t_evt.rows[i + 1]
        for j, val in enumerate(row_data):
            cell = row.cells[j]
            cell.width = evt_widths[j]
            if (i % 2) == 1:
                set_cell_background(cell, "F7F9FB")
            set_cell_margins(cell, top=45, bottom=45, left=50, right=50)
            p = cell.paragraphs[0]
            run = p.add_run(val)
            run.font.name = "Times New Roman"
            run.font.size = Pt(7.5)
            if j == 0:
                run.font.bold = True

    add_fig(
        "Assets/CipherCourtPolish/UploadedDiagrams/event_table.jpg",
        "Fig. 4.1: Comprehensive Event Table and System Trigger-Response Matrix (E-01 to E-10)",
        width=Inches(6.0)
    )

    # 4.3.2 Class Diagram
    add_subsec("2. Class Diagram", "4.3.2")
    add_p(
        "The Class Diagram specifies the object-oriented structure of Cipher Court. It details the primary entities, controllers, "
        "services, and data repositories: Player, GameManager, Level, Timer, HintSystem, ScoreSystem, Admin, GameData, Puzzle, and Cipher. "
        "Attributes and operations define clean separation of concerns, managing timer ticks, hint deductions, score computations, "
        "and cryptographic encryption/decryption routines:"
    )
    add_fig(
        "Assets/CipherCourtPolish/UploadedDiagrams/class_diagram.png",
        "Fig. 4.2: Comprehensive Unified Class Diagram (Controllers, Services, Repositories, and Entities)",
        width=Inches(5.6)
    )

    # 4.3.3 Object Diagram
    add_subsec("3. Object Diagram", "4.3.3")
    add_p(
        "The Object Diagram captures a concrete runtime instance snapshot during an active investigation session. "
        "Figure 4.3 depicts active memory references: `player1: Player` (Alex, score=500, currentLevel=2), `game1: GameManager` (Running), "
        "`level2: Level` (Prison Archive, Medium), `timer1: Timer` (180s remaining), `hint1: HintSystem` ('Shift letters', penalty=20), "
        "`score1: ScoreSystem` (score=500, bonus=100), `puzzle1: Puzzle` (Decode Message 'JUSTICE'), and `cipher1: Cipher` (Caesar k=3, 'MXYWLFH'):"
    )
    add_fig(
        "Assets/CipherCourtPolish/UploadedDiagrams/object_diagram.png",
        "Fig. 4.3: UML Object Diagram illustrating Concrete Runtime Instances during Gameplay",
        width=Inches(5.4)
    )

    # 4.3.4 Use Case Diagram
    add_subsec("4. Use Case Diagram", "4.3.4")
    add_p(
        "The Use Case Diagram delineates interactions between the primary human actors (Player, Admin) and the system boundary ('CIPHER CODE – ESCAPE TO JUSTICE'). "
        "Player use cases include 'View Instructions', 'Start Game <<include>> Select Level', 'View Timer', 'View Score', 'Pause Game', 'Exit Game', "
        "and 'Solve Cipher <<include>> Enter Answer' with extended capability '<<extend>> Request Hint'. Administrator use cases provide supervisory "
        "access: 'Login', 'Add Puzzle', 'Update Puzzle', 'Delete Puzzle', and 'View Game Data':"
    )
    add_fig(
        "Assets/CipherCourtPolish/UploadedDiagrams/use_case_diagram.png",
        "Fig. 4.4: UML Use Case Diagram for Player and Administrator Interaction Vectors",
        width=Inches(5.2)
    )

    # 4.3.5 Sequence Diagram
    add_subsec("5. Sequence Diagram", "4.3.5")
    add_p(
        "The Sequence Diagram documents the dynamic inter-object message passing chronology across the nine lifelines: "
        "Player, Game UI, Game Manager, Puzzle System, Cipher System, Timer, Hint System, Score System, and Game Data. "
        "It models the chronological execution flow for starting a game, displaying levels, submitting cipher answers, validating solutions, "
        "awarding score points, saving progress, unlocking subsequent rooms, processing hint requests with penalties, and handling time expiration:"
    )
    add_fig(
        "Assets/CipherCourtPolish/UploadedDiagrams/sequence_diagram.png",
        "Fig. 4.5: UML Sequence Diagram for Gameplay, Cipher Validation, Hint Request, and Score Processing",
        width=Inches(4.8)
    )

    # 4.3.6 Activity Diagram
    add_subsec("6. Activity Diagram", "4.3.6")
    add_p(
        "The Activity Diagram specifies the step-by-step algorithmic control flow from Start to End. The workflow guides the player "
        "through launching the game, viewing instructions, initiating the level countdown timer, entering cipher answers, validating correctness, "
        "branching into door clearance and points award upon success, or displaying error messages, checking retry limits, and managing hint penalties:"
    )
    add_fig(
        "Assets/CipherCourtPolish/UploadedDiagrams/activity_diagram.png",
        "Fig. 4.6: UML Activity Diagram Depicting End-to-End Game Flow and Puzzle Decision Logic",
        width=Inches(3.3)
    )

    # 4.3.7 Component Diagram
    add_subsec("7. Component Diagram", "4.3.7")
    add_p(
        "The Component Diagram details the modular structural topology of Cipher Court across four interconnected tiers: "
        "(1) PLAYER DEVICE containing Player/Game UI, Player Input, and Unity 3D Game; (2) GAME CORE encapsulating Game Manager, Puzzle Manager, "
        "Level Manager, and Cipher Engine; (3) GAME SERVICES providing Score Service, Audio Manager, Save/Load Service, Hint Service, and Timer Service; "
        "and (4) DATA LAYER housing Game Data, Score Data, Puzzle Data, and Player Progress repositories:"
    )
    add_fig(
        "Assets/CipherCourtPolish/UploadedDiagrams/component_diagram.png",
        "Fig. 4.7: UML Component Diagram Illustrating Player Device, Game Core, Services, and Data Layers",
        width=Inches(6.0)
    )

    # 4.3.8 Deployment Diagram
    add_subsec("8. Deployment Diagram", "4.3.8")
    add_p(
        "The Deployment Diagram illustrates the physical runtime allocation of software artifacts across execution nodes: "
        "(1) <<Device>> PLAYER PC / LAPTOP executing <<Artifact>> Cipher Code 3D Game inside the <<Execution Environment>> Unity; "
        "(2) <<Device>> APPLICATION SERVER hosting <<Artifact>> Game Backend and <<Component>> Game API communicating over secure HTTPS; "
        "and (3) <<Device>> DATABASE SERVER hosting the persistent <<Database>> Game Database connected via dedicated Database Connection:"
    )
    add_fig(
        "Assets/CipherCourtPolish/UploadedDiagrams/deployment_diagram.png",
        "Fig. 4.8: UML Deployment Diagram showing Player PC, Application Server, and Database Topology",
        width=Inches(5.5)
    )

    # 4.4 Class Specifications
    add_sec("Class-by-Class Method and Field Specifications", "4.4")
    add_p("To provide rigorous object-oriented documentation, the internal member structures of the principal engine scripts are specified in Tables 4.2 through 4.5:")

    # Class Table: PlayerController
    add_subsec("Class Specification: PlayerController", "4.4.1")
    t_pc = doc.add_table(rows=7, cols=4)
    t_pc.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_pc.autofit = False
    set_table_borders(t_pc)
    pc_headers = ["Member Name", "Type", "Access Modifier", "Functional Description"]
    pc_widths = [Inches(1.8), Inches(1.2), Inches(1.2), Inches(2.3)]
    for j, h in enumerate(pc_headers):
        cell = t_pc.cell(0, j)
        cell.width = pc_widths[j]
        set_cell_background(cell, "102C57")
        set_cell_margins(cell, top=60, bottom=60, left=50, right=50)
        p = cell.paragraphs[0]
        run = p.add_run(h)
        run.font.name = "Times New Roman"
        run.font.size = Pt(8.5)
        run.font.bold = True
        run.font.color.rgb = RGBColor(255, 255, 255)

    pc_data = [
        ("walkSpeed", "float (4.5f)", "private (SerializeField)", "Ground translational velocity in meters per second."),
        ("gravity", "float (-18.0f)", "private (SerializeField)", "Downwards gravitational acceleration vector."),
        ("mouseSensitivity", "float (2.0f)", "private (SerializeField)", "Mouse look scalar coefficient for angular delta."),
        ("rotationX", "float", "private", "Current clamped vertical pitch angle in degrees [-85, +85]."),
        ("Awake()", "void", "private", "Initializes CharacterController and main Camera references."),
        ("Update()", "void", "private", "Per-frame physics integration: WASD input, jump, gravity, and mouse look."),
    ]
    for i, row_data in enumerate(pc_data):
        row = t_pc.rows[i + 1]
        for j, val in enumerate(row_data):
            cell = row.cells[j]
            cell.width = pc_widths[j]
            if (i % 2) == 1:
                set_cell_background(cell, "F7F9FB")
            set_cell_margins(cell, top=50, bottom=50, left=50, right=50)
            p = cell.paragraphs[0]
            run = p.add_run(val)
            run.font.name = "Times New Roman"
            run.font.size = Pt(8)
            if j == 0:
                run.font.bold = True

    # Class Table: PlayerInteraction
    add_subsec("Class Specification: PlayerInteraction", "4.4.2")
    t_pi = doc.add_table(rows=6, cols=4)
    t_pi.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_pi.autofit = False
    set_table_borders(t_pi)
    for j, h in enumerate(pc_headers):
        cell = t_pi.cell(0, j)
        cell.width = pc_widths[j]
        set_cell_background(cell, "35598E")
        set_cell_margins(cell, top=60, bottom=60, left=50, right=50)
        p = cell.paragraphs[0]
        run = p.add_run(h)
        run.font.name = "Times New Roman"
        run.font.size = Pt(8.5)
        run.font.bold = True
        run.font.color.rgb = RGBColor(255, 255, 255)

    pi_data = [
        ("interactionDistance", "float (2.5f)", "private (SerializeField)", "Maximum raycast penetration boundary in meters."),
        ("reticleImage", "Image", "private (SerializeField)", "HUD UI crosshair image for visual hover interpolation."),
        ("currentInteractable", "GameObject", "private", "Cached reference to currently focused interactable target."),
        ("PerformRaycast()", "void", "private", "Casts Physics.Raycast along camera forward vector; updates reticle state."),
        ("Update()", "void", "private", "Executes raycast query and listens for KeyCode.E interaction triggers."),
    ]
    for i, row_data in enumerate(pi_data):
        row = t_pi.rows[i + 1]
        for j, val in enumerate(row_data):
            cell = row.cells[j]
            cell.width = pc_widths[j]
            if (i % 2) == 1:
                set_cell_background(cell, "F7F9FB")
            set_cell_margins(cell, top=50, bottom=50, left=50, right=50)
            p = cell.paragraphs[0]
            run = p.add_run(val)
            run.font.name = "Times New Roman"
            run.font.size = Pt(8)
            if j == 0:
                run.font.bold = True

    # Class Table: Level1KeypadPuzzle
    add_subsec("Class Specification: Level1KeypadPuzzle", "4.4.3")
    t_l1 = doc.add_table(rows=7, cols=4)
    t_l1.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_l1.autofit = False
    set_table_borders(t_l1)
    for j, h in enumerate(pc_headers):
        cell = t_l1.cell(0, j)
        cell.width = pc_widths[j]
        set_cell_background(cell, "102C57")
        set_cell_margins(cell, top=60, bottom=60, left=50, right=50)
        p = cell.paragraphs[0]
        run = p.add_run(h)
        run.font.name = "Times New Roman"
        run.font.size = Pt(8.5)
        run.font.bold = True
        run.font.color.rgb = RGBColor(255, 255, 255)

    l1_data = [
        ("targetCode", "string ('1011')", "private (SerializeField)", "Correct binary keypad passcode for room clearance."),
        ("currentInput", "string", "private", "String buffer storing accumulated player digit entries."),
        ("isSolved", "bool", "private", "Boolean state flag preventing redundant input post-solution."),
        ("OnDigitPressed(string)", "void", "public", "Appends digit, triggers audio click SFX, invokes validation at length 4."),
        ("ValidateKeypadCode()", "void", "private", "Compares buffer against targetCode; triggers green chime or red buzzer."),
        ("Update()", "void", "private", "Interpolates door rotation slerp when isOpeningDoor flag is true."),
    ]
    for i, row_data in enumerate(l1_data):
        row = t_l1.rows[i + 1]
        for j, val in enumerate(row_data):
            cell = row.cells[j]
            cell.width = pc_widths[j]
            if (i % 2) == 1:
                set_cell_background(cell, "F7F9FB")
            set_cell_margins(cell, top=50, bottom=50, left=50, right=50)
            p = cell.paragraphs[0]
            run = p.add_run(val)
            run.font.name = "Times New Roman"
            run.font.size = Pt(8)
            if j == 0:
                run.font.bold = True

    # Class Table: Level2BallisticsPuzzle
    add_subsec("Class Specification: Level2BallisticsPuzzle", "4.4.4")
    t_l2 = doc.add_table(rows=6, cols=4)
    t_l2.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_l2.autofit = False
    set_table_borders(t_l2)
    for j, h in enumerate(pc_headers):
        cell = t_l2.cell(0, j)
        cell.width = pc_widths[j]
        set_cell_background(cell, "35598E")
        set_cell_margins(cell, top=60, bottom=60, left=50, right=50)
        p = cell.paragraphs[0]
        run = p.add_run(h)
        run.font.name = "Times New Roman"
        run.font.size = Pt(8.5)
        run.font.bold = True
        run.font.color.rgb = RGBColor(255, 255, 255)

    l2_data = [
        ("targetAngle", "float (38.5f)", "private (SerializeField)", "Target ballistic elevation angle derived from autopsy spatter."),
        ("currentAngle", "float (20.0f)", "private", "Current player-selected elevation angle displayed on monitor."),
        ("isAligned", "bool", "private", "Flag indicating verified trajectory alignment."),
        ("AdjustAngle(float)", "void", "public", "Modulates currentAngle within [0, 90] bounds and evaluates alignment."),
        ("CheckAlignment()", "void", "private", "Verifies |currentAngle - targetAngle| < 0.5f tolerance; opens vault gate."),
    ]
    for i, row_data in enumerate(l2_data):
        row = t_l2.rows[i + 1]
        for j, val in enumerate(row_data):
            cell = row.cells[j]
            cell.width = pc_widths[j]
            if (i % 2) == 1:
                set_cell_background(cell, "F7F9FB")
            set_cell_margins(cell, top=50, bottom=50, left=50, right=50)
            p = cell.paragraphs[0]
            run = p.add_run(val)
            run.font.name = "Times New Roman"
            run.font.size = Pt(8)
            if j == 0:
                run.font.bold = True

    # Class Table: Level3CipherPuzzle
    add_subsec("Class Specification: Level3CipherPuzzle", "4.4.5")
    t_l3 = doc.add_table(rows=6, cols=4)
    t_l3.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_l3.autofit = False
    set_table_borders(t_l3)
    for j, h in enumerate(pc_headers):
        cell = t_l3.cell(0, j)
        cell.width = pc_widths[j]
        set_cell_background(cell, "102C57")
        set_cell_margins(cell, top=60, bottom=60, left=50, right=50)
        p = cell.paragraphs[0]
        run = p.add_run(h)
        run.font.name = "Times New Roman"
        run.font.size = Pt(8.5)
        run.font.bold = True
        run.font.color.rgb = RGBColor(255, 255, 255)

    l3_data = [
        ("targetShiftKey", "int (3)", "private (SerializeField)", "Caesar shift key offset k=3."),
        ("currentShift", "int", "private", "Current angular offset index mod 26."),
        ("encryptedMemo", "string", "private (SerializeField)", "Ciphertext string 'FRXUW URRP'."),
        ("RotateRotorClockwise()", "void", "public", "Rotates physical 3D rotor by 360/26 degrees and triggers decryption."),
        ("EvaluateDecryption()", "void", "private", "Computes modular shift string; verifies target decryption text."),
    ]
    for i, row_data in enumerate(l3_data):
        row = t_l3.rows[i + 1]
        for j, val in enumerate(row_data):
            cell = row.cells[j]
            cell.width = pc_widths[j]
            if (i % 2) == 1:
                set_cell_background(cell, "F7F9FB")
            set_cell_margins(cell, top=50, bottom=50, left=50, right=50)
            p = cell.paragraphs[0]
            run = p.add_run(val)
            run.font.name = "Times New Roman"
            run.font.size = Pt(8)
            if j == 0:
                run.font.bold = True

    # Class Table: Level4LockerPuzzle
    add_subsec("Class Specification: Level4LockerPuzzle", "4.4.6")
    t_l4 = doc.add_table(rows=6, cols=4)
    t_l4.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_l4.autofit = False
    set_table_borders(t_l4)
    for j, h in enumerate(pc_headers):
        cell = t_l4.cell(0, j)
        cell.width = pc_widths[j]
        set_cell_background(cell, "35598E")
        set_cell_margins(cell, top=60, bottom=60, left=50, right=50)
        p = cell.paragraphs[0]
        run = p.add_run(h)
        run.font.name = "Times New Roman"
        run.font.size = Pt(8.5)
        run.font.bold = True
        run.font.color.rgb = RGBColor(255, 255, 255)

    l4_data = [
        ("targetCombination", "int[]", "private (SerializeField)", "Target permutation vector [4, 2, 7]."),
        ("currentDials", "int[]", "private", "Current tumbler state array [t0, t1, t2]."),
        ("isUnlocked", "bool", "private", "State flag indicating bolt retraction."),
        ("AdvanceDial(int)", "void", "public", "Increments selected tumbler index modulo 10; updates 3D text mesh."),
        ("CheckCombination()", "void", "private", "Compares all 3 tumblers against targetCombination; swings locker door."),
    ]
    for i, row_data in enumerate(l4_data):
        row = t_l4.rows[i + 1]
        for j, val in enumerate(row_data):
            cell = row.cells[j]
            cell.width = pc_widths[j]
            if (i % 2) == 1:
                set_cell_background(cell, "F7F9FB")
            set_cell_margins(cell, top=50, bottom=50, left=50, right=50)
            p = cell.paragraphs[0]
            run = p.add_run(val)
            run.font.name = "Times New Roman"
            run.font.size = Pt(8)
            if j == 0:
                run.font.bold = True

    # Class Table: Level5EvidencePresentation
    add_subsec("Class Specification: Level5EvidencePresentation", "4.4.7")
    t_l5 = doc.add_table(rows=5, cols=4)
    t_l5.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_l5.autofit = False
    set_table_borders(t_l5)
    for j, h in enumerate(pc_headers):
        cell = t_l5.cell(0, j)
        cell.width = pc_widths[j]
        set_cell_background(cell, "102C57")
        set_cell_margins(cell, top=60, bottom=60, left=50, right=50)
        p = cell.paragraphs[0]
        run = p.add_run(h)
        run.font.name = "Times New Roman"
        run.font.size = Pt(8.5)
        run.font.bold = True
        run.font.color.rgb = RGBColor(255, 255, 255)

    l5_data = [
        ("contradictoryIndex", "int (2)", "private (SerializeField)", "Target statement index that contains factual falsehood."),
        ("statementExposed", "bool", "private", "Flag indicating proven contradiction."),
        ("PresentEvidence(int)", "void", "public", "Tests evidence against statement; unlocks judge chambers double doors."),
        ("feedbackUI", "TextMeshProUGUI", "private (SerializeField)", "HUD banner displaying legal argument verification results."),
    ]
    for i, row_data in enumerate(l5_data):
        row = t_l5.rows[i + 1]
        for j, val in enumerate(row_data):
            cell = row.cells[j]
            cell.width = pc_widths[j]
            if (i % 2) == 1:
                set_cell_background(cell, "F7F9FB")
            set_cell_margins(cell, top=50, bottom=50, left=50, right=50)
            p = cell.paragraphs[0]
            run = p.add_run(val)
            run.font.name = "Times New Roman"
            run.font.size = Pt(8)
            if j == 0:
                run.font.bold = True

    # Class Table: Level6VerdictPuzzle
    add_subsec("Class Specification: Level6VerdictPuzzle", "4.4.8")
    t_l6 = doc.add_table(rows=6, cols=4)
    t_l6.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_l6.autofit = False
    set_table_borders(t_l6)
    for j, h in enumerate(pc_headers):
        cell = t_l6.cell(0, j)
        cell.width = pc_widths[j]
        set_cell_background(cell, "35598E")
        set_cell_margins(cell, top=60, bottom=60, left=50, right=50)
        p = cell.paragraphs[0]
        run = p.add_run(h)
        run.font.name = "Times New Roman"
        run.font.size = Pt(8.5)
        run.font.bold = True
        run.font.color.rgb = RGBColor(255, 255, 255)

    l6_data = [
        ("verdictDelivered", "bool", "private", "Flag indicating judge's bench verdict conclusion."),
        ("openingDoor", "bool", "private", "Drives final courtroom double exit slerp animation."),
        ("gavelSFX", "AudioClip", "private (SerializeField)", "High-resonance wooden gavel strike acoustic sample."),
        ("DeliverFinalVerdict(bool)", "void", "public", "Evaluates final indictment; triggers gavel audio and courtroom door."),
        ("Update()", "void", "private", "Slerps finalExitDoor transform smoothly to 90 degrees open."),
    ]
    for i, row_data in enumerate(l6_data):
        row = t_l6.rows[i + 1]
        for j, val in enumerate(row_data):
            cell = row.cells[j]
            cell.width = pc_widths[j]
            if (i % 2) == 1:
                set_cell_background(cell, "F7F9FB")
            set_cell_margins(cell, top=50, bottom=50, left=50, right=50)
            p = cell.paragraphs[0]
            run = p.add_run(val)
            run.font.name = "Times New Roman"
            run.font.size = Pt(8)
            if j == 0:
                run.font.bold = True

    # 4.5 Cryptographic and Mathematical Formalisms
    add_sec("Cryptographic and Mathematical Formalisms", "4.5")
    add_p("Each level in Cipher Court is founded upon rigorous mathematical and computer science formalisms. Table 4.2 details the formal equations and logic proofs implemented in the game engine.")

    t42 = doc.add_table(rows=7, cols=3)
    t42.alignment = WD_TABLE_ALIGNMENT.CENTER
    t42.autofit = False
    set_table_borders(t42)

    t42_headers = ["Game Level", "Mathematical / Cryptographic Formulation", "Algorithmic Verification Proof"]
    t42_widths = [Inches(1.5), Inches(2.7), Inches(2.3)]

    for j, h in enumerate(t42_headers):
        cell = t42.cell(0, j)
        cell.width = t42_widths[j]
        set_cell_background(cell, "102C57")
        set_cell_margins(cell, top=70, bottom=70, left=60, right=60)
        p = cell.paragraphs[0]
        run = p.add_run(h)
        run.font.name = "Times New Roman"
        run.font.size = Pt(8.5)
        run.font.bold = True
        run.font.color.rgb = RGBColor(255, 255, 255)

    math_data = [
        ("Level 1: Crime Scene Keypad", "Positional Binary Summation:\nV = Sum_{i=0}^{3} (b_i * 2^{3-i})\nTarget: b=[1,0,1,1] => V = 8 + 0 + 2 + 1 = 11", "Bitwise AND Mask Validation:\n(input_mask & 0x0F) == 0x0B (Decimal 11). Correct digits trigger DoorOpenEvent()."),
        ("Level 2: Forensic Ballistics", "Parabolic Kinematic Trajectory:\ny(x) = x*tan(theta) - (g*x^2)/(2*v_0^2*cos^2(theta))\nAligning impact coordinate (x_t, y_t).", "Root-finding convergence tolerance:\n|y(x_t) - y_target| < epsilon (0.05m). Validates bullet trajectory alignment."),
        ("Level 3: Steganographic Archive", "Modular Caesar Rotor Shift:\nC_i = (P_i + k) mod 26\nDecryption: P_i = (C_i - k + 26) mod 26 with k=3.", "Character-by-character string comparison against decrypted court memo plain text hash."),
        ("Level 4: Multi-Tumbler Vault", "Permutation Lock State Vector:\nS = [t_0, t_1, t_2] in Z_10^3\nTarget combination S_target = [4, 2, 7].", "Tuple equality assertion:\n(t0 == 4) && (t1 == 2) && (t2 == 7). Mechanical lock bolt retracted."),
        ("Level 5: Pre-Trial Chambers", "Propositional Contradiction Matrix:\nStatement S, Evidence E.\nTruth condition: (S_true ^ E_true) => Contradiction.", "Boolean matrix evaluation: Evaluating whether physical evidence refutes witness alibi statement."),
        ("Level 6: Grand Courtroom", "Bayesian Weight-of-Evidence Formulation:\nP(Guilt | E_1, ..., E_n) = (P(E | G)*P(G)) / P(E)\nThreshold: Sum(W_i) >= W_critical.", "Courtroom state machine evaluates aggregate evidence score. Score >= 80% triggers 'JUSTICE SERVED' verdict."),
    ]

    for i, row_data in enumerate(math_data):
        row = t42.rows[i + 1]
        for j, val in enumerate(row_data):
            cell = row.cells[j]
            cell.width = t42_widths[j]
            if (i % 2) == 1:
                set_cell_background(cell, "F7F9FB")
            set_cell_margins(cell, top=50, bottom=50, left=60, right=60)
            p = cell.paragraphs[0]
            run = p.add_run(val)
            run.font.name = "Times New Roman"
            run.font.size = Pt(8)
            if j == 0:
                run.font.bold = True

    # 4.6 State Transition Matrix
    add_sec("State Transition Matrix for Puzzle FSM Execution", "4.6")
    add_p("To ensure deterministic execution and prevent race conditions between player input, raycasting, and physics triggers, every puzzle state machine implements a formalized State Transition Matrix. Table 4.3 specifies the inputs, guard conditions, and resulting actions:")

    t43 = doc.add_table(rows=7, cols=5)
    t43.alignment = WD_TABLE_ALIGNMENT.CENTER
    t43.autofit = False
    set_table_borders(t43)

    t43_headers = ["Current State", "Input Event / Stimulus", "Guard Condition", "Output Transition Action", "Next Target State"]
    t43_widths = [Inches(1.5), Inches(1.3), Inches(1.4), Inches(1.5), Inches(1.3)]

    for j, h in enumerate(t43_headers):
        cell = t43.cell(0, j)
        cell.width = t43_widths[j]
        set_cell_background(cell, "35598E")
        set_cell_margins(cell, top=60, bottom=60, left=50, right=50)
        p = cell.paragraphs[0]
        run = p.add_run(h)
        run.font.name = "Times New Roman"
        run.font.size = Pt(8)
        run.font.bold = True
        run.font.color.rgb = RGBColor(255, 255, 255)

    fsm_data = [
        ("STATE_IDLE_EXPLORE", "Reticle Raycast Focus", "Target != null && Distance <= 2.5m", "Set Reticle Cyan; Scale 1.35x; Show Prompt", "STATE_FOCUS_PROMPT"),
        ("STATE_FOCUS_PROMPT", "Press KeyCode.E", "IInteractable Component Present", "Disable Movement; Display Inspection Canvas", "STATE_INSPECT_ACTIVE"),
        ("STATE_KEYPAD_ENTRY", "Digit Pressed (0-9)", "currentInput.Length == 4", "Evaluate targetCode == '1011'", "STATE_CODE_EVAL"),
        ("STATE_CODE_EVAL", "Evaluation Passed", "Input == '1011'", "Trigger Green Chime; Start Slerp Door Open", "STATE_LEVEL_SOLVED"),
        ("STATE_CODE_EVAL", "Evaluation Failed", "Input != '1011'", "Trigger Red Buzzer; Clear Buffer after 1.2s", "STATE_KEYPAD_ENTRY"),
        ("STATE_LEVEL_SOLVED", "Player Enters Exit Trigger", "Collider.CompareTag('Player')", "Fade Screen Alpha 1.0; LoadSceneAsync()", "STATE_SCENE_TRANSITION"),
    ]

    for i, row_data in enumerate(fsm_data):
        row = t43.rows[i + 1]
        for j, val in enumerate(row_data):
            cell = row.cells[j]
            cell.width = t43_widths[j]
            if (i % 2) == 1:
                set_cell_background(cell, "F7F9FB")
            set_cell_margins(cell, top=50, bottom=50, left=50, right=50)
            p = cell.paragraphs[0]
            run = p.add_run(val)
            run.font.name = "Times New Roman"
            run.font.size = Pt(7.5)
            if j == 0:
                run.font.bold = True

    doc.add_page_break()
