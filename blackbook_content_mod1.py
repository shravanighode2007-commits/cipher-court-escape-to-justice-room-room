# blackbook_content_mod1.py
# Module 1 Content: Front Matter, Chapters 1, 2, 3, 4, 5 for Cipher Court Project Blackbook

import os
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from blackbook_helpers import (
    FONT_NAME, set_cell_background, set_cell_margins, set_table_borders, set_table_grid_borders,
    add_module_banner, add_chapter_title, add_heading, add_subheading,
    add_body_paragraph, add_bullet_point, add_image_diagram, add_single_page_diagram, add_code_block
)

def add_front_matter(doc, toc_data, tot_data, tof_data):
    """Generates all Front Matter pages adhering to University and Blackbook guidelines."""
    
    # ---------------------------------------------------------
    # 1. TITLE PAGE (No header/footer)
    # ---------------------------------------------------------
    for _ in range(3):
        doc.add_paragraph()

    p_proj = doc.add_paragraph()
    p_proj.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p_proj.add_run("A PROJECT REPORT\n\nOn\n\n")
    r.font.name = FONT_NAME
    r.font.size = Pt(14)
    r.font.bold = True

    r_title = p_proj.add_run("CIPHER COURT: AN INTERACTIVE 3D CYBERSECURITY INVESTIGATION AND PUZZLE-BASED ESCAPE ROOM GAME\n")
    r_title.font.name = FONT_NAME
    r_title.font.size = Pt(16)
    r_title.font.bold = True

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sub = p_sub.add_run("Submitted by\n\n")
    r_sub.font.name = FONT_NAME
    r_sub.font.size = Pt(12)
    r_sub.font.bold = True

    r_name = p_sub.add_run("Ms. Shravani Laxman Ghode\n(Roll No. 9022)\n\n")
    r_name.font.name = FONT_NAME
    r_name.font.size = Pt(14)
    r_name.font.bold = True

    r_deg = p_sub.add_run("in partial fulfillment for the award of the degree\nof\nBACHELOR OF SCIENCE\nin\nCOMPUTER SCIENCE\n\nunder the guidance of\n")
    r_deg.font.name = FONT_NAME
    r_deg.font.size = Pt(12)

    r_guide = p_sub.add_run("PROF. PRANJALI CHAUDHARI\nDepartment of Computer Science\n\n")
    r_guide.font.name = FONT_NAME
    r_guide.font.size = Pt(13)
    r_guide.font.bold = True

    logo_path = os.path.abspath("e:/vyt/extracted_assets/college_logo.png")
    if os.path.exists(logo_path):
        p_logo = doc.add_paragraph()
        p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_logo.paragraph_format.space_before = Pt(4)
        p_logo.paragraph_format.space_after = Pt(8)
        p_logo.add_run().add_picture(logo_path, width=Inches(1.3))

    p_col = doc.add_paragraph()
    p_col.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_col = p_col.add_run("Modern Education Society’s\nThe D. G. Ruparel College of Arts, Science & Commerce\n(Sem - V)\n(2026 – 2027)")
    r_col.font.name = FONT_NAME
    r_col.font.size = Pt(12)
    r_col.font.bold = True

    doc.add_page_break()

    # ---------------------------------------------------------
    # 2. CERTIFICATE (Page ii)
    # ---------------------------------------------------------
    if os.path.exists(logo_path):
        p_logo2 = doc.add_paragraph()
        p_logo2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_logo2.paragraph_format.space_before = Pt(10)
        p_logo2.paragraph_format.space_after = Pt(6)
        p_logo2.add_run().add_picture(logo_path, width=Inches(1.2))

    p_c_head = doc.add_paragraph()
    p_c_head.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_c_head.paragraph_format.space_after = Pt(18)
    r_ch = p_c_head.add_run("Modern Education Society’s\nThe D. G. Ruparel College of Arts, Science & Commerce,\nsenapati bapat marg, opp. Matunga road station (w.r.), mahim, mumbai 400 016\n\nDepartment of Computer Science\n\nCERTIFICATE")
    r_ch.font.name = FONT_NAME
    r_ch.font.size = Pt(13)
    r_ch.font.bold = True

    p_c_body = doc.add_paragraph()
    p_c_body.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_c_body.paragraph_format.line_spacing = 1.35
    p_c_body.paragraph_format.space_after = Pt(28)
    r_cb = p_c_body.add_run(
        "This is to certify that Ms. Shravani Laxman Ghode, Seat no: 9022 of T.Y.B.Sc. (Sem V) class has "
        "satisfactorily completed the project entitled \"CIPHER COURT – ESCAPE TO JUSTICE ROOM: "
        "AN INTERACTIVE 3D CYBERSECURITY INVESTIGATION AND PUZZLE-BASED ESCAPE ROOM GAME USING PYTHON, "
        "AES ENCRYPTION, SQLITE, AND UNITY C#\", to be submitted in the partial fulfillment for the award "
        "of Bachelor of Science in Computer Science during the academic year 2026 – 2027."
    )
    r_cb.font.name = FONT_NAME
    r_cb.font.size = Pt(12)

    p_date = doc.add_paragraph()
    p_date.paragraph_format.space_after = Pt(36)
    r_dt = p_date.add_run("Date of Submission: ______________________")
    r_dt.font.name = FONT_NAME
    r_dt.font.size = Pt(12)
    r_dt.font.bold = True

    # Signatures Table
    sig_tbl = doc.add_table(rows=2, cols=2)
    sig_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    sig_tbl.autofit = False
    for row in sig_tbl.rows:
        for cell in row.cells:
            cell.width = Inches(3.2)
            set_cell_margins(cell, 80, 80, 80, 80)
    
    r0c0 = sig_tbl.cell(0, 0).paragraphs[0]
    r0c0.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r0c0.add_run("Project Guide\nProf. Pranjali Chaudhari").font.name = FONT_NAME
    r0c0.runs[0].font.bold = True
    r0c0.runs[0].font.size = Pt(12)

    r0c1 = sig_tbl.cell(0, 1).paragraphs[0]
    r0c1.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r0c1.add_run("Head / Incharge,\nDepartment Computer Science").font.name = FONT_NAME
    r0c1.runs[0].font.bold = True
    r0c1.runs[0].font.size = Pt(12)

    r1c0 = sig_tbl.cell(1, 0).paragraphs[0]
    r1c0.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r1c0.paragraph_format.space_before = Pt(30)
    r1c0.add_run("College Seal").font.name = FONT_NAME
    r1c0.runs[0].font.bold = True
    r1c0.runs[0].font.size = Pt(12)

    r1c1 = sig_tbl.cell(1, 1).paragraphs[0]
    r1c1.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r1c1.paragraph_format.space_before = Pt(30)
    r1c1.add_run("Signature of Examiner").font.name = FONT_NAME
    r1c1.runs[0].font.bold = True
    r1c1.runs[0].font.size = Pt(12)

    doc.add_page_break()

    # ---------------------------------------------------------
    # 3. ACKNOWLEDGEMENTS (Page iii)
    # ---------------------------------------------------------
    p_ack = doc.add_paragraph()
    p_ack.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_ack.paragraph_format.space_before = Pt(20)
    p_ack.paragraph_format.space_after = Pt(16)
    r_at = p_ack.add_run("ACKNOWLEDGEMENTS")
    r_at.font.name = FONT_NAME
    r_at.font.size = Pt(16)
    r_at.font.bold = True

    add_body_paragraph(doc, "I would like to express my sincere gratitude to all those who provided guidance and support throughout the completion of this project.")
    add_body_paragraph(
        doc,
        "First and foremost, I extend my heartfelt thanks to my project guide, Prof. Pranjali Chaudhari, "
        "whose expert advice, encouragement, and constructive feedback were invaluable in shaping this project. "
        "Their guidance helped me navigate the technical challenges of developing an interactive 3D cybersecurity serious game, "
        "structuring the modular Unity 6 Universal Render Pipeline (URP) architecture, implementing distance-bounded raycast interaction systems, "
        "AES-256 cryptographic verification routines, and full-stack event persistence with Python and SQLite/PostgreSQL."
    )
    add_body_paragraph(
        doc,
        "I am deeply grateful to the Head / Incharge and the faculty members of the Department of Computer Science "
        "at Modern Education Society’s The D.G. Ruparel College of Arts, Commerce and Science, Mahim, Mumbai, "
        "for providing the necessary laboratory resources, computing facilities, GPU rendering hardware, and academic environment "
        "that facilitated this project's development through the requirement engineering, system design, implementation, testing, and evaluation phases."
    )
    add_body_paragraph(
        doc,
        "I would also like to thank the creators and maintainers of the open-source tools, engines, libraries, and technologies used in this project, "
        "including Unity Technologies (Unity 6 LTS, Universal Render Pipeline, TextMeshPro), Microsoft (C# 9.0, Visual Studio Code), "
        "Python Software Foundation (Python 3.12, SQLite 3, FastAPI/Flask, Psycopg2), Git, and GitHub. "
        "Their excellent documentation and robust platforms greatly accelerated the development, real-time spatial physics tuning, and database verification processes."
    )
    add_body_paragraph(
        doc,
        "I also acknowledge the support received from my classmates, peers, and everyone who contributed suggestions, testing feedback, "
        "or encouragement during the development and documentation stages of Cipher Court. Their perceptive observations during user trials "
        "helped identify reticle alignment challenges, refined puzzle feedback timers, and polished the solemn legal courtroom aesthetic."
    )
    add_body_paragraph(
        doc,
        "The completion of this project has provided valuable practical experience in requirements engineering, 3D serious game architecture, "
        "cryptographic algorithms, full-stack database integration, software testing, and technical documentation. "
        "I am grateful for the opportunity to apply the concepts learned during the Bachelor of Science in Computer Science programme to a complete working project."
    )
    add_body_paragraph(doc, "Finally, I would like to thank my family and friends for their continuous support and understanding during the project, which enabled me to dedicate the time and focus required for its successful completion.")

    doc.add_page_break()

    # ---------------------------------------------------------
    # 4. DECLARATION (Page iv)
    # ---------------------------------------------------------
    p_dec = doc.add_paragraph()
    p_dec.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_dec.paragraph_format.space_before = Pt(20)
    p_dec.paragraph_format.space_after = Pt(16)
    r_dt = p_dec.add_run("DECLARATION")
    r_dt.font.name = FONT_NAME
    r_dt.font.size = Pt(16)
    r_dt.font.bold = True

    add_body_paragraph(
        doc,
        "I, Shravani Laxman Ghode (Roll No. 9022), student of the T.Y.B.Sc. (Computer Science – Sem V) class, hereby declare that the project entitled "
        "\"Cipher Court: An Interactive 3D Cybersecurity Investigation and Puzzle-Based Escape Room Game using Python, AES Encryption, SQLite, and Unity Hub, C#\" "
        "submitted in partial fulfillment for the award of the degree of Bachelor of Science in Computer Science during the academic year 2026 – 2027 is my original work. "
        "The project has been carried out under the guidance of Prof. Pranjali Chaudhari and represents the work completed by me as part of the prescribed academic project requirements. "
        "Furthermore, this project has not formed the basis for the award of any degree, associateship, fellowship, or any other similar titles."
    )
    add_body_paragraph(
        doc,
        "I further declare that the problem identification, feasibility study, requirement engineering specifications, system architecture design, "
        "database schemas, Unified Modeling Language (UML) diagrams, Data Flow Diagrams (DFD), application implementation, testing records, "
        "user interface operational workflows, and source code excerpts included in this report across Module 1 and Module 2 have been prepared for the academic evaluation of the Cipher Court project."
    )
    add_body_paragraph(
        doc,
        "Wherever external open-source libraries, software frameworks, asset textures, audio clips, or technical documentation—including Unity 6, URP, C#, "
        "Python 3.12, SQLite 3, PostgreSQL, Visual Studio Code, Git, and GitHub—have been used, they have been acknowledged appropriately in the References section of this report."
    )
    add_body_paragraph(
        doc,
        "I understand that the submission is subject to the academic rules and regulations of D.G. Ruparel College of Arts, Commerce and Science, Mahim, "
        "and that the responsibility for the originality and accuracy of the submitted work rests with me."
    )

    p_sig_info = doc.add_paragraph()
    p_sig_info.paragraph_format.space_before = Pt(20)
    p_sig_info.paragraph_format.line_spacing = 1.3
    r_si = p_sig_info.add_run(
        "Name of the Student: Ms. Shravani Laxman Ghode\n"
        "Roll No.: 9022\n"
        "Class: T.Y.B.Sc. (Computer Science – Sem V)\n"
        "Signature of the Student: ______________________\n\n"
        "Place: Mumbai\n"
        "Date: ______________________"
    )
    r_si.font.name = FONT_NAME
    r_si.font.size = Pt(12)
    r_si.font.bold = True

    doc.add_page_break()

    # ---------------------------------------------------------
    # 5. LIST OF ABBREVIATIONS (Page v)
    # ---------------------------------------------------------
    p_abb = doc.add_paragraph()
    p_abb.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_abb.paragraph_format.space_before = Pt(20)
    p_abb.paragraph_format.space_after = Pt(16)
    r_at = p_abb.add_run("LIST OF ABBREVIATIONS")
    r_at.font.name = FONT_NAME
    r_at.font.size = Pt(16)
    r_at.font.bold = True

    abbreviations = [
        ("AES", "Advanced Encryption Standard"),
        ("API", "Application Programming Interface"),
        ("CALL", "Computer-Assisted Language / Learning Platform"),
        ("CPU", "Central Processing Unit"),
        ("CSS", "Cascading Style Sheets"),
        ("DFD", "Data Flow Diagram"),
        ("ER", "Entity-Relationship"),
        ("FPS", "Frames Per Second"),
        ("FR", "Functional Requirement"),
        ("GPU", "Graphics Processing Unit"),
        ("GUI", "Graphical User Interface"),
        ("HLSL", "High-Level Shader Language"),
        ("HTML", "HyperText Markup Language"),
        ("IDR", "Integrated Development Requirement"),
        ("JSON", "JavaScript Object Notation"),
        ("NFR", "Non-Functional Requirement"),
        ("PBR", "Physically Based Rendering"),
        ("PK / FK", "Primary Key / Foreign Key"),
        ("RAM", "Random Access Memory"),
        ("REST", "Representational State Transfer"),
        ("SDF", "Signed Distance Field"),
        ("SDLC", "Software Development Life Cycle"),
        ("SQL", "Structured Query Language"),
        ("SRS", "Software Requirements Specification"),
        ("SUS", "System Usability Scale"),
        ("UI / UX", "User Interface / User Experience"),
        ("UML", "Unified Modeling Language"),
        ("URP", "Universal Render Pipeline (Unity 6)"),
        ("WBS", "Work Breakdown Structure"),
    ]

    abb_tbl = doc.add_table(rows=len(abbreviations) + 1, cols=2)
    abb_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    abb_tbl.autofit = False
    set_table_grid_borders(abb_tbl)

    col_widths = [Inches(2.2), Inches(4.3)]
    for row in abb_tbl.rows:
        for i, cell in enumerate(row.cells):
            cell.width = col_widths[i]
            set_cell_margins(cell, 80, 80, 100, 100)

    hdr_c0 = abb_tbl.cell(0, 0).paragraphs[0]
    hdr_c0.add_run("Abbreviation").font.bold = True
    hdr_c0.runs[0].font.name = FONT_NAME
    hdr_c0.runs[0].font.size = Pt(12)
    set_cell_background(abb_tbl.cell(0, 0), "F2F2F2")

    hdr_c1 = abb_tbl.cell(0, 1).paragraphs[0]
    hdr_c1.add_run("Full Form").font.bold = True
    hdr_c1.runs[0].font.name = FONT_NAME
    hdr_c1.runs[0].font.size = Pt(12)
    set_cell_background(abb_tbl.cell(0, 1), "F2F2F2")

    for idx, (abbr, full) in enumerate(abbreviations):
        c0 = abb_tbl.cell(idx + 1, 0).paragraphs[0]
        c0.add_run(abbr).font.bold = True
        c0.runs[0].font.name = FONT_NAME
        c0.runs[0].font.size = Pt(11)

        c1 = abb_tbl.cell(idx + 1, 1).paragraphs[0]
        c1.add_run(full).font.name = FONT_NAME
        c1.runs[0].font.size = Pt(11)

    doc.add_page_break()

    # ---------------------------------------------------------
    # 6. TABLE OF CONTENTS (Page vi)
    # ---------------------------------------------------------
    p_toc = doc.add_paragraph()
    p_toc.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_toc.paragraph_format.space_before = Pt(20)
    p_toc.paragraph_format.space_after = Pt(16)
    r_tt = p_toc.add_run("TABLE OF CONTENTS")
    r_tt.font.name = FONT_NAME
    r_tt.font.size = Pt(16)
    r_tt.font.bold = True

    toc_tbl = doc.add_table(rows=len(toc_data) + 1, cols=3)
    toc_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    toc_tbl.autofit = False
    set_table_grid_borders(toc_tbl)

    t_widths = [Inches(1.2), Inches(4.5), Inches(0.8)]
    for row in toc_tbl.rows:
        for i, cell in enumerate(row.cells):
            cell.width = t_widths[i]
            set_cell_margins(cell, 70, 70, 90, 90)

    h0 = toc_tbl.cell(0, 0).paragraphs[0]
    h0.add_run("Topic / No.").font.bold = True
    h0.runs[0].font.name = FONT_NAME
    h0.runs[0].font.size = Pt(11)
    set_cell_background(toc_tbl.cell(0, 0), "F2F2F2")

    h1 = toc_tbl.cell(0, 1).paragraphs[0]
    h1.add_run("Chapter / Section Description").font.bold = True
    h1.runs[0].font.name = FONT_NAME
    h1.runs[0].font.size = Pt(11)
    set_cell_background(toc_tbl.cell(0, 1), "F2F2F2")

    h2 = toc_tbl.cell(0, 2).paragraphs[0]
    h2.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    h2.add_run("Page No.").font.bold = True
    h2.runs[0].font.name = FONT_NAME
    h2.runs[0].font.size = Pt(11)
    set_cell_background(toc_tbl.cell(0, 2), "F2F2F2")

    for idx, (num, desc, page_str) in enumerate(toc_data):
        c0 = toc_tbl.cell(idx + 1, 0).paragraphs[0]
        r0 = c0.add_run(num)
        r0.font.name = FONT_NAME
        r0.font.size = Pt(10.5)
        if "MODULE" in num or "CHAPTER" in num or num == "-":
            r0.font.bold = True

        c1 = toc_tbl.cell(idx + 1, 1).paragraphs[0]
        r1 = c1.add_run(desc)
        r1.font.name = FONT_NAME
        r1.font.size = Pt(10.5)
        if "MODULE" in num or "CHAPTER" in num or num == "-":
            r1.font.bold = True

        c2 = toc_tbl.cell(idx + 1, 2).paragraphs[0]
        c2.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        r2 = c2.add_run(str(page_str))
        r2.font.name = FONT_NAME
        r2.font.size = Pt(10.5)
        if "MODULE" in num or "CHAPTER" in num or num == "-":
            r2.font.bold = True

    doc.add_page_break()

    # ---------------------------------------------------------
    # 7. TABLE OF TABLES (Page viii)
    # ---------------------------------------------------------
    p_tot = doc.add_paragraph()
    p_tot.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_tot.paragraph_format.space_before = Pt(20)
    p_tot.paragraph_format.space_after = Pt(16)
    r_tot_t = p_tot.add_run("TABLE OF TABLES")
    r_tot_t.font.name = FONT_NAME
    r_tot_t.font.size = Pt(16)
    r_tot_t.font.bold = True

    tot_tbl = doc.add_table(rows=len(tot_data) + 1, cols=3)
    tot_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tot_tbl.autofit = False
    set_table_grid_borders(tot_tbl)

    tot_widths = [Inches(1.3), Inches(4.4), Inches(0.8)]
    for row in tot_tbl.rows:
        for i, cell in enumerate(row.cells):
            cell.width = tot_widths[i]
            set_cell_margins(cell, 70, 70, 90, 90)

    th0 = tot_tbl.cell(0, 0).paragraphs[0]
    th0.add_run("Table No.").font.bold = True
    th0.runs[0].font.name = FONT_NAME
    th0.runs[0].font.size = Pt(11)
    set_cell_background(tot_tbl.cell(0, 0), "F2F2F2")

    th1 = tot_tbl.cell(0, 1).paragraphs[0]
    th1.add_run("Table Title / Description").font.bold = True
    th1.runs[0].font.name = FONT_NAME
    th1.runs[0].font.size = Pt(11)
    set_cell_background(tot_tbl.cell(0, 1), "F2F2F2")

    th2 = tot_tbl.cell(0, 2).paragraphs[0]
    th2.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    th2.add_run("Page No.").font.bold = True
    th2.runs[0].font.name = FONT_NAME
    th2.runs[0].font.size = Pt(11)
    set_cell_background(tot_tbl.cell(0, 2), "F2F2F2")

    for idx, (t_no, t_desc, t_page) in enumerate(tot_data):
        c0 = tot_tbl.cell(idx + 1, 0).paragraphs[0]
        r0 = c0.add_run(t_no)
        r0.font.name = FONT_NAME
        r0.font.size = Pt(10.5)
        r0.font.bold = True

        c1 = tot_tbl.cell(idx + 1, 1).paragraphs[0]
        r1 = c1.add_run(t_desc)
        r1.font.name = FONT_NAME
        r1.font.size = Pt(10.5)

        c2 = tot_tbl.cell(idx + 1, 2).paragraphs[0]
        c2.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        r2 = c2.add_run(str(t_page))
        r2.font.name = FONT_NAME
        r2.font.size = Pt(10.5)

    doc.add_page_break()

    # ---------------------------------------------------------
    # 8. TABLE OF FIGURES (Page ix)
    # ---------------------------------------------------------
    p_tof = doc.add_paragraph()
    p_tof.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_tof.paragraph_format.space_before = Pt(20)
    p_tof.paragraph_format.space_after = Pt(16)
    r_tof_t = p_tof.add_run("TABLE OF FIGURES")
    r_tof_t.font.name = FONT_NAME
    r_tof_t.font.size = Pt(16)
    r_tof_t.font.bold = True

    tof_tbl = doc.add_table(rows=len(tof_data) + 1, cols=3)
    tof_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tof_tbl.autofit = False
    set_table_grid_borders(tof_tbl)

    for row in tof_tbl.rows:
        for i, cell in enumerate(row.cells):
            cell.width = tot_widths[i]
            set_cell_margins(cell, 70, 70, 90, 90)

    fh0 = tof_tbl.cell(0, 0).paragraphs[0]
    fh0.add_run("Figure No.").font.bold = True
    fh0.runs[0].font.name = FONT_NAME
    fh0.runs[0].font.size = Pt(11)
    set_cell_background(tof_tbl.cell(0, 0), "F2F2F2")

    fh1 = tof_tbl.cell(0, 1).paragraphs[0]
    fh1.add_run("Figure Title / Description").font.bold = True
    fh1.runs[0].font.name = FONT_NAME
    fh1.runs[0].font.size = Pt(11)
    set_cell_background(tof_tbl.cell(0, 1), "F2F2F2")

    fh2 = tof_tbl.cell(0, 2).paragraphs[0]
    fh2.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    fh2.add_run("Page No.").font.bold = True
    fh2.runs[0].font.name = FONT_NAME
    fh2.runs[0].font.size = Pt(11)
    set_cell_background(tof_tbl.cell(0, 2), "F2F2F2")

    for idx, (f_no, f_desc, f_page) in enumerate(tof_data):
        c0 = tof_tbl.cell(idx + 1, 0).paragraphs[0]
        r0 = c0.add_run(f_no)
        r0.font.name = FONT_NAME
        r0.font.size = Pt(10.5)
        r0.font.bold = True

        c1 = tof_tbl.cell(idx + 1, 1).paragraphs[0]
        r1 = c1.add_run(f_desc)
        r1.font.name = FONT_NAME
        r1.font.size = Pt(10.5)

        c2 = tof_tbl.cell(idx + 1, 2).paragraphs[0]
        c2.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        r2 = c2.add_run(str(f_page))
        r2.font.name = FONT_NAME
        r2.font.size = Pt(10.5)

    doc.add_page_break()


