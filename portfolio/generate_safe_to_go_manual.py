#!/usr/bin/env python3
"""
Safe to Go: Power Zone Operations Manual
Amazon Waterspider Edition
PDF Generator with placeholder diagram zones
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
    KeepTogether, Frame, Image
)
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from datetime import datetime

def create_header_footer(canvas_obj, doc):
    """Add header and footer to each page"""
    canvas_obj.saveState()
    
    # Header
    canvas_obj.setFont('Helvetica-Bold', 9)
    canvas_obj.drawString(inch, letter[1] - 0.5*inch, "Safe to Go: Power Zone Operations Manual")
    canvas_obj.setFont('Helvetica', 8)
    canvas_obj.drawRightString(letter[0] - inch, letter[1] - 0.5*inch, "Amazon Waterspider Edition")
    
    # Footer
    canvas_obj.setFont('Helvetica', 8)
    canvas_obj.drawString(inch, 0.5*inch, f"© {datetime.now().year} Contruil LLC | Control Your World")
    canvas_obj.drawCentredString(letter[0]/2, 0.5*inch, f"Page {doc.page}")
    canvas_obj.drawRightString(letter[0] - inch, 0.5*inch, f"Generated: {datetime.now().strftime('%Y-%m-%d')}")
    
    canvas_obj.restoreState()

def create_safe_to_go_manual():
    """Generate the complete Safe to Go operations manual"""
    
    # Create PDF - using workspace directory instead of /mnt
    filename = "Safe_to_Go_Operations_Manual.pdf"
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        rightMargin=inch,
        leftMargin=inch,
        topMargin=1.25*inch,
        bottomMargin=1*inch
    )
    
    # Container for the 'Flowable' objects
    story = []
    
    # Define styles
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#1a1a1a'),
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Normal'],
        fontSize=14,
        textColor=colors.HexColor('#666666'),
        spaceAfter=40,
        alignment=TA_CENTER,
        fontName='Helvetica-Oblique'
    )
    
    heading1_style = ParagraphStyle(
        'CustomHeading1',
        parent=styles['Heading1'],
        fontSize=18,
        textColor=colors.HexColor('#1a1a1a'),
        spaceAfter=12,
        spaceBefore=20,
        fontName='Helvetica-Bold'
    )
    
    heading2_style = ParagraphStyle(
        'CustomHeading2',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=colors.HexColor('#333333'),
        spaceAfter=10,
        spaceBefore=15,
        fontName='Helvetica-Bold'
    )
    
    heading3_style = ParagraphStyle(
        'CustomHeading3',
        parent=styles['Heading3'],
        fontSize=12,
        textColor=colors.HexColor('#444444'),
        spaceAfter=8,
        spaceBefore=12,
        fontName='Helvetica-Bold'
    )
    
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontSize=11,
        textColor=colors.HexColor('#1a1a1a'),
        spaceAfter=12,
        alignment=TA_JUSTIFY,
        leading=16
    )
    
    callout_style = ParagraphStyle(
        'Callout',
        parent=styles['Normal'],
        fontSize=10,
        textColor=colors.HexColor('#2c5aa0'),
        spaceAfter=10,
        leftIndent=20,
        rightIndent=20,
        borderPadding=10,
        borderColor=colors.HexColor('#2c5aa0'),
        borderWidth=1,
        leading=14
    )
    
    code_style = ParagraphStyle(
        'Code',
        parent=styles['Code'],
        fontSize=9,
        fontName='Courier',
        leftIndent=20,
        spaceAfter=10,
        textColor=colors.HexColor('#1a1a1a'),
        backColor=colors.HexColor('#f5f5f5')
    )
    
    # ============================================================
    # COVER PAGE
    # ============================================================
    
    story.append(Spacer(1, 2*inch))
    
    story.append(Paragraph("SAFE TO GO", title_style))
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph("Power Zone Operations Manual", subtitle_style))
    story.append(Spacer(1, 0.5*inch))
    
    # Cover callout
    cover_box = [
        ["<b>System Architecture for Physical Performance</b>"],
        ["Treating warehouse operations as high-availability infrastructure"],
        [""],
        ["Amazon Waterspider Edition"],
    ]
    
    cover_table = Table(cover_box, colWidths=[5*inch])
    cover_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#f0f4f8')),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.HexColor('#1a1a1a')),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
        ('TOPPADDING', (0, 0), (-1, -1), 12),
        ('BOX', (0, 0), (-1, -1), 2, colors.HexColor('#2c5aa0')),
    ]))
    
    story.append(cover_table)
    story.append(Spacer(1, 1*inch))
    
    # Metadata box
    metadata = [
        ["<b>Author:</b>", "Timothy Wheels"],
        ["<b>Company:</b>", "Contruil LLC"],
        ["<b>Framework:</b>", "Control Your World (CYW) OS"],
        ["<b>Version:</b>", "1.0"],
        ["<b>Generated:</b>", datetime.now().strftime('%B %d, %Y')],
    ]
    
    metadata_table = Table(metadata, colWidths=[1.5*inch, 3.5*inch])
    metadata_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
    ]))
    
    story.append(metadata_table)
    
    story.append(PageBreak())
    
    # ============================================================
    # TABLE OF CONTENTS
    # ============================================================
    
    story.append(Paragraph("Table of Contents", heading1_style))
    story.append(Spacer(1, 0.3*inch))
    
    toc_data = [
        ["Section", "Page"],
        ["1. Executive Summary", "3"],
        ["2. Power Zone Framework Overview", "4"],
        ["3. System Architecture: Body as Infrastructure", "5"],
        ["4. Safe to Go Protocol Stack", "6"],
        ["5. Daily Operational Templates", "9"],
        ["6. Strain Reduction Modules", "11"],
        ["7. Data Collection & Pattern Recognition", "13"],
        ["8. Implementation Roadmap", "14"],
        ["Appendix A: Quick Reference Cards", "15"],
        ["Appendix B: Diagram Placeholder Zones", "16"],
    ]
    
    toc_table = Table(toc_data, colWidths=[4*inch, 1*inch])
    toc_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2c5aa0')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('TOPPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#f9f9f9')),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
        ('TOPPADDING', (0, 1), (-1, -1), 8),
    ]))
    
    story.append(toc_table)
    story.append(PageBreak())
    
    # ============================================================
    # 1. EXECUTIVE SUMMARY
    # ============================================================
    
    story.append(Paragraph("1. Executive Summary", heading1_style))
    
    story.append(Paragraph(
        "<b>Objective:</b> Transform Amazon Waterspider operations from reactive injury "
        "avoidance to proactive performance architecture using Control Your World (CYW) "
        "Power Zone principles.",
        body_style
    ))
    
    story.append(Paragraph(
        "<b>Core Insight:</b> Your body during warehouse operations functions as a "
        "high-availability system under continuous load. Traditional 'Safe to Go' focuses "
        "on compliance checkpoints. This manual implements Safe to Go as an operational "
        "system with monitoring, adaptation protocols, and iterative optimization.",
        body_style
    ))
    
    story.append(Spacer(1, 0.2*inch))
    
    # Key principles box
    principles_data = [
        ["<b>Power Zone Principle</b>", "<b>Operational Translation</b>"],
        ["Systems thinking", "Body = Infrastructure requiring architecture"],
        ["Modular organization", "Protocols for lift/push/route/recovery"],
        ["Iterative refinement", "Daily micro-adjustments compound"],
        ["Pattern recognition", "Track strain triggers, optimize technique"],
        ["Scalable clarity", "Reusable templates for consistent execution"],
    ]
    
    principles_table = Table(principles_data, colWidths=[2.5*inch, 3*inch])
    principles_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2c5aa0')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
        ('TOPPADDING', (0, 0), (-1, -1), 10),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#f9f9f9')),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
    ]))
    
    story.append(principles_table)
    
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph(
        "<b>Expected Outcomes:</b>",
        heading3_style
    ))
    
    outcomes = [
        "Reduce cumulative strain through systematic technique optimization",
        "Increase shift sustainability via real-time adaptation protocols",
        "Build reusable operational knowledge (not just anecdotal experience)",
        "Maintain high-availability performance across 60+ hour work weeks",
        "Document patterns for continuous improvement and knowledge transfer",
    ]
    
    for outcome in outcomes:
        story.append(Paragraph(f"• {outcome}", body_style))
    
    story.append(PageBreak())
    
    # ============================================================
    # 2. POWER ZONE FRAMEWORK OVERVIEW
    # ============================================================
    
    story.append(Paragraph("2. Power Zone Framework Overview", heading1_style))
    
    story.append(Paragraph(
        "Your Power Zone represents the operational range where cognitive strengths, "
        "learned skills, and environmental conditions produce maximum leverage with "
        "minimum friction.",
        body_style
    ))
    
    story.append(Paragraph("<b>2.1 Core Components</b>", heading2_style))
    
    # Four components table
    components_data = [
        ["<b>Component</b>", "<b>Description</b>", "<b>Physical Application</b>"],
        [
            "Cognitive Strengths",
            "Systems architecture thinking, pattern recognition, modular organization",
            "Analyze movement patterns as system protocols"
        ],
        [
            "Skill Strengths",
            "Workflow optimization, protocol creation, iterative refinement",
            "Design lift/push/route techniques for reuse"
        ],
        [
            "Motivational Drivers",
            "Building scalable systems, creating clarity from chaos",
            "Transform warehouse chaos into predictable operations"
        ],
        [
            "Environmental Conditions",
            "Autonomy, iteration capability, peer dynamics",
            "Self-directed technique adjustment within shift structure"
        ],
    ]
    
    components_table = Table(components_data, colWidths=[1.3*inch, 2*inch, 2.2*inch])
    components_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2c5aa0')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#f9f9f9')),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
    ]))
    
    story.append(components_table)
    
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("<b>2.2 Power Zone Statement</b>", heading2_style))
    
    story.append(Paragraph(
        "<i>\"Systems architect for scalable clarity: I design modular workflows and "
        "protocols that make complex ideas teachable, actionable, and enduring.\"</i>",
        callout_style
    ))
    
    story.append(Paragraph(
        "Applied to warehouse operations: <b>Design reusable movement protocols that "
        "transform repetitive strain into iteratively optimized performance.</b>",
        body_style
    ))
    
    story.append(Spacer(1, 0.3*inch))
    
    # Diagram placeholder
    diagram_box = [
        ["<b>[DIAGRAM ZONE 1: POWER ZONE VENN DIAGRAM]</b>"],
        [""],
        ["Insert visual showing intersection of:"],
        ["• Cognitive Engines (top circle)"],
        ["• Skill Outputs (left circle)"],
        ["• Environmental Fit (right circle)"],
        ["• Power Zone (center intersection)"],
        [""],
        ["Recommended size: 5\" x 3.5\""],
        ["Format: PNG or SVG"],
    ]
    
    diagram_table = Table(diagram_box, colWidths=[5.5*inch])
    diagram_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#fffacd')),
        ('TEXTCOLOR', (0, 0), (0, 0), colors.HexColor('#b8860b')),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (0, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (0, 0), 11),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
        ('TOPPADDING', (0, 0), (-1, -1), 10),
        ('BOX', (0, 0), (-1, -1), 2, colors.HexColor('#b8860b')),
        ('LINEABOVE', (0, 2), (-1, 2), 1, colors.HexColor('#daa520')),
    ]))
    
    story.append(diagram_table)
    
    story.append(PageBreak())
    
    # ============================================================
    # 3. SYSTEM ARCHITECTURE: BODY AS INFRASTRUCTURE
    # ============================================================
    
    story.append(Paragraph("3. System Architecture: Body as Infrastructure", heading1_style))
    
    story.append(Paragraph(
        "Traditional approach: React to pain signals after strain accumulates.<br/>"
        "Power Zone approach: <b>Treat your body as a distributed system requiring "
        "continuous monitoring, load balancing, and preventive maintenance.</b>",
        body_style
    ))
    
    story.append(Paragraph("<b>3.1 Infrastructure Mapping</b>", heading2_style))
    
    # Infrastructure comparison
    infra_data = [
        ["<b>Network Concept</b>", "<b>Physical Equivalent</b>", "<b>Monitoring Metric</b>"],
        ["Bandwidth capacity", "Muscular endurance", "Fatigue accumulation rate"],
        ["Latency", "Movement efficiency", "Wasted motion per task"],
        ["Packet loss", "Technique breakdown", "Form degradation frequency"],
        ["Load balancing", "Muscle group rotation", "Symmetrical strain distribution"],
        ["Failover systems", "Backup movement patterns", "Alternative technique availability"],
        ["Health checks", "Body scans", "Hourly self-assessment"],
        ["Performance logs", "Shift documentation", "Daily strain journal"],
    ]
    
    infra_table = Table(infra_data, colWidths=[2*inch, 2*inch, 1.5*inch])
    infra_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2c5aa0')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#f9f9f9')),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
    ]))
    
    story.append(infra_table)
    
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("<b>3.2 High-Availability Design Principles</b>", heading2_style))
    
    ha_principles = [
        ("<b>Redundancy:</b>", "Multiple movement patterns for same task (e.g., 3 different cart-pushing grips)"),
        ("<b>Graceful Degradation:</b>", "Reduced-intensity protocols when fatigue accumulates"),
        ("<b>Circuit Breakers:</b>", "Automatic rest triggers when strain thresholds exceeded"),
        ("<b>Health Monitoring:</b>", "Continuous self-assessment via hourly body scans"),
        ("<b>Horizontal Scaling:</b>", "Distribute load across multiple muscle groups instead of overloading single areas"),
    ]
    
    for principle, description in ha_principles:
        story.append(Paragraph(f"{principle} {description}", body_style))
    
    story.append(Spacer(1, 0.3*inch))
    
    # Diagram placeholder
    diagram_box2 = [
        ["<b>[DIAGRAM ZONE 2: BODY-AS-INFRASTRUCTURE FLOWCHART]</b>"],
        [""],
        ["Insert Mermaid diagram showing:"],
        ["Shift Start → Power Zone Body Scan → Energy Level Assessment → Task Selection"],
        ["→ Hourly Micro-Audits → Strain Detection → Adaptation Protocol → End Shift Debrief"],
        [""],
        ["Include decision nodes for:"],
        ["• Energy level routing (High/Medium/Low)"],
        ["• Strain signal detection (Yes/No)"],
        ["• Adaptation triggers"],
        [""],
        ["Recommended size: 6\" x 4\""],
    ]
    
    diagram_table2 = Table(diagram_box2, colWidths=[5.5*inch])
    diagram_table2.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#fffacd')),
        ('TEXTCOLOR', (0, 0), (0, 0), colors.HexColor('#b8860b')),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (0, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (0, 0), 11),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
        ('TOPPADDING', (0, 0), (-1, -1), 10),
        ('BOX', (0, 0), (-1, -1), 2, colors.HexColor('#b8860b')),
        ('LINEABOVE', (0, 2), (-1, 2), 1, colors.HexColor('#daa520')),
    ]))
    
    story.append(diagram_table2)
    
    story.append(PageBreak())
    
    # ============================================================
    # 4. SAFE TO GO PROTOCOL STACK
    # ============================================================
    
    story.append(Paragraph("4. Safe to Go Protocol Stack", heading1_style))
    
    story.append(Paragraph(
        "The Safe to Go Protocol Stack is a layered system of operational procedures "
        "designed for real-time execution during warehouse operations. Each module is "
        "modular, reusable, and optimized for < 5-minute implementation.",
        body_style
    ))
    
    story.append(Paragraph("<b>4.1 Pre-Shift Assessment Protocol</b>", heading2_style))
    
    story.append(Paragraph("<b>Duration:</b> 2 minutes | <b>Timing:</b> Before clocking in", heading3_style))
    
    story.append(Paragraph("<b>Checklist:</b>", body_style))
    
    pre_shift_data = [
        ["<b>Assessment Item</b>", "<b>Rating Scale</b>", "<b>Action Threshold</b>"],
        ["Sleep quality", "1-5 (5 = excellent)", "< 3 = Conservative strain threshold"],
        ["Pre-existing muscle tension", "None / Mild / Moderate / Severe", "Moderate+ = Document location, adjust technique"],
        ["Mental clarity", "1-5 (5 = sharp)", "< 3 = Increase focus on form checks"],
        ["Hydration status", "Well / Adequate / Dehydrated", "Dehydrated = Immediate intake + monitor"],
    ]
    
    pre_shift_table = Table(pre_shift_data, colWidths=[2*inch, 1.75*inch, 1.75*inch])
    pre_shift_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2c5aa0')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#f9f9f9')),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
    ]))
    
    story.append(pre_shift_table)
    
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph(
        "<b>Strain Threshold Setting:</b><br/>"
        "Based on assessment, select today's operational mode:",
        body_style
    ))
    
    threshold_modes = [
        ("<b>Aggressive (Green Zone):</b>", "Sleep 4-5, no tension, high clarity → Standard rate, technique experimentation allowed"),
        ("<b>Moderate (Yellow Zone):</b>", "Sleep 3, mild tension, adequate clarity → Reduced pace, focus on proven techniques"),
        ("<b>Conservative (Red Zone):</b>", "Sleep 1-2, moderate+ tension, low clarity → Minimum viable output, prioritize injury prevention"),
    ]
    
    for mode, desc in threshold_modes:
        story.append(Paragraph(f"{mode} {desc}", body_style))
    
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("<b>4.2 Hourly Micro-Audit Protocol</b>", heading2_style))
    
    story.append(Paragraph("<b>Duration:</b> 30 seconds | <b>Frequency:</b> Top of each hour", heading3_style))
    
    story.append(Paragraph(
        "Quick body scan to detect early strain signals before they become injuries. "
        "Use natural transition moments (restroom breaks, route changes) to execute.",
        body_style
    ))
    
    story.append(Paragraph("<b>Three-Point Assessment:</b>", body_style))
    
    micro_audit_items = [
        "<b>Shoulders:</b> Tension level (None / Mild / Moderate / Severe)",
        "<b>Lower Back:</b> Stability status (Solid / Fatigued / Strained)",
        "<b>Knees/Ankles:</b> Joint integrity (Normal / Achy / Sharp pain)",
    ]
    
    for item in micro_audit_items:
        story.append(Paragraph(f"• {item}", body_style))
    
    story.append(Spacer(1, 0.1*inch))
    
    story.append(Paragraph(
        "<b>Decision Rule:</b> If 2+ areas flagged with Moderate/Fatigued/Achy or worse "
        "→ Trigger Adaptation Protocol immediately.",
        callout_style
    ))
    
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("<b>4.3 Real-Time Adaptation Protocol</b>", heading2_style))
    
    story.append(Paragraph(
        "Executed when strain signals detected during Hourly Micro-Audit. Select 1-3 "
        "interventions based on specific strain location:",
        body_style
    ))
    
    adaptation_data = [
        ["<b>Strain Location</b>", "<b>Immediate Adaptation</b>", "<b>Technique Modification</b>"],
        [
            "Shoulders",
            "30-second arm circles, shoulder shrugs",
            "Switch cart pushing to pulling, lower grip position"
        ],
        [
            "Lower Back",
            "Cat-cow stretches (3 reps), forward fold",
            "Engage core before lifts, hinge from hips not spine"
        ],
        [
            "Knees/Ankles",
            "Ankle rotations, quad stretches",
            "Shorten stride length, reduce cart speed by 15%"
        ],
        [
            "General Fatigue",
            "2-minute complete stop, hydration",
            "Request route variation, switch to lighter tasks"
        ],
    ]
    
    adaptation_table = Table(adaptation_data, colWidths=[1.5*inch, 2*inch, 2*inch])
    adaptation_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2c5aa0')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#f9f9f9')),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
    ]))
    
    story.append(adaptation_table)
    
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("<b>4.4 End-Shift Documentation Protocol</b>", heading2_style))
    
    story.append(Paragraph("<b>Duration:</b> 3 minutes | <b>Timing:</b> Immediately after clocking out", heading3_style))
    
    story.append(Paragraph(
        "Critical for pattern recognition and iterative improvement. Capture data while "
        "experiences are fresh. Use voice notes if writing is impractical.",
        body_style
    ))
    
    story.append(Paragraph("<b>Four-Part Documentation:</b>", body_style))
    
    doc_sections = [
        ("<b>1. Technique Wins:</b>", "What movement modifications worked well today? (e.g., 'Wide-grip cart push reduced shoulder strain by ~50%')"),
        ("<b>2. Strain Triggers:</b>", "What caused pain/fatigue spikes? (e.g., 'Repeated overhead reaches at station 7')"),
        ("<b>3. Pattern Recognition:</b>", "Any recurring issues from previous shifts? (e.g., 'Third consecutive shift with right knee ache')"),
        ("<b>4. Next Shift Adjustment:</b>", "One specific change to test tomorrow (e.g., 'Try left-foot-forward stance for cart pushing')"),
    ]
    
    for section, desc in doc_sections:
        story.append(Paragraph(f"{section} {desc}", body_style))
    
    story.append(PageBreak())
    
    # ============================================================
    # 5. DAILY OPERATIONAL TEMPLATES
    # ============================================================
    
    story.append(Paragraph("5. Daily Operational Templates", heading1_style))
    
    story.append(Paragraph(
        "Pre-built templates for consistent execution. Copy these into your preferred "
        "note-taking system (Notion, paper notebook, phone notes).",
        body_style
    ))
    
    story.append(Paragraph("<b>5.1 Master Daily Template</b>", heading2_style))
    
    story.append(Paragraph(
        "Use this as your primary tracking document. One per shift.",
        body_style
    ))
    
    # Template in code block style
    template_text = """
