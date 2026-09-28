import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, mm

def generate_pdf():
    pdf_filename = "A2_Group_Evidence.pdf"
    doc = SimpleDocTemplate(
        pdf_filename,
        pagesize=A4,
        leftMargin=15 * mm,
        rightMargin=15 * mm,
        topMargin=15 * mm,
        bottomMargin=15 * mm
    )

    styles = getSampleStyleSheet()

    # Pure Black & White / Grayscale Palette
    NAVY = colors.HexColor("#000000")          # Solid pure black for titles, primary lines, table headers
    SECONDARY = colors.HexColor("#222222")     # Deep charcoal for subheaders
    ACCENT = colors.HexColor("#000000")        # Black for links & accents
    LIGHT_BG = colors.HexColor("#F4F4F4")      # Subtle 5% gray for cards
    BORDER_COLOR = colors.HexColor("#444444")  # Sharp dark gray for borders
    RED_ACCENT = colors.HexColor("#000000")
    RED_BG = colors.HexColor("#C0C0C0")        # 25% gray for Extreme / Critical items
    GREEN_BG = colors.HexColor("#ECECEC")      # Light 7% gray for Done / Approved
    GREEN_TEXT = colors.HexColor("#000000")
    YELLOW_BG = colors.HexColor("#D8D8D8")     # 15% gray for High / Milestones
    YELLOW_TEXT = colors.HexColor("#000000")

    # Custom typography styles (Monochrome)
    title_cover = ParagraphStyle(
        'CoverTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=22,
        leading=26,
        textColor=NAVY,
        alignment=1 # Center
    )
    subtitle_cover = ParagraphStyle(
        'CoverSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor("#333333"),
        alignment=1
    )
    inst_header = ParagraphStyle(
        'InstHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=18,
        textColor=NAVY,
        alignment=1
    )
    unit_header = ParagraphStyle(
        'UnitHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13,
        textColor=colors.HexColor("#333333"),
        alignment=1
    )
    sec_title = ParagraphStyle(
        'SectionTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=16,
        textColor=NAVY,
        spaceAfter=6
    )
    sub_title = ParagraphStyle(
        'SubTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13,
        textColor=NAVY,
        spaceBefore=6,
        spaceAfter=4
    )
    body_text = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=colors.HexColor("#000000"),
        spaceAfter=4
    )
    body_bold = ParagraphStyle(
        'BodyBold',
        parent=body_text,
        fontName='Helvetica-Bold'
    )
    tbl_hdr = ParagraphStyle(
        'TblHdr',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        textColor=colors.white,
        alignment=0
    )
    tbl_cell = ParagraphStyle(
        'TblCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.5,
        leading=9.5,
        textColor=colors.HexColor("#000000")
    )
    tbl_cell_bold = ParagraphStyle(
        'TblCellBold',
        parent=tbl_cell,
        fontName='Helvetica-Bold'
    )
    tbl_cell_center = ParagraphStyle(
        'TblCellCenter',
        parent=tbl_cell,
        alignment=1
    )
    tbl_cell_center_bold = ParagraphStyle(
        'TblCellCenterBold',
        parent=tbl_cell_bold,
        alignment=1
    )
    caption_style = ParagraphStyle(
        'Caption',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=7.5,
        leading=9.5,
        textColor=colors.HexColor("#333333"),
        alignment=1,
        spaceBefore=3,
        spaceAfter=6
    )

    story = []

    # =========================================================================
    # PAGE 1: COVER PAGE
    # =========================================================================
    story.append(Spacer(1, 10 * mm))
    story.append(Paragraph("AUSTRALIAN INSTITUTE OF HIGHER EDUCATION", inst_header))
    story.append(Paragraph("BISY2004 PROJECT MANAGEMENT — ASSESSMENT 2", unit_header))
    story.append(Spacer(1, 4 * mm))
    story.append(HRFlowable(width="100%", thickness=2, color=NAVY, spaceAfter=20))

    story.append(Spacer(1, 10 * mm))
    story.append(Paragraph("OFFICIAL PDF EVIDENCE PACK (SECURE LANE)", ParagraphStyle('Badge', fontName='Helvetica-Bold', fontSize=9, textColor=SECONDARY, alignment=1)))
    story.append(Spacer(1, 4 * mm))
    story.append(Paragraph("PROJECT OMNIPORTAL", title_cover))
    story.append(Spacer(1, 2 * mm))
    story.append(Paragraph("Consolidation of University Student-Facing Digital Portals", subtitle_cover))
    story.append(Spacer(1, 10 * mm))

    # Meta Table
    meta_data = [
        [Paragraph("Selected Scenario:", tbl_cell_bold), Paragraph("Scenario C — University Student Portal Consolidation", tbl_cell)],
        [Paragraph("Target Institution:", tbl_cell_bold), Paragraph("Apex Metropolitan University (28,000 Students, 3,200 Staff)", tbl_cell)],
        [Paragraph("Live Website URL:", tbl_cell_bold), Paragraph("<b>https://sadiksk07.github.io/omniportal-bisy2004/</b>", tbl_cell)],
        [Paragraph("Website Platform:", tbl_cell_bold), Paragraph("GitHub Pages (Approved Free Platform / 24/7 Accessibility Checked)", tbl_cell)],
        [Paragraph("Approved Budget Cap:", tbl_cell_bold), Paragraph("$450,000 AUD (Base BAC: $385,000 AUD | Baseline: $423,500 AUD)", tbl_cell)],
        [Paragraph("Project Timeline:", tbl_cell_bold), Paragraph("24 Weeks (120 Working Days: 02-Feb-2026 to 17-Jul-2026)", tbl_cell)],
        [Paragraph("Submission Date:", tbl_cell_bold), Paragraph("Session 8, 2026", tbl_cell)]
    ]
    t_meta = Table(meta_data, colWidths=[40 * mm, 120 * mm])
    t_meta.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), LIGHT_BG),
        ('BOX', (0,0), (-1,-1), 1, BORDER_COLOR),
        ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_meta)
    story.append(Spacer(1, 15 * mm))

    # Team Members Table
    story.append(Paragraph("CONTRIBUTING GROUP MEMBERS & ROLE ALLOCATION", sub_title))
    team_data = [
        [Paragraph("Student Name", tbl_hdr), Paragraph("Student ID", tbl_hdr), Paragraph("Assigned Project Role", tbl_hdr), Paragraph("Primary Functional Responsibility", tbl_hdr)],
        [Paragraph("<b>Tanvir Ahmed</b>", tbl_cell), Paragraph("238983", tbl_cell_center_bold), Paragraph("Project Lead & Systems Architect", tbl_cell), Paragraph("Sections 1 & 2: Scope, Charter, WBS, ProjectLibre Schedule", tbl_cell)],
        [Paragraph("<b>Momen Ahmed</b>", tbl_cell), Paragraph("242048", tbl_cell_center_bold), Paragraph("Risk, Finance & Governance Lead", tbl_cell), Paragraph("Sections 2 & 3: Cost Model, 5x5 Heat Map, Stakeholder Matrix", tbl_cell)],
        [Paragraph("<b>MD Rejvi Jaman Mafti</b>", tbl_cell), Paragraph("241964", tbl_cell_center_bold), Paragraph("Quality, Delivery & Tracking Lead", tbl_cell), Paragraph("Sections 4, 5 & 6: Quality, Change CR-01, RACI, Trello, EVM", tbl_cell)]
    ]
    t_team = Table(team_data, colWidths=[38 * mm, 24 * mm, 48 * mm, 60 * mm])
    t_team.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), NAVY),
        ('BOX', (0,0), (-1,-1), 1, BORDER_COLOR),
        ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_team)

    story.append(PageBreak())

    # =========================================================================
    # PAGE 2: TOOL-EVIDENCE INDEX
    # =========================================================================
    story.append(Paragraph("1. Tool-Evidence Index & Authorship Attestation", sec_title))
    story.append(Paragraph("This index formally maps all project management artefacts displayed on the live website to the approved software applications and the responsible group members:", body_text))

    tool_data = [
        [Paragraph("Artefact Description", tbl_hdr), Paragraph("Software Tool", tbl_hdr), Paragraph("Source File Reference", tbl_hdr), Paragraph("Author", tbl_hdr), Paragraph("Role & Contribution", tbl_hdr)],
        [Paragraph("Work Breakdown Structure", tbl_cell_bold), Paragraph("diagrams.net", tbl_cell), Paragraph("A2_Group_WBS_Diagram.drawio", tbl_cell), Paragraph("Tanvir Ahmed (238983)", tbl_cell), Paragraph("Decomposed 6 phases, 28 work packages, 6 milestones", tbl_cell)],
        [Paragraph("Project Schedule & Critical Path", tbl_cell_bold), Paragraph("ProjectLibre", tbl_cell), Paragraph("A2_GroupXX_ProjectLibre.pod", tbl_cell), Paragraph("Tanvir Ahmed (238983)", tbl_cell), Paragraph("Calculated 120-day duration, 86-day critical path, float", tbl_cell)],
        [Paragraph("Cost Baseline & Budget Model", tbl_cell_bold), Paragraph("MS Excel", tbl_cell), Paragraph("A2_GroupXX_ProjectData.xlsx (Tab 3)", tbl_cell), Paragraph("Momen Ahmed (242048)", tbl_cell), Paragraph("Costed 305 resource days ($219.6k), Capex ($90.5k), reserves", tbl_cell)],
        [Paragraph("5x5 Risk Register & Heat Map", tbl_cell_bold), Paragraph("MS Excel", tbl_cell), Paragraph("A2_GroupXX_ProjectData.xlsx (Tab 4)", tbl_cell), Paragraph("Momen Ahmed (242048)", tbl_cell), Paragraph("Modeled 10 risks; scored R01 at 20, R02 at 15 on 5x5 grid", tbl_cell)],
        [Paragraph("Stakeholder Power-Interest Grid", tbl_cell_bold), Paragraph("diagrams.net", tbl_cell), Paragraph("A2_Group_Stakeholder_Matrix.drawio", tbl_cell), Paragraph("Momen Ahmed (242048)", tbl_cell), Paragraph("Segmented 8 stakeholders into 4 operational quadrants", tbl_cell)],
        [Paragraph("Quality Standards & Metrics", tbl_cell_bold), Paragraph("MS Excel", tbl_cell), Paragraph("A2_GroupXX_ProjectData.xlsx (Tab 6)", tbl_cell), Paragraph("MD Rejvi Jaman (241964)", tbl_cell), Paragraph("Defined 6 measurable criteria (99.95% uptime, 100% data fidelity)", tbl_cell)],
        [Paragraph("Change Control Log (CR-01)", tbl_cell_bold), Paragraph("MS Excel", tbl_cell), Paragraph("A2_GroupXX_ProjectData.xlsx (Tab 6)", tbl_cell), Paragraph("MD Rejvi Jaman (241964)", tbl_cell), Paragraph("Documented MFA change: +$14.5k cost, +8 days effort", tbl_cell)],
        [Paragraph("RACI Governance Matrix", tbl_cell_bold), Paragraph("MS Excel", tbl_cell), Paragraph("A2_GroupXX_ProjectData.xlsx (Tab 6)", tbl_cell), Paragraph("MD Rejvi Jaman (241964)", tbl_cell), Paragraph("Enforced single-point accountability across 6 phases", tbl_cell)],
        [Paragraph("Sprint Tracking Kanban Board", tbl_cell_bold), Paragraph("Trello", tbl_cell), Paragraph("https://trello.com/b/6aba6567933223c336fb8dfc/", tbl_cell), Paragraph("MD Rejvi Jaman (241964)", tbl_cell), Paragraph("Managed 5 workflow columns and 20 WBS-linked task cards", tbl_cell)],
        [Paragraph("EVM Tracking Dashboard", tbl_cell_bold), Paragraph("MS Excel", tbl_cell), Paragraph("A2_GroupXX_ProjectData.xlsx (Tab 7)", tbl_cell), Paragraph("MD Rejvi Jaman (241964)", tbl_cell), Paragraph("Diagnosed Wk 14 SPI=0.880; planned crashing & fast-tracking", tbl_cell)],
        [Paragraph("Integrated Project Website", tbl_cell_bold), Paragraph("GitHub Pages", tbl_cell), Paragraph("https://sadiksk07.github.io/omniportal-bisy2004/", tbl_cell), Paragraph("All Members", tbl_cell), Paragraph("Synthesized 6 sections (~1,500 words), responsive layout", tbl_cell)]
    ]
    t_tools = Table(tool_data, colWidths=[36 * mm, 24 * mm, 42 * mm, 34 * mm, 44 * mm])
    t_tools.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), NAVY),
        ('BOX', (0,0), (-1,-1), 1, BORDER_COLOR),
        ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_tools)
    story.append(Spacer(1, 4 * mm))

    # Note
    note_box = [
        [Paragraph("<b>Secure Lane Verification:</b> All primary artefacts indexed above have been constructed manually by the group using authorized software tools. Each student possesses independent mastery over their maintained tools and calculations, ready for live examination during the individual viva.", tbl_cell)]
    ]
    t_note = Table(note_box, colWidths=[180 * mm])
    t_note.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), LIGHT_BG),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#444444")),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_note)

    story.append(PageBreak())

    # =========================================================================
    # PAGE 3: WBS DIAGRAM & DELIVERABLES
    # =========================================================================
    story.append(Paragraph("2. Scope & Work Breakdown Structure (WBS) Evidence", sec_title))
    story.append(Paragraph("The WBS establishes the 100% boundary of project deliverables, constructed in <b>diagrams.net</b> (<code>A2_Group_WBS_Diagram.drawio</code>).", body_text))

    wbs_summary = [
        [Paragraph("WBS Code", tbl_hdr), Paragraph("Deliverable / Work Package Name", tbl_hdr), Paragraph("Duration", tbl_hdr), Paragraph("Cost ($)", tbl_hdr), Paragraph("Milestone Gate", tbl_hdr), Paragraph("Critical?", tbl_hdr)],
        [Paragraph("1.0", tbl_cell_bold), Paragraph("PROJECT INITIATION & GOVERNANCE", tbl_cell_bold), Paragraph("15 Days", tbl_cell), Paragraph("$16,500", tbl_cell), Paragraph("M1: Charter Sign-off", tbl_cell), Paragraph("Yes", tbl_cell_bold)],
        [Paragraph("1.1", tbl_cell), Paragraph("Project Charter & Stakeholder Approval", tbl_cell), Paragraph("5 Days", tbl_cell), Paragraph("$4,500", tbl_cell), Paragraph("-", tbl_cell), Paragraph("Yes", tbl_cell)],
        [Paragraph("1.2", tbl_cell), Paragraph("Project Management Plan & Risk Framework", tbl_cell), Paragraph("5 Days", tbl_cell), Paragraph("$3,800", tbl_cell), Paragraph("-", tbl_cell), Paragraph("Yes", tbl_cell)],
        [Paragraph("2.0", tbl_cell_bold), Paragraph("REQUIREMENTS & ARCHITECTURE", tbl_cell_bold), Paragraph("20 Days", tbl_cell), Paragraph("$31,200", tbl_cell), Paragraph("M2: Specs Approved", tbl_cell), Paragraph("Yes", tbl_cell_bold)],
        [Paragraph("2.1", tbl_cell), Paragraph("Stakeholder Requirements Gathering", tbl_cell), Paragraph("8 Days", tbl_cell), Paragraph("$9,600", tbl_cell), Paragraph("-", tbl_cell), Paragraph("Yes", tbl_cell)],
        [Paragraph("2.2", tbl_cell), Paragraph("Data Privacy & Compliance Review (APP)", tbl_cell), Paragraph("6 Days", tbl_cell), Paragraph("$6,400", tbl_cell), Paragraph("-", tbl_cell), Paragraph("No (4d Float)", tbl_cell)],
        [Paragraph("2.3", tbl_cell), Paragraph("Cloud Architecture Specification (AWS Multi-AZ)", tbl_cell), Paragraph("10 Days", tbl_cell), Paragraph("$12,800", tbl_cell), Paragraph("-", tbl_cell), Paragraph("Yes", tbl_cell)],
        [Paragraph("3.0", tbl_cell_bold), Paragraph("DATA MIGRATION & SECURITY SETUP", tbl_cell_bold), Paragraph("25 Days", tbl_cell), Paragraph("$39,500", tbl_cell), Paragraph("M3: ETL Ready", tbl_cell), Paragraph("Yes", tbl_cell_bold)],
        [Paragraph("3.1", tbl_cell), Paragraph("Legacy Data Profiling & Cleansing", tbl_cell), Paragraph("10 Days", tbl_cell), Paragraph("$14,000", tbl_cell), Paragraph("-", tbl_cell), Paragraph("Yes", tbl_cell)],
        [Paragraph("3.2", tbl_cell_bold), Paragraph("Automated ETL Scripts Development (Critical Bottleneck)", tbl_cell_bold), Paragraph("10 Days", tbl_cell), Paragraph("$15,200", tbl_cell), Paragraph("-", tbl_cell), Paragraph("Yes (Zero Float)", tbl_cell_bold)],
        [Paragraph("3.3", tbl_cell), Paragraph("Cloud Database Schema & Index Tuning", tbl_cell), Paragraph("5 Days", tbl_cell), Paragraph("$6,800", tbl_cell), Paragraph("-", tbl_cell), Paragraph("Yes", tbl_cell)],
        [Paragraph("4.0", tbl_cell_bold), Paragraph("PORTAL CORE DEVELOPMENT (Agile Sprints)", tbl_cell_bold), Paragraph("35 Days", tbl_cell), Paragraph("$68,000", tbl_cell), Paragraph("M4: Feature Complete", tbl_cell), Paragraph("Yes", tbl_cell_bold)],
        [Paragraph("4.1", tbl_cell), Paragraph("Sprint 1: SSO & Unified Authentication", tbl_cell), Paragraph("10 Days", tbl_cell), Paragraph("$17,500", tbl_cell), Paragraph("-", tbl_cell), Paragraph("Yes", tbl_cell)],
        [Paragraph("4.2", tbl_cell), Paragraph("Sprint 2: Academic Records & Timetabling", tbl_cell), Paragraph("10 Days", tbl_cell), Paragraph("$18,200", tbl_cell), Paragraph("-", tbl_cell), Paragraph("Yes", tbl_cell)],
        [Paragraph("4.3", tbl_cell), Paragraph("Sprint 3: Course Enrolment & Cart Flow", tbl_cell), Paragraph("10 Days", tbl_cell), Paragraph("$18,500", tbl_cell), Paragraph("-", tbl_cell), Paragraph("Yes", tbl_cell)],
        [Paragraph("4.4", tbl_cell), Paragraph("Sprint 4: Financial Payment Gateway Integration", tbl_cell), Paragraph("8 Days", tbl_cell), Paragraph("$13,800", tbl_cell), Paragraph("-", tbl_cell), Paragraph("Yes", tbl_cell)],
        [Paragraph("4.5", tbl_cell), Paragraph("Sprint 5: Mobile UI Polish & Accessibility", tbl_cell), Paragraph("7 Days", tbl_cell), Paragraph("$9,800", tbl_cell), Paragraph("-", tbl_cell), Paragraph("No (3d Float)", tbl_cell)],
        [Paragraph("5.0", tbl_cell_bold), Paragraph("TESTING, QA & PILOT", tbl_cell_bold), Paragraph("20 Days", tbl_cell), Paragraph("$34,800", tbl_cell), Paragraph("M5: UAT Sign-off", tbl_cell), Paragraph("Yes", tbl_cell_bold)],
        [Paragraph("5.1", tbl_cell), Paragraph("Performance & Concurrency Load Testing", tbl_cell), Paragraph("8 Days", tbl_cell), Paragraph("$11,200", tbl_cell), Paragraph("-", tbl_cell), Paragraph("Yes", tbl_cell)],
        [Paragraph("5.2", tbl_cell), Paragraph("Independent Penetration Testing (CREST)", tbl_cell), Paragraph("5 Days", tbl_cell), Paragraph("$8,500", tbl_cell), Paragraph("-", tbl_cell), Paragraph("Yes", tbl_cell)],
        [Paragraph("5.3", tbl_cell), Paragraph("User Acceptance Testing (UAT) with 50 Users", tbl_cell), Paragraph("7 Days", tbl_cell), Paragraph("$9,500", tbl_cell), Paragraph("-", tbl_cell), Paragraph("Yes", tbl_cell)],
        [Paragraph("6.0", tbl_cell_bold), Paragraph("TRAINING, DEPLOYMENT & CLOSURE", tbl_cell_bold), Paragraph("15 Days", tbl_cell), Paragraph("$24,200", tbl_cell), Paragraph("M6: Final Closure", tbl_cell), Paragraph("Yes", tbl_cell_bold)],
        [Paragraph("6.1", tbl_cell), Paragraph("End-User Guides & Video Walkthroughs", tbl_cell), Paragraph("5 Days", tbl_cell), Paragraph("$5,400", tbl_cell), Paragraph("-", tbl_cell), Paragraph("No (8d Float)", tbl_cell)],
        [Paragraph("6.3", tbl_cell), Paragraph("Production Cutover (Blue-Green Deployment)", tbl_cell), Paragraph("4 Days", tbl_cell), Paragraph("$8,200", tbl_cell), Paragraph("-", tbl_cell), Paragraph("Yes", tbl_cell)],
        [Paragraph("6.4", tbl_cell), Paragraph("Post-Implementation Review & Lessons Learned", tbl_cell), Paragraph("4 Days", tbl_cell), Paragraph("$3,400", tbl_cell), Paragraph("-", tbl_cell), Paragraph("Yes", tbl_cell)]
    ]
    t_wbs = Table(wbs_summary, colWidths=[18 * mm, 74 * mm, 20 * mm, 20 * mm, 30 * mm, 18 * mm])
    t_wbs.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), NAVY),
        ('BOX', (0,0), (-1,-1), 1, BORDER_COLOR),
        ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
    ]))
    story.append(t_wbs)
    story.append(Paragraph("<b>Figure 1:</b> Work Breakdown Structure work package register and milestone summary (Source: <code>A2_Group_WBS_Diagram.drawio</code>).", caption_style))

    story.append(PageBreak())

    # =========================================================================
    # PAGE 4: PROJECTLIBRE SCHEDULE & COST
    # =========================================================================
    story.append(Paragraph("3. ProjectLibre Schedule & Cost Baseline Evidence", sec_title))
    story.append(Paragraph("The project schedule was constructed in <b>ProjectLibre Desktop</b> (Source: <code>A2_GroupXX_ProjectLibre.pod</code>) and costed in <b>Microsoft Excel</b> (Tab 3).", body_text))

    sched_meta = [
        [Paragraph("Timeline Window:", tbl_cell_bold), Paragraph("02 February 2026 to 17 July 2026 (24 Calendar Weeks / 120 Working Days)", tbl_cell)],
        [Paragraph("Critical Path Length:", tbl_cell_bold), Paragraph("86 Working Days (Zero total float along Tasks 1.1 -> 2.4 -> 3.2 -> 4.4 -> 5.3 -> 6.3)", tbl_cell)],
        [Paragraph("Milestone Gates:", tbl_cell_bold), Paragraph("6 Zero-day milestones (M1 Charter, M2 Specs, M3 ETL, M4 Core Dev, M5 UAT, M6 Closure)", tbl_cell)],
        [Paragraph("Critical Bottleneck:", tbl_cell_bold), Paragraph("WBS 3.2: Automated ETL Scripts Development (Zero float; caused Week 14 variance)", tbl_cell)]
    ]
    t_sched_meta = Table(sched_meta, colWidths=[40 * mm, 140 * mm])
    t_sched_meta.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), LIGHT_BG),
        ('BOX', (0,0), (-1,-1), 1, BORDER_COLOR),
        ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_sched_meta)
    story.append(Spacer(1, 4 * mm))

    # Cost Table
    story.append(Paragraph("Project Budget Breakdown & Reserve Structure", sub_title))
    cost_data = [
        [Paragraph("Cost Element", tbl_hdr), Paragraph("Resource / Line Item Basis", tbl_hdr), Paragraph("Scheduled Cost ($)", tbl_hdr), Paragraph("Financial Role", tbl_hdr)],
        [Paragraph("Project Manager", tbl_cell), Paragraph("50 Days @ $95/hr ($760/day) — Tanvir Ahmed", tbl_cell), Paragraph("$38,000", tbl_cell), Paragraph("Direct Labour", tbl_cell)],
        [Paragraph("Solutions Architect", tbl_cell), Paragraph("35 Days @ $115/hr ($920/day) — Contractor", tbl_cell), Paragraph("$32,200", tbl_cell), Paragraph("Direct Labour", tbl_cell)],
        [Paragraph("Senior Developers (2)", tbl_cell), Paragraph("80 Days @ $85/hr ($680/day) — Full-Stack Team", tbl_cell), Paragraph("$54,400", tbl_cell), Paragraph("Direct Labour", tbl_cell)],
        [Paragraph("Database Specialist", tbl_cell), Paragraph("45 Days @ $95/hr ($760/day) — Momen Ahmed / Contractor", tbl_cell), Paragraph("$34,200", tbl_cell), Paragraph("Direct Labour", tbl_cell)],
        [Paragraph("QA & Security Engineer", tbl_cell), Paragraph("40 Days @ $80/hr ($640/day) — MD Rejvi Jaman", tbl_cell), Paragraph("$25,600", tbl_cell), Paragraph("Direct Labour", tbl_cell)],
        [Paragraph("Change Specialist", tbl_cell), Paragraph("30 Days @ $75/hr ($600/day) — Change Lead", tbl_cell), Paragraph("$18,000", tbl_cell), Paragraph("Direct Labour", tbl_cell)],
        [Paragraph("Systems Analyst", tbl_cell), Paragraph("30 Days @ $85/hr ($680/day) — Contractor", tbl_cell), Paragraph("$20,400", tbl_cell), Paragraph("Direct Labour", tbl_cell)],
        [Paragraph("AWS Cloud Infrastructure", tbl_cell), Paragraph("Multi-AZ Cloud Hosting, RDS PostgreSQL, Redis (6 mo)", tbl_cell), Paragraph("$28,500", tbl_cell), Paragraph("Capex Non-Labour", tbl_cell)],
        [Paragraph("Okta Enterprise Licences", tbl_cell), Paragraph("1-Year University SSO & Identity Federation", tbl_cell), Paragraph("$24,000", tbl_cell), Paragraph("Capex Non-Labour", tbl_cell)],
        [Paragraph("CREST Penetration Test", tbl_cell), Paragraph("Independent CyberSec External Security Audit", tbl_cell), Paragraph("$16,500", tbl_cell), Paragraph("Capex Non-Labour", tbl_cell)],
        [Paragraph("Training Media Production", tbl_cell), Paragraph("Video studio guides for students & academic staff", tbl_cell), Paragraph("$9,500", tbl_cell), Paragraph("Capex Non-Labour", tbl_cell)],
        [Paragraph("Design & Payment Testing", tbl_cell), Paragraph("Figma UI lab ($6.2k) + Payment gateway escrow ($5.8k)", tbl_cell), Paragraph("$12,000", tbl_cell), Paragraph("Capex Non-Labour", tbl_cell)],
        [Paragraph("<b>SUBTOTAL BASELINE (BAC)</b>", tbl_cell_bold), Paragraph("Direct Labour ($219.6k) + Capex Non-Labour ($90.5k)", tbl_cell_bold), Paragraph("<b>$385,000</b>", tbl_cell_bold), Paragraph("Baseline Cost", tbl_cell_bold)],
        [Paragraph("Contingency Reserve (10%)", tbl_cell), Paragraph("Allocated for identified technical risks (ETL variance, CR-01)", tbl_cell), Paragraph("$38,500", tbl_cell), Paragraph("PM Managed Reserve", tbl_cell)],
        [Paragraph("<b>TOTAL COST BASELINE</b>", tbl_cell_bold), Paragraph("BAC + 10% Technical Contingency Reserve", tbl_cell_bold), Paragraph("<b>$423,500</b>", tbl_cell_bold), Paragraph("Cost Baseline", tbl_cell_bold)],
        [Paragraph("Management Reserve (5%)", tbl_cell), Paragraph("Held by Sponsor/CIO for unforeseen institutional scope shifts", tbl_cell), Paragraph("$19,250", tbl_cell), Paragraph("Executive Reserve", tbl_cell)],
        [Paragraph("<b>TOTAL PROJECT BUDGET</b>", tbl_cell_bold), Paragraph("Approved Institutional Funding Envelope", tbl_cell_bold), Paragraph("<b>$442,750</b>", tbl_cell_bold), Paragraph("Budget Cap: $450,000", tbl_cell_bold)]
    ]
    t_cost = Table(cost_data, colWidths=[45 * mm, 75 * mm, 30 * mm, 30 * mm])
    t_cost.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), NAVY),
        ('BOX', (0,0), (-1,-1), 1, BORDER_COLOR),
        ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('BACKGROUND', (0,13), (-1,13), colors.HexColor("#EAEAEA")),
        ('BACKGROUND', (0,15), (-1,15), colors.HexColor("#DFDFDF")),
        ('BACKGROUND', (0,17), (-1,17), colors.HexColor("#D2D2D2")),
    ]))
    story.append(t_cost)
    story.append(Paragraph("<b>Figure 2:</b> Cost Baseline and Budget Allocation table modeling BAC, Reserves, and $450,000 Institutional Cap (Source: <code>A2_GroupXX_ProjectData.xlsx</code> Tab 3).", caption_style))

    story.append(PageBreak())

    # =========================================================================
    # PAGE 5: 5x5 RISK HEAT MAP & TOP RISKS
    # =========================================================================
    story.append(Paragraph("4. 5×5 Risk Assessment & Heat Map Evidence", sec_title))
    story.append(Paragraph("Risks are evaluated using a 5×5 scoring formula: <b>Score = Likelihood (1–5) × Impact (1–5)</b> (Source: <code>A2_GroupXX_ProjectData.xlsx</code> Tab 4).", body_text))

    # Heat Map Table
    story.append(Paragraph("5×5 Risk Heat Map Matrix", sub_title))
    hmap_data = [
        [Paragraph("Likelihood \\ Impact", tbl_hdr), Paragraph("1 - Insignificant", tbl_hdr), Paragraph("2 - Minor", tbl_hdr), Paragraph("3 - Moderate", tbl_hdr), Paragraph("4 - Major", tbl_hdr), Paragraph("5 - Severe", tbl_hdr)],
        [Paragraph("<b>5 - Almost Certain</b>", tbl_cell), Paragraph("Low (5)", tbl_cell_center), Paragraph("Med (10)", tbl_cell_center), Paragraph("High (15)", tbl_cell_center), Paragraph("Ext (20)", tbl_cell_center), Paragraph("Ext (25)", tbl_cell_center)],
        [Paragraph("<b>4 - Likely</b>", tbl_cell), Paragraph("Low (4)", tbl_cell_center), Paragraph("<b>Med (8): R10</b>", tbl_cell_center), Paragraph("<b>High (12): R03,R05</b>", tbl_cell_center), Paragraph("High (16)", tbl_cell_center), Paragraph("<b>EXT (20): R01</b>", tbl_cell_center_bold)],
        [Paragraph("<b>3 - Possible</b>", tbl_cell), Paragraph("Low (3)", tbl_cell_center), Paragraph("<b>Med (6): R08</b>", tbl_cell_center), Paragraph("<b>Med (9): R07</b>", tbl_cell_center), Paragraph("High (12)", tbl_cell_center), Paragraph("<b>EXT (15): R02</b>", tbl_cell_center_bold)],
        [Paragraph("<b>2 - Unlikely</b>", tbl_cell), Paragraph("Low (2)", tbl_cell_center), Paragraph("Low (4)", tbl_cell_center), Paragraph("Med (6)", tbl_cell_center), Paragraph("<b>Med (8): R06,R09</b>", tbl_cell_center), Paragraph("<b>High (10): R04</b>", tbl_cell_center)],
        [Paragraph("<b>1 - Rare</b>", tbl_cell), Paragraph("Low (1)", tbl_cell_center), Paragraph("Low (2)", tbl_cell_center), Paragraph("Low (3)", tbl_cell_center), Paragraph("Med (4)", tbl_cell_center), Paragraph("Med (5)", tbl_cell_center)]
    ]
    t_hmap = Table(hmap_data, colWidths=[35 * mm, 29 * mm, 29 * mm, 29 * mm, 29 * mm, 29 * mm])
    t_hmap.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), NAVY),
        ('BOX', (0,0), (-1,-1), 1, BORDER_COLOR),
        ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('BACKGROUND', (5,2), (5,2), RED_BG),
        ('BACKGROUND', (5,3), (5,3), RED_BG),
        ('BACKGROUND', (3,2), (3,2), YELLOW_BG),
        ('BACKGROUND', (5,4), (5,4), YELLOW_BG),
    ]))
    story.append(t_hmap)
    story.append(Paragraph("<b>Figure 3:</b> 5×5 Risk Matrix showing technical data migration (R01) and concurrency overload (R02) in the shaded Extreme priority zone.", caption_style))
    story.append(Spacer(1, 3 * mm))

    # Top Risks Table
    story.append(Paragraph("Top Priority Risks & Planned Mitigation Controls", sub_title))
    top_risks = [
        [Paragraph("ID", tbl_hdr), Paragraph("Risk Description", tbl_hdr), Paragraph("L", tbl_hdr), Paragraph("I", tbl_hdr), Paragraph("Score", tbl_hdr), Paragraph("Priority", tbl_hdr), Paragraph("Owner", tbl_hdr), Paragraph("Mitigation & Contingency Strategy", tbl_hdr)],
        [Paragraph("R01", tbl_cell_bold), Paragraph("Legacy database schema mismatch & data corruption during automated ETL.", tbl_cell), Paragraph("4", tbl_cell_center), Paragraph("5", tbl_cell_center), Paragraph("20", tbl_cell_center_bold), Paragraph("Extreme", tbl_cell_center_bold), Paragraph("Momen Ahmed", tbl_cell), Paragraph("Staged sandbox ETL with 10% sampling; checksum validation; instant rollback.", tbl_cell)],
        [Paragraph("R02", tbl_cell_bold), Paragraph("Cloud infrastructure outage during peak enrolment surge (>10,000 users).", tbl_cell), Paragraph("3", tbl_cell_center), Paragraph("5", tbl_cell_center), Paragraph("15", tbl_cell_center_bold), Paragraph("Extreme", tbl_cell_center_bold), Paragraph("Tanvir Ahmed", tbl_cell), Paragraph("AWS Auto-Scaling & Redis caching; stress testing at 250% capacity (15k sessions).", tbl_cell)],
        [Paragraph("R03", tbl_cell_bold), Paragraph("Faculty and administrative staff resistance to adopting new grading interface.", tbl_cell), Paragraph("4", tbl_cell_center), Paragraph("3", tbl_cell_center), Paragraph("12", tbl_cell_center_bold), Paragraph("High", tbl_cell_center_bold), Paragraph("MD Rejvi Jaman", tbl_cell), Paragraph("Appoint 12 departmental 'Change Champions'; 30-min clinics & video guides.", tbl_cell)],
        [Paragraph("R04", tbl_cell_bold), Paragraph("Student PII data breach violating Australian Privacy Principles (APP).", tbl_cell), Paragraph("2", tbl_cell_center), Paragraph("5", tbl_cell_center), Paragraph("10", tbl_cell_center_bold), Paragraph("High", tbl_cell_center_bold), Paragraph("Tanvir Ahmed", tbl_cell), Paragraph("AES-256 encryption; independent CREST penetration testing ($16.5k quote).", tbl_cell)],
        [Paragraph("R05", tbl_cell_bold), Paragraph("Scope creep driven by conflicting inter-faculty customization demands.", tbl_cell), Paragraph("4", tbl_cell_center), Paragraph("3", tbl_cell_center), Paragraph("12", tbl_cell_center_bold), Paragraph("High", tbl_cell_center_bold), Paragraph("Tanvir Ahmed", tbl_cell), Paragraph("Strict CCB review; non-essential enhancements deferred to Phase 2 backlog.", tbl_cell)]
    ]
    t_top_risks = Table(top_risks, colWidths=[10 * mm, 50 * mm, 8 * mm, 8 * mm, 12 * mm, 16 * mm, 26 * mm, 50 * mm])
    t_top_risks.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), NAVY),
        ('BOX', (0,0), (-1,-1), 1, BORDER_COLOR),
        ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('BACKGROUND', (5,1), (5,2), RED_BG),
        ('BACKGROUND', (5,3), (5,5), YELLOW_BG),
    ]))
    story.append(t_top_risks)

    story.append(PageBreak())

    # =========================================================================
    # PAGE 6: STAKEHOLDERS, CHANGE CR-01 & RACI
    # =========================================================================
    story.append(Paragraph("5. Stakeholders, Change Control & RACI Governance", sec_title))

    # Stakeholder Table
    story.append(Paragraph("Stakeholder Power-Interest Classification & Engagement Matrix", sub_title))
    stk_table = [
        [Paragraph("Quadrant", tbl_hdr), Paragraph("Stakeholder Name / Group", tbl_hdr), Paragraph("Power", tbl_hdr), Paragraph("Interest", tbl_hdr), Paragraph("Core Win Condition", tbl_hdr), Paragraph("Engagement Strategy", tbl_hdr)],
        [Paragraph("<b>Manage Closely</b>", tbl_cell_bold), Paragraph("CIO / Project Sponsor (SH01)", tbl_cell), Paragraph("High", tbl_cell_center), Paragraph("High", tbl_cell_center), Paragraph("Budget adherence, zero data leaks", tbl_cell), Paragraph("Weekly 1-on-1 briefings & milestone sign-offs", tbl_cell)],
        [Paragraph("<b>Manage Closely</b>", tbl_cell_bold), Paragraph("University Registrar (SH02)", tbl_cell), Paragraph("High", tbl_cell_center), Paragraph("High", tbl_cell_center), Paragraph("100% record fidelity, seamless enrolment", tbl_cell), Paragraph("Fortnightly steering meetings, UAT validation", tbl_cell)],
        [Paragraph("<b>Manage Closely</b>", tbl_cell_bold), Paragraph("Central IT Security & Ops (SH05)", tbl_cell), Paragraph("High", tbl_cell_center), Paragraph("High", tbl_cell_center), Paragraph("ISO 27001 compliance, AWS stability", tbl_cell), Paragraph("Weekly technical architectural checkpoint", tbl_cell)],
        [Paragraph("<b>Keep Satisfied</b>", tbl_cell_bold), Paragraph("Academic Senate & Deans (SH03)", tbl_cell), Paragraph("High", tbl_cell_center), Paragraph("Low", tbl_cell_center), Paragraph("Teaching continuity, easy mark entry", tbl_cell), Paragraph("Monthly executive digest & faculty demos", tbl_cell)],
        [Paragraph("<b>Keep Satisfied</b>", tbl_cell_bold), Paragraph("TEQSA & Privacy Commissioner (SH08)", tbl_cell), Paragraph("High", tbl_cell_center), Paragraph("Low", tbl_cell_center), Paragraph("Regulatory standards adherence", tbl_cell), Paragraph("Maintain comprehensive DPIA & audit trails", tbl_cell)],
        [Paragraph("<b>Keep Informed</b>", tbl_cell_bold), Paragraph("Student Body & SRC (SH04)", tbl_cell), Paragraph("Low", tbl_cell_center), Paragraph("High", tbl_cell_center), Paragraph("Intuitive mobile UI, fast course cart", tbl_cell), Paragraph("Bi-weekly updates, 50-student focus group", tbl_cell)],
        [Paragraph("<b>Keep Informed</b>", tbl_cell_bold), Paragraph("Helpdesk & Support Staff (SH07)", tbl_cell), Paragraph("Low", tbl_cell_center), Paragraph("High", tbl_cell_center), Paragraph("Fewer tickets, clear triage runbooks", tbl_cell), Paragraph("Hands-on clinics 3 weeks prior to cutover", tbl_cell)]
    ]
    t_stk = Table(stk_table, colWidths=[28 * mm, 45 * mm, 14 * mm, 14 * mm, 38 * mm, 41 * mm])
    t_stk.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), NAVY),
        ('BOX', (0,0), (-1,-1), 1, BORDER_COLOR),
        ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_stk)
    story.append(Spacer(1, 3 * mm))

    # CR-01 Table
    story.append(Paragraph("Formal Change Request Log: Change Request CR-01", sub_title))
    cr_data = [
        [Paragraph("Title / ID:", tbl_cell_bold), Paragraph("<b>CR-01: Mandatory Multi-Factor Authentication (MFA) Integration</b>", tbl_cell)],
        [Paragraph("Origin / Reason:", tbl_cell_bold), Paragraph("University Cybersecurity Board mandate to meet ACSC Essential Eight standards.", tbl_cell)],
        [Paragraph("Scope Impact:", tbl_cell_bold), Paragraph("Added Twilio SMS microservice, Authenticator app TOTP hooks, secure device cookies.", tbl_cell)],
        [Paragraph("Schedule Impact:", tbl_cell_bold), Paragraph("+8 working days. Absorbed via fast-tracking UI testing with Sprint 2 (Zero go-live slip).", tbl_cell)],
        [Paragraph("Cost Impact:", tbl_cell_bold), Paragraph("<b>+$14,500 AUD</b>, funded 100% via the $38,500 Contingency Reserve (BAC unaffected).", tbl_cell)],
        [Paragraph("CCB Decision:", tbl_cell_bold), Paragraph("<b>APPROVED</b> by Project Sponsor (CIO) on 18-Apr-2026 for Sprint 3 implementation.", tbl_cell)]
    ]
    t_cr = Table(cr_data, colWidths=[35 * mm, 145 * mm])
    t_cr.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), LIGHT_BG),
        ('BOX', (0,0), (-1,-1), 1, BORDER_COLOR),
        ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_cr)
    story.append(Spacer(1, 3 * mm))

    # RACI Table
    story.append(Paragraph("RACI Responsibility Assignment Matrix", sub_title))
    raci_data = [
        [Paragraph("Phase", tbl_hdr), Paragraph("Sponsor", tbl_hdr), Paragraph("PM", tbl_hdr), Paragraph("Architect", tbl_hdr), Paragraph("Dev Team", tbl_hdr), Paragraph("DB Lead", tbl_hdr), Paragraph("QA Lead", tbl_hdr), Paragraph("Change", tbl_hdr)],
        [Paragraph("1.0 Initiation", tbl_cell_bold), Paragraph("A", tbl_cell_center_bold), Paragraph("R", tbl_cell_center_bold), Paragraph("C", tbl_cell_center), Paragraph("I", tbl_cell_center), Paragraph("I", tbl_cell_center), Paragraph("I", tbl_cell_center), Paragraph("C", tbl_cell_center)],
        [Paragraph("2.0 Requirements", tbl_cell_bold), Paragraph("I", tbl_cell_center), Paragraph("A", tbl_cell_center_bold), Paragraph("R", tbl_cell_center_bold), Paragraph("C", tbl_cell_center), Paragraph("C", tbl_cell_center), Paragraph("C", tbl_cell_center), Paragraph("C", tbl_cell_center)],
        [Paragraph("3.0 Data Migration", tbl_cell_bold), Paragraph("I", tbl_cell_center), Paragraph("A", tbl_cell_center_bold), Paragraph("C", tbl_cell_center), Paragraph("C", tbl_cell_center), Paragraph("R", tbl_cell_center_bold), Paragraph("C", tbl_cell_center), Paragraph("I", tbl_cell_center)],
        [Paragraph("4.0 Core Portal Dev", tbl_cell_bold), Paragraph("I", tbl_cell_center), Paragraph("A", tbl_cell_center_bold), Paragraph("C", tbl_cell_center), Paragraph("R", tbl_cell_center_bold), Paragraph("C", tbl_cell_center), Paragraph("C", tbl_cell_center), Paragraph("I", tbl_cell_center)],
        [Paragraph("5.0 QA & Pilot", tbl_cell_bold), Paragraph("I", tbl_cell_center), Paragraph("A", tbl_cell_center_bold), Paragraph("C", tbl_cell_center), Paragraph("C", tbl_cell_center), Paragraph("C", tbl_cell_center), Paragraph("R", tbl_cell_center_bold), Paragraph("C", tbl_cell_center)],
        [Paragraph("6.0 Cutover & Closure", tbl_cell_bold), Paragraph("A", tbl_cell_center_bold), Paragraph("R", tbl_cell_center_bold), Paragraph("C", tbl_cell_center), Paragraph("C", tbl_cell_center), Paragraph("C", tbl_cell_center), Paragraph("C", tbl_cell_center), Paragraph("R", tbl_cell_center_bold)]
    ]
    t_raci = Table(raci_data, colWidths=[40 * mm, 20 * mm, 20 * mm, 20 * mm, 20 * mm, 20 * mm, 20 * mm, 20 * mm])
    t_raci.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), NAVY),
        ('BOX', (0,0), (-1,-1), 1, BORDER_COLOR),
        ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
    ]))
    story.append(t_raci)

    story.append(PageBreak())

    # =========================================================================
    # PAGE 7: EVM DASHBOARD & TRACKING
    # =========================================================================
    story.append(Paragraph("6. Project Tracking & EVM Dashboard Evidence", sec_title))
    story.append(Paragraph("Mid-project tracking combines <b>Trello Kanban</b> sprint cards with <b>Earned Value Management (EVM)</b> in Excel to monitor velocity against baseline (Source: <code>A2_GroupXX_ProjectData.xlsx</code> Tab 7).", body_text))
    story.append(Paragraph("<b>Live Public Trello Board:</b> <font color='#0066CC'><u>https://trello.com/b/6aba6567933223c336fb8dfc/</u></font>", body_text))

    # EVM KPIs
    story.append(Paragraph("Earned Value Performance Metrics at Week 14 Review (Data Date: 08-May-2026)", sub_title))
    evm_summary = [
        [Paragraph("Planned Value (PV)", tbl_hdr), Paragraph("Earned Value (EV)", tbl_hdr), Paragraph("Actual Cost (AC)", tbl_hdr), Paragraph("Schedule Var (SV)", tbl_hdr), Paragraph("Cost Var (CV)", tbl_hdr), Paragraph("SPI (EV/PV)", tbl_hdr), Paragraph("CPI (EV/AC)", tbl_hdr)],
        [Paragraph("$225,000", tbl_cell_center_bold), Paragraph("$198,000", tbl_cell_center_bold), Paragraph("$210,000", tbl_cell_center_bold), Paragraph("-$27,000", tbl_cell_center_bold), Paragraph("-$12,000", tbl_cell_center_bold), Paragraph("0.880", tbl_cell_center_bold), Paragraph("0.943", tbl_cell_center_bold)]
    ]
    t_evm = Table(evm_summary, colWidths=[26 * mm, 26 * mm, 26 * mm, 26 * mm, 26 * mm, 25 * mm, 25 * mm])
    t_evm.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), NAVY),
        ('BOX', (0,0), (-1,-1), 1, BORDER_COLOR),
        ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('BACKGROUND', (0,1), (-1,1), LIGHT_BG),
    ]))
    story.append(t_evm)
    story.append(Spacer(1, 4 * mm))

    # Variance Analysis Table
    story.append(Paragraph("Variance Diagnosis & Corrective Management Intervention", sub_title))
    var_detail = [
        [Paragraph("Performance Dimension", tbl_hdr), Paragraph("Diagnostic Finding & Empirical Evidence", tbl_hdr), Paragraph("Corrective Management Action Taken", tbl_hdr)],
        [
            Paragraph("<b>Schedule Delay (SPI = 0.880)</b>", tbl_cell_bold),
            Paragraph("At Week 14, EV ($198k) lagged PV ($225k) by -$27k (10 working days behind on Critical Path task 3.2: Automated ETL Scripts). Root cause: 14 unindexed tables in legacy Banner caused script timeouts.", tbl_cell),
            Paragraph("<b>Schedule Crashing:</b> Released $6,800 from Contingency Reserve to contract an external Senior ETL Engineer for 2 weeks to run SQL optimizations in parallel, recovering 7 days by Week 16.", tbl_cell)
        ],
        [
            Paragraph("<b>Cost Variance (CPI = 0.943)</b>", tbl_cell_bold),
            Paragraph("AC ($210k) exceeded EV ($198k) by -$12k due to unplanned senior database contractor hours required to resolve schema normalization.", tbl_cell),
            Paragraph("<b>Contingency Absorption:</b> Absorbed via pre-allocated $38.5k technical contingency. Projected EAC ($406.3k) remains well below the $450k budget ceiling.", tbl_cell)
        ],
        [
            Paragraph("<b>Workflow Linkage (Trello)</b>", tbl_cell_bold),
            Paragraph("Card [WBS 3.2] stalled in 'In Progress' for 8 days, exceeding WIP limits and triggering daily standup escalation.", tbl_cell),
            Paragraph("<b>Fast-Tracking:</b> Decoupled Sprint 3 course enrolment frontend, developing UI screens against mock endpoints while ETL was resolved.", tbl_cell)
        ]
    ]
    t_var = Table(var_detail, colWidths=[38 * mm, 71 * mm, 71 * mm])
    t_var.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), NAVY),
        ('BOX', (0,0), (-1,-1), 1, BORDER_COLOR),
        ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_var)

    story.append(PageBreak())

    # =========================================================================
    # PAGE 8: ACADEMIC INTEGRITY & DECLARATION
    # =========================================================================
    story.append(Paragraph("7. Academic Integrity & No-AI Declaration", sec_title))

    decl_text = """
    We, the undersigned group members for Project OmniPortal (Scenario C), hereby certify and declare under academic integrity guidelines:
    <br/><br/>
    1. <b>Secure Lane Compliance:</b> This submission conforms strictly to the Secure Lane — No Generative AI policy set by the Australian Institute of Higher Education.
    <br/>
    2. <b>Original Intellectual Effort:</b> The final live project website (<code>https://sadiksk07.github.io/omniportal-bisy2004/</code>), all written analytical interpretations, cost models, schedules, diagrams, and management recommendations represent our group's own authentic intellectual effort.
    <br/>
    3. <b>Approved Software Operation:</b> All primary project management outputs have been created manually through direct operation of the approved tools: ProjectLibre Desktop (v1.9+), Microsoft Excel 365, diagrams.net, and Trello.
    <br/>
    4. <b>Individual Mastery & Viva Readiness:</b> Every group member has actively contributed to and comprehends the end-to-end project evidence, and is fully equipped to defend our methodologies, trade-offs, and critical path reasoning during the individual viva.
    """
    story.append(Paragraph(decl_text, body_text))
    story.append(Spacer(1, 8 * mm))

    # Signature Table
    sig_data = [
        [Paragraph("Student Full Name", tbl_hdr), Paragraph("Student ID", tbl_hdr), Paragraph("Assigned Project Role", tbl_hdr), Paragraph("Attested Signature", tbl_hdr), Paragraph("Date", tbl_hdr)],
        [Paragraph("<b>Tanvir Ahmed</b>", tbl_cell), Paragraph("238983", tbl_cell_center_bold), Paragraph("Project Lead & Systems Architect", tbl_cell), Paragraph("<i>Tanvir Ahmed</i>", tbl_cell_center_bold), Paragraph("28 / 09 / 2026", tbl_cell_center)],
        [Paragraph("<b>Momen Ahmed</b>", tbl_cell), Paragraph("242048", tbl_cell_center_bold), Paragraph("Risk, Finance & Governance Lead", tbl_cell), Paragraph("<i>Momen Ahmed</i>", tbl_cell_center_bold), Paragraph("28 / 09 / 2026", tbl_cell_center)],
        [Paragraph("<b>MD Rejvi Jaman Mafti</b>", tbl_cell), Paragraph("241964", tbl_cell_center_bold), Paragraph("Quality, Delivery & Tracking Lead", tbl_cell), Paragraph("<i>M.R.J. Mafti</i>", tbl_cell_center_bold), Paragraph("28 / 09 / 2026", tbl_cell_center)]
    ]
    t_sig = Table(sig_data, colWidths=[40 * mm, 24 * mm, 52 * mm, 36 * mm, 28 * mm])
    t_sig.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), NAVY),
        ('BOX', (0,0), (-1,-1), 1, BORDER_COLOR),
        ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_sig)
    story.append(Spacer(1, 8 * mm))

    # References
    story.append(Paragraph("8. References (APA 7th Edition)", sec_title))
    refs = [
        "Australian Cyber Security Centre. (2023). <i>Essential Eight maturity model</i>. Australian Signals Directorate. https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/essential-eight/essential-eight-maturity-model",
        "Office of the Australian Information Commissioner. (2022). <i>Australian Privacy Principles guidelines: Privacy Act 1988</i>. OAIC. https://www.oaic.gov.au/privacy/australian-privacy-principles-guidelines",
        "Project Management Institute. (2021). <i>A guide to the project management body of knowledge (PMBOK guide)</i> (7th ed.). Project Management Institute.",
        "Tertiary Education Quality and Standards Agency. (2021). <i>Higher education standards framework (Threshold Standards) 2021</i>. Australian Government. https://www.teqsa.gov.au/",
        "Web Accessibility Initiative. (2018). <i>Web content accessibility guidelines (WCAG) 2.1</i>. World Wide Web Consortium (W3C). https://www.w3.org/TR/WCAG21/"
    ]
    for r in refs:
        story.append(Paragraph(f"• {r}", ParagraphStyle('Ref', parent=body_text, leftIndent=15, firstLineIndent=-15, spaceAfter=4)))

    doc.build(story)
    print(f"Successfully generated {pdf_filename} ({os.path.getsize(pdf_filename)} bytes)")

if __name__ == "__main__":
    generate_pdf()