def add_chapter_1(doc):
    """Adds Chapter 1: Problem Identification & Feasibility Study (Strictly matching Syllabus & Sample Blackbook)."""
    add_module_banner(doc, "1", "PROBLEM IDENTIFICATION, REQUIREMENT ENGINEERING & SYSTEM DESIGN PHASE")
    add_chapter_title(doc, "1", "PROBLEM IDENTIFICATION & FEASIBILITY STUDY")

    add_heading(doc, "Role and Responsibility")
    add_bullet_point(doc, "Cipher Court: An Interactive 3D Cybersecurity Investigation and Puzzle-Based Escape Room Game using Python, AES Encryption, SQLite, and Unity Hub, C#", bold_prefix="• Project Title:")
    add_bullet_point(doc, "Ms. Shravani Laxman Ghode (Roll No. 9022)", bold_prefix="• Student Name:")
    add_bullet_point(doc, "T.Y.B.Sc. (Computer Science – Sem V)", bold_prefix="• Class:")
    add_bullet_point(doc, "Prof. Pranjali Chaudhari", bold_prefix="• Project Guide:")

    add_subheading(doc, "Table 1.1: Role and Responsibility Across Project Phases")
    
    roles = [
        ("Module 1: Problem Identification & Requirement Engineering", 
         "Conducted comprehensive literature survey of existing cybersecurity educational systems, identified industry and institutional awareness bottlenecks, performed TELOS feasibility study, and authored IEEE Std 830-1998 Functional and Non-Functional Requirements."),
        ("Module 1: SDLC Planning & UML System Modeling", 
         "Selected the Prototype SDLC Model, formulated the 5-Phase Work Breakdown Structure (WBS) and Project Gantt Chart, engineered the System Event Table, and authored the complete UML model suite (Class, Object, Use Case, Sequence, Activity, Component, and Deployment diagrams)."),
        ("Module 1: 3-Tier Architecture & Database Schema Design", 
         "Architected decoupled 3-tier system design (Unity 3D client, C# game logic, Python database API), designed relational schema across six core entities (PLAYER, LEVEL, GAME_PROGRESS, CLUE, PUZZLE_ATTEMPT, EVIDENCE_RECORD), and formulated RESTful JSON API contracts."),
        ("Module 2: Full-Stack Serious Game Development", 
         "Engineered interactive 3D courtroom environment in Unity 6 URP, authored C# first-person controller and distance-bounded raycast interaction pipeline, implemented AES-256 evidence decryption and Caesar shift algorithms, and developed Python/SQLite backend audit server."),
        ("Module 2: System Testing, Desktop Deployment & Documentation", 
         "Executed 25 verification test cases across Unit, Integration, and Black-Box system testing, benchmarked 60 FPS graphics latency and <50ms interaction response, established GitHub repository version control, and compiled the complete Project Blackbook.")
    ]

    tbl = doc.add_table(rows=len(roles) + 1, cols=2)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    set_table_grid_borders(tbl)
    
    col_w = [Inches(2.2), Inches(4.3)]
    for row in tbl.rows:
        for i, cell in enumerate(row.cells):
            cell.width = col_w[i]
            set_cell_margins(cell, 80, 80, 100, 100)

    h0 = tbl.cell(0, 0).paragraphs[0]
    h0.add_run("Module / Phase").font.bold = True
    h0.runs[0].font.name = FONT_NAME
    h0.runs[0].font.size = Pt(11)
    set_cell_background(tbl.cell(0, 0), "F2F2F2")

    h1 = tbl.cell(0, 1).paragraphs[0]
    h1.add_run("Key Engineering Responsibilities Executed").font.bold = True
    h1.runs[0].font.name = FONT_NAME
    h1.runs[0].font.size = Pt(11)
    set_cell_background(tbl.cell(0, 1), "F2F2F2")

    for idx, (m_name, m_resp) in enumerate(roles):
        c0 = tbl.cell(idx + 1, 0).paragraphs[0]
        r0 = c0.add_run(m_name)
        r0.font.name = FONT_NAME
        r0.font.size = Pt(10.5)
        r0.font.bold = True

        c1 = tbl.cell(idx + 1, 1).paragraphs[0]
        r1 = c1.add_run(m_resp)
        r1.font.name = FONT_NAME
        r1.font.size = Pt(10.5)

    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    # 1.1 Background and Motivation
    add_heading(doc, "1.1 Background and Motivation")
    add_body_paragraph(
        doc,
        "In contemporary computing society, cyber scams, social engineering, phishing vectors, and digital extortion have escalated "
        "exponentially. Despite the proliferation of sophisticated automated security tools, the human element remains the single most "
        "vulnerable link in the cybersecurity defensive perimeter. Most end-users, students, and institutional employees possess only superficial, "
        "passive awareness of fundamental cryptographic safeguards and digital forensic workflows. Conventional pedagogical techniques—dominated by "
        "monotonous lectures, static text manuals, and disconnected multiple-choice quizzes—fail to cultivate intuitive analytical instincts or "
        "demonstrate the real-world consequences of insecure operational behavior."
    )
    add_body_paragraph(
        doc,
        "Serious games and interactive 3D virtual simulations represent an empirical leap forward in educational technology. By immersing "
        "learners inside a high-stakes, narrative-driven virtual environment, abstract concepts such as cryptographic ciphers, bitwise data masks, "
        "digital hashes, and forensic evidence collection are transformed into tangible, physical challenges. \"Cipher Court: Escape to Justice\" "
        "bridges this critical divide by casting the student as a forensic cybersecurity investigator trapped inside a grand judicial court complex "
        "under sudden digital lockdown. The player must physically explore 3D architectural spaces, inspect encrypted workstations, discover hidden "
        "clues, decode ciphertexts using mathematical and logical principles, and assemble an unassailable digital evidence dossier to deliver "
        "the final verdict before the court."
    )

    # 1.2 Objectives
    add_heading(doc, "1.2 Objectives")
    add_body_paragraph(doc, "The core engineering and pedagogical objectives of the Cipher Court platform are formulated as follows:")
    add_bullet_point(doc, "Develop an interactive 3D serious game in Unity 6 Universal Render Pipeline (URP) combining cybersecurity education, cryptographic codebreaking, and courtroom forensic reasoning.")
    add_bullet_point(doc, "Engineer a responsive first-person character controller and distance-bounded (2.5m) reticle raycast interaction system for inspecting physical 3D clues.")
    add_bullet_point(doc, "Implement progressive cryptographic puzzle modules, including binary/hexadecimal keypad decoding, Caesar rotor substitution, multi-tumbler mechanical lock simulation, and AES-256 evidence decryption.")
    add_bullet_point(doc, "Develop a robust attempt-limiting (maximum 3 attempts) and synchronized countdown timer (5:00 minutes per level) system that enforces disciplined forensic deduction.")
    add_bullet_point(doc, "Architect a decoupled full-stack persistence service utilizing Python 3.12, SQLite 3, and PostgreSQL to capture live audit logs of player submissions, clue discoveries, and time metrics.")
    add_bullet_point(doc, "Deliver a realistic 6-stage courtroom campaign culminating in a final judicial verdict confrontation where collected evidence is evaluated against contradictory witness statements.")
    add_bullet_point(doc, "Conduct comprehensive testing (Unit, Integration, Black-Box) to verify 60 FPS graphics stability, sub-50ms interaction latency, and tamper-resistant state validation.")

    # 1.3 Identification of a Real-World Problem
    add_heading(doc, "1.3 Identification of a Real-World Problem (Industry / Social / Institutional)")
    add_body_paragraph(
        doc,
        "A rigorous domain investigation reveals four critical structural bottlenecks that hinder cybersecurity literacy in academic institutions and enterprise environments:"
    )
    add_bullet_point(doc, "Limited Practical Application (Industry Gap): Corporate training and academic courses overwhelmingly rely on passive slides and abstract slides. Employees and undergraduates are never exposed to realistic attack scenarios or required to manually decrypt intercepted payloads under operational pressure.")
    add_bullet_point(doc, "Fragmented Learning Tools (Institutional Challenge): Concepts of basic cryptography, forensic evidence handling, password hygiene, and legal culpability are taught as separate, disconnected syllabi across multiple semesters, lacking a cohesive simulation that connects mathematical theory to judicial evidence.")
    add_bullet_point(doc, "Binary/Superficial Feedback (Pedagogical Bottleneck): Existing online quiz modules merely return binary 'Correct/Incorrect' checkmarks without illustrating the underlying logic of cipher shifts, key entropy, or how malicious actors exploit insecure communication channels.")
    add_bullet_point(doc, "High Barrier to Practical Labs (Social & Self-Learner Barrier): Setting up traditional Linux-based penetration testing laboratories (such as Kali Linux, Metasploit, or Snort) requires substantial systems administration expertise and high-end hardware, excluding non-specialist students and casual learners.")

    # 1.4 Problem Justification and Scope Definition
    add_heading(doc, "1.4 Problem Justification and Scope Definition")
    add_body_paragraph(
        doc,
        "To reconcile the disparity between theoretical security instruction and active cognitive skill acquisition, there is an imperative "
        "need for a standalone, highly engaging 3D desktop simulation that unifies forensic exploration with mathematical puzzle solving. "
        "By packaging complex security mechanics within an atmospheric narrative escape room, Cipher Court provides immediate tactile feedback, "
        "instilling lasting defensive habits.",
        bold_prefix="Core Problem Justification:"
    )
    add_body_paragraph(
        doc,
        "The project encompasses a standalone 6-level single-player investigation campaign built in Unity 6 URP for Windows 64-bit systems. "
        "The scope includes: Level 1 (Crime Scene Investigation & Evidence Clues), Level 2 (Cyber Forensic Terminal & Password Puzzle), "
        "Level 3 (Steganographic Legal Archive & Caesar Cipher Decryption), Level 4 (Secure Vault & 3-Digit Keypad Puzzle), "
        "Level 5 (Case File Synthesis & Suspect Statement Analysis), and Level 6 (High Courtroom Final Verdict Showdown). "
        "Backend persistence is handled via a local Python REST service with SQLite/PostgreSQL storage.",
        bold_prefix="Current Academic Scope:"
    )
    add_body_paragraph(
        doc,
        "Future releases plan to incorporate collaborative network multiplayer (allowing paired investigator-judge roles), "
        "virtual reality (VR) immersive headset tracking, adaptive procedural puzzle generation powered by Large Language Models (LLMs), "
        "and cloud-synchronized competitive leaderboards across academic institutions.",
        bold_prefix="Future Scope & Delimitations:"
    )

    # 1.5 Stakeholder Identification & Beneficiary Analysis
    add_heading(doc, "1.5 Stakeholder Identification & Beneficiary Analysis")
    add_bullet_point(doc, "Undergraduate and secondary school students gain a zero-cost, highly visual, experiential platform to master foundational cryptographic principles, digital hygiene, and forensic analysis in a risk-free environment.", bold_prefix="• Primary Beneficiaries (Students & Self-Learners):")
    add_bullet_point(doc, "Professors, lab assistants, and institutional evaluators utilize the simulation as an interactive laboratory exercise, leveraging live database audit trails to assess individual deduction proficiency.", bold_prefix="• Secondary Stakeholders (Faculty & Instructors):")
    add_bullet_point(doc, "Serious game engineers, security curriculum designers, and system administrators benefit from the modular C# Unity script architecture and decoupled Python REST endpoints to expand puzzle banks and integrate advanced cipher algorithms.", bold_prefix="• System Administrators & Developers:")

    # 1.6 Feasibility Analysis
    add_heading(doc, "1.6 Feasibility Analysis (Technical, Economic, Operational, Legal, Schedule)")
    add_body_paragraph(doc, "A comprehensive feasibility study was executed using the standard TELOS framework to validate the technical and operational viability of Cipher Court:")
    
    add_bullet_point(doc, "Technical Feasibility: The Unity 6 Universal Render Pipeline (URP) natively provides performant, photorealistic rendering across standard PC hardware. C# 9.0 delivers type-safe, event-driven gameplay logic, and Python 3.12 with SQLite provides non-blocking, asynchronous REST persistence without external network latency.")
    add_bullet_point(doc, "Economic Feasibility: Built entirely utilizing the free Unity Personal license, open-source software (Python, SQLite, VS Code, Git), and custom-authored 3D procedural environments. The financial cost of development and deployment stands at strictly ₹0.")
    add_bullet_point(doc, "Operational Feasibility: Operates as a lightweight standalone Windows desktop application requiring no specialized server configuration or complex administrative installation. The user interface utilizes universal WASD and mouse navigation conventions that are immediately intuitive to learners.")
    add_bullet_point(doc, "Legal & Ethical Feasibility: All puzzles and forensic scenarios are crafted strictly for defensive educational awareness. Cryptographic implementations comply with open cryptographic standards (AES-256, SHA-256). All architectural textures and sound effects are licensed under permissive Creative Commons and MIT licenses.")
    add_bullet_point(doc, "Schedule Feasibility: Structured across five disciplined Agile prototype development phases, enabling complete design, modeling, scripting, testing, and documentation within the prescribed academic semester timeline.")

    doc.add_page_break()


