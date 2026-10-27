"""
Generate a professional, publication-grade PowerPoint Presentation for CognitivePulse AI.
Aspect Ratio: 16:9 Widescreen (13.333 x 7.5 inches)
Theme: Obsidian / Deep Slate with Electric Indigo & Cyan Accents
Note: Pure slide content only — zero speaker notes / speaker scripts.
"""

import os
import shutil
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

# --- COLOR PALETTE DEFINITIONS ---
BG_DARK = RGBColor(11, 15, 25)         # #0B0F19 - Deep Obsidian
CARD_BG = RGBColor(23, 31, 51)         # #171F33 - Dark Slate Card
CARD_BORDER = RGBColor(45, 55, 72)     # #2D3748 - Border
TEXT_WHITE = RGBColor(248, 250, 252)   # #F8FAFC - Primary Text
TEXT_MUTED = RGBColor(148, 163, 184)   # #94A3B8 - Secondary Muted Text
ACCENT_INDIGO = RGBColor(99, 102, 241) # #6366F1 - Electric Indigo
ACCENT_CYAN = RGBColor(6, 182, 212)    # #06B6D4 - Cyber Cyan
ACCENT_EMERALD = RGBColor(16, 185, 129)# #10B981 - Success Emerald
ACCENT_AMBER = RGBColor(245, 158, 11)  # #F59E0B - Warning Amber
ACCENT_ROSE = RGBColor(244, 63, 94)    # #F43F5E - Crimson Rose
TABLE_HEADER_BG = RGBColor(30, 41, 59) # #1E293B
TABLE_ROW_ALT = RGBColor(17, 24, 39)   # #111827

def apply_background(slide, prs):
    """Draw full-bleed dark obsidian background."""
    bg = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), prs.slide_width, prs.slide_height
    )
    bg.fill.solid()
    bg.fill.fore_color.rgb = BG_DARK
    bg.line.fill.background()
    return bg

def add_header(slide, category: str, title: str, subtitle: str = ""):
    """Standardized slide header with category tag and title."""
    header_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(1.1))
    tf = header_box.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

    p_cat = tf.paragraphs[0]
    p_cat.text = category.upper()
    p_cat.font.name = "Calibri"
    p_cat.font.size = Pt(10)
    p_cat.font.bold = True
    p_cat.font.color.rgb = ACCENT_CYAN
    p_cat.space_after = Pt(2)

    p_title = tf.add_paragraph()
    p_title.text = title
    p_title.font.name = "Calibri"
    p_title.font.size = Pt(22)
    p_title.font.bold = True
    p_title.font.color.rgb = TEXT_WHITE
    
    if subtitle:
        p_title.space_after = Pt(2)
        p_sub = tf.add_paragraph()
        p_sub.text = subtitle
        p_sub.font.name = "Calibri"
        p_sub.font.size = Pt(11)
        p_sub.font.color.rgb = TEXT_MUTED

def add_card(slide, left, top, width, height, title="", border_color=CARD_BORDER, bg_color=CARD_BG):
    """Draws a card shape container for modular visual layouts."""
    card = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(height)
    )
    card.fill.solid()
    card.fill.fore_color.rgb = bg_color
    card.line.color.rgb = border_color
    card.line.width = Pt(1)

    if title:
        tb = slide.shapes.add_textbox(Inches(left + 0.2), Inches(top + 0.15), Inches(width - 0.4), Inches(0.45))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        p = tf.paragraphs[0]
        p.text = title
        p.font.name = "Calibri"
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = ACCENT_INDIGO
    return card

def add_bullet_points(tf, points, default_size=11, space_after=6, text_color=TEXT_WHITE):
    """Populates text frame with clean bullet points."""
    first = True
    for pt in points:
        p = tf.paragraphs[0] if first else tf.add_paragraph()
        first = False
        p.space_after = Pt(space_after)
        p.font.name = "Calibri"
        p.font.size = Pt(default_size)
        
        if isinstance(pt, tuple):
            prefix, body = pt
            r1 = p.add_run()
            r1.text = prefix + " "
            r1.font.bold = True
            r1.font.color.rgb = ACCENT_CYAN
            r2 = p.add_run()
            r2.text = body
            r2.font.color.rgb = text_color
        else:
            r = p.add_run()
            r.text = pt
            r.font.color.rgb = text_color

