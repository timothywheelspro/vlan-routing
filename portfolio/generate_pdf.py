#!/usr/bin/env python3
"""
Generate PDF from Triangle Test Protocol lead magnet markdown.
Uses ReportLab for professional PDF generation.
"""

from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
import re

def parse_markdown(md_content):
    """Parse markdown content into structured elements."""
    elements = []
    lines = md_content.split('\n')
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Skip empty lines (will add spacers later)
        if not line:
            elements.append(('spacer', None))
            i += 1
            continue
        
        # Headers
        if line.startswith('# '):
            elements.append(('h1', line[2:]))
        elif line.startswith('## '):
            elements.append(('h2', line[3:]))
        elif line.startswith('### '):
            elements.append(('h3', line[4:]))
        elif line.startswith('#### '):
            elements.append(('h4', line[5:]))
        elif line.startswith('---'):
            elements.append(('hr', None))
        # Bold text
        elif line.startswith('**') and line.endswith('**'):
            elements.append(('bold', line[2:-2]))
        # List items
        elif line.startswith('- ') or line.startswith('* '):
            elements.append(('li', line[2:]))
        # Code blocks (skip for now)
        elif line.startswith('```'):
            i += 1
            while i < len(lines) and not lines[i].strip().startswith('```'):
                i += 1
        # Tables (basic detection)
        elif '|' in line and line.count('|') > 2:
            table_rows = []
            while i < len(lines) and '|' in lines[i]:
                if '---' not in lines[i]:  # Skip separator lines
                    cells = [cell.strip() for cell in lines[i].split('|')[1:-1]]
                    table_rows.append(cells)
                i += 1
            if table_rows:
                elements.append(('table', table_rows))
            continue
        else:
            # Regular paragraph
            elements.append(('p', line))
        
        i += 1
    
    return elements

def create_pdf(md_file, output_file):
    """Generate PDF from markdown file."""
    
    # Read markdown
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Parse markdown
    elements = parse_markdown(md_content)
    
    # Create PDF
    doc = SimpleDocTemplate(
        output_file,
        pagesize=letter,
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=18
    )
    
    # Styles
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#0b0f14'),
        spaceAfter=12,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    h1_style = ParagraphStyle(
        'CustomH1',
        parent=styles['Heading1'],
        fontSize=18,
        textColor=colors.HexColor('#0b0f14'),
        spaceAfter=12,
        spaceBefore=12,
        fontName='Helvetica-Bold'
    )
    
    h2_style = ParagraphStyle(
        'CustomH2',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=colors.HexColor('#764ba2'),
        spaceAfter=10,
        spaceBefore=10,
        fontName='Helvetica-Bold'
    )
    
    h3_style = ParagraphStyle(
        'CustomH3',
        parent=styles['Heading3'],
        fontSize=12,
        textColor=colors.HexColor('#667eea'),
        spaceAfter=8,
        spaceBefore=8,
        fontName='Helvetica-Bold'
    )
    
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontSize=11,
        textColor=colors.HexColor('#333333'),
        spaceAfter=6,
        leading=14,
        alignment=TA_JUSTIFY,
        fontName='Helvetica'
    )
    
    bold_style = ParagraphStyle(
        'CustomBold',
        parent=body_style,
        fontName='Helvetica-Bold',
        textColor=colors.HexColor('#0b0f14')
    )
    
    # Build story
    story = []
    
    for elem_type, content in elements:
        if elem_type == 'h1':
            if story:  # Add page break before major sections
                story.append(PageBreak())
            story.append(Paragraph(content, title_style))
            story.append(Spacer(1, 0.2*inch))
        elif elem_type == 'h2':
            story.append(Spacer(1, 0.15*inch))
            story.append(Paragraph(content, h1_style))
        elif elem_type == 'h3':
            story.append(Spacer(1, 0.1*inch))
            story.append(Paragraph(content, h2_style))
        elif elem_type == 'h4':
            story.append(Paragraph(content, h3_style))
        elif elem_type == 'bold':
            story.append(Paragraph(content, bold_style))
        elif elem_type == 'li':
            # Format list item
            bullet = '• '
            text = bullet + content
            # Clean markdown formatting
            text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
            text = re.sub(r'`(.*?)`', r'<font name="Courier">\1</font>', text)
            story.append(Paragraph(text, body_style))
        elif elem_type == 'hr':
            story.append(Spacer(1, 0.2*inch))
            # Draw a line
            story.append(Spacer(1, 0.1*inch))
        elif elem_type == 'table':
            if content:
                # Create table
                table = Table(content)
                table.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#f0f0f0')),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.HexColor('#0b0f14')),
                    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                    ('FONTSIZE', (0, 0), (-1, 0), 10),
                    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                    ('BACKGROUND', (0, 1), (-1, -1), colors.white),
                    ('TEXTCOLOR', (0, 1), (-1, -1), colors.HexColor('#333333')),
                    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
                    ('FONTSIZE', (0, 1), (-1, -1), 9),
                    ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#e0e0e0')),
                    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ]))
                story.append(table)
                story.append(Spacer(1, 0.15*inch))
        elif elem_type == 'p' and content:
            # Clean markdown formatting in paragraphs
            text = content
            text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
            text = re.sub(r'`(.*?)`', r'<font name="Courier">\1</font>', text)
            text = re.sub(r'\[(.*?)\]\((.*?)\)', r'<link href="\2" color="blue"><u>\1</u></link>', text)
            
            # Skip placeholder comments
            if '[INSERT:' in text or '**End of Document**' in text:
                continue
            
            story.append(Paragraph(text, body_style))
        elif elem_type == 'spacer':
            story.append(Spacer(1, 0.1*inch))
    
    # Build PDF
    doc.build(story)
    print(f"✓ PDF generated: {output_file}")

if __name__ == '__main__':
    import sys
    
    md_file = 'TRIANGLE_TEST_PROTOCOL_LEAD_MAGNET.md'
    output_file = 'triangle-test-protocol.pdf'
    
    if len(sys.argv) > 1:
        md_file = sys.argv[1]
    if len(sys.argv) > 2:
        output_file = sys.argv[2]
    
    print(f"Generating PDF from {md_file}...")
    create_pdf(md_file, output_file)
    print("Done!")

