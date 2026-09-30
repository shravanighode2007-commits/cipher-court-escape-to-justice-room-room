# Complete Black Book data modules incorporating Proposal, SRS, UML, Architecture, Frontend, Logic Code, Databases, and Test Cases
import os
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def add_database_chapter(doc, helpers):
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

    # ═════════════════════════════════════════════════════════════════════════
    # CHAPTER 5: DATABASE AND DATA PERSISTENCE DESIGN
    # ═════════════════════════════════════════════════════════════════════════
    add_ch("Database and Data Persistence Design", "5")

    add_sec("Data Architecture in Interactive Serious Games", "5.1")
    add_p(
        "While traditional business software utilizes centralized client-server relational databases (such as PostgreSQL or MySQL), "
        "a high-performance real-time 3D serious game requires a hybrid data persistence model. In Cipher Court, data architecture "
        "is split into two complementary subsystems:", bold_prefix="Data Persistence Model:"
    )
    add_bullet("1. In-Memory Relational State Cache: Maintains active session parameters (player transform coordinates, raycast reticle focus states, collected evidence inventories, and unlocked door flags) in low-overhead contiguous managed memory arrays to guarantee sub-millisecond access times without GC allocation overhead.")
    add_bullet("2. Structured Serialization Data Layer: Manages persistent game state across scene transitions and application restarts. This layer implements both a relational SQLite-compatible schema (for institutional grading, audit logging, and forensic score evaluation) and a lightweight JSON document store (`SaveData.json`) for seamless standalone PC file serialization.")

    add_sec("Entity-Relationship (ER) Diagram & Conceptual Schema", "5.2")
    add_p(
        "The conceptual data model is structured around six core entities: `PlayerSession`, `LevelProgress`, "
        "`EvidenceItem`, `WitnessStatement`, `PuzzleAttemptRecord`, and `CourtVerdictEvaluation`. "
        "The relational cardinality is specified as follows:"
    )
    add_bullet("A PlayerSession (1) initiates one or more LevelProgress records (1..N).")
    add_bullet("Each LevelProgress record (1) contains multiple EvidenceItem entities (1..N) discovered via raycast interaction.")
    add_bullet("WitnessStatement entities (1..N) are associated with specific LevelProgress records, evaluated against EvidenceItem entities via contradiction truth relations (N..M).")
    add_bullet("Each puzzle interaction generates a PuzzleAttemptRecord (1..N) logging timestamp, user input string, validation status, and completion latency.")
    add_bullet("The culminating level produces a single CourtVerdictEvaluation record (1..1) storing aggregate bayesian evidence weights and jury verdict outcomes.")

    add_fig(
        "Assets/CipherCourtPolish/Diagrams/uml_er_diagram.png",
        "Fig. 5.1: Entity-Relationship (ER) Diagram for Game Session, Inventory, and Evaluation Architecture",
        width=Inches(6.0)
    )

    add_sec("Relational Database Schema & Table Specifications", "5.3")
    add_p(
        "To support institutional assessment, telemetry logging, and forensic verification, formal relational tables "
        "are defined below. Tables 5.1 through 5.5 detail the entity attributes, data types, constraints, and relational foreign keys:"
    )

    # Table 5.1: tbl_player_session
    add_subsec("Table 5.1: tbl_player_session (Session Telemetry Record)", "5.3.1")
    t51 = doc.add_table(rows=7, cols=5)
    t51.alignment = WD_TABLE_ALIGNMENT.CENTER
    t51.autofit = False
    set_table_borders(t51)

    t51_headers = ["Field Name", "Data Type", "Constraint", "Default Value", "Description"]
    t51_widths = [Inches(1.5), Inches(1.1), Inches(1.1), Inches(1.0), Inches(1.8)]

    for j, h in enumerate(t51_headers):
        cell = t51.cell(0, j)
        cell.width = t51_widths[j]
        set_cell_background(cell, "102C57")
        set_cell_margins(cell, top=60, bottom=60, left=50, right=50)
        p = cell.paragraphs[0]
        run = p.add_run(h)
        run.font.name = "Times New Roman"
        run.font.size = Pt(8)
        run.font.bold = True
        run.font.color.rgb = RGBColor(255, 255, 255)

    s_data = [
        ("session_id", "VARCHAR(36)", "PRIMARY KEY", "UUID v4", "Unique session identifier generated at launch."),
        ("candidate_id", "VARCHAR(20)", "NOT NULL", "'CS-9012'", "Institutional candidate roll number."),
        ("start_timestamp", "DATETIME", "NOT NULL", "CURRENT_TIMESTAMP", "Session initiation timestamp."),
        ("total_duration_sec", "FLOAT", "NOT NULL", "0.0", "Total active gameplay duration in seconds."),
        ("overall_status", "VARCHAR(16)", "CHECK IN ('Active', 'Complete', 'Aborted')", "'Active'", "Terminal session status flag."),
        ("final_score", "INTEGER", "CHECK (0 <= score <= 100)", "0", "Evaluated legal forensic score out of 100."),
    ]

    for i, row_data in enumerate(s_data):
        row = t51.rows[i + 1]
        for j, val in enumerate(row_data):
            cell = row.cells[j]
            cell.width = t51_widths[j]
            if (i % 2) == 1:
                set_cell_background(cell, "F7F9FB")
            set_cell_margins(cell, top=50, bottom=50, left=50, right=50)
            p = cell.paragraphs[0]
            run = p.add_run(val)
            run.font.name = "Times New Roman"
            run.font.size = Pt(7.5)
            if j == 0:
                run.font.bold = True

    # Table 5.2: tbl_evidence_inventory
    add_subsec("Table 5.2: tbl_evidence_inventory (Forensic Exhibit Registry)", "5.3.2")
    t52 = doc.add_table(rows=7, cols=5)
    t52.alignment = WD_TABLE_ALIGNMENT.CENTER
    t52.autofit = False
    set_table_borders(t52)

    for j, h in enumerate(t51_headers):
        cell = t52.cell(0, j)
        cell.width = t51_widths[j]
        set_cell_background(cell, "35598E")
        set_cell_margins(cell, top=60, bottom=60, left=50, right=50)
        p = cell.paragraphs[0]
        run = p.add_run(h)
        run.font.name = "Times New Roman"
        run.font.size = Pt(8)
        run.font.bold = True
        run.font.color.rgb = RGBColor(255, 255, 255)

    ev_data = [
        ("evidence_id", "VARCHAR(16)", "PRIMARY KEY", "Auto-generated", "Unique legal exhibit code (e.g., 'EX-01-BALLISTICS')."),
        ("session_id", "VARCHAR(36)", "FOREIGN KEY REFERENCES tbl_player_session", "None", "Associated candidate session foreign key."),
        ("discovered_level", "INTEGER", "CHECK (1 <= level <= 6)", "1", "Level number where artifact was discovered."),
        ("evidence_title", "VARCHAR(64)", "NOT NULL", "None", "Human-readable exhibit label (e.g., '9mm Bullet Casing')."),
        ("discovery_time_sec", "FLOAT", "NOT NULL", "0.0", "Elapsed session time when clue was examined."),
        ("is_used_in_verdict", "BOOLEAN", "NOT NULL", "FALSE", "Flag denoting exhibit presentation during trial."),
    ]

    for i, row_data in enumerate(ev_data):
        row = t52.rows[i + 1]
        for j, val in enumerate(row_data):
            cell = row.cells[j]
            cell.width = t51_widths[j]
            if (i % 2) == 1:
                set_cell_background(cell, "F7F9FB")
            set_cell_margins(cell, top=50, bottom=50, left=50, right=50)
            p = cell.paragraphs[0]
            run = p.add_run(val)
            run.font.name = "Times New Roman"
            run.font.size = Pt(7.5)
            if j == 0:
                run.font.bold = True

    # Table 5.3: tbl_puzzle_state
    add_subsec("Table 5.3: tbl_puzzle_state (Level State Machine Entity)", "5.3.3")
    t53 = doc.add_table(rows=7, cols=5)
    t53.alignment = WD_TABLE_ALIGNMENT.CENTER
    t53.autofit = False
    set_table_borders(t53)

    for j, h in enumerate(t51_headers):
        cell = t53.cell(0, j)
        cell.width = t51_widths[j]
        set_cell_background(cell, "102C57")
        set_cell_margins(cell, top=60, bottom=60, left=50, right=50)
        p = cell.paragraphs[0]
        run = p.add_run(h)
        run.font.name = "Times New Roman"
        run.font.size = Pt(8)
        run.font.bold = True
        run.font.color.rgb = RGBColor(255, 255, 255)

    puz_data = [
        ("puzzle_id", "VARCHAR(16)", "PRIMARY KEY", "None", "Puzzle identifier (e.g., 'PUZ-L1-KEYPAD')."),
        ("session_id", "VARCHAR(36)", "FOREIGN KEY REFERENCES tbl_player_session", "None", "Session association foreign key."),
        ("attempts_count", "INTEGER", "CHECK (attempts >= 0)", "0", "Total incorrect attempts before successful clearance."),
        ("solution_input", "VARCHAR(32)", "NOT NULL", "None", "Recorded player input string (e.g., '1011', '38.5')."),
        ("is_solved", "BOOLEAN", "NOT NULL", "FALSE", "Validation flag driving door motor trigger."),
        ("solve_duration_sec", "FLOAT", "NOT NULL", "0.0", "Time spent actively engaged with puzzle console."),
    ]

    for i, row_data in enumerate(puz_data):
        row = t53.rows[i + 1]
        for j, val in enumerate(row_data):
            cell = row.cells[j]
            cell.width = t51_widths[j]
            if (i % 2) == 1:
                set_cell_background(cell, "F7F9FB")
            set_cell_margins(cell, top=50, bottom=50, left=50, right=50)
            p = cell.paragraphs[0]
            run = p.add_run(val)
            run.font.name = "Times New Roman"
            run.font.size = Pt(7.5)
            if j == 0:
                run.font.bold = True

    add_sec("JSON Serialization Document Schema (SaveData.json)", "5.4")
    add_p(
        "For client-side local standalone execution, the game state serializes directly into a structured JSON payload "
        "managed by Unity's `JsonUtility` engine. Listing 5.1 illustrates the exact schema format utilized:"
    )

    json_code = """{
  "saveFormatVersion": 1,
  "sessionId": "f4f5088a-0c8e-444b-b9e7-7b0123372187",
  "candidateName": "Sahil Kate",
  "rollNumber": "CS-9012",
  "currentScene": "Level6_FinalVerdict",
  "playerCoordinates": {
    "x": 0.0,
    "y": 1.0,
    "z": -6.2
  },
  "puzzleStates": {
    "level1_keypad_solved": true,
    "level2_ballistics_aligned": true,
    "level3_cipher_decrypted": true,
    "level4_locker_unlocked": true,
    "level5_statement_contradicted": true,
    "level6_verdict_delivered": true
  },
  "inventoryExhibits": [
    "EX_01_BLOOD_SPATTER",
    "EX_02_BALLISTICS_LOG",
    "EX_03_CIPHER_MEMO",
    "EX_04_MURDER_WEAPON",
    "EX_05_ALIBI_CONTRADICTION"
  ],
  "audioSettings": {
    "masterVolume": 0.85,
    "sfxVolume": 1.0,
    "ambientVolume": 0.7
  }
}"""
    add_code(json_code, "Listing 5.17: Complete Game State JSON Serialization Schema (SaveData.json)")
    add_p(
        "Data Integrity Rationale: Listing 5.17 provides complete state persistence without circular references. "
        "Because `JsonUtility` compiles to native IL2CPP/C++ serializers, deserialization executes in under 2 milliseconds, "
        "eliminating loading lag when players continue investigations across game launches."
    )

    doc.add_page_break()

