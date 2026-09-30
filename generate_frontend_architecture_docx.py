# generate_frontend_architecture_docx.py
# Generates the standalone "Cipher Court: Level-Wise Frontend Prototype Architecture" Word Document

import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

FONT_NAME = "Times New Roman"
COLOR_NAVY = RGBColor(10, 25, 47)      # #0A192F
COLOR_GOLD = RGBColor(212, 175, 55)    # #D4AF37
COLOR_CHARCOAL = RGBColor(50, 50, 50)
COLOR_GRAY = RGBColor(100, 100, 100)

def set_cell_background(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=60, bottom=60, left=80, right=80):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def set_table_borders(table):
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'<w:top w:val="single" w:sz="8" w:space="0" w:color="0A192F"/>'
        f'<w:left w:val="none"/>'
        f'<w:bottom w:val="single" w:sz="8" w:space="0" w:color="0A192F"/>'
        f'<w:right w:val="none"/>'
        f'<w:insideH w:val="single" w:sz="4" w:space="0" w:color="D3D3D3"/>'
        f'<w:insideV w:val="none"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)

def add_title(doc, text, subtitle=None):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(16)
    p.paragraph_format.space_after = Pt(4)
    run = p.add_run(text)
    run.font.name = FONT_NAME
    run.font.size = Pt(20)
    run.font.bold = True
    run.font.color.rgb = COLOR_NAVY

    if subtitle:
        p_sub = doc.add_paragraph()
        p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_sub.paragraph_format.space_after = Pt(18)
        run_sub = p_sub.add_run(subtitle)
        run_sub.font.name = FONT_NAME
        run_sub.font.size = Pt(12)
        run_sub.font.italic = True
        run_sub.font.color.rgb = COLOR_GOLD