# Safe to Go Daily Log - [DATE]

## Pre-Shift Assessment (Before clocking in)
- Sleep Quality: ___/5
- Pre-existing Tension: ___ (location: ___)
- Mental Clarity: ___/5
- Hydration: Well / Adequate / Dehydrated
- **Today's Strain Threshold:** Aggressive / Moderate / Conservative

## Hourly Micro-Audits
**Hour 1 (___:___):** Shoulders ___ | Back ___ | Legs ___
**Hour 2 (___:___):** Shoulders ___ | Back ___ | Legs ___
**Hour 3 (___:___):** Shoulders ___ | Back ___ | Legs ___
**Hour 4 (___:___):** Shoulders ___ | Back ___ | Legs ___
**Hour 5 (___:___):** Shoulders ___ | Back ___ | Legs ___
**Hour 6 (___:___):** Shoulders ___ | Back ___ | Legs ___
**Hour 7 (___:___):** Shoulders ___ | Back ___ | Legs ___
**Hour 8 (___:___):** Shoulders ___ | Back ___ | Legs ___

## Adaptation Protocols Triggered
- [ ] Shoulder intervention @ ___:___
- [ ] Back intervention @ ___:___
- [ ] Knee/Ankle intervention @ ___:___
- [ ] General fatigue protocol @ ___:___