def add_chapter_2(doc):
    """Adds Chapter 2: Requirement Engineering (Strictly matching Syllabus & SRS Document)."""
    add_chapter_title(doc, "2", "REQUIREMENT ENGINEERING")

    add_heading(doc, "2.1 Functional Requirements Specification")
    add_body_paragraph(doc, "The functional requirements define the core operational behaviors, input handling, puzzle validation routines, and progression state management of Cipher Court:")

    add_subheading(doc, "Table 2.1: Functional Requirements Specification Table")

    fr_data = [
        ("FR-01", "Game Initialization", "The system shall allow the player to start a new game from the main menu, initializing all level states.", "High"),
        ("FR-02", "3D Scene Rendering", "The system shall display a photorealistic 3D courtroom/escape-room environment with URP lighting and materials.", "High"),
        ("FR-03", "Character Kinematics", "The system shall allow the player to move smoothly within the 3D space using standard keyboard (WASD) and mouse controls.", "High"),
        ("FR-04", "Raycast Object Interaction", "The system shall allow the player to interact with doors, files, documents, computers, locks, and clues within a 2.5m range.", "High"),
        ("FR-05", "Cipher Puzzle Delivery", "The system shall provide cipher-based puzzles (Caesar shift, binary/hex, AES) that the player must solve to progress.", "High"),
        ("FR-06", "Clue Presentation", "The system shall provide interactive physical clues and descriptive text prompts related to the active cipher puzzles.", "High"),
        ("FR-07", "Interactive Code Entry", "The system shall present on-screen input modals and keypads allowing the player to submit proposed passwords and codes.", "High"),
        ("FR-08", "Code Validation", "The system shall validate the player's submitted code against the target solution and display immediate correct/incorrect feedback.", "High"),
        ("FR-09", "Door Unlocking Logic", "The system shall trigger physical door unlocking and motorized opening animations when the correct puzzle solution is verified.", "High"),
        ("FR-10", "Progressive Area Unlocking", "The system shall unlock corresponding rooms, security lockers, or case archives upon successful puzzle resolution.", "High"),
        ("FR-11", "Game Progress Tracking", "The system shall maintain and update current player progress, completed puzzle flags, and collected evidence in memory.", "High"),
        ("FR-12", "Synchronized Timer", "The system shall provide a synchronized 5-minute (05:00) countdown timer for each puzzle room to track operational speed.", "Medium"),
        ("FR-13", "Contextual Hint System", "The system shall provide progressive contextual hints upon player request, applying an appropriate score deduction penalty.", "Medium"),
        ("FR-14", "Audio-Visual Feedback", "The system shall display distinct visual banner notifications and play acoustic cues for successful and failed interactions.", "Medium"),
        ("FR-15", "Pause & Navigation Menu", "The system shall provide a pause overlay containing Resume, Restart Level, Audio Toggle, and Main Menu Exit options.", "Medium"),
        ("FR-16", "Victory Completion Display", "The system shall display a dedicated victory screen summarizing forensic score, time taken, and accuracy upon solving all stages.", "High"),
        ("FR-17", "Level Restart Capability", "The system shall allow the player to restart the current room from its initial state upon puzzle failure or time expiration.", "Medium"),
        ("FR-18", "Dynamic Sound & Audio", "The system shall provide spatial 3D audio, background atmospheric hums, and UI chimes for important game events.", "Low"),
        ("FR-19", "Judicial Climax Trigger", "The system shall detect completion of all preliminary levels and trigger the final Level 6 Courtroom verdict trial sequence.", "High"),
        ("FR-20", "Graceful Application Exit", "The system shall provide a clean exit option that terminates the process and releases all memory and hardware hooks.", "Low")
    ]

    fr_tbl = doc.add_table(rows=len(fr_data) + 1, cols=4)
    fr_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    fr_tbl.autofit = False
    set_table_grid_borders(fr_tbl)

    widths = [Inches(0.9), Inches(1.8), Inches(3.1), Inches(0.9)]
    for row in fr_tbl.rows:
        for i, cell in enumerate(row.cells):
            cell.width = widths[i]
            set_cell_margins(cell, 60, 60, 80, 80)

    hdr = ["Req ID", "Module / Feature", "Functional Description", "Priority"]
    for i, title in enumerate(hdr):
        c = fr_tbl.cell(0, i).paragraphs[0]
        c.add_run(title).font.bold = True
        c.runs[0].font.name = FONT_NAME
        c.runs[0].font.size = Pt(11)
        set_cell_background(fr_tbl.cell(0, i), "F2F2F2")

    for idx, (rid, feat, desc, prio) in enumerate(fr_data):
        r = fr_tbl.rows[idx + 1]
        for col_idx, val in enumerate([rid, feat, desc, prio]):
            cp = r.cells[col_idx].paragraphs[0]
            r_run = cp.add_run(val)
            r_run.font.name = FONT_NAME
            r_run.font.size = Pt(10)
            if col_idx == 0 or col_idx == 3:
                r_run.font.bold = True

    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    # 2.2 Non-Functional Requirements Specification
    add_heading(doc, "2.2 Non-Functional Requirements Specification")
    add_body_paragraph(doc, "Non-functional requirements specify quality attributes, latency constraints, stability benchmarks, and developmental integrity standards:")

    add_subheading(doc, "Table 2.2: Non-Functional Requirements Specification Table")

    nfr_data = [
        ("NFR-01", "Performance & Frame Rate", "The game must maintain a smooth 60 frames per second (FPS) rendering on standard target hardware without stutter.", "High"),
        ("NFR-02", "Usability & UI Simplicity", "The interface must be minimalist, intuitive, and clearly indicate interactive objects via crosshair reticle state changes.", "High"),
        ("NFR-03", "Security & Access Control", "Game configuration values, puzzle answer hashes, and backend administrative routes must be protected from tampering.", "High"),
        ("NFR-04", "State Consistency", "The system shall maintain mathematical consistency of attempt counters, timer countdowns, and evidence states across scene loads.", "High"),
        ("NFR-05", "Modularity & Maintainability", "Code architecture must decouple player kinematics, raycast detection, puzzle evaluation, and UI systems into separate C# classes.", "High"),
        ("NFR-06", "Runtime Stability", "The standalone application must run stably without unhandled null pointer exceptions, memory leaks, or unexpected crashes.", "High"),
        ("NFR-07", "Scene Loading Latency", "3D room environments and asset materials must load within 2.5 seconds on modern desktop SSD/HDD storage.", "Medium"),
        ("NFR-08", "Control Responsiveness", "Player movement, camera look dampening, and mouse input polling must respond with sub-16ms latency.", "High"),
        ("NFR-09", "Instant Puzzle Feedback", "Validation logic must process string comparisons and update attempt counters within 50 milliseconds of submission.", "High"),
        ("NFR-10", "Feedback Clarity", "Modal dialogue boxes must clearly differentiate between incorrect attempts, out-of-time penalties, and unlocked states.", "Medium"),
        ("NFR-11", "Hardware Portability", "The application must execute reliably across diverse Windows 10 and Windows 11 systems running Intel, AMD, or NVIDIA GPUs.", "High"),
        ("NFR-12", "Asset Decoupling", "Textures, audio clips, materials, and UI prefabs must be structured independently to allow hot-swapping without re-scripting.", "Medium"),
        ("NFR-13", "Resource Optimization", "Total runtime system memory (RAM) allocation must remain under 1.8 GB and GPU VRAM footprint under 1.2 GB.", "Medium"),
        ("NFR-14", "Error Dialog Resilience", "When unsupported inputs or out-of-range interactions occur, graceful error notifications must prevent input locking.", "Medium"),
        ("NFR-15", "Self-Healing EventSystem", "UI canvas managers must enforce cursor unlock routines dynamically to eliminate game-freezing mouse lock states.", "High")
    ]

    nfr_tbl = doc.add_table(rows=len(nfr_data) + 1, cols=4)
    nfr_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    nfr_tbl.autofit = False
    set_table_grid_borders(nfr_tbl)

    for row in nfr_tbl.rows:
        for i, cell in enumerate(row.cells):
            cell.width = widths[i]
            set_cell_margins(cell, 60, 60, 80, 80)

    hdr_nfr = ["Req ID", "Category", "Metric / Specification", "Priority"]
    for i, title in enumerate(hdr_nfr):
        c = nfr_tbl.cell(0, i).paragraphs[0]
        c.add_run(title).font.bold = True
        c.runs[0].font.name = FONT_NAME
        c.runs[0].font.size = Pt(11)
        set_cell_background(nfr_tbl.cell(0, i), "F2F2F2")

    for idx, (rid, cat, spec, prio) in enumerate(nfr_data):
        r = nfr_tbl.rows[idx + 1]
        for col_idx, val in enumerate([rid, cat, spec, prio]):
            cp = r.cells[col_idx].paragraphs[0]
            r_run = cp.add_run(val)
            r_run.font.name = FONT_NAME
            r_run.font.size = Pt(10)
            if col_idx == 0 or col_idx == 3:
                r_run.font.bold = True

    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    # 2.3 Use-Case Analysis & Actor Profiles
    add_heading(doc, "2.3 Use-Case Analysis & Actor Profiles")
    add_body_paragraph(doc, "The functional boundaries and interaction patterns of Cipher Court are modeled around three primary actors:")
    add_bullet_point(doc, "Navigates 3D rooms via WASD/Mouse, casts distance-bounded interaction rays toward physical evidence, inspects clue texts, submits proposed passwords/codes to puzzle terminals, requests hints under score penalty, and selects the final courtroom verdict.", bold_prefix="1. Player / Forensic Investigator:")
    add_bullet_point(doc, "Executes real-time physics collisions, manages 5-minute level countdown timers, decrements remaining attempts (3 max), validates string inputs against mathematical cipher hashes, triggers motorized door slerp animations, and dispatches JSON audit logs to the backend.", bold_prefix="2. System / Game Engine (Unity C# Runtime):")
    add_bullet_point(doc, "Monitors student deduction performance, inspects historical event logs via the Python HTTP dashboard, configures room cipher solutions, and evaluates overall cybersecurity awareness scores.", bold_prefix="3. Academic Instructor / System Administrator:")

    add_body_paragraph(doc, "Core operational use-case narratives include:")
    add_bullet_point(doc, "UC-01 (Game Launch & Level 1 Scene Entry): Player clicks 'START GAME' on MainMenu. SceneManager loads Level1_Investigation, initializes character controller at SpawnPoint, resets player attempts to 3, and starts LevelTimer at 300 seconds.")
    add_bullet_point(doc, "UC-02 (Raycast Inspection & Clue Collection): Player approaches an evidence marker and presses 'E'. Reticle raycast hits CollectibleItem collider, displays full clue text on HUD, records evidence into memory, and plays an audio chime.")
    add_bullet_point(doc, "UC-03 (Puzzle Terminal & Cipher Verification): Player interacts with terminal keypad, unlocking the mouse cursor. Player enters code (e.g., 'COURT2026' or '472'). System validates input: if valid, stops timer, plays victory chime, and rotates door open; if invalid, decrements attempts.")
    add_bullet_point(doc, "UC-04 (Attempt Depletion & Scene Failure): If player exhausts 3 attempts or timer hits 00:00, System locks input fields, displays 'LEVEL FAILED' overlay, and prompts 'RETRY LEVEL'.")
    add_bullet_point(doc, "UC-05 (Courtroom Final Verdict): In Level 6, player evaluates three witness statements against gathered evidence, submits Statement 2, and triggers the grand 'JUSTICE SERVED' victory climax.")

    # 2.4 Requirement Prioritization (MoSCoW Matrix)
    add_heading(doc, "2.4 Requirement Prioritization (MoSCoW Matrix)")
    add_body_paragraph(doc, "To ensure systematic project delivery within the academic semester, system requirements were classified via the MoSCoW prioritization model:")

    add_subheading(doc, "Table 2.3: MoSCoW Requirement Prioritization Matrix")

    moscow_data = [
        ("Must Have (M)", "FR-01, FR-02, FR-03, FR-04, FR-05, FR-08, FR-09, FR-11, NFR-01, NFR-04, NFR-06", 
         "Non-negotiable core serious game foundation: 3D scene rendering, WASD/mouse kinematics, 2.5m raycasting, code validation, door motorized unlocking, progress state tracking, 60 FPS graphics."),
        ("Should Have (S)", "FR-06, FR-07, FR-12, FR-14, FR-16, FR-19, NFR-02, NFR-08, NFR-09, NFR-15", 
         "High-value functional features: 5:00 countdown timer, attempt limiting (3 max), audio-visual feedback banners, final Level 6 verdict climax, self-healing EventSystem UI managers."),
        ("Could Have (C)", "FR-13, FR-15, FR-18, NFR-10, NFR-13", 
         "Enrichment & usability enhancements: Contextual hint system with score penalties, pause menu audio controls, spatial 3D ambient hums, and Python SQLite real-time audit logging dashboard."),
        ("Won't Have (W)", "Multiplayer & VR Scope Items", 
         "Deferred to future post-graduate research: Real-time peer-to-peer multiplayer forensic competition, VR motion tracking (Meta Quest / SteamVR), and neural LLM-driven procedural clue synthesis.")
    ]

    mos_tbl = doc.add_table(rows=len(moscow_data) + 1, cols=3)
    mos_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    mos_tbl.autofit = False
    set_table_grid_borders(mos_tbl)

    m_widths = [Inches(1.5), Inches(2.2), Inches(3.0)]
    for row in mos_tbl.rows:
        for i, cell in enumerate(row.cells):
            cell.width = m_widths[i]
            set_cell_margins(cell, 70, 70, 90, 90)

    m_hdr = ["Priority Level", "Requirement IDs", "Deliverable Scope & Justification"]
    for i, title in enumerate(m_hdr):
        c = mos_tbl.cell(0, i).paragraphs[0]
        c.add_run(title).font.bold = True
        c.runs[0].font.name = FONT_NAME
        c.runs[0].font.size = Pt(11)
        set_cell_background(mos_tbl.cell(0, i), "F2F2F2")

    for idx, (prio, ids, just) in enumerate(moscow_data):
        r = mos_tbl.rows[idx + 1]
        c0 = r.cells[0].paragraphs[0]
        r0 = c0.add_run(prio)
        r0.font.name = FONT_NAME
        r0.font.size = Pt(10.5)
        r0.font.bold = True

        c1 = r.cells[1].paragraphs[0]
        r1 = c1.add_run(ids)
        r1.font.name = FONT_NAME
        r1.font.size = Pt(10)

        c2 = r.cells[2].paragraphs[0]
        r2 = c2.add_run(just)
        r2.font.name = FONT_NAME
        r2.font.size = Pt(10)

    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    # 2.5 Constraints and Assumptions
    add_heading(doc, "2.5 Constraints and Assumptions")
    add_bullet_point(doc, "Standalone Execution Target: Application is compiled strictly as a standalone 64-bit Windows executable (`CipherCourt.exe`), requiring DirectX 11/12 compatible graphics.", bold_prefix="• Technical Constraints:")
    add_bullet_point(doc, "Fixed Forensic Difficulty: To guarantee standardized academic evaluation, puzzle codes (COURT2026, 472, 427, 315) and cipher keys (k=3) are statically mapped in this version.", bold_prefix="• Curricular Boundary:")
    add_bullet_point(doc, "Strict Level Time Limit: Each room enforces an uncompromising 5-minute countdown clock (300 seconds); exceeding the limit triggers an immediate level fail.", bold_prefix="• Temporal Constraints:")
    add_bullet_point(doc, "Desktop Peripheral Availability: Players are assumed to have a standard physical keyboard, mouse, and display running at least 1920x1080 resolution.", bold_prefix="• User Hardware Assumptions:")
    add_bullet_point(doc, "English Language Fluency: Clues, legal statements, and cryptographic cipher instructions are presented in English.", bold_prefix="• Pedagogical Assumptions:")

    # 2.6 Preliminary Product Description & Technology Stack Survey
    add_heading(doc, "2.6 Preliminary Product Description & Technology Stack Survey")
    add_body_paragraph(
        doc,
        "Cipher Court is architected as an interactive 3D serious game leveraging a decoupled three-tier technology stack:",
        bold_prefix="Product Overview:"
    )
    add_bullet_point(doc, "Unity 6 LTS & Universal Render Pipeline (URP): Serves as the core 3D simulation engine. URP provides high-performance Single-Pass Forward+ lighting, physical materials, and post-processing volumes that establish an authentic judicial court ambiance.")
    add_bullet_point(doc, "C# 9.0 (.NET Standard 2.1): Drives all client-side kinematics, reticle raycast mathematical evaluations, door motorized transformations, attempt state tracking, and UI modal transitions.")
    add_bullet_point(doc, "TextMeshPro & SDF Typography: Eliminates texture pixelation on puzzle keypads and clue notes by rendering text via Signed Distance Field shaders.")
    add_bullet_point(doc, "Python 3.12 Backend Server (FastAPI / HTTP Server): Operates an asynchronous micro-service providing REST endpoints for storing live gameplay audit records and calculating investigative metrics.")
    add_bullet_point(doc, "SQLite 3 & PostgreSQL Persistence: Stores player profile identities, completed stage timestamps, puzzle error logs, and forensic deduction scores.")
    add_bullet_point(doc, "Visual Studio Code & Git: Primary development environment and version control repository hosting.")

    # 2.7 Conceptual Models (Literature Review)
    add_heading(doc, "2.7 Conceptual Models (Literature Review of Existing CALL / Serious Game Systems)")
    add_body_paragraph(
        doc,
        "An in-depth review of existing cybersecurity training systems, serious games, and forensic puzzle titles was conducted "
        "to establish comparative advantages:"
    )
    add_bullet_point(doc, "Capcom Ace Attorney Series: Regarded as the benchmark in courtroom drama, but relies entirely on static 2D sprites, visual novel text trees, and scripted inventory combination. Completely lacks spatial 3D exploration and real cryptographic codebreaking.", bold_prefix="• Phoenix Wright: Ace Attorney:")
    add_bullet_point(doc, "Fireproof Games' 'The Room': Masterful in 3D mechanical tactile puzzles, but focuses exclusively on fantasy/mechanical themes without educational cybersecurity grounding or legal deduction.", bold_prefix="• The Room Series:")
    add_bullet_point(doc, "Cybersecurity Range Platforms (TryHackMe, HackTheBox): Highly technical terminal-based CTFs (Capture The Flag), but suffer from steep learning curves, lack 3D narrative immersion, and alienate introductory students.", bold_prefix="• Enterprise Cyber Ranges:")

    add_subheading(doc, "Table 2.4: Comparative Analysis Matrix of Existing Cybersecurity Learning Systems")

    comp_data = [
        ("Core Capability / Feature", "Cipher Court (Proposed System)", "Ace Attorney Series", "The Room Series", "TryHackMe / HTB"),
        ("3D First-Person Spatial Navigation", "Yes (Full WASD 3D)", "No (Static 2D Sprites)", "Partial (Fixed Orbit)", "No (Terminal CLI)"),
        ("Cryptographic Ciphers & Hash Verification", "Yes (Caesar, AES, Keypads)", "No (Narrative Logic)", "No (Mechanical Only)", "Yes (Command Line)"),
        ("Atmospheric Judicial Courtroom Climax", "Yes (Evidence vs. Witness)", "Yes (2D Visual Novel)", "No (Occult Mystery)", "No (Technical CTF)"),
        ("Attempt Throttling (3 Max) & Timer (5:00)", "Yes (Disciplined Rules)", "Partial (Life Bar)", "No (Untimed)", "No (Untimed Labs)"),
        ("Decoupled SQL/Python Audit Persistence", "Yes (REST Event Logging)", "No (Local Saves)", "No (Local Saves)", "Yes (Web Scoreboard)"),
        ("Accessibility for CS Undergraduate Students", "High (Interactive 3D Game)", "High (Casual Game)", "High (Casual Game)", "Low (Steep CLI Barrier)")
    ]

    comp_tbl = doc.add_table(rows=len(comp_data), cols=5)
    comp_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    comp_tbl.autofit = False
    set_table_grid_borders(comp_tbl)

    c_widths = [Inches(1.8), Inches(1.3), Inches(1.2), Inches(1.1), Inches(1.3)]
    for row in comp_tbl.rows:
        for i, cell in enumerate(row.cells):
            cell.width = c_widths[i]
            set_cell_margins(cell, 60, 60, 70, 70)

    for i, col_title in enumerate(comp_data[0]):
        c = comp_tbl.cell(0, i).paragraphs[0]
        c.add_run(col_title).font.bold = True
        c.runs[0].font.name = FONT_NAME
        c.runs[0].font.size = Pt(10.5)
        set_cell_background(comp_tbl.cell(0, i), "F2F2F2")

    for r_idx, row_vals in enumerate(comp_data[1:]):
        r = comp_tbl.rows[r_idx + 1]
        for c_idx, val in enumerate(row_vals):
            cp = r.cells[c_idx].paragraphs[0]
            r_run = cp.add_run(val)
            r_run.font.name = FONT_NAME
            r_run.font.size = Pt(9.5)
            if c_idx == 0:
                r_run.font.bold = True

    doc.add_page_break()