def add_heading_1(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(16)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = FONT_NAME
    run.font.size = Pt(15)
    run.font.bold = True
    run.font.color.rgb = COLOR_NAVY

def add_heading_2(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = FONT_NAME
    run.font.size = Pt(13)
    run.font.bold = True
    run.font.color.rgb = RGBColor(30, 60, 100)

def add_body_p(doc, text, bold_prefix=None):
    p = doc.add_paragraph()
    p.paragraph_format.line_spacing = 1.15
    p.paragraph_format.space_after = Pt(6)
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    if bold_prefix:
        r_pre = p.add_run(bold_prefix + " ")
        r_pre.font.name = FONT_NAME
        r_pre.font.size = Pt(11)
        r_pre.font.bold = True
        r_pre.font.color.rgb = COLOR_NAVY
    run = p.add_run(text)
    run.font.name = FONT_NAME
    run.font.size = Pt(11)
    run.font.color.rgb = COLOR_CHARCOAL
    return p

def add_bullet(doc, text, bold_prefix=None):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.line_spacing = 1.15
    p.paragraph_format.space_after = Pt(4)
    if bold_prefix:
        r_pre = p.add_run(bold_prefix + " ")
        r_pre.font.name = FONT_NAME
        r_pre.font.size = Pt(10.5)
        r_pre.font.bold = True
        r_pre.font.color.rgb = COLOR_NAVY
    run = p.add_run(text)
    run.font.name = FONT_NAME
    run.font.size = Pt(10.5)
    run.font.color.rgb = COLOR_CHARCOAL
    return p

def add_image_figure(doc, img_rel_path, caption_text, width=Inches(5.6)):
    full_path = os.path.abspath(f"e:/vyt/{img_rel_path}")
    if os.path.exists(full_path):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.keep_with_next = True
        r = p.add_run()
        r.add_picture(full_path, width=width)
        
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.paragraph_format.space_after = Pt(8)
        r_cap = p_cap.add_run(caption_text)
        r_cap.font.name = FONT_NAME
        r_cap.font.size = Pt(10)
        r_cap.font.italic = True
        r_cap.font.color.rgb = COLOR_GRAY

def build_frontend_architecture_doc(output_docx_path):
    doc = docx.Document()
    
    # 1-inch margins
    for sec in doc.sections:
        sec.top_margin = Inches(1.0)
        sec.bottom_margin = Inches(1.0)
        sec.left_margin = Inches(1.0)
        sec.right_margin = Inches(1.0)

    # Header
    header = doc.sections[0].header
    h_p = header.paragraphs[0]
    h_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    h_run = h_p.add_run("Cipher Court: Escape to Justice — Level-Wise Frontend Prototype Architecture")
    h_run.font.name = FONT_NAME
    h_run.font.size = Pt(8.5)
    h_run.font.italic = True
    h_run.font.color.rgb = COLOR_GRAY

    # Document Title
    add_title(
        doc,
        "CIPHER COURT: ESCAPE TO JUSTICE",
        "Frontend Prototype Architecture & Level-Wise Component Specification"
    )

    add_body_p(
        doc,
        "This technical document provides the complete, level-by-level architectural specification of the frontend prototype for "
        "Cipher Court: Escape to Justice. The client application is developed in Unity 6 LTS using the Universal Render Pipeline (URP), "
        "leveraging a decoupled UI/UX Canvas Scaler hierarchy, distance-bounded first-person raycasting, and in-memory persistent singletons."
    )

    # =========================================================================
    # SECTION 1: GLOBAL ARCHITECTURAL FRAMEWORK
    # =========================================================================
    add_heading_1(doc, "1. Global Frontend Architecture & Interaction Pipeline")
    
    add_body_p(
        doc,
        "The presentation tier coordinates through a centralized, persistent core engine and unified interaction protocols across all scenes:",
        bold_prefix="Core Interaction Framework:"
    )

    add_bullet(doc, "Canvas Scaler Hierarchy: Every UI canvas implements CanvasScaler set to ScaleWithScreenSize with a reference resolution of 1920x1080 pixels (MatchWidthOrHeight = 0.5), guaranteeing consistent layout scaling from 16:9 desktop monitors up to 4K displays.", bold_prefix="• Responsive Canvas Scaler:")
    add_bullet(doc, "TextMeshPro Signed Distance Field (SDF) Typography: All on-screen and world-space text elements utilize multi-channel SDF font assets (LiberationSans SDF, Orbitron SDF, Inconsolata SDF, NotoSerif SDF), ensuring crisp visual rendering under post-processing depth of field and dynamic camera distances.", bold_prefix="• SDF Typography Engine:")
    add_bullet(doc, "Persistent Singleton State (GameManager.cs): Instantiated on game bootstrap with DontDestroyOnLoad(gameObject), GameManager tracks active investigator identity, room completion bitmasks, aggregate score, and forensic clue inventories across scene transitions.", bold_prefix="• Global State Persistence:")
    add_bullet(doc, "Distance-Bounded Viewport Raycaster (PuzzleInteraction.cs): Center-screen raycasting (ViewportPointToRay(0.5, 0.5)) evaluates spatial intersections with the 'InteractiveProps' LayerMask, enforcing a strict Euclidean reach limit of d <= 2.50 meters.", bold_prefix="• Spatial Interaction Arbitrator:")
    add_bullet(doc, "Hardware Cursor Governance: The system dynamically manages cursor states: locked and hidden (CursorLockMode.Locked; Cursor.visible = false) during first-person locomotion; unlocked and visible (CursorLockMode.None; Cursor.visible = true) during puzzle modal inspection.", bold_prefix="• Hardware Cursor Lifecycle:")

    # =========================================================================
    # SECTION 2: LEVEL-WISE PROTOTYPE ARCHITECTURE
    # =========================================================================
    add_heading_1(doc, "2. Level-Wise Frontend Prototype Architecture")

    # --- LEVEL 0: MAIN MENU ---
    add_heading_2(doc, "Level 0: Main Menu Gateway (MainMenu.unity)")
    add_image_figure(doc, "Assets/CipherCourtPolish/Backgrounds/REAL_MainMenu_Clean.jpg", "Figure 1: Main Menu Gateway Interface — Cinematic Courtroom Panorama (MainMenu.unity)")
    add_bullet(doc, "UI Hierarchy: MainMenuCanvas (Screen Space - Overlay) -> BackgroundVignette (RawImage: Dark Navy #0A192F) -> TitleContainer (Gold Embossed TMP) -> ProfileInputModal (TMP_InputField) -> MenuButtonGroup (VerticalLayoutGroup: 'START GAME', 'INSTRUCTIONS', 'QUIT') -> InstructionsModal (CanvasGroup).", bold_prefix="• UI Component Hierarchy:")
    add_bullet(doc, "Active Interactor Scripts: MainMenuManager.cs, GameManager.cs.", bold_prefix="• Primary C# Controllers:")
    add_bullet(doc, "Handled Events: OnPointerEnter audio triggers, OnSelect profile field, OnClick(Btn_StartGame) generating active session ID and invoking SceneManager.LoadSceneAsync('Level1_Investigation').", bold_prefix="• User Interactions & Handled Events:")
    add_bullet(doc, "Validation Protocols: Alphanumeric regex guard (^[A-Za-z0-9_-]{3,20}$); fallback to default token INVESTIGATOR-9022-<GUID> if blank. Failsafe cursor lock release.", bold_prefix="• Client-Side Validation Rules:")

    # --- LEVEL 1: CRIME SCENE ---
    add_heading_2(doc, "Level 1: Crime Scene Investigation (Level1_Investigation.unity)")
    add_image_figure(doc, "Assets/CipherCourtPolish/Backgrounds/REAL_Level1_CrimeScene.png", "Figure 2: Level 1 Crime Scene — Reticle Clue Interaction Prompt Active (Level1_Investigation.unity)")
    add_bullet(doc, "UI Hierarchy: MainCamera Stack -> ReticleCanvas (Screen Space - Overlay) -> CenterReticle (Image: Dynamic 12x12 Outline) -> TooltipTag ('[E] Inspect Evidence Marker') -> ClueModalContainer -> ClueImageCard (Image) -> ClueDescription (TMP).", bold_prefix="• UI Component Hierarchy:")
    add_bullet(doc, "Active Interactor Scripts: PuzzleInteraction.cs, CollectibleItem.cs, PasswordClue.cs, Level1Progress.cs.", bold_prefix="• Primary C# Controllers:")
    add_bullet(doc, "Handled Events: First-person camera gimbal (WASD + MouseLook), KeyCode.E raycast trigger displaying modal clue card, Close modal returning camera agency.", bold_prefix="• User Interactions & Handled Events:")
    add_bullet(doc, "Validation Protocols: Raycast distance <= 2.50m; forward vector dot product >= 0.50. Level1Progress unlocks corridor exit door upon collecting all 4 evidentiary markers.", bold_prefix="• Client-Side Validation Rules:")

    # --- LEVEL 2: CYBER TERMINAL ---
    add_heading_2(doc, "Level 2: Forensic Cyber Terminal & Password Decryption (Level2_Computer.unity)")
    add_image_figure(doc, "Assets/CipherCourtPolish/Backgrounds/REAL_Level2_Puzzle_Screenshot.png", "Figure 3: Level 2 Cyber Forensics Terminal & Password Decryption Station (Level2_Computer.unity)")
    add_bullet(doc, "UI Hierarchy: In-World Monitor Quad (CRT Scanline Material) -> PasswordModal (Screen Space - Overlay) -> TerminalFrame (Cyan Glow #38BDF8) -> Input_Passcode (TMP_InputField) -> AttemptIndicatorGroup (3x Shield Badges) -> Btn_Authenticate -> FeedbackBanner.", bold_prefix="• UI Component Hierarchy:")
    add_bullet(doc, "Active Interactor Scripts: PasswordPuzzle.cs, PasswordPuzzleInteraction.cs, PasswordPuzzleUI.cs, Level2Progress.cs.", bold_prefix="• Primary C# Controllers:")
    add_bullet(doc, "Handled Events: CRT raycast focus, password text input, OnClick(Btn_Authenticate) / KeyCode.Return triggering cryptographic verification.", bold_prefix="• User Interactions & Handled Events:")
    add_bullet(doc, "Validation Protocols: String sanitization via .Trim().ToUpper(), length clamping (4-16 characters). 3-attempt quota limiter with lockout penalty. Correct key 'COURT2026' slerps open security blast doors.", bold_prefix="• Client-Side Validation Rules:")

    # --- LEVEL 3: CAESAR CIPHER ---
    add_heading_2(doc, "Level 3: Steganographic Legal Archive & Caesar Cipher (Level3_Evidence.unity)")
    add_image_figure(doc, "Assets/CipherCourtPolish/Backgrounds/REAL_Level3_CipherPuzzle.png", "Figure 4: Level 3 Steganographic Caesar Cipher Decoding Interface (Level3_Evidence.unity)")
    add_bullet(doc, "UI Hierarchy: CaesarCipherModal (Screen Space - Overlay) -> AntiqueParchmentBacking (#F4EEDD) -> CiphertextCard (TMP: 'MXVWLFH') -> RotorWheelAssembly (Concentric 26-character rings) -> ShiftDisplay ('Shift Key: k = 3') -> Input_Plaintext -> Btn_VerifyCipher.", bold_prefix="• UI Component Hierarchy:")
    add_bullet(doc, "Active Interactor Scripts: CipherPuzzle.cs, PuzzleUI.cs, EvidenceItem.cs, Level3Progress.cs.", bold_prefix="• Primary C# Controllers:")
    add_bullet(doc, "Handled Events: Rotor wheel mouse drag rotating in 13.84-degree increments, input field typing, OnClick(Btn_VerifyCipher) calculating Pi = (Ci - 3) mod 26.", bold_prefix="• User Interactions & Handled Events:")
    add_bullet(doc, "Validation Protocols: Regex filter stripping non-alphabetic symbols ([^A-Za-z]). Plaintext verification against 'JUSTICE' unlatches evidence vault and awards 200 forensic points.", bold_prefix="• Client-Side Validation Rules:")

    # --- LEVEL 4: ARCHIVE SAFE ---
    add_heading_2(doc, "Level 4: Underground Archival Vault & Numeric Keypad Safe (Level4_Archive.unity)")
    add_image_figure(doc, "Assets/CipherCourtPolish/Backgrounds/Level4_Archive_Background.png", "Figure 5: Level 4 Underground Archive Records Vault (Level4_Archive.unity)")
    add_bullet(doc, "UI Hierarchy: SafeDoorQuad -> SafeKeypadCanvas (World Space) -> BrushedSteelHousing -> LEDDisplayPanel (7-Segment Font: '_ _ _') -> ButtonMatrix_3x4 (GridLayoutGroup: PushButtons 0-9, Btn_Clear, Btn_Enter) -> MechanicalTumblerAudio.", bold_prefix="• UI Component Hierarchy:")
    add_bullet(doc, "Active Interactor Scripts: ArchiveKeypad.cs, Level4ArchivePuzzle.cs, Level4Clue.cs.", bold_prefix="• Primary C# Controllers:")
    add_bullet(doc, "Handled Events: Physical push-button mouse clicks with spring depression shader, buffer concatenation, audio tumbler click on each keypress.", bold_prefix="• User Interactions & Handled Events:")
    add_bullet(doc, "Validation Protocols: Fixed-length 3-digit buffer clamp; 250ms software debounce. Verification matches '427' (recovered from medical examiner report). Incorrect code flashes red LED and enforces 3s penalty.", bold_prefix="• Client-Side Validation Rules:")

    # --- LEVEL 5: CASE FILES ---
    add_heading_2(doc, "Level 5: Case Files & Financial Affidavits (Level5_CaseFiles.unity)")
    add_image_figure(doc, "Assets/CipherCourtPolish/Backgrounds/Level5_Statements_Background.png", "Figure 6: Level 5 Case Files & Sworn Affidavits Deliberation Chamber (Level5_CaseFiles.unity)")
    add_bullet(doc, "UI Hierarchy: CaseFilesModal (Screen Space - Overlay) -> SplitPaneLayout (HorizontalLayoutGroup) -> LeftPane (ScrollRect: Bank Ledgers & Invoices) -> RightPane (Affidavit Summary, DiscrepancyCodeInput, Btn_ConfirmDiscrepancy) -> StatusBanner.", bold_prefix="• UI Component Hierarchy:")
    add_bullet(doc, "Active Interactor Scripts: Level5Terminal.cs, Level5CasePuzzle.cs, Level5File.cs.", bold_prefix="• Primary C# Controllers:")
    add_bullet(doc, "Handled Events: Vertical ledger scrolling, document cross-referencing, typing 3-digit discrepancy code, submitting audit verification.", bold_prefix="• User Interactions & Handled Events:")
    add_bullet(doc, "Validation Protocols: Validates transaction code '315' against bank record exhibits. Unlocks double oak doors into Level 6 Courtroom.", bold_prefix="• Client-Side Validation Rules:")

    # --- LEVEL 6: COURTROOM CLIMAX ---
    add_heading_2(doc, "Level 6: Grand Judicial Courtroom Final Verdict (Level6_FinalVerdict.unity)")
    add_image_figure(doc, "Assets/CipherCourtPolish/Backgrounds/REAL_Level6_SelectStatement.png", "Figure 7: Level 6 Grand Courtroom Witness Cross-Examination Interface (Level6_FinalVerdict.unity)")
    add_bullet(doc, "UI Hierarchy: CourtroomVerdictModal (Screen Space - Overlay) -> JudicialBannerHeader ('CROSS-EXAMINATION') -> WitnessSpeechBubble (Dynamic Dialogue) -> StatementRadioGroup (VerticalLayoutGroup: 3x Toggles) -> EvidenceReferenceCarousel -> Btn_ObjectAndAccuse (Gavel Action Button).", bold_prefix="• UI Component Hierarchy:")
    add_bullet(doc, "Active Interactor Scripts: Level6Terminal.cs, Level6Statement.cs, Level6VerdictPuzzle.cs, FinalLevelExit.cs.", bold_prefix="• Primary C# Controllers:")
    add_bullet(doc, "Handled Events: Statement selection via radio toggles, horizontal evidence carousel scrolling, OnClick(Btn_ObjectAndAccuse) presenting contradiction.", bold_prefix="• User Interactions & Handled Events:")
    add_bullet(doc, "Validation Protocols: Mutually exclusive selection via ToggleGroup. Identifies Statement 2 as perjury (contradicting Level 2 timestamped terminal logs). Correct accusation plays gavel audio, displays conviction ruling, and routes to victory.", bold_prefix="• Client-Side Validation Rules:")

    # --- LEVEL 7: GAME COMPLETE ---
    add_heading_2(doc, "Level 7: Mission Debriefing & Final Case Verdict (GameComplete.unity)")
    add_image_figure(doc, "Assets/CipherCourtPolish/Backgrounds/REAL_GameComplete_Screenshot.png", "Figure 8: Game Complete Victory Debriefing — Justice Served (GameComplete.unity)")
    add_bullet(doc, "UI Hierarchy: GameCompleteCanvas (Screen Space - Overlay) -> ParchmentCertificateCard (#F4EEDD) -> GoldenLaurelGavelSeal (Image) -> CongratulatoryHeadline -> MetricsGrid (2x2 Cards: Elapsed Time, Deduction Accuracy %, Evidence Found 6/6, Final Forensic Score) -> ActionButtons (Btn_ExportReport, Btn_ReturnToMenu).", bold_prefix="• UI Component Hierarchy:")
    add_bullet(doc, "Active Interactor Scripts: GameCompleteManager.cs, GameManager.cs.", bold_prefix="• Primary C# Controllers:")
    add_bullet(doc, "Handled Events: Automatic aggregate calculation from GameManager on Start(), OnClick(Btn_ExportReport) triggering local JSON audit export, OnClick(Btn_ReturnToMenu) cleanly resetting session singletons.", bold_prefix="• User Interactions & Handled Events:")
    add_bullet(doc, "Validation Protocols: Integrity check on completed level flags before calculating score bonuses. Disposes in-memory web request textures upon exit.", bold_prefix="• Client-Side Validation Rules:")

    # =========================================================================
    # SECTION 3: SUMMARY COMPONENT MATRIX TABLE
    # =========================================================================
    add_heading_1(doc, "3. Level-Wise Component & Script Mapping Matrix")

    table_data = [
        ("0", "MainMenu.unity", "MainMenuManager.cs", "Screen Space - Overlay", "Mouse / Keyboard", "Alphanumeric Regex", "Authenticate & Launch Session"),
        ("1", "Level1_Investigation.unity", "PuzzleInteraction.cs / CollectibleItem.cs", "HUD Reticle + Modal Card", "Raycast (E Key)", "Distance <= 2.5m, Vector Dot", "Catalog 4 Crime Scene Clues"),
        ("2", "Level2_Computer.unity", "PasswordPuzzle.cs / PasswordPuzzleUI.cs", "World Space CRT + Screen Modal", "Keyboard InputField", "Trim().ToUpper(), 3-Quota", "Crack Cyber Terminal ('COURT2026')"),
        ("3", "Level3_Evidence.unity", "CipherPuzzle.cs / PuzzleUI.cs", "Screen Space - Overlay", "Mouse Drag Rotor / TMP", "Shift k=3, Regex [^A-Za-z]", "Decrypt Caesar Cipher ('JUSTICE')"),
        ("4", "Level4_Archive.unity", "ArchiveKeypad.cs / Level4ArchivePuzzle.cs", "World Space Safe Keypad", "Virtual Keypad Buttons", "3-Digit Clamp, 250ms Debounce", "Unlock Ballistics Safe ('427')"),
        ("5", "Level5_CaseFiles.unity", "Level5Terminal.cs / Level5CasePuzzle.cs", "Split-Pane Dossier Modal", "ScrollRect & InputField", "Ledger Discrepancy Matching", "Identify Anomaly Code ('315')"),
        ("6", "Level6_FinalVerdict.unity", "Level6VerdictPuzzle.cs / FinalLevelExit.cs", "Screen Space - Overlay", "Radio Toggles & Gavel Btn", "Mutually Exclusive Toggle", "Expose Perjury in Statement 2"),
        ("7", "GameComplete.unity", "GameCompleteManager.cs", "Parchment Certificate Card", "Mouse Click Action Buttons", "Level Completion Bitmask", "Debrief Case & Export Audit")
    ]

    t = doc.add_table(rows=len(table_data) + 1, cols=7)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    set_table_borders(t)

    widths = [Inches(0.4), Inches(1.3), Inches(1.3), Inches(1.1), Inches(0.9), Inches(1.1), Inches(1.1)]
    for r in t.rows:
        for i, c in enumerate(r.cells):
            c.width = widths[i]
            set_cell_margins(c, 40, 40, 50, 50)

    headers = ["Lvl", "Scene File", "Primary C# Controller", "Canvas Render Mode", "Input Method", "Validation Guard", "Mission Objective"]
    for i, h in enumerate(headers):
        cp = t.cell(0, i).paragraphs[0]
        r = cp.add_run(h)
        r.font.name = FONT_NAME
        r.font.size = Pt(8.5)
        r.font.bold = True
        r.font.color.rgb = COLOR_NAVY
        set_cell_background(t.cell(0, i), "F0F4F8")

    for idx, row in enumerate(table_data):
        r = t.rows[idx + 1]
        for col_idx, val in enumerate(row):
            cp = r.cells[col_idx].paragraphs[0]
            r_run = cp.add_run(val)
            r_run.font.name = FONT_NAME
            r_run.font.size = Pt(8.0)
            if col_idx == 0 or col_idx == 1:
                r_run.font.bold = True

    doc.add_paragraph().paragraph_format.space_after = Pt(12)

    # Save Document
    doc.save(output_docx_path)
    print(f"Successfully generated standalone Word document: {output_docx_path}")

if __name__ == "__main__":
    out_path = os.path.abspath("e:/vyt/Cipher_Court_Frontend_Prototype_Architecture.docx")
    build_frontend_architecture_doc(out_path)
