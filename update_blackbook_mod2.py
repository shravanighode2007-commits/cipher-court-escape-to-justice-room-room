# update_blackbook_mod2.py
# Generates the comprehensive blackbook_content_mod2.py with overhauled Chapter 6 and Chapter 10

content = '''# blackbook_content_mod2.py
# Module 2 Content: Chapters 6, 7, 8, 9, 10, 11, References, Glossary for Cipher Court Project Blackbook

import os
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from blackbook_helpers import (
    FONT_NAME, set_cell_background, set_cell_margins, set_table_borders, set_table_grid_borders,
    add_module_banner, add_chapter_title, add_heading, add_subheading,
    add_body_paragraph, add_bullet_point, add_image_diagram, add_screenshot_placeholder, add_code_block
)

def add_chapter_6(doc):
    """
    Adds Chapter 6: Application Development & Practical Implementation.
    Complete rewrite providing exhaustive technical walkthrough of Frontend and Backend implementations.
    """
    add_module_banner(doc, "2", "IMPLEMENTATION, TESTING, DEPLOYMENT & EVALUATION PHASE")
    add_chapter_title(doc, "6", "APPLICATION DEVELOPMENT & PRACTICAL IMPLEMENTATION")

    # =========================================================================
    # 6.1 FRONTEND IMPLEMENTATION ARCHITECTURE & COMPONENT FLOW
    # =========================================================================
    add_heading(doc, "6.1 Frontend Implementation Architecture & Component Flow")
    add_body_paragraph(
        doc,
        "The frontend architecture of Cipher Court is engineered within the Unity 6 Long Term Support (LTS 6000.3.21f1) "
        "engine utilizing the Universal Render Pipeline (URP). URP provides a performant, physically based rendering (PBR) "
        "framework capable of rendering complex courtroom architecture, realistic dynamic lighting, screen-space reflections, "
        "and multi-camera viewports while maintaining an uncompromised 60 frames-per-second (FPS) runtime budget on standard "
        "academic workstations.",
        bold_prefix="Graphics & Scene Pipeline Architecture:"
    )

    add_body_paragraph(
        doc,
        "The frontend software topology is decomposed into four foundational architectural pillars that guarantee visual fidelity, "
        "responsive user interaction, and seamless synchronization with the backend microservice: (1) UI/UX Design System & Layout "
        "Hierarchy, (2) Global State Management & Persistence Pipeline, (3) Client-Side Routing & Scene Lifecycle Orchestration, "
        "and (4) Asynchronous API Integration & Network Dispatching.",
        bold_prefix="Core Architectural Subsystems:"
    )

    # 6.1.1 Architectural Foundations
    add_subheading(doc, "6.1.1 UI/UX Architecture, Design Tokens & Canvas Scaler Framework")
    add_body_paragraph(
        doc,
        "The graphical user interface is structured across multi-layered Unity Canvases configured to distinct Render Modes: "
        "Screen Space - Overlay is utilized for HUD reticles, evidence dossiers, and puzzle interaction modals, ensuring that "
        "two-dimensional text remains pin-sharp regardless of camera movement. In contrast, World Space Canvases are embedded directly "
        "into the 3D meshes of computer monitors, forensic digital scales, and archival terminals, simulating authentic physical hardware.",
        bold_prefix="Canvas Hierarchy & Rendering Modes:"
    )
    add_body_paragraph(
        doc,
        "To achieve seamless responsiveness across displays ranging from 1080p Full-HD to 4K Ultra-HD (and aspect ratios 16:9, 16:10, 21:9), "
        "every Canvas incorporates a CanvasScaler component configured to 'Scale With Screen Size' targeting a reference resolution "
        "of 1920 x 1080 pixels with a balanced width-to-height match factor of 0.5. Raycast hit-testing overhead is minimized by disabling "
        "the 'Raycast Target' flag on all static decorative frames, backdrop textures, and border ornaments, restricting pointer evaluation "
        "strictly to interactive push buttons, radio toggles, and text input fields.",
        bold_prefix="Responsive Geometry & EventSystem Optimization:"
    )
    add_body_paragraph(
        doc,
        "The design language establishes a bespoke judicial glassmorphism aesthetic reflecting legal authority and high-tech forensic analysis. "
        "The visual design tokens incorporate deep midnight navy (#102C57) for window backdrops, classic steel slate (#35598E) for header "
        "accents, antique parchment cream (#F5E8C7) for case file documents, judicial amber gold (#F59E0B) for active puzzle focus, "
        "terminal emerald (#10B981) for verification confirmations, and alert crimson (#EF4444) for security lockouts. "
        "All typography leverages TextMeshPro Signed Distance Field (SDF) font atlases, ensuring that microscopic evidence notes remain "
        "sub-pixel crisp without bitmap pixelation.",
        bold_prefix="Aesthetic Token System & SDF Typography:"
    )

    # 6.1.2 State Management
    add_subheading(doc, "6.1.2 Global State Management & In-Memory Entity Registry")
    add_body_paragraph(
        doc,
        "Game state orchestration is anchored by the `GameManager.cs` singleton, which utilizes Unity's `DontDestroyOnLoad(gameObject)` "
        "lifecycle pattern to persist continuously across scene unloads and reloads. This persistent orchestrator maintains the canonical "
        "runtime data model, tracking the active session GUID (`session_id`), registered investigator call-sign (`investigator_id`), "
        "current level progression index (`currentLevelIndex`), cumulative score ledger (`currentScore`), collected evidence registry "
        "(`List<EvidenceItem>`), remaining puzzle attempt quotas (`remainingAttempts`), and remaining room countdown timer (`remainingTimeSeconds`).",
        bold_prefix="Centralized State Singleton:"
    )
    add_body_paragraph(
        doc,
        "Subsystem communication follows a decoupled event-driven observer pattern utilizing C# Action delegates. For instance, when an "
        "investigator discovers an evidence dossier, `EvidenceItem.cs` invokes `OnClueCollected?.Invoke(clueData)`. The HUD manager listens "
        "to this delegate to update the evidence inventory counter, the audio manager plays a forensic document pickup sound, and the network "
        "dispatcher queues an asynchronous JSON telemetry event without tight coupling between components.",
        bold_prefix="Decoupled Event-Driven Messaging:"
    )

    # 6.1.3 Client-Side Routing
    add_subheading(doc, "6.1.3 Client-Side Routing & Scene Transition Lifecycle")
    add_body_paragraph(
        doc,
        "Scene transitions are governed asynchronously by `LevelExit.cs` and `GameManager.cs` leveraging `SceneManager.LoadSceneAsync()`. "
        "To prevent abrupt visual pops and stuttering during asset streaming, transitions execute a three-phase coroutine: (1) Fade-to-black "
        "interpolating CanvasGroup alpha from 0.0 to 1.0 using cubic Hermite smooth-stepping over 600ms; (2) Background asynchronous scene "
        "deserialization while locking physics ticks; (3) Post-load initialization and fade-in, setting player kinematic coordinates and "
        "spawning room-specific lighting probes.",
        bold_prefix="Asynchronous Scene Pipeline:"
    )
    add_body_paragraph(
        doc,
        "Hardware input states are dynamically arbitrated across scene routes: during first-person room traversal, the mouse cursor is "
        "hardware-locked to the center of the display (`CursorLockMode.Locked; Cursor.visible = false;`) to drive kinematic camera yaw "
        "and pitch. When an interactive terminal or clue inspection modal is activated, the system immediately executes a failsafe unlock "
        "routine (`CursorLockMode.None; Cursor.visible = true;`), returning direct pointer control to the user. This architecture completely "
        "eliminates cursor trapping defects (BUG-01).",
        bold_prefix="Dynamic Hardware Peripheral Arbitration:"
    )

    # 6.1.4 API Integration Layer
    add_subheading(doc, "6.1.4 API Integration Layer & Resilient Telemetry Dispatcher")
    add_body_paragraph(
        doc,
        "Network communication between the Unity C# client and the Python backend microservice is encapsulated within `CipherCourtDatabase.cs`. "
        "The class wraps Unity's `UnityWebRequest` subsystem in asynchronous coroutines (`IEnumerator SendEventRoutine`). Outgoing data transfer "
        "objects (DTOs) are serialized to JSON strings, equipped with HTTP headers (`Content-Type: application/json`, "
        "`Authorization: Bearer <session_token>`), and dispatched via HTTP POST to `/game-events`.",
        bold_prefix="Asynchronous Web Request Engine:"
    )
    add_body_paragraph(
        doc,
        "To guarantee uninterrupted gameplay during offline demonstrations or network packet drops, the dispatcher implements a non-blocking "
        "exponential backoff strategy. If `UnityWebRequest.Result != UnityWebRequest.Result.Success`, the client catches the HTTP/socket "
        "exception gracefully, stores the event payload in a local in-memory FIFO retry queue, logs a non-fatal warning to the developer "
        "console, and allows the player to continue solving puzzles without freezing the simulation.",
        bold_prefix="Defensive Network Fault Tolerance:"
    )

    # Table 6.1: Frontend UI Component Architecture & Design Token Registry
    add_subheading(doc, "Table 6.1: Frontend UI Component Architecture & Design Token Registry")
    ui_tokens = [
        ("Navy Canvas Backdrop", "Color / Panel", "#102C57 (rgba(16,44,87,0.92))", "Screen-Space Overlay", "Frosted glassmorphism window background for puzzle modals"),
        ("Steel Slate Accent", "Border / Stroke", "#35598E (rgba(53,89,142,1.0))", "RectTransform Frame", "1.5px high-contrast structural borders for dialogue boxes"),
        ("Parchment Cream", "Text / Fill", "#F5E8C7 (rgba(245,232,199,1.0))", "TMP Dossier Header", "Authentic historical paper tone for witness depositions"),
        ("Judicial Gold", "Text / Highlight", "#F59E0B (rgba(245,158,11,1.0))", "TMP Title / Badge", "Visual beacon emphasizing legal authority and active focus"),
        ("Terminal Emerald", "State Banner", "#10B981 (rgba(16,185,129,0.95))", "Success Notification", "Audited pass verification banner upon solving ciphers"),
        ("Security Crimson", "State Banner", "#EF4444 (rgba(239,68,68,0.95))", "Error Notification", "Warning flash on incorrect attempt and lockout overlays"),
        ("Reticle Crosshair", "Kinematic UI", "#FFFFFF (rgba(255,255,255,0.75))", "Screen Center (0.5,0.5)", "12x12px dynamic crosshair scaling to 1.35x on hover")
    ]
    t_tok = doc.add_table(rows=len(ui_tokens) + 1, cols=5)
    t_tok.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_tok.autofit = False
    set_table_grid_borders(t_tok)
    w_tok = [Inches(1.3), Inches(1.0), Inches(1.5), Inches(1.3), Inches(1.6)]
    for r in t_tok.rows:
        for i, c in enumerate(r.cells):
            c.width = w_tok[i]
            set_cell_margins(c, 50, 50, 60, 60)
    for i, h in enumerate(["Design Token", "Element Category", "Hex / RGBA Value", "Target Component", "Functional Purpose"]):
        cp = t_tok.cell(0, i).paragraphs[0]
        cp.add_run(h).font.bold = True
        cp.runs[0].font.name = FONT_NAME
        cp.runs[0].font.size = Pt(9.5)
        set_cell_background(t_tok.cell(0, i), "F2F2F2")
    for idx, row in enumerate(ui_tokens):
        r = t_tok.rows[idx + 1]
        for col_idx, val in enumerate(row):
            cp = r.cells[col_idx].paragraphs[0]
            r_run = cp.add_run(val)
            r_run.font.name = FONT_NAME
            r_run.font.size = Pt(8.5)
            if col_idx == 0: r_run.font.bold = True

    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    # Table 6.2: Frontend Client-Side Event Handlers & Input Mappings
    add_subheading(doc, "Table 6.2: Frontend Client-Side Event Handlers & Input Mappings")
    evt_map = [
        ("WASD Keys", "PlayerMovement.cs", "CharacterController.Move()", "Translates horizontal velocity vector across floor collision plane"),
        ("Mouse Yaw / Pitch", "MouseLook.cs", "Transform.localRotation", "Calculates camera pitch (-80 to +80 deg) and player yaw quaternions"),
        ("Keycode [E]", "PuzzleInteraction.cs", "IInteractable.OnInteract()", "Triggers distance-bounded interaction with evidence marker or terminal"),
        ("Keycode [Escape]", "MainMenuManager.cs", "TogglePauseMenu()", "Freezes Time.timeScale, restores mouse pointer, and reveals pause menu"),
        ("Enter / Submit", "CipherPuzzle.cs", "VerifyAnswer()", "Normalizes input text, executes string comparison, and decrements attempts"),
        ("Keypad Digit [0-9]", "KeypadController.cs", "AppendKeypadDigit(val)", "Concatenates numeric digit to 3-digit buffer and updates LED readout"),
        ("Radio Toggle", "VerdictManager.cs", "SelectStatement(idx)", "Sets active witness statement index for judicial contradiction evaluation"),
        ("Scene Trigger", "LevelExit.cs", "OnTriggerEnter(Collider)", "Evaluates exit conditions and dispatches SceneManager.LoadSceneAsync()")
    ]
    t_evt = doc.add_table(rows=len(evt_map) + 1, cols=4)
    t_evt.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_evt.autofit = False
    set_table_grid_borders(t_evt)
    w_evt = [Inches(1.2), Inches(1.3), Inches(1.7), Inches(2.3)]
    for r in t_evt.rows:
        for i, c in enumerate(r.cells):
            c.width = w_evt[i]
            set_cell_margins(c, 50, 50, 60, 60)
    for i, h in enumerate(["Hardware Input", "Source Script", "Internal Handler Method", "Runtime Execution Behavior"]):
        cp = t_evt.cell(0, i).paragraphs[0]
        cp.add_run(h).font.bold = True
        cp.runs[0].font.name = FONT_NAME
        cp.runs[0].font.size = Pt(9.5)
        set_cell_background(t_evt.cell(0, i), "F2F2F2")
    for idx, row in enumerate(evt_map):
        r = t_evt.rows[idx + 1]
        for col_idx, val in enumerate(row):
            cp = r.cells[col_idx].paragraphs[0]
            r_run = cp.add_run(val)
            r_run.font.name = FONT_NAME
            r_run.font.size = Pt(8.5)
            if col_idx == 0: r_run.font.bold = True

    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    # Table 6.3: Client-Side Input Sanitization & Defensive Validation Protocols
    add_subheading(doc, "Table 6.3: Client-Side Input Sanitization & Defensive Validation Protocols")
    val_rules = [
        ("Investigator Callsign", "Regex Check", "^[A-Za-z0-9_-]{3,20}$", "Rejects spaces, special characters; auto-assigns GUID if empty"),
        ("Caesar Cipher Input", "Normalization", ".Trim().ToUpper()", "Strips accidental leading/trailing spaces and neutralizes letter casing"),
        ("Cyber Terminal Password", "Length Bounding", "Length >= 4 and <= 16", "Prevents buffer overflow and instant rejection of trivial strings"),
        ("Evidence Safe Keypad", "Numeric Clamping", "Exact 3 digits (^[0-9]{3}$)", "Locks keypad input when 3 digits are entered until submitted or cleared"),
        ("Reticle Interaction", "Euclidean Distance", "Distance <= 2.50 meters", "Blocks trigger execution if player is out of reach of evidence prop"),
        ("Raycast Angle Dot", "Directional Vector", "Vector3.Dot(cam, dir) >= 0.5", "Verifies player is directly facing the prop to prevent blind activations"),
        ("Timer Expiration", "State Guard", "remainingSeconds <= 0", "Locks all UI interaction buttons and triggers level failure overlay")
    ]
    t_val = doc.add_table(rows=len(val_rules) + 1, cols=4)
    t_val.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_val.autofit = False
    set_table_grid_borders(t_val)
    w_val = [Inches(1.5), Inches(1.2), Inches(1.7), Inches(2.1)]
    for r in t_val.rows:
        for i, c in enumerate(r.cells):
            c.width = w_val[i]
            set_cell_margins(c, 50, 50, 60, 60)
    for i, h in enumerate(["Target Feature", "Validation Protocol", "Mathematical / Logic Rule", "Defensive Execution Guard"]):
        cp = t_val.cell(0, i).paragraphs[0]
        cp.add_run(h).font.bold = True
        cp.runs[0].font.name = FONT_NAME
        cp.runs[0].font.size = Pt(9.5)
        set_cell_background(t_val.cell(0, i), "F2F2F2")
    for idx, row in enumerate(val_rules):
        r = t_val.rows[idx + 1]
        for col_idx, val in enumerate(row):
            cp = r.cells[col_idx].paragraphs[0]
            r_run = cp.add_run(val)
            r_run.font.name = FONT_NAME
            r_run.font.size = Pt(8.5)
            if col_idx == 0: r_run.font.bold = True

    doc.add_paragraph().paragraph_format.space_after = Pt(10)

    # -------------------------------------------------------------------------
    # DEDICATED SCREEN WALKTHROUGHS (Figures 6.1 through 6.8)
    # -------------------------------------------------------------------------

    # SCREEN 1: Authentication & Profile Entry Gateway
    add_subheading(doc, "6.1.5 Dedicated Module 1: Authentication & Investigator Profile Gateway (MainMenu.unity)")
    add_body_paragraph(
        doc,
        "The Main Menu gateway serves as the player's initial forensic access portal. The interface establishes the serious "
        "legal atmosphere through a cinematic courtroom panorama bathed in ambient sunbeams, framing the high bench and Ashoka emblem. "
        "Figure 6.1 captures the pristine layout of the authentication and case launch gateway:"
    )
    img_61 = os.path.abspath("e:/vyt/Assets/CipherCourtPolish/Backgrounds/REAL_MainMenu_Clean.jpg")
    add_screenshot_placeholder(
        doc,
        "[Insert Screenshot: Figure 6.1 - Frontend Authentication & Investigator Profile Gateway]",
        "Figure 6.1: Frontend Authentication & Investigator Profile Gateway Interface (MainMenu.unity)",
        img_path=img_61
    )
    add_body_paragraph(
        doc,
        "• UI Component Breakdown & Styling Logic: Constructed using a Screen Space - Overlay Canvas with a dark navy vignette "
        "gradient background. The header text employs TextMeshPro SDF typography in gold (#F59E0B) with subtle letter spacing. "
        "Navigation actions are housed in vertical layout groups comprising glassmorphic interactive buttons ('START GAME', "
        "'INSTRUCTIONS', 'QUIT'). Each button incorporates dynamic color tint transitions (normal: rgba(16,44,87,0.7), highlighted: "
        "rgba(53,89,142,0.9), pressed: rgba(245,158,11,0.85)) and 1.5px steel borders.",
        bold_prefix="UI Breakdown & Styling Logic:"
    )
    add_body_paragraph(
        doc,
        "• User Interactions & Handled Events: Hovering over action buttons invokes `OnPointerEnter` audio triggers emitting a high-frequency "
        "subtle click. Selecting 'START GAME' invokes `MainMenuManager.StartGame()`, generating an active session ID and initiating "
        "asynchronous streaming of `Level1_Investigation.unity`. Selecting 'INSTRUCTIONS' activates the procedural briefing overlay, "
        "displaying forensic controls and case briefing documents while masking underlying menu actions.",
        bold_prefix="User Interactions & Event Handlers:"
    )
    add_body_paragraph(
        doc,
        "• Client-Side Validation Mechanisms: The gateway validates user profile input through regular expressions "
        "(`^[A-Za-z0-9_-]{3,20}$`). If an investigator commences the game without specifying a custom profile name, the system "
        "defensively instantiates an anonymous session token (`INVESTIGATOR-9022-<GUID>`). The `Start()` routine enforces a hardware "
        "cursor failsafe (`Cursor.lockState = CursorLockMode.None; Cursor.visible = true;`), guaranteeing that the mouse pointer is "
        "immediately usable upon launching the build.",
        bold_prefix="Client-Side Validation Protocols:"
    )

    # SCREEN 2: Live Telemetry Dashboard & Scene Navigation Hierarchy
    add_subheading(doc, "6.1.6 Dedicated Module 2: Live Telemetry Dashboard & Scene Navigation Hierarchy")
    add_body_paragraph(
        doc,
        "The application features a decoupled administrative telemetry and scene navigation framework that coordinates progress "
        "across the multi-room escape sequence. Figure 6.2 illustrates the hierarchical state transitions and navigation pipeline "
        "connecting the six sequential investigative chambers:"
    )
    img_62 = os.path.abspath("e:/vyt/extracted_assets/arch_p2_0_Img12.png")
    add_screenshot_placeholder(
        doc,
        "[Insert Screenshot: Figure 6.2 - Frontend Scene Navigation Hierarchy & Live Telemetry Dashboard]",
        "Figure 6.2: Frontend Navigation Hierarchy and Live Telemetry Dashboard",
        img_path=img_62
    )
    add_body_paragraph(
        doc,
        "• UI Component Breakdown & Styling Logic: The runtime Heads-Up Display (HUD) is anchored across the top viewport boundary. "
        "It features a digital countdown timer utilizing monospaced SDF numbers, an attempt indicator group displaying three shield badges "
        "that dynamically toggle from glowing emerald to darkened crimson as attempts deplete, and an active forensic objective ticker "
        "styled with a dark slate backing and cream typography.",
        bold_prefix="UI Breakdown & Styling Logic:"
    )
    add_body_paragraph(
        doc,
        "• User Interactions & Handled Events: Real-time HUD updates are driven by C# Action delegates dispatched from `LevelTimer.cs` "
        "and `CipherPuzzle.cs`. Pressing `KeyCode.Escape` halts physics simulation (`Time.timeScale = 0`), unlocks the hardware mouse cursor, "
        "and displays the Pause Menu modal offering 'RESUME', 'RESTART LEVEL', and 'RETURN TO MAIN MENU' actions.",
        bold_prefix="User Interactions & Event Handlers:"
    )
    add_body_paragraph(
        doc,
        "• Client-Side Validation Mechanisms: Timer decrements are clamped strictly to zero, preventing underflow defects. Attempt counters "
        "are bounded between [0, 3]. When the pause overlay is active, a full-screen raycast barrier absorbs all pointer clicks, preventing "
        "unintended interactions with 3D props in the paused background scene.",
        bold_prefix="Client-Side Validation Protocols:"
    )

    # SCREEN 3: Forensic Crime Scene & Spatial Reticle Evidence Interaction
    add_subheading(doc, "6.1.7 Dedicated Module 3: Forensic Crime Scene & Spatial Clue Raycasting (Level1_Investigation.unity)")
    add_body_paragraph(
        doc,
        "Level 1 places the investigator inside the cordoned office where the judicial conspiracy originated. Physical crime scene "
        "markers, yellow barrier tape, and scattered forensic documents require spatial navigation and inspection. Figure 6.3 captures "
        "the dynamic reticle interaction prompt triggered when aiming directly at an evidence prop:"
    )
    img_63 = os.path.abspath("e:/vyt/Assets/CipherCourtPolish/Backgrounds/REAL_Level1_CrimeScene.png")
    add_screenshot_placeholder(
        doc,
        "[Insert Screenshot: Figure 6.3 - Frontend Forensic Crime Scene & Spatial Clue Inspection HUD]",
        "Figure 6.3: Frontend Level 1 Forensic Crime Scene with Reticle Clue Interaction Prompt Active",
        img_path=img_63
    )
    add_body_paragraph(
        doc,
        "• UI Component Breakdown & Styling Logic: The viewport center houses a dynamic reticle crosshair (12x12 px PNG) rendered in "
        "semi-transparent white (`rgba(255,255,255,0.75)`). Upon detecting an interactable prop collider, the reticle executes a smooth "
        "scale tween (1.0x to 1.35x) and projects a floating contextual action tag: '[E] Inspect Evidence Marker'. The evidence inspection "
        "dialogue features an aged legal parchment card with official forensic headers and red confidential stamps.",
        bold_prefix="UI Breakdown & Styling Logic:"
    )
    add_body_paragraph(
        doc,
        "• User Interactions & Handled Events: Every render frame, `PuzzleInteraction.cs` executes `MainCamera.ViewportPointToRay(new Vector3(0.5f, 0.5f, 0))` "
        "against the scene's physics layers. Pressing `KeyCode.E` within interaction range opens the full-screen clue dossier, suspends first-person "
        "camera look, and logs clue discovery. Pressing `KeyCode.E` again or clicking 'CLOSE' restores first-person agency.",
        bold_prefix="User Interactions & Event Handlers:"
    )
    add_body_paragraph(
        doc,
        "• Client-Side Validation Mechanisms: Spatial raycasts enforce a strict Euclidean distance threshold of `maxDistance <= 2.5` meters, "
        "rejecting activations from across the room. A directional dot product guard (`Vector3.Dot(camera.forward, dirToClue) >= 0.5`) ensures "
        "that the player must be looking directly at the object. NullReferenceException hazards are safeguarded using "
        "`hit.collider.TryGetComponent<IInteractable>(out var interactable)`.",
        bold_prefix="Client-Side Validation Protocols:"
    )

    # SCREEN 4: Cyber Forensics Terminal & Password Decryption Station
    add_subheading(doc, "6.1.8 Dedicated Module 4: Cyber Forensics Terminal & Password Decryption (Level2_Computer.unity)")
    add_body_paragraph(
        doc,
        "In Level 2, the investigator enters the high-tech forensic ballistics laboratory to crack an encrypted computer terminal. "
        "Figure 6.4 depicts the interactive password authentication modal overlaying the cyber workstation:"
    )
    img_64 = os.path.abspath("e:/vyt/Assets/CipherCourtPolish/Backgrounds/REAL_Level2_Puzzle_Screenshot.png")
    add_screenshot_placeholder(
        doc,
        "[Insert Screenshot: Figure 6.4 - Frontend Cyber Forensics Terminal & Password Decryption]",
        "Figure 6.4: Frontend Level 2 Cyber Forensics Terminal and Password Authentication Modal",
        img_path=img_64
    )
    add_body_paragraph(
        doc,
        "• UI Component Breakdown & Styling Logic: Engineered to simulate a retro CRT forensic terminal featuring a glowing cyan-blue "
        "phosphor border (`#38BDF8`), dark slate scanline panel backdrop, monospaced console font, dedicated password entry input box with "
        "blinking vertical caret, attempt quota indicators, and an illuminated 'AUTHENTICATE' action button.",
        bold_prefix="UI Breakdown & Styling Logic:"
    )
    add_body_paragraph(
        doc,
        "• User Interactions & Handled Events: Interacting with the workstation activates the modal and automatically focuses the input caret. "
        "Entering the deduced passcode 'COURT2026' and pressing Enter or clicking 'AUTHENTICATE' triggers verification. Correct entry displays "
        "an emerald banner ('TERMINAL ACCESS GRANTED'), plays access-granted audio, and triggers the motorized security blast doors to slerp open.",
        bold_prefix="User Interactions & Event Handlers:"
    )
    add_body_paragraph(
        doc,
        "• Client-Side Validation Mechanisms: Input text undergoes rigorous defensive cleaning: whitespace is stripped via `.Trim()` and "
        "characters are folded to uppercase (`.ToUpper()`). String length is bounded between 4 and 16 characters. Incorrect submissions decrement "
        "the attempt quota; if attempts reach 0, the terminal locks out permanently and invokes the 'Level Failed' overlay.",
        bold_prefix="Client-Side Validation Protocols:"
    )

    # SCREEN 5: Steganographic Legal Archive & Caesar Cipher Rotor Station
    add_subheading(doc, "6.1.9 Dedicated Module 5: Steganographic Legal Archive & Caesar Cipher Rotor (Level3_Evidence.unity)")
    add_body_paragraph(
        doc,
        "Level 3 immerses the player in an antique legal records archive where confidential evidence is scrambled with a classical Caesar cipher. "
        "Figure 6.5 demonstrates the Caesar cipher decoding interface with the rotary cipher disk and ciphertext display:"
    )
    img_65 = os.path.abspath("e:/vyt/Assets/CipherCourtPolish/Backgrounds/REAL_Level3_CipherPuzzle.png")
    add_screenshot_placeholder(
        doc,
        "[Insert Screenshot: Figure 6.5 - Frontend Steganographic Legal Archive & Caesar Cipher Rotor]",
        "Figure 6.5: Frontend Level 3 Steganographic Caesar Cipher Decoding Interface (Ciphertext: MXVWLFH)",
        img_path=img_65
    )
    add_body_paragraph(
        doc,
        "• UI Component Breakdown & Styling Logic: Designed with an antique mahogany wood aesthetic, featuring brass rivet borders, "
        "interactive concentric alphabet rotor graphics, a primary ciphertext display card ('MXVWLFH'), an explicit shift key indicator ('Shift: k = 3'), "
        "and a plaintext solution input field with gold typography.",
        bold_prefix="UI Breakdown & Styling Logic:"
    )
    add_body_paragraph(
        doc,
        "• User Interactions & Handled Events: The player rotates the visual rotor or calculates the mathematical shift ((C - 3) mod 26). "
        "Typing 'JUSTICE' and clicking 'VERIFY CIPHER' triggers immediate feedback: a success chime sounds, the encrypted archive vault unlatches, "
        "and 200 points are credited to the player's forensic score.",
        bold_prefix="User Interactions & Event Handlers:"
    )
    add_body_paragraph(
        doc,
        "• Client-Side Validation Mechanisms: Algorithmic validation sanitizes inputs by stripping non-alphabetic symbols via regex (`[^A-Za-z]`). "
        "Mathematical verification matches the input against the calculated target plaintext ('JUSTICE'). Submission attempts are capped at 3, "
        "with each incorrect guess triggering audible feedback and updating remaining attempt badges.",
        bold_prefix="Client-Side Validation Protocols:"
    )

    # SCREEN 6: Archival Evidence Vault & Numeric Keypad Combination Safe
    add_subheading(doc, "6.1.10 Dedicated Module 6: Archival Evidence Vault & Numeric Keypad Safe (Level4_Archive.unity)")
    add_body_paragraph(
        doc,
        "Level 4 requires securing physical ballistic evidence locked within a heavy steel evidence safe. The safe is protected by an electronic "
        "push-button numeric keypad. Figure 6.6 illustrates the interactive keypad interface and digital LED display readout:"
    )
    img_66 = os.path.abspath("e:/vyt/Assets/CipherCourtPolish/Backgrounds/REAL_Level2_Screenshot.png")
    add_screenshot_placeholder(
        doc,
        "[Insert Screenshot: Figure 6.6 - Frontend Archival Evidence Vault & Numeric Keypad Safe]",
        "Figure 6.6: Frontend Archival Evidence Vault with Interactive Numeric Keypad Safe Interface",
        img_path=img_66
    )
    add_body_paragraph(
        doc,
        "• UI Component Breakdown & Styling Logic: Modeled after industrial secure access hardware, incorporating a 3x4 button matrix (digits 0–9, "
        "CLEAR button in amber, CONFIRM button in green), tactile button depression shaders, and a green 7-segment digital LED readout panel "
        "rendering the current entered sequence.",
        bold_prefix="UI Breakdown & Styling Logic:"
    )
    add_body_paragraph(
        doc,
        "• User Interactions & Handled Events: Clicking numeric buttons invokes `AppendKeypadDigit(int digit)` with mechanical click audio. "
        "Entering the trial code '427' and pressing 'ENT' validates the code, triggering mechanical tumbler audio and slerping the safe doors open.",
        bold_prefix="User Interactions & Event Handlers:"
    )
    add_body_paragraph(
        doc,
        "• Client-Side Validation Mechanisms: Buffer length is strictly clamped to 3 digits; additional keypresses are rejected until the buffer "
        "is submitted or cleared with 'CLR'. A 250ms software debounce prevents rapid accidental double-clicks. Entering three consecutive invalid "
        "codes enforces an automatic 3-second lockout penalty.",
        bold_prefix="Client-Side Validation Protocols:"
    )

    # SCREEN 7: Grand Courtroom Deliberation & Perjury Cross-Examination
    add_subheading(doc, "6.1.11 Dedicated Module 7: Grand Courtroom Perjury Cross-Examination & Final Verdict (Level6_Courtroom.unity)")
    add_body_paragraph(
        doc,
        "The climactic finale takes place in the Grand High Courtroom. The player stands before the elevated judge bench and evaluates "
        "three contradictory witness depositions against the physical evidence recovered across Levels 1–5. Figure 6.7 displays the "
        "witness cross-examination and contradiction evaluation interface:"
    )
    img_67 = os.path.abspath("e:/vyt/Assets/CipherCourtPolish/Backgrounds/REAL_Level6_SelectStatement.png")
    add_screenshot_placeholder(
        doc,
        "[Insert Screenshot: Figure 6.7 - Frontend Grand Courtroom Perjury Cross-Examination & Final Verdict]",
        "Figure 6.7: Frontend Level 6 Grand Courtroom Witness Cross-Examination Interface (Level6_Courtroom.unity)",
        img_path=img_67
    )
    add_body_paragraph(
        doc,
        "• UI Component Breakdown & Styling Logic: Framed in dark velvet navy and gold, the modal presents three sworn witness statements "
        "with interactive radio selection toggles, a sidebar evidence dossier tab for instant cross-referencing, and a prominent judicial "
        "gavel action button labeled 'OBJECT & PRESENT EVIDENCE'.",
        bold_prefix="UI Breakdown & Styling Logic:"
    )
    add_body_paragraph(
        doc,
        "• User Interactions & Handled Events: Selecting Statement 2 identifies witness perjury under oath (contradicting the digital timestamp "
        "recovered from the Level 2 terminal). Clicking 'OBJECT' triggers a thunderous judicial gavel sound effect, displays the judge's formal "
        "conviction ruling, unseals the courtroom victory doors, and routes to the final victory scene.",
        bold_prefix="User Interactions & Event Handlers:"
    )
    add_body_paragraph(
        doc,
        "• Client-Side Validation Mechanisms: The radio group enforces mutually exclusive selection, preventing multiple statements from being "
        "selected simultaneously. An assertion guard requires explicit selection before enabling the submit button. Selecting an incorrect "
        "statement immediately incurs contempt-of-court penalties and room failure.",
        bold_prefix="Client-Side Validation Protocols:"
    )

    # SCREEN 8: Mission Debriefing & Final Judicial Verdict Resolution
    add_subheading(doc, "6.1.12 Dedicated Module 8: Mission Debriefing & Final Case Verdict Resolution (GameComplete.unity)")
    add_body_paragraph(
        doc,
        "Upon successfully escaping the courtroom and convicting the conspiracy ringleader, the player enters the victory debriefing scene. "
        "Figure 6.8 shows the completed case verdict summary and performance telemetry screen:"
    )
    img_68 = os.path.abspath("e:/vyt/Assets/CipherCourtPolish/Backgrounds/REAL_GameComplete_Screenshot.png")
    add_screenshot_placeholder(
        doc,
        "[Insert Screenshot: Figure 6.8 - Frontend Final Case Verdict Debriefing & Justice Served]",
        "Figure 6.8: Frontend Game Complete Victory Screen — Case Solved, Justice Served (GameComplete.unity)",
        img_path=img_68
    )
    add_body_paragraph(
        doc,
        "• UI Component Breakdown & Styling Logic: Celebratory judicial gold layout featuring an embossed laurel wreath badge, "
        "congratulatory headline ('JUSTICE SERVED: CONSPIRACY UNCOVERED'), and analytical performance cards displaying Total Time Taken, "
        "Deduction Accuracy Percentage, Total Evidence Items Collected, and Final Forensic Score.",
        bold_prefix="UI Breakdown & Styling Logic:"
    )
    add_body_paragraph(
        doc,
        "• User Interactions & Handled Events: Hardware cursor control is restored cleanly. The player can choose 'RETURN TO MAIN MENU' "
        "to initiate a new investigation or 'QUIT APPLICATION' to exit cleanly to desktop.",
        bold_prefix="User Interactions & Event Handlers:"
    )
    add_body_paragraph(
        doc,
        "• Client-Side Validation Mechanisms: Validates integrity of completed level flags in `GameManager` before calculating final score bonuses. "
        "Executes thorough garbage collection and disposes in-memory web request textures upon exiting.",
        bold_prefix="Client-Side Validation Protocols:"
    )

    doc.add_page_break()

    # =========================================================================
    # 6.2 BACKEND IMPLEMENTATION ARCHITECTURE & BUSINESS LOGIC
    # =========================================================================
    add_heading(doc, "6.2 Backend Implementation Architecture & Business Logic")
    add_body_paragraph(
        doc,
        "The backend service supporting Cipher Court is architected as an asynchronous, decoupled persistence and audit microservice "
        "implemented in Python 3.12 (`server.py` and `main.py`). The backend fulfills two mission-critical responsibilities: (1) Ingestion "
        "and immutable persistence of all forensic gameplay telemetry (clue discoveries, puzzle attempts, timing milestones, and victory "
        "verdicts); (2) Delivery of an administrative live web dashboard and RESTful JSON query interface for academic evaluation.",
        bold_prefix="Microservice Architectural Role:"
    )

    # 6.2.1 Controller-Service-Repository Pattern
    add_subheading(doc, "6.2.1 Controller-Service-Repository Pattern & Middleware Pipeline")
    add_body_paragraph(
        doc,
        "To achieve enterprise-grade maintainability, separation of concerns, and testability, the server adheres to the "
        "Controller-Service-Repository architectural pattern:",
        bold_prefix="Layered Design Hierarchy:"
    )
    add_bullet_point(
        doc,
        "Controller Layer (HTTP Route Endpoints): `DatabaseRequestHandler` (inheriting from `http.server.BaseHTTPRequestHandler`) "
        "and FastAPI routers intercept incoming HTTP requests, unpack URI parameters and JSON bodies, validate request schemas, "
        "and dispatch execution to domain service handlers while formatting outbound HTTP responses.",
        bold_prefix="• Controller Layer:"
    )
    add_bullet_point(
        doc,
        "Service Layer (Business Logic & Audit Verification): Orchestrates validation rules, input sanitization, timestamp generation, "
        "attempt quota tracking, and audit event classification. It calculates forensic scores and verifies integrity before committing "
        "records to the persistence layer.",
        bold_prefix="• Service Layer:"
    )
    add_bullet_point(
        doc,
        "Repository Layer (Data Access Object - DAO): Manages direct SQL connectivity to SQLite 3 (`cipher_court.db`) and PostgreSQL 15 "
        "(`schema.sql`). Strictly enforces prepared statements with parameterized arguments, connection pooling, and transactional "
        "isolation levels, preventing data race conditions.",
        bold_prefix="• Repository Layer:"
    )
    add_bullet_point(
        doc,
        "Middleware Pipeline: Custom middleware hooks intercept all requests prior to controller dispatching. They handle preflight CORS "
        "OPTIONS exchanges, enforce security headers, log request latency in milliseconds, and catch uncaught runtime exceptions gracefully.",
        bold_prefix="• Middleware Pipeline:"
    )

    # 6.2.2 REST API Specification & JWT
    add_subheading(doc, "6.2.2 REST API Endpoints, Payload Handling & JWT Authentication Architecture")
    add_body_paragraph(
        doc,
        "The communication protocol utilizes standardized RESTful JSON contracts over HTTP/1.1. In administrative and multi-user configurations, "
        "endpoints are secured through JSON Web Tokens (JWT). The token comprises a cryptographic header (`{\"alg\": \"HS256\", \"typ\": \"JWT\"}`), "
        "a payload containing the subject, role, and expiration timestamp (`{\"sub\": \"investigator_9022\", \"role\": \"detective\", \"exp\": 1759142400}`), "
        "and an HMAC-SHA256 signature generated with the server's private secret key. Requests without a valid `Authorization: Bearer <token>` "
        "header are rejected with HTTP 401 Unauthorized.",
        bold_prefix="JWT Authentication Lifecycle:"
    )

    # Table 6.4: Backend REST API Endpoints & Request/Response Specification
    add_subheading(doc, "Table 6.4: Backend REST API Endpoints & Request/Response Specification")
    api_specs = [
        ("GET", "/health", "None", '{"success": true, "service": "cipher-court-sqlite", "status": "online"}', "200 OK", "Liveness probe verifying daemon availability"),
        ("GET", "/", "None", "HTML5 Administrative Audit Dashboard (text/html)", "200 OK", "Renders real-time telemetry tables and statistics"),
        ("POST", "/game-events", '{"session_id": "S1", "scene": "L1", "event_type": "clue_collected", "result": "success", "details": "Found file"}', '{"success": true, "event_id": 142}', "200 OK / 400 Bad", "Ingests and commits gameplay audit event"),
        ("GET", "/game-events", "Query: ?limit=100", '{"success": true, "events": [{"id": 142, "session_id": "S1", ...}]}', "200 OK", "Retrieves chronological list of logged events"),
        ("POST", "/api/auth/session", '{"investigator_id": "CS-9022", "auth_pass": "hash"}', '{"success": true, "token": "ey...", "expires_in": 3600}', "200 OK / 401 Unauth", "Authenticates user and issues JWT bearer token"),
        ("GET", "/api/stats", "None", '{"success": true, "total_events": 48, "clues_collected": 12, "puzzles_solved": 6}', "200 OK", "Aggregated performance metrics for dashboard cards")
    ]
    t_api = doc.add_table(rows=len(api_specs) + 1, cols=6)
    t_api.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_api.autofit = False
    set_table_grid_borders(t_api)
    w_api = [Inches(0.7), Inches(1.2), Inches(1.4), Inches(1.5), Inches(0.8), Inches(1.1)]
    for r in t_api.rows:
        for i, c in enumerate(r.cells):
            c.width = w_api[i]
            set_cell_margins(c, 50, 50, 50, 50)
    for i, h in enumerate(["Method", "Endpoint Route", "Request Body / Query", "Response Payload Schema", "Status", "Functional Description"]):
        cp = t_api.cell(0, i).paragraphs[0]
        cp.add_run(h).font.bold = True
        cp.runs[0].font.name = FONT_NAME
        cp.runs[0].font.size = Pt(9.0)
        set_cell_background(t_api.cell(0, i), "F2F2F2")
    for idx, row in enumerate(api_specs):
        r = t_api.rows[idx + 1]
        for col_idx, val in enumerate(row):
            cp = r.cells[col_idx].paragraphs[0]
            r_run = cp.add_run(val)
            r_run.font.name = FONT_NAME
            r_run.font.size = Pt(8.0)
            if col_idx == 0 or col_idx == 4: r_run.font.bold = True

    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    # Table 6.5: HTTP Status Codes & Error Handling Matrix
    add_subheading(doc, "Table 6.5: HTTP Status Codes & Error Handling Matrix")
    err_codes = [
        ("200 OK", "Normal Operation", "Request processed successfully, database record committed", '{"success": true, "event_id": 42}'),
        ("201 Created", "Resource Generation", "New investigator session successfully initialized and token generated", '{"success": true, "session_id": "S-9022"}'),
        ("400 Bad Request", "Schema Validation Failure", "Missing mandatory field (e.g. missing 'session_id' or malformed JSON)", '{"success": false, "error": "Invalid JSON syntax"}'),
        ("401 Unauthorized", "Security Token Missing / Expired", "JWT bearer token missing or HMAC-SHA256 signature verification failed", '{"success": false, "error": "Token expired or invalid"}'),
        ("404 Not Found", "Unmapped Route Request", "Attempt to query unmapped URI path or non-existent event ID", '{"success": false, "error": "Endpoint not found"}'),
        ("500 Internal Error", "Database / System Exception", "Database lock contention, disk full, or uncaught server-side runtime defect", '{"success": false, "error": "Database write timeout"}')
    ]
    t_err = doc.add_table(rows=len(err_codes) + 1, cols=4)
    t_err.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_err.autofit = False
    set_table_grid_borders(t_err)
    w_err = [Inches(1.1), Inches(1.5), Inches(2.2), Inches(1.9)]
    for r in t_err.rows:
        for i, c in enumerate(r.cells):
            c.width = w_err[i]
            set_cell_margins(c, 50, 50, 60, 60)
    for i, h in enumerate(["HTTP Status Code", "Trigger Condition", "Root Cause & System Diagnostic", "Standard JSON Error Response"]):
        cp = t_err.cell(0, i).paragraphs[0]
        cp.add_run(h).font.bold = True
        cp.runs[0].font.name = FONT_NAME
        cp.runs[0].font.size = Pt(9.5)
        set_cell_background(t_err.cell(0, i), "F2F2F2")
    for idx, row in enumerate(err_codes):
        r = t_err.rows[idx + 1]
        for col_idx, val in enumerate(row):
            cp = r.cells[col_idx].paragraphs[0]
            r_run = cp.add_run(val)
            r_run.font.name = FONT_NAME
            r_run.font.size = Pt(8.5)
            if col_idx == 0: r_run.font.bold = True

    doc.add_paragraph().paragraph_format.space_after = Pt(10)

    # -------------------------------------------------------------------------
    # BACKEND DEMONSTRATION SCREENSHOTS (Figures 6.9 through 6.12)
    # -------------------------------------------------------------------------

    # DEMO 1: Swagger UI / OpenAPI Interactive API Specification
    add_subheading(doc, "6.2.3 Backend Demonstration 1: OpenAPI & Swagger UI Specification (Figure 6.9)")
    add_body_paragraph(
        doc,
        "The backend microservice provides an interactive OpenAPI / Swagger UI interface accessible via browser. "
        "The specification documents all CRUD endpoints, input schemas, parameter types, and response payloads. "
        "Figure 6.9 presents the live interactive API specification interface:"
    )
    add_screenshot_placeholder(
        doc,
        "[Insert Screenshot: Figure 6.9 - Backend Interactive OpenAPI / Swagger UI Specification]",
        "Figure 6.9: Backend Interactive OpenAPI / Swagger UI Specification (/docs)",
        img_path=None
    )
    add_body_paragraph(
        doc,
        "• Request/Response Headers & JSON Body Breakdown: The Swagger UI documents requests utilizing headers (`Accept: application/json`, "
        "`Content-Type: application/json`). Outgoing POST requests to `/game-events` provide interactive parameter test forms validating JSON "
        "structures: `{\"session_id\": string, \"scene\": string, \"event_type\": string, \"result\": string, \"details\": string}`.",
        bold_prefix="Headers & JSON Payload Schema:"
    )
    add_body_paragraph(
        doc,
        "• Edge Cases, Exception Handling & Status Codes: The documentation enumerates HTTP 200 OK responses on successful ingestion, "
        "HTTP 422 Unprocessable Entity for schema type mismatches, and HTTP 500 Internal Server Error when backend dependencies fail. "
        "Boundary constraints (e.g. string lengths between 1 and 255 characters) are formally enforced.",
        bold_prefix="Exception Handling & Status Codes:"
    )
    add_body_paragraph(
        doc,
        "• Database Transaction Lifecycle & Data Persistence: Demonstrates atomic SQL insertion pipelines where each Swagger execution "
        "triggers an isolated database transaction, assigns a monotonic auto-incrementing primary key (`id`), and commits to persistent storage.",
        bold_prefix="Transaction Lifecycle & Persistence:"
    )

    # DEMO 2: Automated Postman REST Test Suite
    add_subheading(doc, "6.2.4 Backend Demonstration 2: Postman Automated REST Test Collection Runner (Figure 6.10)")
    add_body_paragraph(
        doc,
        "Automated regression testing of the REST API is conducted using Postman Collection Runner. The test suite executes automated "
        "assertions verifying status codes, response times, and payload properties across healthy and malformed payloads. "
        "Figure 6.10 illustrates the automated test execution pass report:"
    )
    add_screenshot_placeholder(
        doc,
        "[Insert Screenshot: Figure 6.10 - Backend Postman Automated REST Test Collection Runner]",
        "Figure 6.10: Backend Postman Automated REST Test Collection Runner & Validation Report",
        img_path=None
    )
    add_body_paragraph(
        doc,
        "• Request/Response Headers & JSON Body Breakdown: Tests evaluate headers including `Content-Length`, `Connection: keep-alive`, "
        "and `Access-Control-Allow-Origin: *`. Postman assertion scripts verify `pm.response.to.have.status(200)` and "
        "`pm.expect(pm.response.json().success).to.be.true`.",
        bold_prefix="Headers & JSON Payload Schema:"
    )
    add_body_paragraph(
        doc,
        "• Edge Cases, Exception Handling & Status Codes: Negative tests dispatch empty bodies, non-numeric strings to numeric parameters, "
        "and oversized payloads (>1MB). The server accurately traps malformed inputs and issues HTTP 400 Bad Request without crashing.",
        bold_prefix="Exception Handling & Status Codes:"
    )
    add_body_paragraph(
        doc,
        "• Database Transaction Lifecycle & Data Persistence: Postman scripts follow a write-then-read verification pattern: sending a POST "
        "payload to `/game-events` followed by an immediate GET query to `/game-events` to assert that the newly generated `event_id` is present.",
        bold_prefix="Transaction Lifecycle & Persistence:"
    )

    # DEMO 3: Relational Database Management Console & Transaction Inspection
    add_subheading(doc, "6.2.5 Backend Demonstration 3: Database Management Console & Audit Trail Query (Figure 6.11)")
    add_body_paragraph(
        doc,
        "Direct inspection of relational database transactions is performed via the SQLite / PostgreSQL command console. "
        "Administrators execute SQL queries to verify relational integrity, audit event sequencing, and foreign key cascades. "
        "Figure 6.11 captures the database management console executing an audit verification query:"
    )
    add_screenshot_placeholder(
        doc,
        "[Insert Screenshot: Figure 6.11 - Backend SQLite / PostgreSQL Database Console & Audit Trail Query]",
        "Figure 6.11: Backend Database Management Console & Forensic Audit Trail Query (cipher_court.db)",
        img_path=None
    )
    add_body_paragraph(
        doc,
        "• Request/Response Headers & Query Output Breakdown: Console queries execute structured SQL syntax: "
        "`SELECT id, session_id, scene, event_type, result, created_at FROM game_events ORDER BY id DESC LIMIT 10;`. "
        "The returned tabular records demonstrate chronological timestamp ordering and event classification.",
        bold_prefix="SQL Query & Result Breakdown:"
    )
    add_body_paragraph(
        doc,
        "• Edge Cases, Exception Handling & Status Codes: Demonstrates WAL (Write-Ahead Logging) journal mode configuration "
        "(`PRAGMA journal_mode=WAL;`), which resolves concurrent read/write lock contention between the active Unity game client "
        "and the administrative web dashboard.",
        bold_prefix="Exception Handling & Concurrency:"
    )
    add_body_paragraph(
        doc,
        "• Database Transaction Lifecycle & Data Persistence: Confirms ACID compliance: transactions execute within `BEGIN TRANSACTION;` "
        "and `COMMIT;` boundaries. Uncommitted or aborted writes automatically roll back, preserving audit trail consistency.",
        bold_prefix="Transaction Lifecycle & Persistence:"
    )

    # DEMO 4: Asynchronous Microservice Log Terminal & Event Ingestion Pipeline
    add_subheading(doc, "6.2.6 Backend Demonstration 4: Threaded Daemon Server Log Terminal & Event Pipeline (Figure 6.12)")
    add_body_paragraph(
        doc,
        "The Python backend daemon runs as a multi-threaded service logging real-time incoming connections, thread IDs, "
        "HTTP request methods, client IP addresses, and response latencies. Figure 6.12 documents the live terminal output "
        "of the active server during a gameplay session:"
    )
    add_screenshot_placeholder(
        doc,
        "[Insert Screenshot: Figure 6.12 - Backend Threaded Daemon Server Log Terminal & Event Pipeline]",
        "Figure 6.12: Backend Threaded Daemon Server Log Terminal & Event Ingestion Pipeline (server.py)",
        img_path=None
    )
    add_body_paragraph(
        doc,
        "• Request/Response Headers & Console Log Breakdown: The terminal prints connection banners (`[CIPHER COURT] Database Web Server online!`), "
        "bound host (`0.0.0.0:8000`), and real-time access logs detailing HTTP verb, target URI, HTTP protocol version, and status code: "
        "`127.0.0.1 - - [2026-09-29 11:45:12] 'POST /game-events HTTP/1.1' 200 -`.",
        bold_prefix="Terminal Telemetry Breakdown:"
    )
    add_body_paragraph(
        doc,
        "• Edge Cases, Exception Handling & Status Codes: Demonstrates socket reuse enablement (`allow_reuse_address = True`) preventing "
        "port bind crashes on restarts, and graceful shutdown handling (`KeyboardInterrupt`) terminating child worker threads cleanly.",
        bold_prefix="Exception Handling & Lifecycle Management:"
    )
    add_body_paragraph(
        doc,
        "• Database Transaction Lifecycle & Data Persistence: Visualizes asynchronous thread concurrency: `ThreadedHTTPServer` delegates "
        "each incoming connection to a separate worker thread, isolating database writes and guaranteeing that high-frequency clue discoveries "
        "do not block the primary HTTP event loop.",
        bold_prefix="Transaction Lifecycle & Concurrency:"
    )

    doc.add_page_break()

    # =========================================================================
    # 6.3 INTEGRATION & ENVIRONMENT CONFIGURATION
    # =========================================================================
    add_heading(doc, "6.3 Integration & Environment Configuration")
    add_body_paragraph(
        doc,
        "Bridging the decoupled Unity 3D client, Python backend service, and relational database requires rigorous environmental "
        "configuration, build pipeline orchestration, and network security policies. This section formalizes the integration parameters:",
        bold_prefix="Integration Architecture:"
    )

    # 6.3.1 Secure Environment Variables Configuration
    add_subheading(doc, "6.3.1 Secure Environment Variables Configuration (.env)")
    add_body_paragraph(
        doc,
        "All sensitive runtime credentials, service endpoints, and database connection strings are decoupled from source code and managed "
        "via secure environment variables (`.env`). The backend utilizes `os.getenv()` with defensive default fallbacks. "
        "Table 6.6 documents the complete environment variable dictionary:",
        bold_prefix="Environment Configuration Dictionary:"
    )

    # Table 6.6: Environment Variables & Security Configuration
    add_subheading(doc, "Table 6.6: Environment Variables & Security Configuration Matrix")
    env_vars = [
        ("HOST", "String", "0.0.0.0", "Network interface to bind server daemon (0.0.0.0 for public / 127.0.0.1 for local)"),
        ("PORT", "Integer", "8000", "TCP port for REST API endpoints and administrative HTML5 dashboard"),
        ("DATABASE_URL", "URI String", "sqlite:///cipher_court.db", "Database connection string (SQLite file path or PostgreSQL URI)"),
        ("JWT_SECRET_KEY", "Hex String", "c8f9a2e1... [256-bit]", "Cryptographic secret key for signing and validating HMAC-SHA256 JWTs"),
        ("JWT_ALGORITHM", "String", "HS256", "Symmetric encryption algorithm used for bearer token signature generation"),
        ("SESSION_TIMEOUT", "Integer", "3600", "Investigator session lifetime in seconds (1 hour auto-expiration)"),
        ("MAX_ATTEMPTS", "Integer", "3", "Global default attempt quota before triggering room security lockout"),
        ("LOG_LEVEL", "String", "INFO", "Logging verbosity threshold ('DEBUG', 'INFO', 'WARNING', 'ERROR')")
    ]
    t_env = doc.add_table(rows=len(env_vars) + 1, cols=4)
    t_env.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_env.autofit = False
    set_table_grid_borders(t_env)
    w_env = [Inches(1.5), Inches(1.1), Inches(1.7), Inches(2.2)]
    for r in t_env.rows:
        for i, c in enumerate(r.cells):
            c.width = w_env[i]
            set_cell_margins(c, 50, 50, 60, 60)
    for i, h in enumerate(["Variable Name", "Data Type", "Default / Example Value", "Security & Functional Scope"]):
        cp = t_env.cell(0, i).paragraphs[0]
        cp.add_run(h).font.bold = True
        cp.runs[0].font.name = FONT_NAME
        cp.runs[0].font.size = Pt(9.5)
        set_cell_background(t_env.cell(0, i), "F2F2F2")
    for idx, row in enumerate(env_vars):
        r = t_env.rows[idx + 1]
        for col_idx, val in enumerate(row):
            cp = r.cells[col_idx].paragraphs[0]
            r_run = cp.add_run(val)
            r_run.font.name = FONT_NAME
            r_run.font.size = Pt(8.5)
            if col_idx == 0: r_run.font.bold = True

    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    # 6.3.2 CORS Policies & Defensive Headers
    add_subheading(doc, "6.3.2 Cross-Origin Resource Sharing (CORS) Policy & Defensive Headers")
    add_body_paragraph(
        doc,
        "Because the administrative dashboard, WebGL web clients, and standalone desktop executables interact with the backend across "
        "distinct origins and protocol boundaries, the Python server incorporates strict Cross-Origin Resource Sharing (CORS) handling:",
        bold_prefix="CORS Protocol Enforcement:"
    )
    add_bullet_point(doc, "Preflight OPTIONS Resolution: The server intercepts HTTP OPTIONS requests (`do_OPTIONS`), returning HTTP 204 No Content with headers `Access-Control-Allow-Origin: *`, `Access-Control-Allow-Methods: GET, POST, OPTIONS`, and `Access-Control-Allow-Headers: Content-Type, Authorization, X-Requested-With`.")
    add_bullet_point(doc, "Defensive Security Headers: To mitigate cross-site scripting (XSS) and MIME-type sniffing, outbound responses append `X-Content-Type-Options: nosniff`, `X-Frame-Options: DENY`, and `Strict-Transport-Security: max-age=31536000; includeSubDomains`.")

    # 6.3.3 Unity Standalone Engine Build Configuration
    add_subheading(doc, "6.3.3 Unity Standalone Engine Build Configuration & Compilation Settings")
    add_body_paragraph(
        doc,
        "The production standalone client is compiled targeting the Windows x86_64 architecture with the following parameters:",
        bold_prefix="Compilation Flags:"
    )
    add_bullet_point(doc, "Scripting Backend & Optimization: Compiled using IL2CPP (Intermediate Language to C++) with C++ Compiler Configuration set to 'Release'. IL2CPP compiles C# bytecode into highly optimized native machine code, yielding substantial CPU performance gains.")
    add_bullet_point(doc, "Graphics API Pipeline: Primary graphics API configured to Direct3D11 / Direct3D12 with Multi-threaded Rendering enabled, ensuring smooth command buffer generation across multi-core CPUs.")
    add_bullet_point(doc, "URP Quality Settings: Render Pipeline Asset configured to UniversalRP-HighQuality, utilizing 4x MSAA anti-aliasing, PBR metallic-roughness shaders, soft shadow cascades, and HDR color grading.")

    doc.add_page_break()
'''

print(f"Content length of Chapter 6 module: {len(content)} characters")
with open("e:/vyt/test_ch6_code.py", "w", encoding="utf-8") as f:
    f.write(content)
print("Saved to e:/vyt/test_ch6_code.py")