def add_chapter_3(doc):
    """Adds Chapter 3: Software Development Life Cycle (SDLC) Planning."""
    add_chapter_title(doc, "3", "SOFTWARE DEVELOPMENT LIFE CYCLE (SDLC) PLANNING")

    add_heading(doc, "3.1 Selection of SDLC Model (Prototype Model)")
    add_body_paragraph(
        doc,
        "The Cipher Court platform was developed utilizing the evolutionary Prototype Software Development Life Cycle (SDLC) Model. "
        "Unlike rigid linear models such as Waterfall, serious 3D games require early physical prototypes to validate player spatial navigation, "
        "reticle raycasting sensitivity, UI readability under dynamic lighting, and puzzle difficulty curves. In game engineering, theoretical "
        "mechanics often look flawless on paper but prove unintuitive or frustrating when experienced in a 3D environment. "
        "The Prototype model enabled an initial bare-bones playable room to be built, play-tested by peer students, analyzed for interaction bugs, "
        "and progressively refined into the photorealistic, robust 6-level judicial experience presented in this dissertation."
    )
    add_body_paragraph(
        doc,
        "Key advantages realized through the Prototype Model include:",
        bold_prefix="Methodological Justification:"
    )
    add_bullet_point(doc, "Rapid Spatial Verification: Allowed immediate physical testing of player collision hulls, door scale, and 2.5m raycasting distance before authoring high-fidelity textures.")
    add_bullet_point(doc, "Early Feedback on Cryptographic Difficulty: Initial play-testing revealed that unassisted cipher decoding caused learner frustration; this motivated the integration of contextual clue cards and attempt throttling.")
    add_bullet_point(doc, "Mitigation of UI Input Freezes: Discovered and rectified EventSystem mouse-locking race conditions early during prototype iterations, resulting in a self-healing UI architecture.")

    # 3.2 Work Breakdown Structure (WBS)
    add_heading(doc, "3.2 Work Breakdown Structure (WBS)")
    add_body_paragraph(doc, "The project lifecycle was divided into five structured engineering work packages corresponding to the iterative prototyping phases:")

    add_subheading(doc, "Table 3.1: Work Breakdown Structure (WBS) & Prototype Deliverables")

    wbs_data = [
        ("Phase 1", "Requirement Analysis & Architectural Modeling", 
         "Author IEEE SRS specification, formulate mathematical puzzle rules (Caesar shifts, AES blocks), design UML models (Use Case, Class, Sequence, Activity), and define database schema.", 
         "Approved SRS & Complete UML Suite"),
        ("Phase 2", "Core Engine Framework & Kinematics", 
         "Initialize Unity 6 URP project, code first-person kinematic movement (`PlayerMovement.cs`), author distance-bounded raycasting (`PuzzleInteraction.cs`), and setup camera rig.", 
         "Playable Kinematic & Interaction Engine"),
        ("Phase 3", "Cryptographic Puzzle & UI Implementation", 
         "Implement Caesar decryption (`CipherPuzzle.cs`), evidence matching (`EvidencePuzzle.cs`), timer countdown (`LevelTimer.cs`), attempt limiter, and TextMeshPro modal dialogs.", 
         "Functional 6-Level Puzzle Suite"),
        ("Phase 4", "Environmental Overhaul & Visual Polish", 
         "Author custom editor script (`CipherCourtVisualPolisher.cs`), assign PBR materials (walnut, marble, brass), bake volumetric lighting, and configure particle ambiance.", 
         "Photorealistic Courtroom Atmosphere"),
        ("Phase 5", "System Testing, Backend & Deployment", 
         "Execute 25 test cases across Unit, Integration, Black-Box suites, deploy Python REST audit backend (`server.py`), package Windows x86_64 standalone build, and compile Blackbook.", 
         "Standalone Build & Final Project Blackbook")
    ]

    wbs_tbl = doc.add_table(rows=len(wbs_data) + 1, cols=4)
    wbs_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    wbs_tbl.autofit = False
    set_table_grid_borders(wbs_tbl)

    w_widths = [Inches(1.0), Inches(1.8), Inches(2.5), Inches(1.4)]
    for row in wbs_tbl.rows:
        for i, cell in enumerate(row.cells):
            cell.width = w_widths[i]
            set_cell_margins(cell, 70, 70, 80, 80)

    w_hdr = ["WBS ID", "Iteration / Phase", "Core Engineering Tasks & Deliverables", "Milestone Output"]
    for i, title in enumerate(w_hdr):
        c = wbs_tbl.cell(0, i).paragraphs[0]
        c.add_run(title).font.bold = True
        c.runs[0].font.name = FONT_NAME
        c.runs[0].font.size = Pt(10.5)
        set_cell_background(wbs_tbl.cell(0, i), "F2F2F2")

    for idx, (wid, ph, desc, out) in enumerate(wbs_data):
        r = wbs_tbl.rows[idx + 1]
        c0 = r.cells[0].paragraphs[0]
        r0 = c0.add_run(wid)
        r0.font.name = FONT_NAME
        r0.font.size = Pt(10)
        r0.font.bold = True

        c1 = r.cells[1].paragraphs[0]
        r1 = c1.add_run(ph)
        r1.font.name = FONT_NAME
        r1.font.size = Pt(10)
        r1.font.bold = True

        c2 = r.cells[2].paragraphs[0]
        r2 = c2.add_run(desc)
        r2.font.name = FONT_NAME
        r2.font.size = Pt(9.5)

        c3 = r.cells[3].paragraphs[0]
        r3 = c3.add_run(out)
        r3.font.name = FONT_NAME
        r3.font.size = Pt(9.5)

    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    # 3.3 Project Timeline & Scheduling (Gantt Chart)
    add_heading(doc, "3.3 Project Timeline & Scheduling (Gantt Chart & Sprint Roadmap)")
    add_body_paragraph(
        doc,
        "The project development roadmap tracked disciplined execution milestones across the academic semester timeline (Sem-V 2026–2027), "
        "beginning from initial Synopsis and Proposal presentation, progressing through SRS and UML architecture modeling, "
        "functional application scripting, visual polish, testing, and final dissertation documentation.",
        bold_prefix="Timeline Overview:"
    )

    gantt_path = os.path.abspath("e:/vyt/extracted_assets/gantt_chart_0.png")
    add_image_diagram(doc, gantt_path, "Figure 3.1: Project Schedule and Prototype Development Gantt Chart Sem-V 2026-27", width=Inches(5.6))

    add_body_paragraph(
        doc,
        "As illustrated in Figure 3.1, the sequential progression enforced clear deliverable deadlines: Synopsis (01 Aug), "
        "Proposal Submission (08 Aug), SRS & UML Diagram Approval (24 Aug), Architecture Design Documentation (03 Sep), "
        "Working Playable Application Milestone (15 Sep), GitHub Repository & Final Technical Blackbook (21 Sep), "
        "culminating in the Final Presentation & Project Demonstration (24 Sep)."
    )

    # 3.4 Resource Planning
    add_heading(doc, "3.4 Resource Planning (Hardware & Software Specifications)")
    add_body_paragraph(doc, "To ensure smooth development, rendering, testing, and execution, the following hardware and software resources were provisioned:")
    add_bullet_point(doc, "Processor: Intel Core i3 / Core i5 (or AMD Ryzen 5) CPU running at 2.8 GHz or higher.", bold_prefix="• Processor:")
    add_bullet_point(doc, "System Memory (RAM): Minimum 8 GB DDR4 RAM (16 GB recommended for concurrent Unity Editor, Visual Studio Code, and browser profiling).", bold_prefix="• RAM:")
    add_bullet_point(doc, "Storage: Minimum 20 GB available SSD/HDD storage space for 3D assets, textures, and build binaries.", bold_prefix="• Storage:")
    add_bullet_point(doc, "Graphics Processing Unit (GPU): Dedicated NVIDIA GeForce GTX 1050 / AMD Radeon RX 560 or better (supporting DirectX 11/12).", bold_prefix="• GPU:")
    add_bullet_point(doc, "Display & Peripherals: Standard 1920x1080 Full-HD display, physical two-button mouse with scroll wheel, and standard QWERTY keyboard.", bold_prefix="• Display & Input:")
    add_bullet_point(doc, "Operating System: Microsoft Windows 10 / Windows 11 (64-bit architecture).", bold_prefix="• OS:")
    add_bullet_point(doc, "Game Engine & Tooling: Unity Hub 3.x, Unity 6 LTS (Version 6000.3.21f1 URP), Visual Studio Code v1.90+.", bold_prefix="• Development Engine:")
    add_bullet_point(doc, "Backend Runtime & Database: Python 3.12, SQLite 3, PostgreSQL 15, Postman API Tester, Git & GitHub.", bold_prefix="• Backend & Database:")

    doc.add_page_break()


