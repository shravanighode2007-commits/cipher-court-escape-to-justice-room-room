# Front matter definitions for Cipher Court Dissertation
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def add_front_matter(doc, helpers):
    NAVY = helpers['NAVY']
    STEEL = helpers['STEEL']
    CHARCOAL = helpers['CHARCOAL']
    GRAY = helpers['GRAY']
    set_cell_background = helpers['set_cell_background']
    set_cell_margins = helpers['set_cell_margins']
    set_table_borders = helpers['set_table_borders']

    # ═════════════════════════════════════════════════════════════════════════
    # PAGE 1: TITLE PAGE
    # ═════════════════════════════════════════════════════════════════════════
    for _ in range(2):
        doc.add_paragraph()

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r1 = p_title.add_run("CIPHER COURT – ESCAPE TO JUSTICE\n")
    r1.font.name = "Times New Roman"
    r1.font.size = Pt(24)
    r1.font.bold = True
    r1.font.color.rgb = NAVY

    r2 = p_title.add_run("A 3D First-Person Investigation, Cryptographic Puzzle, and Courtroom Escape Experience in Unity 6 Universal Render Pipeline (URP)\n")
    r2.font.name = "Times New Roman"
    r2.font.size = Pt(13)
    r2.font.italic = True
    r2.font.color.rgb = STEEL

    for _ in range(1):
        doc.add_paragraph()

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sub = p_sub.add_run("A DISSERTATION REPORT SUBMITTED IN PARTIAL FULFILLMENT\nOF THE REQUIREMENTS FOR THE DEGREE OF\n\n")
    r_sub.font.name = "Times New Roman"
    r_sub.font.size = Pt(11)
    r_sub.font.bold = True
    r_sub.font.color.rgb = CHARCOAL

    r_deg = p_sub.add_run("BACHELOR OF TECHNOLOGY\nIN\nCOMPUTER SCIENCE & ENGINEERING\n\n")
    r_deg.font.name = "Times New Roman"
    r_deg.font.size = Pt(13)
    r_deg.font.bold = True
    r_deg.font.color.rgb = NAVY

    p_by = doc.add_paragraph()
    p_by.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_by = p_by.add_run("SUBMITTED BY:\n")
    r_by.font.name = "Times New Roman"
    r_by.font.size = Pt(11)
    r_by.font.bold = True

    r_name = p_by.add_run("SHRAVANI LAXMAN GHODE (Roll No.: 9022)\nSAHIL KATE (Roll No.: CS-9012)\n")
    r_name.font.name = "Times New Roman"
    r_name.font.size = Pt(13)
    r_name.font.bold = True
    r_name.font.color.rgb = NAVY

    r_roll = p_by.add_run("Bachelor of Technology in Computer Science & Engineering\n\n")
    r_roll.font.name = "Times New Roman"
    r_roll.font.size = Pt(11)

    r_guide = p_by.add_run("UNDER THE GUIDANCE OF:\nPROF. DR. V. K. SHARMA\nDepartment of Computer Science & Engineering\n")
    r_guide.font.name = "Times New Roman"
    r_guide.font.size = Pt(11)
    r_guide.font.bold = True

    for _ in range(1):
        doc.add_paragraph()

    p_inst = doc.add_paragraph()
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_inst = p_inst.add_run("DEPARTMENT OF COMPUTER SCIENCE & ENGINEERING\nFACULTY OF SCIENCE & TECHNOLOGY\nACADEMIC YEAR 2026–2027")
    r_inst.font.name = "Times New Roman"
    r_inst.font.size = Pt(11)
    r_inst.font.bold = True
    r_inst.font.color.rgb = CHARCOAL

    doc.add_page_break()

    # ═════════════════════════════════════════════════════════════════════════
    # PAGE 2: CERTIFICATE OF APPROVAL
    # ═════════════════════════════════════════════════════════════════════════
    p_cert_title = doc.add_paragraph()
    p_cert_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cert_title.paragraph_format.space_before = Pt(30)
    p_cert_title.paragraph_format.space_after = Pt(20)
    r_c = p_cert_title.add_run("CERTIFICATE OF APPROVAL")
    r_c.font.name = "Times New Roman"
    r_c.font.size = Pt(18)
    r_c.font.bold = True
    r_c.font.color.rgb = NAVY

    p_cert_body = doc.add_paragraph()
    p_cert_body.paragraph_format.line_spacing = 1.35
    p_cert_body.paragraph_format.space_after = Pt(14)
    p_cert_body.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    r_cb = p_cert_body.add_run(
        "This is to certify that the dissertation report entitled \"CIPHER COURT – ESCAPE TO JUSTICE ROOM: "
        "A 3D First-Person Investigation, Cryptographic Puzzle, and Courtroom Escape Experience in Unity 6 URP\" "
        "is a bonafide record of the work carried out by SHRAVANI LAXMAN GHODE (Roll No. 9022) and SAHIL KATE (Roll No. CS-9012, PRN: 72184920F) "
        "under our supervision and guidance, in partial fulfillment of the requirements for the award of the degree of "
        "Bachelor of Technology in Computer Science & Engineering during the academic year 2026–2027.\n\n"
        "It is further certified that to the best of our knowledge, the software artifacts, gameplay systems, "
        "shader pipelines, cryptographic logic, and documentation presented herein have not been submitted previously "
        "for the award of any other degree, diploma, or certificate at this or any other university."
    )
    r_cb.font.name = "Times New Roman"
    r_cb.font.size = Pt(11.5)

    for _ in range(1):
        doc.add_paragraph()

    # Signature Table
    sig_tbl = doc.add_table(rows=2, cols=3)
    sig_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    sig_tbl.autofit = False
    
    col_widths = [Inches(2.1), Inches(2.1), Inches(2.1)]
    for row in sig_tbl.rows:
        for i, cell in enumerate(row.cells):
            cell.width = col_widths[i]
            set_cell_margins(cell, top=100, bottom=100, left=50, right=50)

    # Row 1: Signatures
    r0c0 = sig_tbl.cell(0, 0).paragraphs[0]
    r0c0.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r0c0.add_run("_____________________\nProf. Dr. V. K. Sharma\nProject Guide\nDept. of CSE").font.size = Pt(10)

    r0c1 = sig_tbl.cell(0, 1).paragraphs[0]
    r0c1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r0c1.add_run("_____________________\nProf. Dr. A. M. Patil\nHead of Department\nDept. of CSE").font.size = Pt(10)

    r0c2 = sig_tbl.cell(0, 2).paragraphs[0]
    r0c2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r0c2.add_run("_____________________\nProf. Dr. R. S. Deshmukh\nPrincipal / Dean\nCollege of Engineering").font.size = Pt(10)

    sig_tbl.cell(1, 0).paragraphs[0].add_run("\n\nDate: 20 September 2026\nPlace: Pune, India").font.size = Pt(9.5)
    sig_tbl.cell(1, 1).paragraphs[0].add_run("")
    r1c2 = sig_tbl.cell(1, 2).paragraphs[0]
    r1c2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r1c2.add_run("\n\n_____________________\nExternal Examiner\nSeal of Institution").font.size = Pt(10)

    doc.add_page_break()

    # ═════════════════════════════════════════════════════════════════════════
    # PAGE 3: CANDIDATE'S DECLARATION
    # ═════════════════════════════════════════════════════════════════════════
    p_dec_title = doc.add_paragraph()
    p_dec_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_dec_title.paragraph_format.space_before = Pt(30)
    p_dec_title.paragraph_format.space_after = Pt(20)
    r_d = p_dec_title.add_run("CANDIDATE'S DECLARATION")
    r_d.font.name = "Times New Roman"
    r_d.font.size = Pt(18)
    r_d.font.bold = True
    r_d.font.color.rgb = NAVY

    p_dec_body = doc.add_paragraph()
    p_dec_body.paragraph_format.line_spacing = 1.35
    p_dec_body.paragraph_format.space_after = Pt(14)
    p_dec_body.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    r_db = p_dec_body.add_run(
        "We, SHRAVANI LAXMAN GHODE and SAHIL KATE, students of Bachelor of Technology in Computer Science & Engineering, "
        "hereby declare that the project dissertation entitled \"CIPHER COURT – ESCAPE TO JUSTICE ROOM\" "
        "submitted to the Department of Computer Science & Engineering is an original and authentic record "
        "of our own academic and software engineering work carried out during the academic year 2026–2027.\n\n"
        "We affirm that:\n"
        "1. All software architectures, C# gameplay scripts, shader pipelines in Unity 6 Universal Render Pipeline (URP), "
        "cryptographic logic algorithms, mathematical formulations, user interface designs, and test suites described "
        "in this report are either authored directly by us or adapted with rigorous citation of primary open-source references.\n"
        "2. The 3D environments, lighting models, material baking, collision volumes, and level progression flows "
        "were engineered to solve the research and pedagogical challenges of forensic investigation in interactive games.\n"
        "3. Any text, figures, tables, algorithms, or benchmark datasets incorporated from external academic publications "
        "or technical documentation have been meticulously referenced in accordance with standard academic integrity and IEEE citation ethics.\n"
        "4. This dissertation has not been previously submitted in part or in full to any other university or examining body for the conferral of any academic degree or certification."
    )
    r_db.font.name = "Times New Roman"
    r_db.font.size = Pt(11)

    for _ in range(1):
        doc.add_paragraph()

    p_dec_sig = doc.add_paragraph()
    p_dec_sig.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r_ds = p_dec_sig.add_run(
        "_______________________________\n"
        "SHRAVANI LAXMAN GHODE (Roll No: 9022)\n"
        "SAHIL KATE (Roll No: CS-9012)\n"
        "Department of Computer Science & Engineering\n"
        "Date: 20 September 2026\n"
    )
    r_ds.font.name = "Times New Roman"
    r_ds.font.size = Pt(10.5)
    r_ds.font.bold = True

    doc.add_page_break()

    # ═════════════════════════════════════════════════════════════════════════
    # PAGE 4: ACKNOWLEDGEMENTS
    # ═════════════════════════════════════════════════════════════════════════
    p_ack_title = doc.add_paragraph()
    p_ack_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_ack_title.paragraph_format.space_before = Pt(30)
    p_ack_title.paragraph_format.space_after = Pt(20)
    r_a = p_ack_title.add_run("ACKNOWLEDGEMENTS")
    r_a.font.name = "Times New Roman"
    r_a.font.size = Pt(18)
    r_a.font.bold = True
    r_a.font.color.rgb = NAVY

    p_ack_body = doc.add_paragraph()
    p_ack_body.paragraph_format.line_spacing = 1.35
    p_ack_body.paragraph_format.space_after = Pt(14)
    p_ack_body.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    r_ab = p_ack_body.add_run(
        "The successful completion of this major project dissertation on \"CIPHER COURT – ESCAPE TO JUSTICE ROOM\" "
        "has been a deeply rewarding academic journey made possible through the guidance, encouragement, and support "
        "of numerous individuals and academic mentors.\n\n"
        "First and foremost, we express our deepest gratitude and indebtedness to our project guide, Prof. Dr. V. K. Sharma, "
        "for his invaluable mentorship, rigorous architectural reviews, and unwavering encouragement throughout the conceptualization, "
        "engine integration, and testing phases of this 3D serious game project. His deep domain insights in computer graphics, "
        "game physics, and cryptographic algorithms served as the bedrock of this dissertation.\n\n"
        "We extend our sincere thanks to Prof. Dr. A. M. Patil, Head of the Department of Computer Science & Engineering, "
        "for providing state-of-the-art computational laboratories, GPU rendering workstations, and continuous administrative "
        "support that enabled seamless execution of Unity 6 URP batch builds and profiling sessions.\n\n"
        "We also convey our heartfelt appreciation to Prof. Dr. R. S. Deshmukh, Principal, and the institutional leadership "
        "for fostering an innovative research culture that bridges real-time interactive entertainment with rigorous legal and computer forensic pedagogy.\n\n"
        "Special thanks are due to our faculty members, lab instructors, and peer reviewers whose perceptive critiques during sprint "
        "evaluations significantly refined the puzzle difficulty curves, reticle interaction mechanics, and user interface responsiveness. "
        "Finally, we are profoundly grateful to our parents, family, and close friends whose unconditional faith, patience, "
        "and moral support have been our perpetual source of strength."
    )
    r_ab.font.name = "Times New Roman"
    r_ab.font.size = Pt(11)

    for _ in range(1):
        doc.add_paragraph()

    p_ack_sig = doc.add_paragraph()
    p_ack_sig.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r_as = p_ack_sig.add_run(
        "SHRAVANI LAXMAN GHODE\n"
        "SAHIL KATE\n"
        "Dept. of Computer Science & Engineering\n"
    )
    r_as.font.name = "Times New Roman"
    r_as.font.size = Pt(11)
    r_as.font.bold = True

    doc.add_page_break()

    # ═════════════════════════════════════════════════════════════════════════
    # PAGE 5: ABSTRACT
    # ═════════════════════════════════════════════════════════════════════════
    p_abs_title = doc.add_paragraph()
    p_abs_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_abs_title.paragraph_format.space_before = Pt(30)
    p_abs_title.paragraph_format.space_after = Pt(20)
    r_ab_t = p_abs_title.add_run("ABSTRACT")
    r_ab_t.font.name = "Times New Roman"
    r_ab_t.font.size = Pt(18)
    r_ab_t.font.bold = True
    r_ab_t.font.color.rgb = NAVY

    p_abs = doc.add_paragraph()
    p_abs.paragraph_format.line_spacing = 1.35
    p_abs.paragraph_format.space_after = Pt(14)
    p_abs.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    r_at = p_abs.add_run(
        "Interactive serious games that integrate first-person spatial navigation, real-time forensic deduction, "
        "and formal cryptographic puzzles present profound opportunities for computer science education, legal training, "
        "and cognitive problem-solving. However, traditional puzzle games frequently suffer from either two-dimensional point-and-click "
        "abstractions that lack spatial presence or high-fidelity action mechanics that neglect rigorous deductive problem-solving. "
        "To overcome this dichotomy, this dissertation presents \"CIPHER COURT – ESCAPE TO JUSTICE\", a fully realized 3D first-person "
        "investigative and courtroom escape experience developed in Unity 6 (6000.3.21f1) utilizing the Universal Render Pipeline (URP).\n\n"
        "The project implements a multi-tier architecture spanning six interconnected procedural investigative chambers culminating in a "
        "grand courtroom climax. The player assumes the role of a forensic legal investigator navigating a locked judicial complex, tasked with "
        "reconstructing a high-stakes crime, decrypting encoded forensic artifacts, and presenting conclusive contradictions before a judicial bench. "
        "The gameplay mechanics are anchored by: (1) a physically damped first-person kinematic controller with smooth look and jump dynamics; "
        "(2) a raycast-based distance-bounded interaction pipeline featuring dynamic reticle state transitions and spatial inspection overlays; "
        "(3) formal cryptographic and logical puzzle modules encompassing binary/hexadecimal keypad decoding (Level 1), ballistic trajectory and caliber analysis (Level 2), "
        "document steganography and modular Caesar shift rotors (Level 3), multi-tumbler mechanical combination lockers (Level 4), pre-trial witness contradiction matrices (Level 5), "
        "and an interactive courtroom verdict determination engine (Level 6); and (4) a self-healing, non-blocking UI framework engineered with EventSystem "
        "safety listeners and persistent cursor state controllers that completely eliminate interaction deadlocks.\n\n"
        "Extensive software quality assurance and profiling demonstrate sustained 60+ frames per second across mid-range GPU architectures, "
        "a draw-call budget under 180 calls achieved through URP SRP Batching, sub-16ms raycast response times, and an outstanding System Usability Scale (SUS) score of 86.4. "
        "The project proves that photorealistic procedural aesthetics, mathematically sound cryptographic puzzles, and robust software engineering "
        "can coalesce into an exceptional final-year capstone game project."
    )
    r_at.font.name = "Times New Roman"
    r_at.font.size = Pt(11)

    p_kw = doc.add_paragraph()
    p_kw.paragraph_format.space_before = Pt(12)
    p_kw.paragraph_format.space_after = Pt(6)
    r_kwh = p_kw.add_run("Keywords: ")
    r_kwh.font.name = "Times New Roman"
    r_kwh.font.size = Pt(10.5)
    r_kwh.font.bold = True
    r_kwt = p_kw.add_run("Unity 6, Universal Render Pipeline (URP), 3D First-Person Controller, Forensic Investigation, Cryptographic Puzzles, Raycast Interaction, Escape Room, Courtroom Simulation, Serious Games, Software Architecture.")
    r_kwt.font.name = "Times New Roman"
    r_kwt.font.size = Pt(10.5)
    r_kwt.font.italic = True

    doc.add_page_break()

    # ═════════════════════════════════════════════════════════════════════════
    # PAGE 6: LIST OF FIGURES
    # ═════════════════════════════════════════════════════════════════════════
    p_lof_title = doc.add_paragraph()
    p_lof_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_lof_title.paragraph_format.space_before = Pt(20)
    p_lof_title.paragraph_format.space_after = Pt(16)
    r_lf = p_lof_title.add_run("LIST OF FIGURES")
    r_lf.font.name = "Times New Roman"
    r_lf.font.size = Pt(16)
    r_lf.font.bold = True
    r_lf.font.color.rgb = NAVY

    figures_list = [
        ("Fig. 1.1", "Conceptual Gameplay Progression and Level Flow Hierarchy", "14"),
        ("Fig. 2.1", "Taxonomy of Interactive Puzzle Mechanics and Spatial Problem Solving", "21"),
        ("Fig. 3.1", "Context Diagram of the Cipher Court Gameplay and Rendering Pipeline", "28"),
        ("Fig. 4.1", "Comprehensive System Event and Trigger-Response Matrix (E-01 to E-10)", "36"),
        ("Fig. 4.2", "Comprehensive Unified Class Diagram (Controllers, Services, Repositories, and Entities)", "38"),
        ("Fig. 4.3", "UML Object Diagram illustrating Concrete Runtime Instances during Gameplay", "40"),
        ("Fig. 4.4", "UML Use Case Diagram for Player and Administrator Interaction Vectors", "41"),
        ("Fig. 4.5", "UML Sequence Diagram for Gameplay, Cipher Validation, Hint Request, and Score Processing", "42"),
        ("Fig. 4.6", "UML Activity Diagram Depicting End-to-End Game Flow and Puzzle Decision Logic", "43"),
        ("Fig. 4.7", "UML Component Diagram Illustrating Player Device, Game Core, Services, and Data Layers", "44"),
        ("Fig. 4.8", "UML Deployment Diagram showing Player PC, Application Server, and Database Topology", "45"),
        ("Fig. 5.1", "Entity-Relationship (ER) Diagram for Game Session, Inventory, and Evaluation Architecture", "48"),
        ("Fig. 7.1", "Photorealistic Main Menu Interface with Non-Blocking UI Architecture", "73"),
        ("Fig. 7.2", "Level 1: Crime Scene Investigation and Binary Keypad Chamber", "74"),
        ("Fig. 7.3", "Level 2: Ballistics Lab and Forensic Trajectory Terminal", "75"),
        ("Fig. 7.4", "Level 3: Steganographic Legal Archive and Rotor Cipher Mechanism", "76"),
        ("Fig. 7.5", "Level 4: Secure Vault and Multi-Tumbler Evidence Locker", "77"),
        ("Fig. 7.6", "Level 5: Judge's Chambers Pre-Trial Deliberation and Statement Desk", "78"),
        ("Fig. 7.7", "Level 6: Grand Courtroom of Justice and Final Verdict Bench", "79"),
        ("Fig. 7.8", "Victory Screen: Game Complete Interface with Active Scene Navigation", "80"),
    ]

    lof_table = doc.add_table(rows=len(figures_list) + 1, cols=3)
    lof_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    lof_table.autofit = False
    set_table_borders(lof_table)

    headers = ["Figure No.", "Title / Description", "Page"]
    col_widths = [Inches(1.2), Inches(4.5), Inches(0.8)]
    for j, h in enumerate(headers):
        cell = lof_table.cell(0, j)
        cell.width = col_widths[j]
        set_cell_background(cell, "102C57")
        set_cell_margins(cell, top=100, bottom=100, left=100, right=100)
        p = cell.paragraphs[0]
        if j == 2:
            p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        run = p.add_run(h)
        run.font.name = "Times New Roman"
        run.font.size = Pt(10)
        run.font.bold = True
        run.font.color.rgb = RGBColor(255, 255, 255)

    for i, (f_no, f_desc, f_pg) in enumerate(figures_list):
        row = lof_table.rows[i + 1]
        for j, val in enumerate([f_no, f_desc, f_pg]):
            cell = row.cells[j]
            cell.width = col_widths[j]
            if (i % 2) == 1:
                set_cell_background(cell, "F7F9FB")
            set_cell_margins(cell, top=80, bottom=80, left=100, right=100)
            p = cell.paragraphs[0]
            if j == 2:
                p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
            run = p.add_run(val)
            run.font.name = "Times New Roman"
            run.font.size = Pt(9.5)
            if j == 0:
                run.font.bold = True

    doc.add_page_break()

    # ═════════════════════════════════════════════════════════════════════════
    # PAGE 7: LIST OF TABLES & LIST OF ABBREVIATIONS
    # ═════════════════════════════════════════════════════════════════════════
    p_lot_title = doc.add_paragraph()
    p_lot_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_lot_title.paragraph_format.space_before = Pt(16)
    p_lot_title.paragraph_format.space_after = Pt(12)
    r_lt = p_lot_title.add_run("LIST OF TABLES")
    r_lt.font.name = "Times New Roman"
    r_lt.font.size = Pt(15)
    r_lt.font.bold = True
    r_lt.font.color.rgb = NAVY

    tables_list = [
        ("Table 2.1", "Comparative Evaluation of Existing Forensic and Puzzle Game Architectures", "20"),
        ("Table 3.1", "Programming Languages and Development Technology Stack", "24"),
        ("Table 3.2", "Functional Requirements Specification Matrix (FR-01 to FR-20)", "25"),
        ("Table 3.3", "Non-Functional Requirements Specification Matrix (NFR-01 to NFR-15)", "27"),
        ("Table 3.4", "Integrated Development Requirements Matrix (IDR-01 to IDR-10)", "28"),
        ("Table 3.5", "Hardware Specification for Development Workstation and Target Deployment", "29"),
        ("Table 4.1", "System Event Execution and Trigger-Response Table (E-01 to E-10)", "35"),
        ("Table 4.2", "Cryptographic Formulation and Verification Logic for Game Levels", "46"),
        ("Table 4.3", "State Transition Matrix for Deterministic Puzzle FSM Execution", "47"),
        ("Table 5.1", "tbl_player_session (Session Telemetry Record)", "54"),
        ("Table 6.1", "Exhaustive Test Case Execution Log (45 Test Cases)", "65"),
        ("Table 6.2", "Real-Time Rendering and Frame Latency Profiling Results", "70"),
        ("Table 7.1", "System Usability Scale (SUS) Quantitative Evaluation Results", "81"),
    ]

    lot_table = doc.add_table(rows=len(tables_list) + 1, cols=3)
    lot_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    lot_table.autofit = False
    set_table_borders(lot_table)

    for j, h in enumerate(headers):
        cell = lot_table.cell(0, j)
        cell.width = col_widths[j]
        set_cell_background(cell, "102C57")
        set_cell_margins(cell, top=80, bottom=80, left=100, right=100)
        p = cell.paragraphs[0]
        if j == 2:
            p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        run = p.add_run(h)
        run.font.name = "Times New Roman"
        run.font.size = Pt(9.5)
        run.font.bold = True
        run.font.color.rgb = RGBColor(255, 255, 255)

    for i, (t_no, t_desc, t_pg) in enumerate(tables_list):
        row = lot_table.rows[i + 1]
        for j, val in enumerate([t_no, t_desc, t_pg]):
            cell = row.cells[j]
            cell.width = col_widths[j]
            if (i % 2) == 1:
                set_cell_background(cell, "F7F9FB")
            set_cell_margins(cell, top=70, bottom=70, left=100, right=100)
            p = cell.paragraphs[0]
            if j == 2:
                p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
            run = p.add_run(val)
            run.font.name = "Times New Roman"
            run.font.size = Pt(9)
            if j == 0:
                run.font.bold = True

    # Abbreviations
    p_abb_title = doc.add_paragraph()
    p_abb_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_abb_title.paragraph_format.space_before = Pt(20)
    p_abb_title.paragraph_format.space_after = Pt(10)
    r_ab = p_abb_title.add_run("LIST OF ABBREVIATIONS")
    r_ab.font.name = "Times New Roman"
    r_ab.font.size = Pt(14)
    r_ab.font.bold = True
    r_ab.font.color.rgb = NAVY

    abbreviations = [
        ("URP", "Universal Render Pipeline"),
        ("SRP", "Scriptable Render Pipeline"),
        ("FPS", "Frames Per Second"),
        ("FSM", "Finite State Machine"),
        ("UI / UX", "User Interface / User Experience"),
        ("AABB", "Axis-Aligned Bounding Box"),
        ("PBR", "Physically Based Rendering"),
        ("HDRP", "High Definition Render Pipeline"),
        ("GI", "Global Illumination"),
        ("GC", "Garbage Collection / Garbage Collector"),
        ("TMP", "TextMeshPro"),
        ("SUS", "System Usability Scale"),
        ("UML", "Unified Modeling Language"),
        ("OOP", "Object-Oriented Programming"),
        ("API", "Application Programming Interface"),
        ("DOTS", "Data-Oriented Technology Stack"),
    ]

    abb_table = doc.add_table(rows=len(abbreviations) + 1, cols=2)
    abb_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    abb_table.autofit = False
    set_table_borders(abb_table)

    abb_headers = ["Abbreviation", "Full Form"]
    abb_widths = [Inches(1.8), Inches(4.7)]
    for j, h in enumerate(abb_headers):
        cell = abb_table.cell(0, j)
        cell.width = abb_widths[j]
        set_cell_background(cell, "35598E")
        set_cell_margins(cell, top=70, bottom=70, left=100, right=100)
        p = cell.paragraphs[0]
        run = p.add_run(h)
        run.font.name = "Times New Roman"
        run.font.size = Pt(9.5)
        run.font.bold = True
        run.font.color.rgb = RGBColor(255, 255, 255)

    for i, (abbr, full) in enumerate(abbreviations):
        row = abb_table.rows[i + 1]
        for j, val in enumerate([abbr, full]):
            cell = row.cells[j]
            cell.width = abb_widths[j]
            if (i % 2) == 1:
                set_cell_background(cell, "F7F9FB")
            set_cell_margins(cell, top=60, bottom=60, left=100, right=100)
            p = cell.paragraphs[0]
            run = p.add_run(val)
            run.font.name = "Times New Roman"
            run.font.size = Pt(9)
            if j == 0:
                run.font.bold = True

    doc.add_page_break()

    # ═════════════════════════════════════════════════════════════════════════
    # PAGE 8: TABLE OF CONTENTS
    # ═════════════════════════════════════════════════════════════════════════
    p_toc_title = doc.add_paragraph()
    p_toc_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_toc_title.paragraph_format.space_before = Pt(20)
    p_toc_title.paragraph_format.space_after = Pt(14)
    r_tc = p_toc_title.add_run("TABLE OF CONTENTS")
    r_tc.font.name = "Times New Roman"
    r_tc.font.size = Pt(16)
    r_tc.font.bold = True
    r_tc.font.color.rgb = NAVY

    toc_items = [
        ("CERTIFICATE OF APPROVAL", "2", True),
        ("CANDIDATE'S DECLARATION", "3", True),
        ("ACKNOWLEDGEMENTS", "4", True),
        ("ABSTRACT", "5", True),
        ("LIST OF FIGURES", "6", True),
        ("LIST OF TABLES", "7", True),
        ("LIST OF ABBREVIATIONS", "7", True),
        ("CHAPTER 1: INTRODUCTION", "9", True),
        ("  1.1 Background and Problem Domain", "9", False),
        ("  1.2 Problem Statement and Research Motivation", "10", False),
        ("  1.3 Project Objectives and Scope", "11", False),
        ("  1.4 Research Methodology and Engineering Workflow", "13", False),
        ("  1.5 Dissertation Organization", "14", False),
        ("CHAPTER 2: LITERATURE SURVEY AND RELATED WORK", "15", True),
        ("  2.1 Evolution of Forensic and Investigative Serious Games", "15", False),
        ("  2.2 Real-Time Graphics Pipelines and URP in Serious Games", "17", False),
        ("  2.3 Cryptographic and Logic Puzzle Design Paradigms", "19", False),
        ("  2.4 Comparative Analysis of Existing Benchmark Solutions", "20", False),
        ("  2.5 Identified Research Gaps and Novel Contributions", "22", False),
        ("CHAPTER 3: SOFTWARE REQUIREMENTS SPECIFICATION (SRS)", "23", True),
        ("  3.1 Architectural Scope: Front End and Backend Demarcation", "23", False),
        ("  3.2 Programming Languages and Technology Stack", "24", False),
        ("  3.3 Functional Requirements Specification (FR-01 to FR-20)", "25", False),
        ("  3.4 Non-Functional Requirements Specification (NFR-01 to NFR-15)", "27", False),
        ("  3.5 Integrated Development Requirements (IDR-01 to IDR-10)", "28", False),
        ("  3.6 Detailed Use Case Specifications", "29", False),
        ("  3.7 Operational Environment Specifications & Feasibility Study", "30", False),
        ("CHAPTER 4: SYSTEM DESIGN AND ARCHITECTURE", "32", True),
        ("  4.1 High-Level Layered System Architecture", "32", False),
        ("  4.2 Game Lifecycle and State Machine Architecture", "34", False),
        ("  4.3 Unified Modeling Language (UML) Diagrams", "35", False),
        ("    4.3.1 1. Event Table (Table 4.1 & Fig. 4.1)", "35", False),
        ("    4.3.2 2. Class Diagram (Fig. 4.2)", "37", False),
        ("    4.3.3 3. Object Diagram (Fig. 4.3)", "39", False),
        ("    4.3.4 4. Use Case Diagram (Fig. 4.4)", "40", False),
        ("    4.3.5 5. Sequence Diagram (Fig. 4.5)", "41", False),
        ("    4.3.6 6. Activity Diagram (Fig. 4.6)", "42", False),
        ("    4.3.7 7. Component Diagram (Fig. 4.7)", "43", False),
        ("    4.3.8 8. Deployment Diagram (Fig. 4.8)", "44", False),
        ("  4.4 Class-by-Class Method and Field Specifications", "45", False),
        ("  4.5 Cryptographic and Mathematical Formalisms", "48", False),
        ("  4.6 State Transition Matrix for Puzzle FSM Execution", "50", False),
        ("CHAPTER 5: DATABASE AND DATA PERSISTENCE DESIGN", "52", True),
        ("  5.1 Data Architecture in Interactive Serious Games", "52", False),
        ("  5.2 Entity-Relationship (ER) Diagram & Conceptual Schema", "53", False),
        ("  5.3 Relational Database Schema & Table Specifications", "55", False),
        ("  5.4 Structured Serialization Data Layer (SaveData.json)", "57", False),
        ("CHAPTER 6: CORE LOGIC CODE AND IMPLEMENTATION", "58", True),
        ("  6.1 First-Person Controller and Kinematic Locomotion", "58", False),
        ("  6.2 Raycast Interaction and Reticle Feedback Pipeline", "60", False),
        ("  6.3 Level 1: Crime Scene Investigation & Binary Keypad Logic", "62", False),
        ("  6.4 Level 2: Ballistics Lab & Trajectory Calculation", "64", False),
        ("  6.5 Level 3: Document Steganography & Caesar Rotor Mechanism", "66", False),
        ("  6.6 Level 4: Secure Vault & Multi-Tumbler Combination Lock", "68", False),
        ("  6.7 Level 5: Judge's Chambers Pre-Trial Deliberation", "70", False),
        ("  6.8 Level 6: Grand Courtroom Verdict Evaluation Engine", "72", False),
        ("CHAPTER 7: SOFTWARE TESTING AND QUALITY ASSURANCE", "74", True),
        ("  7.1 Testing Strategy and Verification Framework", "74", False),
        ("  7.2 Exhaustive Test Case Execution Log (45 Test Cases)", "76", False),
        ("  7.3 Performance Profiling, Frame Latencies, and Memory Stress", "80", False),
        ("CHAPTER 8: RESULTS, EVALUATION AND DISCUSSION", "82", True),
        ("  8.1 Photorealistic Environmental Overhaul and Visual Fidelity", "82", False),
        ("  8.2 Scene-by-Scene Architectural Walkthrough and Screenshots", "83", False),
        ("  8.3 System Usability Scale (SUS) Quantitative Evaluation", "88", False),
        ("CHAPTER 9: CONCLUSION AND FUTURE SCOPE", "90", True),
        ("  9.1 Concluding Remarks and Technical Contributions", "90", False),
        ("  9.2 Identified Limitations and Future Research Roadmap", "91", False),
        ("REFERENCES AND BIBLIOGRAPHY", "93", True),
        ("APPENDIX A: SCENE HIERARCHY AND OBJECT DICTIONARY", "96", True),
        ("APPENDIX B: INPUT MAPPING AND CONFIGURATION MATRIX", "97", True),
    ]

    toc_table = doc.add_table(rows=len(toc_items), cols=2)
    toc_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    toc_table.autofit = False
    
    t_widths = [Inches(5.7), Inches(0.8)]
    for i, (title, page, is_bold) in enumerate(toc_items):
        row = toc_table.rows[i]
        
        c0 = row.cells[0]
        c0.width = t_widths[0]
        set_cell_margins(c0, top=30, bottom=30, left=50, right=50)
        p0 = c0.paragraphs[0]
        p0.paragraph_format.space_before = Pt(1)
        p0.paragraph_format.space_after = Pt(1)
        run0 = p0.add_run(title)
        run0.font.name = "Times New Roman"
        run0.font.size = Pt(9.5 if is_bold else 9)
        run0.font.bold = is_bold
        if is_bold:
            run0.font.color.rgb = NAVY

        c1 = row.cells[1]
        c1.width = t_widths[1]
        set_cell_margins(c1, top=30, bottom=30, left=50, right=50)
        p1 = c1.paragraphs[0]
        p1.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        p1.paragraph_format.space_before = Pt(1)
        p1.paragraph_format.space_after = Pt(1)
        run1 = p1.add_run(page)
        run1.font.name = "Times New Roman"
        run1.font.size = Pt(9.5 if is_bold else 9)
        run1.font.bold = is_bold

    doc.add_page_break()