def add_proposal_and_srs(doc, helpers):
    add_ch = helpers['add_chapter_heading']
    add_sec = helpers['add_sec_heading']
    add_subsec = helpers['add_subsec_heading']
    add_p = helpers['add_body_p']
    add_bullet = helpers['add_bullet_p']
    set_cell_background = helpers['set_cell_background']
    set_cell_margins = helpers['set_cell_margins']
    set_table_borders = helpers['set_table_borders']
    NAVY = helpers['NAVY']
    STEEL = helpers['STEEL']

    # ═════════════════════════════════════════════════════════════════════════
    # PROPOSAL SECTION (Within Chapter 1)
    # ═════════════════════════════════════════════════════════════════════════
    add_sec("Formal Project Proposal and Work Breakdown Structure (WBS)", "1.7")
    add_p(
        "This project was initiated under a formal engineering dissertation proposal submitted to the Department of "
        "Computer Science & Engineering. The project proposal established the motivation, milestone deliverables, "
        "and Work Breakdown Structure (WBS) governing development across four four-week Agile sprint cycles:"
    )

    # Proposal WBS Table
    t_wbs = doc.add_table(rows=6, cols=5)
    t_wbs.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_wbs.autofit = False
    set_table_borders(t_wbs)

    wbs_headers = ["WBS ID", "Sprint / Milestone Phase", "Primary Technical Deliverables", "Target Timeline", "Status"]
    wbs_widths = [Inches(0.9), Inches(1.6), Inches(2.3), Inches(1.1), Inches(0.6)]

    for j, h in enumerate(wbs_headers):
        cell = t_wbs.cell(0, j)
        cell.width = wbs_widths[j]
        set_cell_background(cell, "102C57")
        set_cell_margins(cell, top=60, bottom=60, left=50, right=50)
        p = cell.paragraphs[0]
        run = p.add_run(h)
        run.font.name = "Times New Roman"
        run.font.size = Pt(8)
        run.font.bold = True
        run.font.color.rgb = RGBColor(255, 255, 255)

    wbs_data = [
        ("WBS 1.0", "Sprint 1: Architecture & Physics", "First-person kinematic controller, CharacterController, raycast reticle.", "Weeks 1–4", "Complete"),
        ("WBS 2.0", "Sprint 2: Logic & Cryptography", "C# modules for Keypad (L1), Ballistics (L2), Caesar Cipher (L3), Safe (L4).", "Weeks 5–8", "Complete"),
        ("WBS 3.0", "Sprint 3: Legal Climax & URP Polish", "Pre-trial chambers (L5), Grand Courtroom (L6), procedural PBR polisher.", "Weeks 9–12", "Complete"),
        ("WBS 4.0", "Sprint 4: UI Self-Healing & QA", "Dynamic button listener healing, cursor unlock safety, 45 test cases.", "Weeks 13–16", "Complete"),
        ("WBS 5.0", "Final Defense & Black Book", "70+ page major project dissertation report, PDF generation, viva demo.", "Week 17", "Complete"),
    ]

    for i, row_data in enumerate(wbs_data):
        row = t_wbs.rows[i + 1]
        for j, val in enumerate(row_data):
            cell = row.cells[j]
            cell.width = wbs_widths[j]
            if (i % 2) == 1:
                set_cell_background(cell, "F7F9FB")
            set_cell_margins(cell, top=50, bottom=50, left=50, right=50)
            p = cell.paragraphs[0]
            run = p.add_run(val)
            run.font.name = "Times New Roman"
            run.font.size = Pt(7.5)
            if j == 0:
                run.font.bold = True
            if j == 4:
                run.font.bold = True
                run.font.color.rgb = RGBColor(0, 140, 40)

    doc.add_page_break()