def add_chapter_4(doc):
    """
    Adds Chapter 4: System Modeling using UML.
    Layout Rule: Strictly ONE diagram per page!
    Clear theoretical explanation for each diagram explaining its role in the project.
    Faculty feedback: Include Frontend wireframes & Backend implementation flow.
    """
    add_chapter_title(doc, "4", "SYSTEM MODELING USING UML")

    # -------------------------------------------------------------
    # 4.1 Event Table (Page 1 of Chapter 4)
    # -------------------------------------------------------------
    add_heading(doc, "4.1 Event Table (System Logic & Event Table)")
    add_body_paragraph(
        doc,
        "Theoretical Foundation: In event-driven serious games, the Event Table serves as the foundational behavioral contract "
        "mapping environmental stimuli to system logic. It systematically links user triggers (such as mouse clicks, keyboard presses, "
        "and spatial collisions) with architectural handlers, state changes, and visual/audio outcomes. "
        "In Cipher Court, the Event Table governs player inputs, timer expirations, cipher evaluations, and stage progression rules."
    )

    ev_path = os.path.abspath("e:/vyt/extracted_assets/srs_p8_0_Img30.jpg")
    add_image_diagram(doc, ev_path, "Figure 4.1: System Logic & Event Table for Cipher Court Gameplay", width=Inches(5.8))
    doc.add_page_break()

    # -------------------------------------------------------------
    # 4.2 Class Diagram (Page 2 of Chapter 4)
    # -------------------------------------------------------------
    add_heading(doc, "4.2 Class Diagram")
    add_body_paragraph(
        doc,
        "Theoretical Foundation: The Class Diagram provides a static structural view of the object-oriented game architecture. "
        "It defines the classes, attributes, methods, and relationships (inheritance, association, composition) governing the system. "
        "In Cipher Court, GameManager coordinates core subsystems: Player, Level, Timer, HintSystem, ScoreSystem, Puzzle, Cipher, "
        "and GameData repository. This diagram establishes clear separation of concerns between input handling, puzzle logic, and data persistence."
    )

    cd_path = os.path.abspath("e:/vyt/extracted_assets/srs_p9_0_Img35.png")
    add_image_diagram(doc, cd_path, "Figure 4.2: Class Diagram Mapping System Entities and Object Relationships", width=Inches(5.6))
    doc.add_page_break()

    # -------------------------------------------------------------
    # 4.3 Object Diagram (Page 3 of Chapter 4)
    # -------------------------------------------------------------
    add_heading(doc, "4.3 Object Diagram")
    add_body_paragraph(
        doc,
        "Theoretical Foundation: An Object Diagram captures a concrete runtime snapshot of the system at a specific execution instant, "
        "instantiating classes into active memory entities with concrete values. "
        "Figure 4.3 illustrates Cipher Court during an active Level 2 gameplay session: player1 (Alex, score=500, currentLevel=2) "
        "interacts with game1 (GameManager, status=Running), executing level2 (Prison Archive, timeLimit=300), "
        "monitoring timer1 (remainingTime=180), and evaluating puzzle1 (Decode Message, Caesar cipher, key=3, ciphertext=MXVWLFH)."
    )

    od_path = os.path.abspath("e:/vyt/extracted_assets/srs_p10_0_Img40.png")
    add_image_diagram(doc, od_path, "Figure 4.3: Object Diagram Illustrating Runtime Instances during Active Gameplay", width=Inches(5.4))
    doc.add_page_break()

    # -------------------------------------------------------------
    # 4.4 Use Case Diagram (Page 4 of Chapter 4)
    # -------------------------------------------------------------
    add_heading(doc, "4.4 Use Case Diagram")
    add_body_paragraph(
        doc,
        "Theoretical Foundation: The Use Case Diagram delineates the system boundary and models user interactions by capturing the "
        "functional requirements from an external actor's perspective. "
        "In Cipher Court, the primary Player actor engages in use cases: View Instructions, Start Game (includes Select Level), "
        "View Timer, View Score, Pause Game, Solve Cipher (includes Enter Answer, extends Request Hint), and Exit Game. "
        "The Admin actor performs management use cases: Login, Add Puzzle, Update Puzzle, Delete Puzzle, and View Game Data."
    )

    uc_path = os.path.abspath("e:/vyt/extracted_assets/srs_p11_0_Img45.png")
    add_image_diagram(doc, uc_path, "Figure 4.4: Use Case Diagram for Cipher Court System Actors and Boundaries", width=Inches(5.4))
    doc.add_page_break()

    # -------------------------------------------------------------
    # 4.5 Sequence Diagram (Page 5 of Chapter 4)
    # -------------------------------------------------------------
    add_heading(doc, "4.5 Sequence Diagram")
    add_body_paragraph(
        doc,
        "Theoretical Foundation: The Sequence Diagram models the dynamic temporal interaction of objects over time, illustrating the "
        "exact order of message exchanges across lifelines. "
        "Figure 4.5 traces the complete puzzle submission lifecycle across seven lifelines: Player, Game UI, Game Manager, "
        "Puzzle System, Cipher System, Timer, Hint System, Score System, and Game Data repository. It details both the success path "
        "(correct answer -> award points -> unlock door -> progress level) and failure paths (incorrect attempt reduction, timer expiration)."
    )

    seq_path = os.path.abspath("e:/vyt/extracted_assets/srs_p12_0_Img50.png")
    add_image_diagram(doc, seq_path, "Figure 4.5: Sequence Diagram for Gameplay, Interaction, and Puzzle Validation Lifecycle", width=Inches(5.6))
    doc.add_page_break()

    # -------------------------------------------------------------
    # 4.6 Activity Diagram (Page 6 of Chapter 4)
    # -------------------------------------------------------------
    add_heading(doc, "4.6 Activity Diagram")
    add_body_paragraph(
        doc,
        "Theoretical Foundation: The Activity Diagram illustrates the operational control flow and procedural step sequences "
        "governing gameplay execution. It maps decision branches, guard conditions, and concurrent paths. "
        "Figure 4.6 documents the flow from Launch Game -> Main Menu -> Select Level -> Display Clues & Start Timer -> "
        "Enter Answer. It models the decision forks: If Answer Correct -> Unlock Door -> Level Complete; If Answer Incorrect -> "
        "Deduct Attempt -> Check Attempts Remaining -> Retry or Level Failed. If Timer reaches 00:00 -> Trigger Game Over."
    )

    act_path = os.path.abspath("e:/vyt/extracted_assets/srs_p13_0_Img55.png")
    add_image_diagram(doc, act_path, "Figure 4.6: Activity Diagram for Level Progression and Puzzle Verification Workflow", width=Inches(5.4))
    doc.add_page_break()

    # -------------------------------------------------------------
    # 4.7 Component Diagram (Page 7 of Chapter 4)
    # -------------------------------------------------------------
    add_heading(doc, "4.7 Component Diagram")
    add_body_paragraph(
        doc,
        "Theoretical Foundation: The Component Diagram describes the structural organization and physical dependencies between software "
        "modules, packages, and services. "
        "Figure 4.7 decomposes Cipher Court into three decoupled subsystems: (1) Player Device Tier (Input, Unity 3D Scene View, Reticle Raycaster); "
        "(2) Game Core Tier (Game Manager, Level Manager, Puzzle Manager, Cipher Engine); (3) Game Services & Data Layer "
        "(Score Service, Audio Manager, Save/Load Service, Hint Service, Timer Service, and persistent Game Database)."
    )

    cmp_path = os.path.abspath("e:/vyt/extracted_assets/srs_p14_0_Img60.png")
    add_image_diagram(doc, cmp_path, "Figure 4.7: Component Diagram Showing Subsystem Interconnections and Service Decoupling", width=Inches(5.6))
    doc.add_page_break()

    # -------------------------------------------------------------
    # 4.8 Deployment Diagram (Page 8 of Chapter 4)
    # -------------------------------------------------------------
    add_heading(doc, "4.8 Deployment Diagram")
    add_body_paragraph(
        doc,
        "Theoretical Foundation: The Deployment Diagram maps the logical software components to physical hardware runtime environments "
        "and execution nodes. "
        "Figure 4.8 illustrates the physical topology: Node 1 (Player PC/Laptop) hosts the Unity Runtime execution environment "
        "running the compiled `Cipher Code 3D Game` artifact; Node 2 (Application Server) runs the Python Game Backend microservice; "
        "and Node 3 (Database Server) hosts the persistent SQLite/PostgreSQL database communicating over TCP/IP and HTTPS."
    )

    dep_path = os.path.abspath("e:/vyt/extracted_assets/srs_p15_0_Img65.png")
    add_image_diagram(doc, dep_path, "Figure 4.8: Deployment Diagram Across Client Workstation and Backend Database Server", width=Inches(5.6))
    doc.add_page_break()

    # -------------------------------------------------------------
    # 4.9 Faculty Feedback: Frontend UI Prototype (Page 9 of Chapter 4)
    # -------------------------------------------------------------
    add_heading(doc, "4.9 Faculty Feedback: Frontend UI Wireframe Prototype & Navigation Flow")
    add_body_paragraph(
        doc,
        "Theoretical Foundation & Faculty Requirement: Incorporating faculty recommendations, this section documents the user-interface "
        "prototyping wireframes and sequential scene navigation architecture. "
        "Figure 4.9 models the macro state machine transitions: from Main Menu -> Level 1 (Investigation) -> Level 2 (Computer) -> "
        "Level 3 (Evidence) -> Level 4 (Archive) -> Level 5 (Case Files) -> Level 6 (Courtroom Climax) -> Game Complete. "
        "Each screen enforces clean HUD reticle states, attempt indicators, and non-blocking modal dialogue layers."
    )

    nav_path = os.path.abspath("e:/vyt/extracted_assets/arch_p2_0_Img12.png")
    add_image_diagram(doc, nav_path, "Figure 4.9: Frontend Navigation Flow and Screen State Hierarchy", width=Inches(5.6))
    doc.add_page_break()

    # -------------------------------------------------------------
    # 4.10 Faculty Feedback: Backend Architecture & Implementation Flow (Page 10 of Chapter 4)
    # -------------------------------------------------------------
    add_heading(doc, "4.10 Faculty Feedback: Backend Architecture & Implementation Flow")
    add_body_paragraph(
        doc,
        "Theoretical Foundation & Faculty Requirement: To satisfy faculty feedback regarding backend engineering visibility, "
        "this diagram illustrates the processing pipeline developed in Visual Studio Code. "
        "Figure 4.10 depicts the end-to-end data pipeline: Player input (keyboard/mouse) is captured by the Unity front-end, "
        "evaluated through C# business rules (attempts, timers, clue states), dispatched via asynchronous HTTP REST payloads "
        "to the Python server, and committed to persistent database storage (PostgreSQL/SQLite) before rendering UI outcome feedback."
    )

    flow_path = os.path.abspath("e:/vyt/extracted_assets/arch_p9_0_Img47.png")
    add_image_diagram(doc, flow_path, "Figure 4.10: Backend Data Flow and System Processing Pipeline", width=Inches(5.6))
    doc.add_page_break()