## End-Shift Documentation
**Technique Wins:**
- 
- 

**Strain Triggers:**
- 
- 

**Pattern Recognition:**
- 

**Next Shift Adjustment:**
- 
"""
    
    story.append(Paragraph(template_text.replace('\n', '<br/>'), code_style))
    
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("<b>5.2 Weekly Pattern Summary Template</b>", heading2_style))
    
    story.append(Paragraph(
        "End-of-week review to identify trends across multiple shifts. Completed every "
        "Sunday evening or before your next work cycle.",
        body_style
    ))
    
    weekly_template = """
# Weekly Pattern Summary - Week of [DATE]

## Shifts Completed This Week: ___

## Most Frequent Strain Locations:
1. ___ (occurred ___ times)
2. ___ (occurred ___ times)
3. ___ (occurred ___ times)

## Top Technique Wins:
1. ___
2. ___
3. ___

## Consistent Strain Triggers to Eliminate:
1. ___
2. ___

## Technique Experiments for Next Week:
1. ___
2. ___

## Overall Trend: Improving / Stable / Declining
"""
    
    story.append(Paragraph(weekly_template.replace('\n', '<br/>'), code_style))
    
    story.append(PageBreak())
    
    # ============================================================
    # 6. STRAIN REDUCTION MODULES
    # ============================================================
    
    story.append(Paragraph("6. Strain Reduction Modules", heading1_style))
    
    story.append(Paragraph(
        "Task-specific technique protocols for the most common Waterspider operations. "
        "Each module includes baseline technique and 2-3 variations to test.",
        body_style
    ))
    
    story.append(Paragraph("<b>6.1 Cart Pushing/Pulling Module</b>", heading2_style))
    
    cart_techniques = [
        ["<b>Technique</b>", "<b>Description</b>", "<b>Best For</b>"],
        [
            "Standard Push (Baseline)",
            "Both hands at hip height, shoulders back, core engaged, push from legs",
            "Light-medium loads, short distances"
        ],
        [
            "Wide-Grip Push",
            "Hands wider than shoulders, distribute force across chest/shoulders",
            "Reducing shoulder strain, heavy loads"
        ],
        [
            "Pull Configuration",
            "Face cart, pull with arms, walk backwards slowly",
            "When shoulders fatigued, navigating tight spaces"
        ],
        [
            "Alternating Push-Pull",
            "Switch between push/pull every 10 carts",
            "Long shifts, distributing load across muscle groups"
        ],
    ]
    
    cart_table = Table(cart_techniques, colWidths=[1.5*inch, 2.5*inch, 1.5*inch])
    cart_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2c5aa0')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#f9f9f9')),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
    ]))
    
    story.append(cart_table)
    
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("<b>6.2 Package Lifting Module</b>", heading2_style))
    
    lift_techniques = [
        ["<b>Technique</b>", "<b>Description</b>", "<b>Best For</b>"],
        [
            "Standard Squat Lift",
            "Feet shoulder-width, squat down, grip package, lift with legs, keep back straight",
            "Heavy packages, floor-level pickup"
        ],
        [
            "Golfer's Lift",
            "One-leg balance, hinge at hip, opposite leg extends back for counterbalance",
            "Light packages, reducing repetitive squatting"
        ],
        [
            "Power Zone Transfer",
            "Move package to waist height (power zone) before further manipulation",
            "Awkward shapes, multi-step handling"
        ],
        [
            "Team Lift Protocol",
            "Request assistance for 50+ lbs, coordinate lift on count",
            "Injury prevention, building team rapport"
        ],
    ]
    
    lift_table = Table(lift_techniques, colWidths=[1.5*inch, 2.5*inch, 1.5*inch])
    lift_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2c5aa0')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#f9f9f9')),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
    ]))
    
    story.append(lift_table)
    
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("<b>6.3 Sustained Standing/Walking Module</b>", heading2_style))
    
    story.append(Paragraph(
        "Micro-mobility protocols to prevent lower-body fatigue during long standing periods.",
        body_style
    ))
    
    mobility_items = [
        "<b>Weight Shift Rotation:</b> Every 5 minutes, shift weight from left to right foot, hold 30 seconds each",
        "<b>Heel-Toe Rock:</b> While waiting, rock from heels to toes repeatedly (improves circulation)",
        "<b>Hip Flexor Activation:</b> Subtle lunges during natural pauses (e.g., waiting for cart to arrive)",
        "<b>Posture Reset:</b> Set phone timer for 15-minute intervals, check: shoulders back, core engaged, knees soft",
    ]
    
    for item in mobility_items:
        story.append(Paragraph(f"• {item}", body_style))
    
    story.append(PageBreak())
    
    # ============================================================
    # 7. DATA COLLECTION & PATTERN RECOGNITION
    # ============================================================
    
    story.append(Paragraph("7. Data Collection & Pattern Recognition", heading1_style))
    
    story.append(Paragraph(
        "Your Power Zone strength is systems thinking and pattern recognition. Apply it "
        "to your own operational data to identify trends invisible to reactive workers.",
        body_style
    ))
    
    story.append(Paragraph("<b>7.1 Key Metrics to Track</b>", heading2_style))
    
    metrics_data = [
        ["<b>Metric</b>", "<b>Collection Method</b>", "<b>Analysis Frequency</b>"],
        ["Sleep quality score", "Pre-shift assessment", "Daily average (weekly review)"],
        ["Strain threshold mode", "Pre-shift assessment", "Mode distribution per week"],
        ["Hourly body scan results", "Micro-audits", "Identify peak strain hours"],
        ["Adaptation protocol frequency", "End-shift documentation", "Trend over time (increasing = problem)"],
        ["Technique win replication", "End-shift documentation", "Which wins become permanent?"],
        ["Recurring strain locations", "Weekly summary", "Chronic issues requiring intervention"],
    ]
    
    metrics_table = Table(metrics_data, colWidths=[1.75*inch, 2*inch, 1.75*inch])
    metrics_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2c5aa0')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#f9f9f9')),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
    ]))
    
    story.append(metrics_table)
    
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("<b>7.2 Pattern Recognition Decision Tree</b>", heading2_style))
    
    story.append(Paragraph(
        "Use this logic flow during weekly reviews to identify root causes:",
        body_style
    ))
    
    decision_tree_items = [
        "<b>IF</b> same strain location appears 3+ shifts in a row → <b>THEN</b> technique modification required (not just stretching)",
        "<b>IF</b> adaptation protocols increasing week-over-week → <b>THEN</b> baseline technique needs redesign",
        "<b>IF</b> strain peaks consistently at same hour → <b>THEN</b> implement preventive micro-break before that hour",
        "<b>IF</b> technique win documented but not replicated → <b>THEN</b> add to pre-shift checklist as reminder",
        "<b>IF</b> sleep quality < 3 for consecutive days → <b>THEN</b> trigger conservative mode automatically + investigate sleep hygiene",
    ]
    
    for item in decision_tree_items:
        story.append(Paragraph(f"• {item}", body_style))
    
    story.append(Spacer(1, 0.3*inch))
    
    # Diagram placeholder
    diagram_box3 = [
        ["<b>[DIAGRAM ZONE 3: WEEKLY PATTERN ANALYSIS FLOWCHART]</b>"],
        [""],
        ["Insert decision tree diagram showing:"],
        ["Weekly data collection → Pattern identification → Root cause analysis → Protocol adjustment"],
        [""],
        ["Include branches for:"],
        ["• Chronic strain location (technique fix)"],
        ["• Increasing adaptation frequency (baseline redesign)"],
        ["• Time-based strain patterns (preventive scheduling)"],
        ["• Sleep quality degradation (lifestyle intervention)"],
        [""],
        ["Recommended size: 6\" x 4\""],
    ]
    
    diagram_table3 = Table(diagram_box3, colWidths=[5.5*inch])
    diagram_table3.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#fffacd')),
        ('TEXTCOLOR', (0, 0), (0, 0), colors.HexColor('#b8860b')),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (0, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (0, 0), 11),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
        ('TOPPADDING', (0, 0), (-1, -1), 10),
        ('BOX', (0, 0), (-1, -1), 2, colors.HexColor('#b8860b')),
        ('LINEABOVE', (0, 2), (-1, 2), 1, colors.HexColor('#daa520')),
    ]))
    
    story.append(diagram_table3)
    
    story.append(PageBreak())
    
    # ============================================================
    # 8. IMPLEMENTATION ROADMAP
    # ============================================================
    
    story.append(Paragraph("8. Implementation Roadmap", heading1_style))
    
    story.append(Paragraph(
        "Phased rollout to avoid overwhelming adoption. Start small, iterate, scale.",
        body_style
    ))
    
    story.append(Paragraph("<b>Phase 1: Foundation (Week 1-2)</b>", heading2_style))
    
    phase1_items = [
        "Implement Pre-Shift Assessment only (master the habit)",
        "Test Daily Template in preferred note-taking system",
        "Document one Technique Win per shift (no pressure for comprehensive data)",
        "Success metric: 80% pre-shift assessment completion rate",
    ]
    
    for item in phase1_items:
        story.append(Paragraph(f"• {item}", body_style))
    
    story.append(Spacer(1, 0.1*inch))
    
    story.append(Paragraph("<b>Phase 2: Monitoring (Week 3-4)</b>", heading2_style))
    
    phase2_items = [
        "Add Hourly Micro-Audits (use phone alarms as reminders)",
        "Practice Adaptation Protocol when strain detected",
        "Complete End-Shift Documentation 50% of shifts",
        "Success metric: Identify 2-3 recurring strain patterns",
    ]
    
    for item in phase2_items:
        story.append(Paragraph(f"• {item}", body_style))
    
    story.append(Spacer(1, 0.1*inch))
    
    story.append(Paragraph("<b>Phase 3: Optimization (Week 5+)</b>", heading2_style))
    
    phase3_items = [
        "Full protocol stack execution (all modules active)",
        "Weekly Pattern Summary reviews every Sunday",
        "Begin testing technique variations from Strain Reduction Modules",
        "Success metric: Measurable reduction in adaptation protocol frequency",
    ]
    
    for item in phase3_items:
        story.append(Paragraph(f"• {item}", body_style))
    
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("<b>Long-Term Vision (Month 3+)</b>", heading2_style))
    
    story.append(Paragraph(
        "Once protocols are internalized and data patterns clear, this system becomes "
        "the foundation for:",
        body_style
    ))
    
    longterm_items = [
        "<b>Content creation:</b> Document your findings for end-of-year video series",
        "<b>Peer training:</b> Share optimized techniques with other Waterspiders",
        "<b>Process Assistant application:</b> Evidence-based operational improvement proposals",
        "<b>CYW OS case study:</b> Real-world proof that Power Zone principles scale from AI orchestration to physical labor",
    ]
    
    for item in longterm_items:
        story.append(Paragraph(f"• {item}", body_style))
    
    story.append(PageBreak())
    
    # ============================================================
    # APPENDIX A: QUICK REFERENCE CARDS
    # ============================================================
    
    story.append(Paragraph("Appendix A: Quick Reference Cards", heading1_style))
    
    story.append(Paragraph(
        "Print-friendly one-pagers for field reference. Cut along dotted lines, laminate "
        "if possible, keep in work bag or locker.",
        body_style
    ))
    
    story.append(Paragraph("<b>A.1 Pre-Shift Assessment Card</b>", heading2_style))
    
    pre_shift_card = [
        ["<b>SAFE TO GO: PRE-SHIFT ASSESSMENT</b>"],
        [""],
        ["<b>Sleep Quality:</b> 1  2  3  4  5 (circle one)"],
        ["<b>Muscle Tension:</b> None / Mild / Moderate / Severe"],
        ["<b>Mental Clarity:</b> 1  2  3  4  5 (circle one)"],
        ["<b>Hydration:</b> Well / Adequate / Dehydrated"],
        [""],
        ["<b>TODAY'S STRAIN THRESHOLD:</b>"],
        ["Aggressive (Sleep 4-5, no tension, high clarity)"],
        ["Moderate (Sleep 3, mild tension, adequate clarity)"],
        ["Conservative (Sleep 1-2, moderate+ tension, low clarity)"],
        [""],
        ["Circle your mode → Proceed to shift"],
    ]
    
    card1_table = Table(pre_shift_card, colWidths=[5.5*inch])
    card1_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, 0), colors.HexColor('#2c5aa0')),
        ('TEXTCOLOR', (0, 0), (0, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (0, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (0, 0), 12),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOX', (0, 0), (-1, -1), 2, colors.HexColor('#2c5aa0')),
        ('LINEABOVE', (0, 1), (-1, 1), 1, colors.grey),
    ]))
    
    story.append(card1_table)
    
    story.append(Spacer(1, 0.3*inch))
    
    story.append(Paragraph("<b>A.2 Hourly Micro-Audit Card</b>", heading2_style))
    
    micro_audit_card = [
        ["<b>SAFE TO GO: HOURLY MICRO-AUDIT</b>"],
        [""],
        ["<b>Three-Point Body Scan (30 seconds):</b>"],
        [""],
        ["Shoulders: None / Mild / Moderate / Severe"],
        ["Lower Back: Solid / Fatigued / Strained"],
        ["Knees/Ankles: Normal / Achy / Sharp Pain"],
        [""],
        ["<b>DECISION RULE:</b>"],
        ["2+ areas flagged → TRIGGER ADAPTATION PROTOCOL"],
        [""],
        ["<b>Quick Adaptations:</b>"],
        ["Shoulders: Switch push to pull, lower grip"],
        ["Back: Engage core, hinge from hips"],
        ["Legs: Shorten stride, reduce speed 15%"],
    ]
    
    card2_table = Table(micro_audit_card, colWidths=[5.5*inch])
    card2_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, 0), colors.HexColor('#2c5aa0')),
        ('TEXTCOLOR', (0, 0), (0, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (0, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (0, 0), 12),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOX', (0, 0), (-1, -1), 2, colors.HexColor('#2c5aa0')),
        ('LINEABOVE', (0, 1), (-1, 1), 1, colors.grey),
    ]))
    
    story.append(card2_table)
    
    story.append(PageBreak())
    
    # ============================================================
    # APPENDIX B: DIAGRAM PLACEHOLDER ZONES
    # ============================================================
    
    story.append(Paragraph("Appendix B: Diagram Placeholder Zones", heading1_style))
    
    story.append(Paragraph(
        "This manual includes three strategic diagram zones for visual enhancement. "
        "Insert your CYW OS-branded graphics in these locations.",
        body_style
    ))
    
    story.append(Paragraph("<b>Zone 1: Power Zone Venn Diagram</b>", heading2_style))
    
    zone1_specs = [
        "<b>Location:</b> Page 4 (Power Zone Framework Overview section)",
        "<b>Purpose:</b> Illustrate intersection of Cognitive Engines, Skill Outputs, and Environmental Fit",
        "<b>Recommended Size:</b> 5\" width × 3.5\" height",
        "<b>Format:</b> PNG (300 DPI) or SVG",
        "<b>Visual Elements:</b> Three overlapping circles with center intersection labeled 'Power Zone'",
        "<b>Branding:</b> Use CYW OS color scheme (blue #2c5aa0 primary)",
    ]
    
    for spec in zone1_specs:
        story.append(Paragraph(f"• {spec}", body_style))
    
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("<b>Zone 2: Body-as-Infrastructure Flowchart</b>", heading2_style))
    
    zone2_specs = [
        "<b>Location:</b> Page 5 (System Architecture section)",
        "<b>Purpose:</b> Show operational workflow from Shift Start through End-Shift Debrief",
        "<b>Recommended Size:</b> 6\" width × 4\" height",
        "<b>Format:</b> Mermaid diagram exported as PNG or PDF",
        "<b>Visual Elements:</b> Decision nodes (Energy Level, Strain Detection), process boxes, feedback loops",
        "<b>Tool Suggestion:</b> Use Mermaid Live Editor or export from existing CYW_OS documentation",
    ]
    
    for spec in zone2_specs:
        story.append(Paragraph(f"• {spec}", body_style))
    
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("<b>Zone 3: Weekly Pattern Analysis Flowchart</b>", heading2_style))
    
    zone3_specs = [
        "<b>Location:</b> Page 13 (Data Collection & Pattern Recognition section)",
        "<b>Purpose:</b> Decision tree for weekly review pattern identification",
        "<b>Recommended Size:</b> 6\" width × 4\" height",
        "<b>Format:</b> Mermaid diagram or custom illustration",
        "<b>Visual Elements:</b> Data inputs → Pattern detection → Root cause branches → Protocol adjustments",
        "<b>Complexity:</b> Medium - should include 4-5 decision branches",
    ]
    
    for spec in zone3_specs:
        story.append(Paragraph(f"• {spec}", body_style))
    
    story.append(Spacer(1, 0.3*inch))
    
    story.append(Paragraph("<b>Diagram Insertion Instructions</b>", heading2_style))
    
    story.append(Paragraph(
        "To add your diagrams after PDF generation:",
        body_style
    ))
    
    insertion_steps = [
        "Open this PDF in Adobe Acrobat or similar PDF editor",
        "Locate the yellow placeholder boxes on pages 4, 5, and 13",
        "Use 'Edit PDF' → 'Add Image' to insert your graphics",
        "Position images to replace placeholder boxes completely",
        "Verify diagram legibility at 100% zoom",
        "Save as final version: <i>Safe_to_Go_Operations_Manual_v1.0_Final.pdf</i>",
    ]
    
    for i, step in enumerate(insertion_steps, 1):
        story.append(Paragraph(f"{i}. {step}", body_style))
    
    story.append(Spacer(1, 0.3*inch))
    
    # Final CYW branding
    story.append(Spacer(1, 0.5*inch))
    
    final_box = [
        ["<b>This is how you Control Your World.</b>"],
        [""],
        ["Engineer this system to compound results, not belief."],
        [""],
        ["© 2025 Contruil LLC | CYW OS Framework"],
    ]
    
    final_table = Table(final_box, colWidths=[5.5*inch])
    final_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#f0f4f8')),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.HexColor('#1a1a1a')),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (0, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (0, 0), 14),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica-Oblique'),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
        ('TOPPADDING', (0, 0), (-1, -1), 12),
        ('BOX', (0, 0), (-1, -1), 2, colors.HexColor('#2c5aa0')),
    ]))
    
    story.append(final_table)
    
    # Build PDF
    doc.build(story, onFirstPage=create_header_footer, onLaterPages=create_header_footer)
    
    return filename

if __name__ == "__main__":
    pdf_file = create_safe_to_go_manual()
    print(f"Safe to Go Operations Manual generated: {pdf_file}")