def build_presentation(output_path: str):
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # =========================================================================
    # SLIDE 1: TITLE SLIDE
    # =========================================================================
    slide1 = prs.slides.add_slide(blank_layout)
    apply_background(slide1, prs)

    bar = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.2), Inches(1.6), Inches(0.12), Inches(4.2))
    bar.fill.solid()
    bar.fill.fore_color.rgb = ACCENT_INDIGO
    bar.line.fill.background()

    tb1 = slide1.shapes.add_textbox(Inches(1.5), Inches(1.5), Inches(10.5), Inches(4.5))
    tf1 = tb1.text_frame
    tf1.word_wrap = True

    p0 = tf1.paragraphs[0]
    p0.text = "RESEARCH & ENGINEERING PRESENTATION"
    p0.font.name = "Calibri"
    p0.font.size = Pt(12)
    p0.font.bold = True
    p0.font.color.rgb = ACCENT_CYAN
    p0.space_after = Pt(12)

    p1 = tf1.add_paragraph()
    p1.text = "AI BASED AUTOMATIC QUESTION PAPER DIFFICULTY ANALYZER"
    p1.font.name = "Calibri"
    p1.font.size = Pt(32)
    p1.font.bold = True
    p1.font.color.rgb = TEXT_WHITE
    p1.space_after = Pt(8)

    p2 = tf1.add_paragraph()
    p2.text = "Automatic Question Paper Difficulty & Cognitive Demand Evaluation\nvia Revised Bloom's Taxonomy and Dual-Task NLP"
    p2.font.name = "Calibri"
    p2.font.size = Pt(18)
    p2.font.color.rgb = ACCENT_INDIGO
    p2.space_after = Pt(28)

    p3 = tf1.add_paragraph()
    p3.text = "Production Architecture  |  Zero-Leakage ML Pipeline  |  Accreditation Ready  |  Human-in-the-Loop"
    p3.font.name = "Calibri"
    p3.font.size = Pt(12)
    p3.font.color.rgb = TEXT_MUTED

    # =========================================================================
    # SLIDE 2: THE PROBLEM & THE CONFLATION FALLACY
    # =========================================================================
    slide2 = prs.slides.add_slide(blank_layout)
    apply_background(slide2, prs)
    add_header(slide2, "Context & Problem Definition", "The Core Problem: Subjectivity & The Conflation Fallacy", 
               "Why traditional institutional moderation fails and why existing automated tools produce skewed audits.")

    add_card(slide2, 0.8, 1.8, 3.6, 5.0, "1. Manual Moderation Bottleneck")
    tb2a = slide2.shapes.add_textbox(Inches(1.0), Inches(2.4), Inches(3.2), Inches(4.2))
    tf2a = tb2a.text_frame
    tf2a.word_wrap = True
    add_bullet_points(tf2a, [
        ("High Subjectivity:", "Inter-rater reliability among faculty moderators averages below 60% on cognitive depth."),
        ("Labor-Intensive:", "Evaluating hundreds of university papers against ABET/NBA accreditation guidelines takes weeks."),
        ("Late Detection:", "Imbalanced exam papers are often discovered post-exam after high student failure rates occur.")
    ])

    add_card(slide2, 4.8, 1.8, 3.6, 5.0, "2. The 'Conflation Fallacy'", border_color=ACCENT_ROSE)
    tb2b = slide2.shapes.add_textbox(Inches(5.0), Inches(2.4), Inches(3.2), Inches(4.2))
    tf2b = tb2b.text_frame
    tf2b.word_wrap = True
    add_bullet_points(tf2b, [
        ("Fatal Assumption:", "Existing EdTech systems treat Cognitive Demand and Question Difficulty as interchangeable."),
        ("The Reality:", "Bloom's Level = Mental operation elicited. Difficulty = Expected student error probability."),
        ("Distortion:", "Treating them as identical invalidates institutional syllabus balance and accreditation outcomes.")
    ])

    add_card(slide2, 8.8, 1.8, 3.7, 5.0, "3. Concrete Real-World Evidence")
    tb2c = slide2.shapes.add_textbox(Inches(9.0), Inches(2.4), Inches(3.3), Inches(4.2))
    tf2c = tb2c.text_frame
    tf2c.word_wrap = True
    add_bullet_points(tf2c, [
        ("High Demand, Low Difficulty:", "'Design a relational schema for a simple 3-entity library.' Cognitive Level: CREATE (Level 6), but empirically EASY for 3rd year CS."),
        ("Low Demand, High Difficulty:", "'State the IEEE 754-2008 exact bit precision for subnormal floats.' Cognitive Level: REMEMBER (Level 1), but empirically HARD.")
    ])

    # =========================================================================
    # SLIDE 3: THEORETICAL FRAMEWORK
    # =========================================================================
    slide3 = prs.slides.add_slide(blank_layout)
    apply_background(slide3, prs)
    add_header(slide3, "Theoretical Foundations", "Dual-Task Formulation: Bloom's Taxonomy & Difficulty Tiers",
               "Grounding in Anderson & Krathwohl's (2001) Revised Taxonomy alongside empirical difficulty scaling.")

    add_card(slide3, 0.8, 1.8, 6.8, 5.0, "Task A: Revised Bloom's Taxonomy (6 Cognitive Processes)")
    tb3a = slide3.shapes.add_textbox(Inches(1.0), Inches(2.4), Inches(6.4), Inches(4.2))
    tf3a = tb3a.text_frame
    tf3a.word_wrap = True
    add_bullet_points(tf3a, [
        ("1. Remember:", "Retrieving knowledge from long-term memory (Define, List, Recall, State)."),
        ("2. Understand:", "Constructing meaning from instructional messages (Explain, Summarize, Interpret)."),
        ("3. Apply:", "Executing or carrying out a procedure in a given scenario (Calculate, Solve, Execute)."),
        ("4. Analyze:", "Deconstructing material into constituent parts & relationships (Differentiate, Deconstruct)."),
        ("5. Evaluate:", "Making critical judgments based on criteria and standards (Critique, Justify, Defend)."),
        ("6. Create:", "Putting elements together to form a novel coherent structure (Design, Synthesize, Formulate).")
    ], default_size=10, space_after=4)

    add_card(slide3, 8.0, 1.8, 4.5, 5.0, "Task B: Question Difficulty Tiers")
    tb3b = slide3.shapes.add_textbox(Inches(8.2), Inches(2.4), Inches(4.1), Inches(4.2))
    tf3b = tb3b.text_frame
    tf3b.word_wrap = True
    add_bullet_points(tf3b, [
        ("Easy Tier:", "Direct single-step reasoning, straightforward recall or fundamental concepts. High success probability across cohort (>75%)."),
        ("Medium Tier:", "Multi-concept synthesis, standard multi-step algorithmic derivation or domain application. Average cohort success (40-75%)."),
        ("Hard Tier:", "Non-trivial edge cases, complex analytical decomposition, cross-disciplinary integration. Low cohort success (<40%)."),
        ("Formal Decoupling:", "Dual Targets: y_bloom in {1..6}, y_diff in {Easy, Medium, Hard}. Formulated as independent classification spaces.")
    ], default_size=10, space_after=6)

    # =========================================================================
    # SLIDE 4: SYSTEM ARCHITECTURE
    # =========================================================================
    slide4 = prs.slides.add_slide(blank_layout)
    apply_background(slide4, prs)
    add_header(slide4, "Full-Stack System Architecture", "End-to-End Modular Engineering Flow",
               "From digital examination ingestion (PDF/DOCX) to ML inference, HITL review, and institutional accreditation.")

    col_w = 2.7
    gap = 0.3
    
    add_card(slide4, 0.8, 1.8, col_w, 5.0, "1. Ingestion & Parsing")
    tb4a = slide4.shapes.add_textbox(Inches(0.95), Inches(2.4), Inches(col_w - 0.3), Inches(4.2))
    tf4a = tb4a.text_frame
    tf4a.word_wrap = True
    add_bullet_points(tf4a, [
        ("PDF Extraction:", "High-fidelity text flow via PyMuPDF (fitz)."),
        ("DOCX Parsing:", "Structure-aware python-docx reader."),
        ("Segmentation:", "Intelligent regex detecting Q1(a), section blocks, and optional choices."),
        ("Score Extraction:", "Preserves allocated marks while separating them from prompt text.")
    ], default_size=9.5, space_after=5)

    add_card(slide4, 0.8 + (col_w + gap), 1.8, col_w, 5.0, "2. Sanitization & ML")
    tb4b = slide4.shapes.add_textbox(Inches(0.95 + (col_w + gap)), Inches(2.4), Inches(col_w - 0.3), Inches(4.2))
    tf4b = tb4b.text_frame
    tf4b.word_wrap = True
    add_bullet_points(tf4b, [
        ("Zero-Leakage Filter:", "Strips marks, labels, and question numbers before inference."),
        ("Feature Engineering:", "Sublinear TF-IDF + Readability + POS metrics."),
        ("Task A Classifier:", "Bloom's 6-Class Champion (LogReg / Linear SVM)."),
        ("Task B Classifier:", "Difficulty 3-Tier Champion (LogReg / Linear SVM).")
    ], default_size=9.5, space_after=5)

    add_card(slide4, 0.8 + 2 * (col_w + gap), 1.8, col_w, 5.0, "3. HITL Faculty Review", border_color=ACCENT_CYAN)
    tb4c = slide4.shapes.add_textbox(Inches(0.95 + 2 * (col_w + gap)), Inches(2.4), Inches(col_w - 0.3), Inches(4.2))
    tf4c = tb4c.text_frame
    tf4c.word_wrap = True
    add_bullet_points(tf4c, [
        ("Interactive UI:", "Next.js 16 + React 19 glassmorphic dashboard."),
        ("Calibrated Confidence:", "Displays model confidence probabilities."),
        ("Teacher Overrides:", "Educators can adjust predictions with logged rationale."),
        ("Audit Trails:", "Relational tracking of original vs revised labels.")
    ], default_size=9.5, space_after=5)

    add_card(slide4, 0.8 + 3 * (col_w + gap), 1.8, col_w, 5.0, "4. Accreditation Audit")
    tb4d = slide4.shapes.add_textbox(Inches(0.95 + 3 * (col_w + gap)), Inches(2.4), Inches(col_w - 0.3), Inches(4.2))
    tf4d = tb4d.text_frame
    tf4d.word_wrap = True
    add_bullet_points(tf4d, [
        ("Cognitive Balance:", "Automated calculation of Bloom Distribution Index."),
        ("PDF ReportLab:", "Institutional PDF with charts, breakdowns & signatures."),
        ("Streaming CSV:", "Machine-readable export for external ERP / LMS integration."),
        ("Accreditation:", "Directly maps to ABET & NBA Criterion 3 outcomes.")
    ], default_size=9.5, space_after=5)

    # =========================================================================
    # SLIDE 5: DATA ENGINEERING & ZERO-LEAKAGE PIPELINE
    # =========================================================================
    slide5 = prs.slides.add_slide(blank_layout)
    apply_background(slide5, prs)
    add_header(slide5, "Data Engineering & Methodological Rigor", "Preventing Shortcut Learning & Label Leakage",
               "How dataset sanitization ensures models learn true semantic constructs rather than typographical cues.")

    add_card(slide5, 0.8, 1.8, 5.6, 5.0, "The Risk of Spurious Correlation")
    tb5a = slide5.shapes.add_textbox(Inches(1.0), Inches(2.4), Inches(5.2), Inches(4.2))
    tf5a = tb5a.text_frame
    tf5a.word_wrap = True
    add_bullet_points(tf5a, [
        ("The 'Marks' Leakage Trap:", "If an NLP model sees '[15 Marks]', it trivially classifies the question as 'Hard' or 'Evaluate' without understanding linguistic complexity."),
        ("The 'Numbering' Cue:", "Questions labeled 'Q1(a)' are statistically more likely to be definitions ('Remember') in typical university syllabi."),
        ("Prior Literature Flaw:", "Many published papers achieve false 98%+ accuracy simply because models memorized bracketed marks and numbering formatting.")
    ], default_size=10, space_after=6)

    add_card(slide5, 6.8, 1.8, 5.7, 5.0, "Our Zero-Leakage Pipeline")
    tb5b = slide5.shapes.add_textbox(Inches(7.0), Inches(2.4), Inches(5.3), Inches(4.2))
    tf5b = tb5b.text_frame
    tf5b.word_wrap = True
    add_bullet_points(tf5b, [
        ("Regex Metadata Cleansing:", "All mark notations (e.g., '[10 pts]', '(5 marks)', 'CO3') and question indices ('Q. 2b.') are parsed into relational metadata and purged from model input."),
        ("Text Normalization:", "Contraction expansion, ASCII standardization, and whitespace normalization applied uniformly across training and inference."),
        ("Stratified Split (70 / 15 / 15):", "Multi-label iterative stratification preserves exact class balance across Train, Validation, and Held-Out Test sets without prompt leakage."),
        ("Audited Baseline Integrity:", "Models are strictly evaluated on held-out test prompts containing solely semantic text.")
    ], default_size=10, space_after=5)

    # =========================================================================
    # SLIDE 6: MODEL COMPARISON & BENCHMARKS
    # =========================================================================
    slide6 = prs.slides.add_slide(blank_layout)
    apply_background(slide6, prs)
    add_header(slide6, "Experimental Results: Task A & Task B", "Model Benchmarks on Held-Out Test Sets",
               "Rigorous empirical evaluation comparing Rule-Based Heuristics, Naive Bayes, Linear SVM, and Logistic Regression.")

    add_card(slide6, 0.8, 1.8, 5.7, 5.0, "Task A: Bloom's Taxonomy (6 Classes)")
    
    table_shape_a = slide6.shapes.add_table(5, 4, Inches(1.0), Inches(2.3), Inches(5.3), Inches(1.8))
    t_a = table_shape_a.table
    t_a.columns[0].width = Inches(2.4)
    t_a.columns[1].width = Inches(1.0)
    t_a.columns[2].width = Inches(1.0)
    t_a.columns[3].width = Inches(0.9)

    headers_a = ["Model Architecture", "Val Acc", "Test Acc", "Test F1"]
    for i, h in enumerate(headers_a):
        cell = t_a.cell(0, i)
        cell.fill.solid()
        cell.fill.fore_color.rgb = TABLE_HEADER_BG
        p = cell.text_frame.paragraphs[0]
        p.text = h
        p.font.name = "Calibri"
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = ACCENT_CYAN
        p.alignment = PP_ALIGN.CENTER if i > 0 else PP_ALIGN.LEFT

    rows_a = [
        ("Action Verb Heuristic", "96.47%", "88.37%", "88.52%"),
        ("TF-IDF + Naive Bayes", "90.59%", "86.05%", "85.98%"),
        ("Linear SVM", "95.29%", "90.70%", "90.81%"),
        ("TF-IDF + LogReg (Champ)", "96.47%", "91.86%", "91.93%")
    ]
    for row_idx, data in enumerate(rows_a, start=1):
        for col_idx, val in enumerate(data):
            cell = t_a.cell(row_idx, col_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = TABLE_ROW_ALT if row_idx % 2 == 0 else CARD_BG
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.name = "Calibri"
            p.font.size = Pt(9)
            p.font.color.rgb = ACCENT_EMERALD if "Champ" in data[0] and col_idx >= 2 else TEXT_WHITE
            p.alignment = PP_ALIGN.CENTER if col_idx > 0 else PP_ALIGN.LEFT

    tb6_sub_a = slide6.shapes.add_textbox(Inches(1.0), Inches(4.3), Inches(5.3), Inches(2.3))
    tf6_sub_a = tb6_sub_a.text_frame
    tf6_sub_a.word_wrap = True
    add_bullet_points(tf6_sub_a, [
        ("Champion Model:", "TF-IDF + Logistic Regression achieves 91.93% Test Macro-F1 across all 6 cognitive levels."),
        ("Superior Generalization:", "Maintains over 91.8% accuracy on unseen examination domains without overfitting.")
    ], default_size=9.5, space_after=4)

    add_card(slide6, 6.8, 1.8, 5.7, 5.0, "Task B: Difficulty Level (3 Classes)")
    table_shape_b = slide6.shapes.add_table(4, 4, Inches(7.0), Inches(2.3), Inches(5.3), Inches(1.5))
    t_b = table_shape_b.table
    t_b.columns[0].width = Inches(2.4)
    t_b.columns[1].width = Inches(1.0)
    t_b.columns[2].width = Inches(1.0)
    t_b.columns[3].width = Inches(0.9)

    headers_b = ["Model Architecture", "Val Acc", "Test Acc", "Test F1"]
    for i, h in enumerate(headers_b):
        cell = t_b.cell(0, i)
        cell.fill.solid()
        cell.fill.fore_color.rgb = TABLE_HEADER_BG
        p = cell.text_frame.paragraphs[0]
        p.text = h
        p.font.name = "Calibri"
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = ACCENT_CYAN
        p.alignment = PP_ALIGN.CENTER if i > 0 else PP_ALIGN.LEFT

    rows_b = [
        ("TF-IDF + Naive Bayes", "88.24%", "89.53%", "89.60%"),
        ("Linear SVM", "94.12%", "94.19%", "94.35%"),
        ("TF-IDF + LogReg (Champ)", "97.65%", "95.35%", "95.56%")
    ]
    for row_idx, data in enumerate(rows_b, start=1):
        for col_idx, val in enumerate(data):
            cell = t_b.cell(row_idx, col_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = TABLE_ROW_ALT if row_idx % 2 == 0 else CARD_BG
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.name = "Calibri"
            p.font.size = Pt(9)
            p.font.color.rgb = ACCENT_EMERALD if "Champ" in data[0] and col_idx >= 2 else TEXT_WHITE
            p.alignment = PP_ALIGN.CENTER if col_idx > 0 else PP_ALIGN.LEFT

    tb6_sub_b = slide6.shapes.add_textbox(Inches(7.0), Inches(4.3), Inches(5.3), Inches(2.3))
    tf6_sub_b = tb6_sub_b.text_frame
    tf6_sub_b.word_wrap = True
    add_bullet_points(tf6_sub_b, [
        ("Outstanding Difficulty Prediction:", "95.56% Test Macro-F1 across Easy, Medium, and Hard tiers."),
        ("Balanced Support:", "High precision across both boundary tiers: 0.964 on Easy and 0.966 on Hard.")
    ], default_size=9.5, space_after=4)

    # =========================================================================
    # SLIDE 7: CLASS-WISE BREAKDOWN
    # =========================================================================
    slide7 = prs.slides.add_slide(blank_layout)
    apply_background(slide7, prs)
    add_header(slide7, "Detailed Model Breakdown", "Task A & B: Class-Wise Performance Metrics",
               "Evaluating precision, recall, and F1-score across all individual cognitive levels and difficulty tiers.")

    add_card(slide7, 0.8, 1.8, 7.2, 5.0, "Bloom's Taxonomy Class-Wise Test Evaluation (Champion)")
    table_shape_c = slide7.shapes.add_table(8, 5, Inches(1.0), Inches(2.3), Inches(6.8), Inches(2.6))
    t_c = table_shape_c.table
    t_c.columns[0].width = Inches(2.0)
    t_c.columns[1].width = Inches(1.2)
    t_c.columns[2].width = Inches(1.2)
    t_c.columns[3].width = Inches(1.2)
    t_c.columns[4].width = Inches(1.2)

    headers_c = ["Cognitive Level", "Precision", "Recall", "F1-Score", "Support"]
    for i, h in enumerate(headers_c):
        cell = t_c.cell(0, i)
        cell.fill.solid()
        cell.fill.fore_color.rgb = TABLE_HEADER_BG
        p = cell.text_frame.paragraphs[0]
        p.text = h
        p.font.name = "Calibri"
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = ACCENT_CYAN
        p.alignment = PP_ALIGN.CENTER if i > 0 else PP_ALIGN.LEFT

    rows_c = [
        ("1. Remember", "1.0000", "1.0000", "1.0000", "14"),
        ("2. Understand", "0.8125", "0.8667", "0.8387", "15"),
        ("3. Apply", "1.0000", "0.7692", "0.8696", "13"),
        ("4. Analyze", "1.0000", "0.9231", "0.9600", "13"),
        ("5. Evaluate", "0.8947", "1.0000", "0.9444", "17"),
        ("6. Create", "0.8750", "0.9333", "0.9032", "15"),
        ("Macro Average", "0.9304", "0.9154", "0.9193", "86")
    ]
    for row_idx, data in enumerate(rows_c, start=1):
        for col_idx, val in enumerate(data):
            cell = t_c.cell(row_idx, col_idx)
            cell.fill.solid()
            is_macro = "Macro" in data[0]
            cell.fill.fore_color.rgb = TABLE_HEADER_BG if is_macro else (TABLE_ROW_ALT if row_idx % 2 == 0 else CARD_BG)
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.name = "Calibri"
            p.font.size = Pt(9)
            p.font.bold = is_macro
            p.font.color.rgb = ACCENT_CYAN if is_macro else (ACCENT_EMERALD if col_idx == 3 and float(val) >= 0.94 else TEXT_WHITE)
            p.alignment = PP_ALIGN.CENTER if col_idx > 0 else PP_ALIGN.LEFT

    tb7_comm = slide7.shapes.add_textbox(Inches(1.0), Inches(5.1), Inches(6.8), Inches(1.5))
    tf7_comm = tb7_comm.text_frame
    tf7_comm.word_wrap = True
    add_bullet_points(tf7_comm, [
        ("Perfect Precision:", "Remember, Apply, and Analyze classes achieved 100% precision on held-out test splits."),
        ("Key Nuance:", "Understand and Apply represent the largest source of soft ambiguity due to multi-clause verbs.")
    ], default_size=9.5, space_after=3)

    add_card(slide7, 8.3, 1.8, 4.2, 5.0, "Difficulty Tier Breakdown (Task B)")
    tb7b = slide7.shapes.add_textbox(Inches(8.5), Inches(2.4), Inches(3.8), Inches(4.2))
    tf7b = tb7b.text_frame
    tf7b.word_wrap = True
    add_bullet_points(tf7b, [
        ("Easy Tier (F1: 0.9643):", "Precision: 0.9643 | Recall: 0.9643 | Support: 28 questions."),
        ("Medium Tier (F1: 0.9310):", "Precision: 0.9310 | Recall: 0.9310 | Support: 29 questions."),
        ("Hard Tier (F1: 0.9655):", "Precision: 0.9655 | Recall: 0.9655 | Support: 29 questions."),
        ("Perfect Stratification:", "Equal balance across tiers prevents majority-class bias in automated audits.")
    ], default_size=10, space_after=8)

    # =========================================================================
    # SLIDE 8: FEATURE ABLATION STUDY
    # =========================================================================
    slide8 = prs.slides.add_slide(blank_layout)
    apply_background(slide8, prs)
    add_header(slide8, "Scientific Research & Feature Ablation", "Linguistic Sensitivity & Multi-Modal Feature Fusion",
               "Investigating the empirical contribution of lexical n-grams, readability formulas, and syntactic POS distributions.")

    add_card(slide8, 0.8, 1.8, 5.6, 5.0, "Controlled Ablation Experiments")
    tb8a = slide8.shapes.add_textbox(Inches(1.0), Inches(2.4), Inches(5.2), Inches(4.2))
    tf8a = tb8a.text_frame
    tf8a.word_wrap = True
    add_bullet_points(tf8a, [
        ("Config 1 (Lexical Baseline):", "Word & character n-grams (1-3 ngrams). Macro-F1 = 91.93%."),
        ("Config 2 (+ Readability Metrics):", "Augmented with Flesch-Kincaid Grade Level, Automated Readability Index (ARI), Coleman-Liau & Gunning Fog. Macro-F1 = 92.65% (+0.72% gain)."),
        ("Config 3 (+ Syntactic POS):", "Verb-to-noun ratios, imperative markers, modal auxiliary frequencies. Macro-F1 = 91.60% (-0.33%)."),
        ("Config 4 (Full Fusion):", "Union of Lexical, Readability, and Syntactic feature sets. Macro-F1 = 92.88% (+0.95% overall gain).")
    ], default_size=10, space_after=6)

    add_card(slide8, 6.8, 1.8, 5.7, 5.0, "Critical Research Insights", border_color=ACCENT_CYAN)
    tb8b = slide8.shapes.add_textbox(Inches(7.0), Inches(2.4), Inches(5.3), Inches(4.2))
    tf8b = tb8b.text_frame
    tf8b.word_wrap = True
    add_bullet_points(tf8b, [
        ("Readability Resolves Ambiguity:", "Incorporating surface readability (Flesch-Kincaid & ARI) yielded a +9.4% F1 improvement on the 'Understand' class."),
        ("The 'Procedural vs Conceptual' Boundary:", "Procedural questions ('Apply') exhibit markedly lower syllable complexity despite sharing similar technical vocabulary with conceptual questions ('Analyze')."),
        ("Syntactic Sparsity:", "Standalone POS tag distributions introduced slight noise for short questions, but fused with lexical n-grams provided strong syntactic constraint.")
    ], default_size=10, space_after=6)

    # =========================================================================
    # SLIDE 9: ERROR ANALYSIS & HITL JUSTIFICATION
    # =========================================================================
    slide9 = prs.slides.add_slide(blank_layout)
    apply_background(slide9, prs)
    add_header(slide9, "Qualitative Error Audits", "Why Pure Automation Fails & Why HITL is Mandatory",
               "Analyzing actual misclassification edge cases proves why automated AI must be paired with human oversight.")

    add_card(slide9, 0.8, 1.8, 3.6, 5.0, "Case 1: Dual-Objective Prompts", border_color=ACCENT_AMBER)
    tb9a = slide9.shapes.add_textbox(Inches(1.0), Inches(2.4), Inches(3.2), Inches(4.2))
    tf9a = tb9a.text_frame
    tf9a.word_wrap = True
    add_bullet_points(tf9a, [
        ("Exam Prompt:", "'Design an authentication flow and justify your choice of hashing algorithm.'"),
        ("Model Assigned:", "EVALUATE (0.58 confidence)."),
        ("Faculty Intended:", "CREATE (0.42 confidence)."),
        ("Takeaway:", "The question contains two action verbs ('Design' = Create, 'Justify' = Evaluate). Faculty intent must govern the primary weight.")
    ], default_size=9.5, space_after=5)

    add_card(slide9, 4.8, 1.8, 3.6, 5.0, "Case 2: Conceptual vs Algorithmic", border_color=ACCENT_AMBER)
    tb9b = slide9.shapes.add_textbox(Inches(5.0), Inches(2.4), Inches(3.2), Inches(4.2))
    tf9b = tb9b.text_frame
    tf9b.word_wrap = True
    add_bullet_points(tf9b, [
        ("Exam Prompt:", "'Describe how Dijkstra's algorithm solves shortest paths on a weighted graph.'"),
        ("Model Assigned:", "UNDERSTAND (due to verb 'Describe')."),
        ("Faculty Intended:", "APPLY (requires mathematical graph trace)."),
        ("Takeaway:", "Surface verbs can mask procedural requirements expected in university grading schemes.")
    ], default_size=9.5, space_after=5)

    add_card(slide9, 8.8, 1.8, 3.7, 5.0, "Case 3: Architectural Trade-Offs", border_color=ACCENT_AMBER)
    tb9c = slide9.shapes.add_textbox(Inches(9.0), Inches(2.4), Inches(3.3), Inches(4.2))
    tf9c = tb9c.text_frame
    tf9c.word_wrap = True
    add_bullet_points(tf9c, [
        ("Exam Prompt:", "'Explain the trade-offs between SQL and NoSQL storage engines.'"),
        ("Model Assigned:", "EVALUATE (triggered by judgment term 'trade-offs')."),
        ("Faculty Intended:", "UNDERSTAND (introductory overview)."),
        ("Takeaway:", "Course level (Freshman vs Graduate) changes the depth of cognitive demand.")
    ], default_size=9.5, space_after=5)

    # =========================================================================
    # SLIDE 10: HITL WORKFLOW & RBAC GOVERNANCE
    # =========================================================================
    slide10 = prs.slides.add_slide(blank_layout)
    apply_background(slide10, prs)
    add_header(slide10, "Institutional Governance", "3-Role RBAC & Human-in-the-Loop (HITL) Workflow",
               "Strict tenant isolation, immutable relational audit trails, and multi-tier role authorization.")

    add_card(slide10, 0.8, 1.8, 3.6, 5.0, "Role 1: Faculty / Teacher", border_color=ACCENT_INDIGO)
    tb10a = slide10.shapes.add_textbox(Inches(1.0), Inches(2.4), Inches(3.2), Inches(4.2))
    tf10a = tb10a.text_frame
    tf10a.word_wrap = True
    add_bullet_points(tf10a, [
        ("Strict Tenant Isolation:", "Faculty members can only access their own uploaded papers and evaluation records."),
        ("Interactive Calibrator:", "Inspect parsed questions, view model confidence scores, and edit predictions."),
        ("Logged Rationale:", "Overrides require a brief justification to prevent arbitrary tampering."),
        ("Export Authority:", "Generate official institutional ReportLab PDF & CSV audit documents.")
    ], default_size=9.5, space_after=5)

    add_card(slide10, 4.8, 1.8, 3.6, 5.0, "Role 2: System Administrator", border_color=ACCENT_CYAN)
    tb10b = slide10.shapes.add_textbox(Inches(5.0), Inches(2.4), Inches(3.2), Inches(4.2))
    tf10b = tb10b.text_frame
    tf10b.word_wrap = True
    add_bullet_points(tf10b, [
        ("User Lifecycle Management:", "Activate, deactivate, and manage institutional accounts with Argon2id passwords."),
        ("Audit & Activity Logs:", "Complete visibility over logins, file uploads, and model inference requests."),
        ("Model Deployment Monitor:", "Check active ML model registry version and system health diagnostics."),
        ("No Public Registration:", "Provisioned via administrative control to protect institutional integrity.")
    ], default_size=9.5, space_after=5)

    add_card(slide10, 8.8, 1.8, 3.7, 5.0, "Role 3: Academic Researcher", border_color=ACCENT_EMERALD)
    tb10c = slide10.shapes.add_textbox(Inches(9.0), Inches(2.4), Inches(3.3), Inches(4.2))
    tf10c = tb10c.text_frame
    tf10c.word_wrap = True
    add_bullet_points(tf10c, [
        ("Scientific Benchmarking:", "Inspect held-out confusion matrices, F1 macro metrics, and ROC curves."),
        ("Ablation Analytics:", "Compare model configurations across lexical, readability, and syntactic feature spaces."),
        ("Zero Cross-Mutation:", "Read-only research boundaries prevent tuning against locked evaluation splits."),
        ("Data Export:", "Download anonymized research splits for academic replication.")
    ], default_size=9.5, space_after=5)

    # =========================================================================
    # SLIDE 11: FULL-STACK TECHNICAL IMPLEMENTATION
    # =========================================================================
    slide11 = prs.slides.add_slide(blank_layout)
    apply_background(slide11, prs)
    add_header(slide11, "Technical Architecture & Tech Stack", "Modern, Production-Hardened Implementation",
               "FastAPI Python 3.11 backend paired with Next.js 16 + React 19 glassmorphic frontend.")

    add_card(slide11, 0.8, 1.8, 2.7, 5.0, "FastAPI Backend")
    tb11a = slide11.shapes.add_textbox(Inches(0.95), Inches(2.4), Inches(2.4), Inches(4.2))
    tf11a = tb11a.text_frame
    tf11a.word_wrap = True
    add_bullet_points(tf11a, [
        ("High-Performance:", "Asynchronous ASGI framework on Python 3.11."),
        ("Data Validation:", "Strict Pydantic v2 schemas and typed contracts."),
        ("ORM & Migrations:", "SQLAlchemy 2.0 with Alembic versioning."),
        ("Documentation:", "Auto-generated OpenAPI (Swagger) endpoints.")
    ], default_size=9.5, space_after=5)

    add_card(slide11, 3.8, 1.8, 2.7, 5.0, "Next.js 16 Frontend")
    tb11b = slide11.shapes.add_textbox(Inches(3.95), Inches(2.4), Inches(2.4), Inches(4.2))
    tf11b = tb11b.text_frame
    tf11b.word_wrap = True
    add_bullet_points(tf11b, [
        ("React 19 & TypeScript:", "Strictly typed components & state management."),
        ("Obsidian & Violet:", "Glassmorphism design tokens with responsive CSS."),
        ("Visual Analytics:", "Interactive Recharts for cognitive distributions."),
        ("Zero-Mock UI:", "Direct real-time binding to backend SQLite/Postgres.")
    ], default_size=9.5, space_after=5)

    add_card(slide11, 6.8, 1.8, 2.7, 5.0, "Document Pipeline")
    tb11c = slide11.shapes.add_textbox(Inches(6.95), Inches(2.4), Inches(2.4), Inches(4.2))
    tf11c = tb11c.text_frame
    tf11c.word_wrap = True
    add_bullet_points(tf11c, [
        ("PyMuPDF Engine:", "Lightning fast binary PDF text extraction."),
        ("python-docx:", "Word document table and paragraph parser."),
        ("Regex Matchers:", "Extracts question numbers, sub-parts, and marks."),
        ("Staging Hygiene:", "Secure file validation and path sanitization.")
    ], default_size=9.5, space_after=5)

    add_card(slide11, 9.8, 1.8, 2.7, 5.0, "Security & Hardening")
    tb11d = slide11.shapes.add_textbox(Inches(9.95), Inches(2.4), Inches(2.4), Inches(4.2))
    tf11d = tb11d.text_frame
    tf11d.word_wrap = True
    add_bullet_points(tf11d, [
        ("Argon2id Hashing:", "Modern cryptographic password hashing."),
        ("JWT Tokens:", "Signed stateless authorization tokens."),
        ("Zero Credential Leak:", "Environment-driven config via .env."),
        ("Container Ready:", "Multi-stage Dockerfile and Docker Compose.")
    ], default_size=9.5, space_after=5)

    # =========================================================================
    # SLIDE 12: ACCREDITATION IMPACT & REPORTING
    # =========================================================================
    slide12 = prs.slides.add_slide(blank_layout)
    apply_background(slide12, prs)
    add_header(slide12, "Institutional Impact & Compliance", "Automated Accreditation Compliance & Institutional Reports",
               "Directly fulfilling ABET, NBA, and Washington Accord outcome-based assessment criteria.")

    add_card(slide12, 0.8, 1.8, 5.6, 5.0, "Accreditation Alignment (ABET / NBA)")
    tb12a = slide12.shapes.add_textbox(Inches(1.0), Inches(2.4), Inches(5.2), Inches(4.2))
    tf12a = tb12a.text_frame
    tf12a.word_wrap = True
    add_bullet_points(tf12a, [
        ("Criterion 3 Outcome Verification:", "Accreditation bodies require proof that exams test complex engineering problems (Apply, Analyze, Evaluate, Create) rather than pure memorization."),
        ("Automated Cognitive Balance Index:", "Quantifies the exact percentage of marks allocated to foundational (Levels 1-2) vs higher-order thinking (Levels 3-6)."),
        ("Difficulty Distribution Check:", "Flags examination papers with skewed difficulty (e.g., >60% Hard or >70% Easy) before exams are administered to students.")
    ], default_size=10, space_after=6)

    add_card(slide12, 6.8, 1.8, 5.7, 5.0, "Institutional Export Engine", border_color=ACCENT_CYAN)
    tb12b = slide12.shapes.add_textbox(Inches(7.0), Inches(2.4), Inches(5.3), Inches(4.2))
    tf12b = tb12b.text_frame
    tf12b.word_wrap = True
    add_bullet_points(tf12b, [
        ("ReportLab Automated PDF:", "Generates formal institutional moderation certificates complete with visual Bloom distribution charts, difficulty breakdown tables, and approval signature blocks."),
        ("Streaming CSV Reports:", "Outputs granular question-by-question metrics (Question Text, Marks, Bloom Level, Difficulty, Confidence, Teacher Notes) for integration into university LMS/ERP systems."),
        ("Audit Compliance:", "Provides verifiable proof of institutional academic rigor for accreditation review visits.")
    ], default_size=10, space_after=6)

    # =========================================================================
    # SLIDE 13: FUTURE EXTENSIONS & ROADMAP
    # =========================================================================
    slide13 = prs.slides.add_slide(blank_layout)
    apply_background(slide13, prs)
    add_header(slide13, "Future Research & Development", "Roadmap: Compact Adapters & Cross-Disciplinary Scaling",
               "Next-generation extensions to expand pedagogical coverage, domain adaptation, and multi-lingual exams.")

    add_card(slide13, 0.8, 1.8, 3.6, 5.0, "1. Edge Parameter-Efficient NLP", border_color=ACCENT_INDIGO)
    tb13a = slide13.shapes.add_textbox(Inches(1.0), Inches(2.4), Inches(3.2), Inches(4.2))
    tf13a = tb13a.text_frame
    tf13a.word_wrap = True
    add_bullet_points(tf13a, [
        ("LoRA Adapters:", "Fine-tuning compact parameter-efficient domain adapters on DeBERTa-v3-small."),
        ("Quantized Inference:", "INT8/ONNX model quantization enabling sub-50ms inference on standard university edge servers without GPUs."),
        ("Contextual Multi-Sentence:", "Modeling complex preamble text and multi-step diagram prompts.")
    ], default_size=9.5, space_after=5)

    add_card(slide13, 4.8, 1.8, 3.6, 5.0, "2. Cross-Disciplinary Coverage", border_color=ACCENT_CYAN)
    tb13b = slide13.shapes.add_textbox(Inches(5.0), Inches(2.4), Inches(3.2), Inches(4.2))
    tf13b = tb13b.text_frame
    tf13b.word_wrap = True
    add_bullet_points(tf13b, [
        ("Beyond STEM:", "Extending corpus coverage to humanities, legal case law, and medical clinical examinations."),
        ("Multimodal Vision NLP:", "Extracting and classifying cognitive demand from circuit diagrams, code snippets, and chemical equations."),
        ("Multi-Lingual Exams:", "Cross-lingual transfer learning to support regional examination boards.")
    ], default_size=9.5, space_after=5)

    add_card(slide13, 8.8, 1.8, 3.7, 5.0, "3. Adaptive Exam Generation", border_color=ACCENT_EMERALD)
    tb13c = slide13.shapes.add_textbox(Inches(9.0), Inches(2.4), Inches(3.3), Inches(4.2))
    tf13c = tb13c.text_frame
    tf13c.word_wrap = True
    add_bullet_points(tf13c, [
        ("Automated Paper Synthesis:", "Invert the model to recommend or synthesize balanced exam papers satisfying exact Bloom target ratios."),
        ("Curricular Co-Pilot:", "Real-time authoring assistant that alerts faculty while they draft new exam questions."),
        ("Historical Calibration:", "Auto-calibrate difficulty predictions against actual student grade distributions.")
    ], default_size=9.5, space_after=5)

    # =========================================================================
    # SLIDE 14: SUMMARY & CONCLUSION
    # =========================================================================
    slide14 = prs.slides.add_slide(blank_layout)
    apply_background(slide14, prs)

    bar14 = slide14.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.2), Inches(1.6), Inches(0.12), Inches(4.2))
    bar14.fill.solid()
    bar14.fill.fore_color.rgb = ACCENT_CYAN
    bar14.line.fill.background()

    tb14 = slide14.shapes.add_textbox(Inches(1.5), Inches(1.5), Inches(10.5), Inches(4.8))
    tf14 = tb14.text_frame
    tf14.word_wrap = True

    p_end0 = tf14.paragraphs[0]
    p_end0.text = "CONCLUSION & SUMMARY"
    p_end0.font.name = "Calibri"
    p_end0.font.size = Pt(12)
    p_end0.font.bold = True
    p_end0.font.color.rgb = ACCENT_CYAN
    p_end0.space_after = Pt(10)

    p_end1 = tf14.add_paragraph()
    p_end1.text = "Key Takeaways: AI BASED AUTOMATIC QUESTION PAPER DIFFICULTY ANALYZER"
    p_end1.font.name = "Calibri"
    p_end1.font.size = Pt(24)
    p_end1.font.bold = True
    p_end1.font.color.rgb = TEXT_WHITE
    p_end1.space_after = Pt(18)

    add_bullet_points(tf14, [
        ("Conceptual Rigor:", "Decouples Bloom's cognitive demand from empirical difficulty, avoiding the Conflation Fallacy."),
        ("State-of-the-Art Accuracy:", "Achieves 91.93% Bloom's Macro-F1 and 95.56% Difficulty Macro-F1 with zero-leakage training."),
        ("Linguistic Contribution:", "Demonstrated that surface readability formulas significantly enhance discrimination on conceptual prompts (+9.4% F1)."),
        ("Production-Grade Engineering:", "FastAPI + Next.js 16 + React 19 + ReportLab PDF generator + 3-role RBAC governance."),
        ("Institutional Value:", "Transforms manual, subjective moderation into an auditable, human-in-the-loop accreditation asset.")
    ], default_size=12, space_after=10)

    p_end2 = tf14.add_paragraph()
    p_end2.text = "\nThank you! Questions & Discussion."
    p_end2.font.name = "Calibri"
    p_end2.font.size = Pt(16)
    p_end2.font.bold = True
    p_end2.font.color.rgb = ACCENT_INDIGO

    # Save presentation to multiple convenient locations
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    prs.save(output_path)
    print(f"[SUCCESS] Saved primary presentation to: {output_path}")

    # Copy to system folders: Downloads & Desktop if available
    user_home = os.path.expanduser("~")
    destinations = [
        os.path.join(user_home, "Downloads"),
        os.path.join(user_home, "OneDrive", "Desktop"),
        os.path.join(user_home, "Desktop"),
        os.path.join(user_home, "OneDrive", "Documents")
    ]
    for dest_dir in destinations:
        if os.path.isdir(dest_dir):
            target = os.path.join(dest_dir, "AI_Exam_Difficulty_Analyzer_Presentation.pptx")
            try:
                shutil.copy2(output_path, target)
                print(f"[SUCCESS] Copied presentation to system folder: {target}")
            except Exception as e:
                print(f"[WARNING] Could not copy to {target}: {e}")

if __name__ == "__main__":
    out_file = os.path.join(os.getcwd(), "AI_Exam_Difficulty_Analyzer_Presentation.pptx")
    build_presentation(out_file)