def add_chapter_5(doc):
    """Adds Chapter 5: System Architecture & Design with comprehensive Frontend Prototype Architecture in 5.1."""
    add_chapter_title(doc, "5", "SYSTEM ARCHITECTURE DESIGN")

    # =========================================================================
    # 5.1 FRONTEND PROTOTYPE ARCHITECTURE & COMPONENT HIERARCHY
    # =========================================================================
    add_heading(doc, "5.1 Frontend Prototype Architecture & Component Hierarchy")
    add_body_paragraph(
        doc,
        "Cipher Court implements a decoupled three-tier architectural paradigm separating the Presentation Layer (Unity 6 URP, "
        "Camera Rig, TextMeshPro UI HUD), Business Logic Layer (C# Kinematics, Reticle Raycast Detection, Cryptographic Engines, "
        "Timer/Attempt Controllers), and Data & Persistence Layer (Python REST API, SQLite/PostgreSQL, JSON audit stores). "
        "The frontend client application is engineered in Unity 6 LTS (6000.3.21f1) utilizing the Universal Render Pipeline (URP), "
        "leveraging a responsive Canvas Scaler hierarchy, distance-bounded first-person raycasting, and in-memory persistent singletons.",
        bold_prefix="Architectural Overview:"
    )

    add_body_paragraph(
        doc,
        "The presentation tier coordinates through a centralized, persistent core engine and unified interaction protocols across all scenes:",
        bold_prefix="Global Frontend Architecture & Interaction Pipeline:"
    )
    add_bullet_point(
        doc,
        "Responsive Canvas Scaler Hierarchy: Every UI canvas implements CanvasScaler set to ScaleWithScreenSize with a reference resolution "
        "of 1920x1080 pixels (MatchWidthOrHeight = 0.5), guaranteeing consistent layout scaling from 16:9 desktop monitors up to 4K displays. "
        "Raycast hit-testing overhead is eliminated by disabling the raycastTarget flag on all static decorative frames, backdrops, and borders.",
        bold_prefix="• Responsive Canvas Scaler:"
    )
    add_bullet_point(
        doc,
        "TextMeshPro Signed Distance Field (SDF) Typography: All on-screen and world-space text elements utilize multi-channel SDF font "
        "assets (LiberationSans SDF, Orbitron SDF, Inconsolata SDF, NotoSerif SDF), ensuring razor-sharp visual rendering under post-processing "
        "depth of field, bloom, and dynamic camera distances without bitmap pixelation.",
        bold_prefix="• SDF Typography Engine:"
    )
    add_bullet_point(
        doc,
        "Persistent Singleton State (GameManager.cs): Instantiated on game bootstrap with DontDestroyOnLoad(gameObject), GameManager tracks "
        "the active investigator identity, room completion bitmasks, aggregate score ledger, and forensic clue inventories across scene transitions.",
        bold_prefix="• Global State Persistence:"
    )
    add_bullet_point(
        doc,
        "Distance-Bounded Viewport Raycaster (PuzzleInteraction.cs): Center-screen raycasting (ViewportPointToRay(0.5, 0.5)) evaluates spatial "
        "intersections with the 'InteractiveProps' LayerMask, enforcing a strict Euclidean reach limit of d <= 2.50 meters.",
        bold_prefix="• Spatial Interaction Arbitrator:"
    )
    add_bullet_point(
        doc,
        "Hardware Cursor Governance: The system dynamically manages cursor states: locked and hidden (CursorLockMode.Locked; Cursor.visible = false) "
        "during first-person locomotion; unlocked and visible (CursorLockMode.None; Cursor.visible = true) during puzzle modal inspection.",
        bold_prefix="• Hardware Cursor Lifecycle:"
    )

    add_body_paragraph(
        doc,
        "The subsections below delineate the technical architecture, UI hierarchy, script interactions, and validation rules for each "
        "level of the game prototype, accompanied by high-resolution visual interface captures rendered in the active runtime engine:",
        bold_prefix="Level-Wise Prototype Architecture & Interface Specifications:"
    )

    # --- LEVEL 0: MAIN MENU ---
    add_subheading(doc, "Level 0: Main Menu Gateway Interface (MainMenu.unity)")
    img_l0 = os.path.abspath("e:/vyt/Assets/CipherCourtPolish/Backgrounds/REAL_MainMenu_Clean.jpg")
    add_image_diagram(doc, img_l0, "Figure 5.1: Level 0 Main Menu Prototype Interface — Cinematic Courtroom Gateway (MainMenu.unity)", width=Inches(5.4))
    add_bullet_point(doc, "MainMenuCanvas (Screen Space - Overlay) -> BackgroundVignette (RawImage: Dark Navy #0A192F) -> TitleContainer (Gold Embossed TMP) -> ProfileInputModal (TMP_InputField) -> MenuButtonGroup (VerticalLayoutGroup: 'START GAME', 'INSTRUCTIONS', 'QUIT') -> InstructionsModal (CanvasGroup).", bold_prefix="• UI Component Hierarchy:")
    add_bullet_point(doc, "MainMenuManager.cs, GameManager.cs.", bold_prefix="• Primary C# Controllers:")
    add_bullet_point(doc, "OnPointerEnter audio triggers, OnSelect profile field, OnClick(Btn_StartGame) generating active session GUID and invoking SceneManager.LoadSceneAsync('Level1_Investigation').", bold_prefix="• User Interactions & Handled Events:")
    add_bullet_point(doc, "Alphanumeric regex guard (^[A-Za-z0-9_-]{3,20}$); fallback to default token INVESTIGATOR-9022-<GUID> if blank. Failsafe cursor lock release.", bold_prefix="• Client-Side Validation Rules:")

    # --- LEVEL 1: CRIME SCENE ---
    add_subheading(doc, "Level 1: Crime Scene Investigation Prototype (Level1_Investigation.unity)")
    img_l1 = os.path.abspath("e:/vyt/Assets/CipherCourtPolish/Backgrounds/REAL_Level1_CrimeScene.png")
    add_image_diagram(doc, img_l1, "Figure 5.2: Level 1 Crime Scene Prototype — Reticle Clue Interaction Prompt Active (Level1_Investigation.unity)", width=Inches(5.4))
    add_bullet_point(doc, "MainCamera Stack -> ReticleCanvas (Screen Space - Overlay) -> CenterReticle (Image: Dynamic 12x12 Outline) -> TooltipTag ('[E] Inspect Evidence Marker') -> ClueModalContainer -> ClueImageCard (Image) -> ClueDescription (TMP).", bold_prefix="• UI Component Hierarchy:")
    add_bullet_point(doc, "PuzzleInteraction.cs, CollectibleItem.cs, PasswordClue.cs, Level1Progress.cs.", bold_prefix="• Primary C# Controllers:")
    add_bullet_point(doc, "First-person camera gimbal (WASD + MouseLook), KeyCode.E raycast trigger displaying modal clue card, Close modal returning camera agency.", bold_prefix="• User Interactions & Handled Events:")
    add_bullet_point(doc, "Raycast distance <= 2.50m; forward vector dot product >= 0.50. Level1Progress unlocks corridor exit door upon collecting all 4 evidentiary markers.", bold_prefix="• Client-Side Validation Rules:")

    # --- LEVEL 2: CYBER TERMINAL ---
    add_subheading(doc, "Level 2: Forensic Cyber Terminal & Password Decryption Prototype (Level2_Computer.unity)")
    img_l2 = os.path.abspath("e:/vyt/Assets/CipherCourtPolish/Backgrounds/REAL_Level2_Puzzle_Screenshot.png")
    add_image_diagram(doc, img_l2, "Figure 5.3: Level 2 Cyber Forensics Terminal & Password Decryption Prototype (Level2_Computer.unity)", width=Inches(5.4))
    add_bullet_point(doc, "In-World Monitor Quad (CRT Scanline Material) -> PasswordModal (Screen Space - Overlay) -> TerminalFrame (Cyan Glow #38BDF8) -> Input_Passcode (TMP_InputField) -> AttemptIndicatorGroup (3x Shield Badges) -> Btn_Authenticate -> FeedbackBanner.", bold_prefix="• UI Component Hierarchy:")
    add_bullet_point(doc, "PasswordPuzzle.cs, PasswordPuzzleInteraction.cs, PasswordPuzzleUI.cs, Level2Progress.cs.", bold_prefix="• Primary C# Controllers:")
    add_bullet_point(doc, "CRT raycast focus, password text input, OnClick(Btn_Authenticate) / KeyCode.Return triggering cryptographic verification.", bold_prefix="• User Interactions & Handled Events:")
    add_bullet_point(doc, "String sanitization via .Trim().ToUpper(), length clamping (4-16 characters). 3-attempt quota limiter with lockout penalty. Correct key 'COURT2026' slerps open security blast doors.", bold_prefix="• Client-Side Validation Rules:")

    # --- LEVEL 3: CAESAR CIPHER ---
    add_subheading(doc, "Level 3: Steganographic Legal Archive & Caesar Cipher Prototype (Level3_Evidence.unity)")
    img_l3 = os.path.abspath("e:/vyt/Assets/CipherCourtPolish/Backgrounds/REAL_Level3_CipherPuzzle.png")
    add_image_diagram(doc, img_l3, "Figure 5.4: Level 3 Steganographic Caesar Cipher Decoding Prototype (Level3_Evidence.unity)", width=Inches(5.4))
    add_bullet_point(doc, "CaesarCipherModal (Screen Space - Overlay) -> AntiqueParchmentBacking (#F4EEDD) -> CiphertextCard (TMP: 'MXVWLFH') -> RotorWheelAssembly (Concentric 26-character rings) -> ShiftDisplay ('Shift Key: k = 3') -> Input_Plaintext -> Btn_VerifyCipher.", bold_prefix="• UI Component Hierarchy:")
    add_bullet_point(doc, "CipherPuzzle.cs, PuzzleUI.cs, EvidenceItem.cs, Level3Progress.cs.", bold_prefix="• Primary C# Controllers:")
    add_bullet_point(doc, "Rotor wheel mouse drag rotating in 13.84-degree increments, input field typing, OnClick(Btn_VerifyCipher) calculating Pi = (Ci - 3) mod 26.", bold_prefix="• User Interactions & Handled Events:")
    add_bullet_point(doc, "Regex filter stripping non-alphabetic symbols ([^A-Za-z]). Plaintext verification against 'JUSTICE' unlatches evidence vault and awards 200 forensic points.", bold_prefix="• Client-Side Validation Rules:")

    # --- LEVEL 4: ARCHIVE SAFE ---
    add_subheading(doc, "Level 4: Underground Archival Vault Records Prototype (Level4_Archive.unity)")
    img_l4 = os.path.abspath("e:/vyt/Assets/CipherCourtPolish/Backgrounds/Level4_Archive_Background.png")
    add_image_diagram(doc, img_l4, "Figure 5.5: Level 4 Underground Archival Vault Records Prototype (Level4_Archive.unity)", width=Inches(5.4))
    add_bullet_point(doc, "SafeDoorQuad -> SafeKeypadCanvas (World Space) -> BrushedSteelHousing -> LEDDisplayPanel (7-Segment Font: '_ _ _') -> ButtonMatrix_3x4 (GridLayoutGroup: PushButtons 0-9, Btn_Clear, Btn_Enter) -> MechanicalTumblerAudio.", bold_prefix="• UI Component Hierarchy:")
    add_bullet_point(doc, "ArchiveKeypad.cs, Level4ArchivePuzzle.cs, Level4Clue.cs.", bold_prefix="• Primary C# Controllers:")
    add_bullet_point(doc, "Physical push-button mouse clicks with spring depression shader, buffer concatenation, audio tumbler click on each keypress.", bold_prefix="• User Interactions & Handled Events:")
    add_bullet_point(doc, "Fixed-length 3-digit buffer clamp; 250ms software debounce. Verification matches '427' (recovered from medical examiner report). Incorrect code flashes red LED and enforces 3s penalty.", bold_prefix="• Client-Side Validation Rules:")

    # --- LEVEL 5: CASE FILES ---
    add_subheading(doc, "Level 5: Case Files & Sworn Affidavits Deliberation Prototype (Level5_Statements.unity)")
    img_l5 = os.path.abspath("e:/vyt/Assets/CipherCourtPolish/Backgrounds/Level5_Statements_Background.png")
    add_image_diagram(doc, img_l5, "Figure 5.6: Level 5 Case Files & Sworn Affidavits Deliberation Prototype (Level5_Statements.unity)", width=Inches(5.4))
    add_bullet_point(doc, "CaseFilesModal (Screen Space - Overlay) -> SplitPaneLayout (HorizontalLayoutGroup) -> LeftPane (ScrollRect: Bank Ledgers & Invoices) -> RightPane (Affidavit Summary, DiscrepancyCodeInput, Btn_ConfirmDiscrepancy) -> StatusBanner.", bold_prefix="• UI Component Hierarchy:")
    add_bullet_point(doc, "Level5Terminal.cs, Level5CasePuzzle.cs, Level5File.cs.", bold_prefix="• Primary C# Controllers:")
    add_bullet_point(doc, "Vertical ledger scrolling, document cross-referencing, typing 3-digit discrepancy code, submitting audit verification.", bold_prefix="• User Interactions & Handled Events:")
    add_bullet_point(doc, "Validates transaction code '315' against bank record exhibits. Unlocks double oak doors into Level 6 Courtroom.", bold_prefix="• Client-Side Validation Rules:")

    # --- LEVEL 6: COURTROOM CLIMAX ---
    add_subheading(doc, "Level 6: Grand Courtroom Cross-Examination Prototype (Level6_Courtroom.unity)")
    img_l6 = os.path.abspath("e:/vyt/Assets/CipherCourtPolish/Backgrounds/REAL_Level6_SelectStatement.png")
    add_image_diagram(doc, img_l6, "Figure 5.7: Level 6 Grand Courtroom Cross-Examination & Perjury Detection Prototype (Level6_Courtroom.unity)", width=Inches(5.4))
    add_bullet_point(doc, "CourtroomVerdictModal (Screen Space - Overlay) -> JudicialBannerHeader ('CROSS-EXAMINATION') -> WitnessSpeechBubble (Dynamic Dialogue) -> StatementRadioGroup (VerticalLayoutGroup: 3x Toggles) -> EvidenceReferenceCarousel -> Btn_ObjectAndAccuse (Gavel Action Button).", bold_prefix="• UI Component Hierarchy:")
    add_bullet_point(doc, "Level6Terminal.cs, Level6Statement.cs, Level6VerdictPuzzle.cs, FinalLevelExit.cs.", bold_prefix="• Primary C# Controllers:")
    add_bullet_point(doc, "Statement selection via radio toggles, horizontal evidence carousel scrolling, OnClick(Btn_ObjectAndAccuse) presenting contradiction.", bold_prefix="• User Interactions & Handled Events:")
    add_bullet_point(doc, "Mutually exclusive selection via ToggleGroup. Identifies Statement 2 as perjury (contradicting Level 2 timestamped terminal logs). Correct accusation plays gavel audio, displays conviction ruling, and routes to victory.", bold_prefix="• Client-Side Validation Rules:")

    # --- LEVEL 7: GAME COMPLETE ---
    add_subheading(doc, "Level 7: Victory Debriefing & Final Case Verdict Screen (GameComplete.unity)")
    img_l7 = os.path.abspath("e:/vyt/Assets/CipherCourtPolish/Backgrounds/REAL_GameComplete_Screenshot.png")
    add_image_diagram(doc, img_l7, "Figure 5.8: Level 7 Victory Debriefing Prototype — Case Solved, Justice Served (GameComplete.unity)", width=Inches(5.4))
    add_bullet_point(doc, "GameCompleteCanvas (Screen Space - Overlay) -> ParchmentCertificateCard (#F4EEDD) -> GoldenLaurelGavelSeal (Image) -> CongratulatoryHeadline -> MetricsGrid (2x2 Cards: Elapsed Time, Deduction Accuracy %, Evidence Found 6/6, Final Forensic Score) -> ActionButtons (Btn_ExportReport, Btn_ReturnToMenu).", bold_prefix="• UI Component Hierarchy:")
    add_bullet_point(doc, "GameCompleteManager.cs, GameManager.cs.", bold_prefix="• Primary C# Controllers:")
    add_bullet_point(doc, "Automatic aggregate calculation from GameManager on Start(), OnClick(Btn_ExportReport) triggering local JSON audit export, OnClick(Btn_ReturnToMenu) cleanly resetting session singletons.", bold_prefix="• User Interactions & Handled Events:")
    add_bullet_point(doc, "Integrity check on completed level flags before calculating score bonuses. Disposes in-memory web request textures upon exit.", bold_prefix="• Client-Side Validation Rules:")

    # Summary Component Matrix Table
    add_subheading(doc, "Table 5.1: Level-Wise Frontend Prototype Architecture & Component Specification Matrix")
    matrix_data = [
        ("Level 0\n(MainMenu.unity)", "MainMenuCanvas &\nProfile Modal", "MainMenuManager.cs\nGameManager.cs", "Button Clicks &\nText Input", "Validates alphanumeric username; dispatches session GUID to GameManager."),
        ("Level 1\n(Level1_Investigation.unity)", "ReticleCanvas &\nEvidence Modal", "PuzzleInteraction.cs\nLevel1Progress.cs", "WASD + MouseLook,\n[E] Key Raycast", "Raycast distance <= 2.5m; unlocks exit door after 4 markers secured."),
        ("Level 2\n(Level2_Computer.unity)", "TerminalFrame &\nPassword Modal", "PasswordPuzzle.cs\nLevel2Progress.cs", "In-world CRT clicks,\nKeyboard entry", "Sanitizes input; requires 'COURT2026'; max 3 attempts before lockout."),
        ("Level 3\n(Level3_Evidence.unity)", "CaesarCipherModal &\nRotor Assembly", "CipherPuzzle.cs\nLevel3Progress.cs", "Rotor mouse drag,\nPlaintext submission", "Validates (C - 3) mod 26; expects 'JUSTICE'; unlocks evidence vault."),
        ("Level 4\n(Level4_Archive.unity)", "SafeKeypadCanvas &\nLED Matrix", "ArchiveKeypad.cs\nLevel4ArchivePuzzle.cs", "World-space 3D keypad\nmouse push-buttons", "Debounced 3-digit buffer; verifies '427'; 3-second lockout penalty."),
        ("Level 5\n(Level5_Statements.unity)", "CaseFilesModal &\nSplit-Pane Ledger", "Level5Terminal.cs\nLevel5CasePuzzle.cs", "Ledger ScrollRect,\nNumeric keypad", "Validates transaction code '315'; unlocks oak double doors to Courtroom."),
        ("Level 6\n(Level6_Courtroom.unity)", "CourtroomVerdictModal &\nCross-Examination", "Level6Terminal.cs\nLevel6VerdictPuzzle.cs", "ToggleGroup radio,\nGavel action button", "Identifies witness statement #2 as perjury; triggers judicial gavel."),
        ("End Stage\n(GameComplete.unity)", "GameCompleteCanvas &\nVictory Certificate", "GameCompleteManager.cs\nGameManager.cs", "Button Clicks\n(Menu / Report)", "Aggregates final score, elapsed time, and evidence completion count.")
    ]
    mat_tbl = doc.add_table(rows=len(matrix_data) + 1, cols=5)
    mat_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    mat_tbl.autofit = False
    set_table_grid_borders(mat_tbl)
    mat_w = [Inches(1.2), Inches(1.3), Inches(1.3), Inches(1.1), Inches(1.6)]
    for r in mat_tbl.rows:
        for i, c in enumerate(r.cells):
            c.width = mat_w[i]
            set_cell_margins(c, 50, 50, 60, 60)
    for i, h in enumerate(["Level & Scene", "UI Screen / Modal", "Primary C# Controller", "Input Mechanism", "Validation Rule & Condition"]):
        cp = mat_tbl.cell(0, i).paragraphs[0]
        cp.add_run(h).font.bold = True
        cp.runs[0].font.name = FONT_NAME
        cp.runs[0].font.size = Pt(9.5)
        set_cell_background(mat_tbl.cell(0, i), "F2F2F2")
    for idx, row in enumerate(matrix_data):
        r = mat_tbl.rows[idx + 1]
        for col_idx, val in enumerate(row):
            cp = r.cells[col_idx].paragraphs[0]
            r_run = cp.add_run(val)
            r_run.font.name = FONT_NAME
            r_run.font.size = Pt(9)
            if col_idx == 0: r_run.font.bold = True

    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    # =========================================================================
    # 5.2 BACKEND ARCHITECTURE & GAME LOGIC
    # =========================================================================
    add_heading(doc, "5.2 Backend Architecture & Game Logic")
    add_body_paragraph(
        doc,
        "The server-side business logic tier is implemented through a lightweight, asynchronous Python REST microservice (`server.py`). "
        "The server exposes RESTful HTTP endpoints that receive serialized JSON payloads from Unity C# web clients, "
        "verifies transaction integrity, updates SQLite/PostgreSQL relational stores, and serves a live HTML5 administrative dashboard.",
        bold_prefix="Backend Service Pipeline:"
    )
    add_body_paragraph(
        doc,
        "Within the Unity runtime, the backend logic is governed by modular C# managers: `GameManager.cs` acts as the singleton "
        "orchestrator managing scene state transitions; `LevelTimer.cs` drives the 1000ms delta-time countdown; and `CipherPuzzle.cs` "
        "executes algorithmic string normalization and cryptographic validation."
    )

    # =========================================================================
    # 5.3 DATABASE SCHEMA DESIGN & DATA DICTIONARIES
    # =========================================================================
    add_heading(doc, "5.3 Database Schema Design & Data Dictionaries")
    add_body_paragraph(
        doc,
        "The persistence layer is structured into six normalized relational tables in SQLite/PostgreSQL. "
        "The data dictionaries below define the schema attributes, types, constraints, and descriptions matching the Architecture Design Document:"
    )

    # Table 5.2: PLAYER
    add_subheading(doc, "Table 5.2: PLAYER (Player Identity & Profiles) Data Dictionary")
    p_data = [
        ("player_id", "SERIAL", "PK, Not Null", "Unique integer identifier for the registered player."),
        ("player_name", "VARCHAR(50)", "Not Null", "Investigator username displayed on HUD and dashboard."),
        ("created_at", "TIMESTAMP", "Default: NOW()", "Timestamp recording initial account creation.")
    ]
    t1 = doc.add_table(rows=len(p_data) + 1, cols=4)
    t1.alignment = WD_TABLE_ALIGNMENT.CENTER
    t1.autofit = False
    set_table_grid_borders(t1)
    w_dict = [Inches(1.5), Inches(1.2), Inches(1.5), Inches(2.3)]
    for r in t1.rows:
        for i, c in enumerate(r.cells):
            c.width = w_dict[i]
            set_cell_margins(c, 50, 50, 70, 70)
    for i, h in enumerate(["Field Name", "Data Type", "Key / Constraint", "Description"]):
        cp = t1.cell(0, i).paragraphs[0]
        cp.add_run(h).font.bold = True
        cp.runs[0].font.name = FONT_NAME
        cp.runs[0].font.size = Pt(10)
        set_cell_background(t1.cell(0, i), "F2F2F2")
    for idx, row in enumerate(p_data):
        r = t1.rows[idx + 1]
        for col_idx, val in enumerate(row):
            cp = r.cells[col_idx].paragraphs[0]
            r_run = cp.add_run(val)
            r_run.font.name = FONT_NAME
            r_run.font.size = Pt(9.5)
            if col_idx == 0: r_run.font.bold = True

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # Table 5.3: LEVEL
    add_subheading(doc, "Table 5.3: LEVEL (Stage Configurations) Data Dictionary")
    l_data = [
        ("level_id", "SERIAL", "PK, Not Null", "Unique identifier for each game level/scene."),
        ("level_name", "VARCHAR(60)", "Unique, Not Null", "Scene name (e.g., Level1_Investigation, Level2_Computer)."),
        ("puzzle_type", "VARCHAR(30)", "Not Null", "Puzzle classification: 'BinaryKeypad', 'Password', 'Caesar', 'Verdict'."),
        ("time_limit", "INT", "Default: 300", "Maximum allocated duration in seconds (05:00 countdown)."),
        ("max_attempts", "INT", "Default: 3", "Maximum incorrect attempts permitted before level failure.")
    ]
    t2 = doc.add_table(rows=len(l_data) + 1, cols=4)
    t2.alignment = WD_TABLE_ALIGNMENT.CENTER
    t2.autofit = False
    set_table_grid_borders(t2)
    for r in t2.rows:
        for i, c in enumerate(r.cells):
            c.width = w_dict[i]
            set_cell_margins(c, 50, 50, 70, 70)
    for i, h in enumerate(["Field Name", "Data Type", "Key / Constraint", "Description"]):
        cp = t2.cell(0, i).paragraphs[0]
        cp.add_run(h).font.bold = True
        cp.runs[0].font.name = FONT_NAME
        cp.runs[0].font.size = Pt(10)
        set_cell_background(t2.cell(0, i), "F2F2F2")
    for idx, row in enumerate(l_data):
        r = t2.rows[idx + 1]
        for col_idx, val in enumerate(row):
            cp = r.cells[col_idx].paragraphs[0]
            r_run = cp.add_run(val)
            r_run.font.name = FONT_NAME
            r_run.font.size = Pt(9.5)
            if col_idx == 0: r_run.font.bold = True

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # Table 5.4: GAME_PROGRESS
    add_subheading(doc, "Table 5.4: GAME_PROGRESS (Player State) Data Dictionary")
    gp_data = [
        ("progress_id", "SERIAL", "PK, Not Null", "Unique tracking identifier for the progress record."),
        ("player_id", "INT", "FK -> PLAYER.player_id", "Foreign key linking progress to registered player."),
        ("level_id", "INT", "FK -> LEVEL.level_id", "Foreign key linking progress to specific game level."),
        ("status", "VARCHAR(20)", "Not Null", "Status indicator: 'active', 'completed', or 'failed'."),
        ("completed_at", "TIMESTAMP", "Nullable", "Timestamp recorded upon successful room clearance.")
    ]
    t3 = doc.add_table(rows=len(gp_data) + 1, cols=4)
    t3.alignment = WD_TABLE_ALIGNMENT.CENTER
    t3.autofit = False
    set_table_grid_borders(t3)
    for r in t3.rows:
        for i, c in enumerate(r.cells):
            c.width = w_dict[i]
            set_cell_margins(c, 50, 50, 70, 70)
    for i, h in enumerate(["Field Name", "Data Type", "Key / Constraint", "Description"]):
        cp = t3.cell(0, i).paragraphs[0]
        cp.add_run(h).font.bold = True
        cp.runs[0].font.name = FONT_NAME
        cp.runs[0].font.size = Pt(10)
        set_cell_background(t3.cell(0, i), "F2F2F2")
    for idx, row in enumerate(gp_data):
        r = t3.rows[idx + 1]
        for col_idx, val in enumerate(row):
            cp = r.cells[col_idx].paragraphs[0]
            r_run = cp.add_run(val)
            r_run.font.name = FONT_NAME
            r_run.font.size = Pt(9.5)
            if col_idx == 0: r_run.font.bold = True

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # Table 5.5: CLUE
    add_subheading(doc, "Table 5.5: CLUE (Forensic Clues) Data Dictionary")
    c_data = [
        ("clue_id", "SERIAL", "PK, Not Null", "Unique identifier for physical clue asset."),
        ("level_id", "INT", "FK -> LEVEL.level_id", "References parent level containing the clue."),
        ("clue_name", "VARCHAR(60)", "Not Null", "Short title (e.g., 'Evidence Marker 1', 'USB Drive')."),
        ("clue_value", "VARCHAR(100)", "Not Null", "Decrypted clue text content or cipher hint.")
    ]
    t4 = doc.add_table(rows=len(c_data) + 1, cols=4)
    t4.alignment = WD_TABLE_ALIGNMENT.CENTER
    t4.autofit = False
    set_table_grid_borders(t4)
    for r in t4.rows:
        for i, c in enumerate(r.cells):
            c.width = w_dict[i]
            set_cell_margins(c, 50, 50, 70, 70)
    for i, h in enumerate(["Field Name", "Data Type", "Key / Constraint", "Description"]):
        cp = t4.cell(0, i).paragraphs[0]
        cp.add_run(h).font.bold = True
        cp.runs[0].font.name = FONT_NAME
        cp.runs[0].font.size = Pt(10)
        set_cell_background(t4.cell(0, i), "F2F2F2")
    for idx, row in enumerate(c_data):
        r = t4.rows[idx + 1]
        for col_idx, val in enumerate(row):
            cp = r.cells[col_idx].paragraphs[0]
            r_run = cp.add_run(val)
            r_run.font.name = FONT_NAME
            r_run.font.size = Pt(9.5)
            if col_idx == 0: r_run.font.bold = True

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # Table 5.6: PUZZLE_ATTEMPT
    add_subheading(doc, "Table 5.6: PUZZLE_ATTEMPT (Submission Audit Logs) Data Dictionary")
    pa_data = [
        ("attempt_id", "SERIAL", "PK, Not Null", "Unique identifier for each individual code submission."),
        ("player_id", "INT", "FK -> PLAYER.player_id", "References the submitting investigator."),
        ("level_id", "INT", "FK -> LEVEL.level_id", "References level where puzzle was attempted."),
        ("submitted_value", "VARCHAR(100)", "Not Null", "Raw text or numeric string submitted by user."),
        ("is_correct", "BOOLEAN", "Not Null", "Boolean indicating validation outcome (True/False)."),
        ("attempt_time", "TIMESTAMP", "Default: NOW()", "Precise timestamp of submission.")
    ]
    t5 = doc.add_table(rows=len(pa_data) + 1, cols=4)
    t5.alignment = WD_TABLE_ALIGNMENT.CENTER
    t5.autofit = False
    set_table_grid_borders(t5)
    for r in t5.rows:
        for i, c in enumerate(r.cells):
            c.width = w_dict[i]
            set_cell_margins(c, 50, 50, 70, 70)
    for i, h in enumerate(["Field Name", "Data Type", "Key / Constraint", "Description"]):
        cp = t5.cell(0, i).paragraphs[0]
        cp.add_run(h).font.bold = True
        cp.runs[0].font.name = FONT_NAME
        cp.runs[0].font.size = Pt(10)
        set_cell_background(t5.cell(0, i), "F2F2F2")
    for idx, row in enumerate(pa_data):
        r = t5.rows[idx + 1]
        for col_idx, val in enumerate(row):
            cp = r.cells[col_idx].paragraphs[0]
            r_run = cp.add_run(val)
            r_run.font.name = FONT_NAME
            r_run.font.size = Pt(9.5)
            if col_idx == 0: r_run.font.bold = True

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # Table 5.7: EVIDENCE_RECORD
    add_subheading(doc, "Table 5.7: EVIDENCE_RECORD (Collected Evidence Registry) Data Dictionary")
    er_data = [
        ("evidence_id", "SERIAL", "PK, Not Null", "Unique identifier for evidence discovery log."),
        ("player_id", "INT", "FK -> PLAYER.player_id", "References discovering player."),
        ("level_id", "INT", "FK -> LEVEL.level_id", "References level where evidence was secured."),
        ("evidence_name", "VARCHAR(60)", "Not Null", "Descriptive exhibit label (e.g., 'Forensic Dossier A')."),
        ("collected_at", "TIMESTAMP", "Default: NOW()", "Timestamp recording moment of physical pickup.")
    ]
    t6 = doc.add_table(rows=len(er_data) + 1, cols=4)
    t6.alignment = WD_TABLE_ALIGNMENT.CENTER
    t6.autofit = False
    set_table_grid_borders(t6)
    for r in t6.rows:
        for i, c in enumerate(r.cells):
            c.width = w_dict[i]
            set_cell_margins(c, 50, 50, 70, 70)
    for i, h in enumerate(["Field Name", "Data Type", "Key / Constraint", "Description"]):
        cp = t6.cell(0, i).paragraphs[0]
        cp.add_run(h).font.bold = True
        cp.runs[0].font.name = FONT_NAME
        cp.runs[0].font.size = Pt(10)
        set_cell_background(t6.cell(0, i), "F2F2F2")
    for idx, row in enumerate(er_data):
        r = t6.rows[idx + 1]
        for col_idx, val in enumerate(row):
            cp = r.cells[col_idx].paragraphs[0]
            r_run = cp.add_run(val)
            r_run.font.name = FONT_NAME
            r_run.font.size = Pt(9.5)
            if col_idx == 0: r_run.font.bold = True

    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    # ER Diagram
    add_body_paragraph(
        doc,
        "Figure 5.9 illustrates the structural Entity-Relationship (ER) model across all six relational tables, "
        "enforcing strict foreign key integrity between PLAYER, LEVEL, GAME_PROGRESS (1:M), CLUE (1:M), "
        "PUZZLE_ATTEMPT (1:M), and EVIDENCE_RECORD (1:M):",
        bold_prefix="Entity-Relationship Diagram:"
    )
    er_path = os.path.abspath("e:/vyt/extracted_assets/arch_p8_0_Img41.png")
    add_image_diagram(doc, er_path, "Figure 5.9: Proposed Entity-Relationship (ER) Diagram for Cipher Court Database Schema", width=Inches(5.4))

    # =========================================================================
    # 5.4 API STRUCTURE, ENDPOINTS & JSON CONTRACTS
    # =========================================================================
    add_heading(doc, "5.4 API Structure, Endpoints & JSON Contracts")
    add_body_paragraph(
        doc,
        "The Python backend microservice exposes RESTful JSON API endpoints to synchronize gameplay state, "
        "audit attempts, and deliver live diagnostics to the web dashboard:"
    )

    add_subheading(doc, "Table 5.8: REST API Endpoints & JSON Contracts")

    api_data = [
        ("POST", "/api/event", "{ session_id, scene, event_type, result, details }", "{ success: true, event_id: <int> }"),
        ("GET", "/api/events", "Query: ?limit=100", "{ success: true, events: [ { id, timestamp, scene, ... } ] }"),
        ("GET", "/api/stats", "None (Header Session)", "{ success: true, total_events: 14, clues_found: 6, puzzles_solved: 5 }"),
        ("POST", "/game-events", "{ session_id, scene, event_type, result, details }", "{ success: true, event_id: <int> }"),
        ("GET", "/health", "None", "{ success: true, service: 'cipher-court-db', status: 'ONLINE' }")
    ]

    api_tbl = doc.add_table(rows=len(api_data) + 1, cols=4)
    api_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    api_tbl.autofit = False
    set_table_grid_borders(api_tbl)

    api_w = [Inches(1.0), Inches(1.6), Inches(2.2), Inches(1.7)]
    for r in api_tbl.rows:
        for i, c in enumerate(r.cells):
            c.width = api_w[i]
            set_cell_margins(c, 60, 60, 80, 80)

    for i, h in enumerate(["HTTP Method", "Endpoint Route", "Request Body / Query Params", "Response JSON Contract"]):
        cp = api_tbl.cell(0, i).paragraphs[0]
        cp.add_run(h).font.bold = True
        cp.runs[0].font.name = FONT_NAME
        cp.runs[0].font.size = Pt(10)
        set_cell_background(api_tbl.cell(0, i), "F2F2F2")

    for idx, (mth, ep, req, res) in enumerate(api_data):
        r = api_tbl.rows[idx + 1]
        for col_idx, val in enumerate([mth, ep, req, res]):
            cp = r.cells[col_idx].paragraphs[0]
            r_run = cp.add_run(val)
            r_run.font.name = FONT_NAME
            r_run.font.size = Pt(9.5)
            if col_idx == 0: r_run.font.bold = True

    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    # =========================================================================
    # 5.5 SECURITY CONSIDERATIONS
    # =========================================================================
    add_heading(doc, "5.5 Security Considerations & Granular Access Control Policies")
    add_body_paragraph(
        doc,
        "To ensure academic rigor and prevent unauthorized bypass or exploitation of the simulation, "
        "multiple security and validation layers were integrated across the client and server:",
        bold_prefix="Security Architecture:"
    )
    add_bullet_point(doc, "AES-256 Symmetric Encryption: High-security forensic evidence files (trial memorandum, ballistics records) are encrypted using AES-256 in CBC mode. Decryption keys are derived dynamically upon solving preliminary room ciphers, demonstrating cryptographic defense principles.")
    add_bullet_point(doc, "Parameterized SQL Query Execution: Server-side queries strictly use parameterized query placeholders (`$1, $2, $3` in PostgreSQL or `?` in SQLite) via `psycopg2` and `sqlite3`, eliminating SQL Injection (SQLi) vulnerabilities.")
    add_bullet_point(doc, "Tamper-Resistant Game State: Puzzle answers and target hash digests are evaluated inside compiled C# memory namespaces rather than plain text scene files. Input strings are trimmed, normalized, and case-folded prior to comparison.")
    add_bullet_point(doc, "Throttling and Attempt Locking: Keypads enforce an automatic 3-second lockout penalty upon entering incorrect codes, preventing brute-force dictionary attacks against numeric vault locks.")

    # =========================================================================
    # 5.6 PROCEDURAL DESIGN & VALIDATION ALGORITHMS
    # =========================================================================
    add_heading(doc, "5.6 Procedural Design (Generic Puzzle Logic Flowchart & Validation Algorithms)")
    add_body_paragraph(
        doc,
        "The procedural flow governing player interaction, clue discovery, code submission, and outcome branching is modeled in Figure 5.10:",
        bold_prefix="Procedural Control Flow:"
    )
    puz_path = os.path.abspath("e:/vyt/extracted_assets/arch_p4_0_Img20.png")
    add_image_diagram(doc, puz_path, "Figure 5.10: Generic Puzzle Business Logic and Attempt Validation Flowchart", width=Inches(4.6))

    add_body_paragraph(
        doc,
        "The core mathematical and procedural validation algorithms governing Cipher Court are formalized below:",
        bold_prefix="Algorithmic Specifications:"
    )

    algo1_code = """Algorithm 1: Distance-Bounded Reticle Raycast Detection
Input: cameraRay (origin, direction), maxDistance = 2.5m, interactionLayerMask
Output: hoveredInteractable, promptState

1. cameraRay = MainCamera.ViewportPointToRay(Vector3(0.5, 0.5, 0));
2. if Physics.Raycast(cameraRay, out hitInfo, maxDistance, interactionLayerMask):
3.    interactable = hitInfo.collider.GetComponent<IInteractable>();
4.    if interactable is not null:
5.       ReticleUI.SetHighlight(true);
6.       HUDPrompt.DisplayText(interactable.GetPromptText()); // e.g. "[E] Inspect Clue"
7.       if Input.GetKeyDown(KeyCode.E):
8.          interactable.OnInteract();
9.    else:
10.      ReticleUI.SetHighlight(false);
11.      HUDPrompt.Clear();
12. else:
13.   ReticleUI.SetHighlight(false);
14.   HUDPrompt.Clear();"""
    add_code_block(doc, algo1_code, caption="Algorithm 1: Distance-Bounded Reticle Raycast Interaction (C# Unity)")

    algo2_code = """Algorithm 2: Cryptographic Caesar Shift Validation Engine
Input: ciphertext = "MXVWLFH", shiftKey = 3, userSubmittedString
Output: isCorrect (Boolean), remainingAttempts (Integer)

1. targetPlaintext = "";
2. for each char c in ciphertext:
3.    if c is uppercase letter:
4.       decryptedChar = (char)(((c - 'A' - shiftKey + 26) % 26) + 'A');
5.       targetPlaintext += decryptedChar; // Decodes to "JUSTICE"
6. cleanInput = userSubmittedString.Trim().ToUpper();
7. if cleanInput == targetPlaintext:
8.    PlayAudioChime(SUCCESS_CLIP);
9.    LevelTimer.StopCountdown();
10.   DoorController.TriggerOpenSlerp();
11.   return (isCorrect = true, attempts = currentAttempts);
12. else:
13.   currentAttempts = currentAttempts - 1;
14.   PlayAudioChime(ERROR_CLIP);
15.   if currentAttempts <= 0:
16.      TriggerLevelFailedModal();
17.   return (isCorrect = false, attempts = currentAttempts);"""
    add_code_block(doc, algo2_code, caption="Algorithm 2: Caesar Cipher Decryption and Attempt Verification")

    doc.add_page_break()

