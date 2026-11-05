from pathlib import Path
import importlib.util
import re

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_SECTION
from docx.shared import Inches, Pt, RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn


ROOT = Path(__file__).parent
OUT = ROOT / "output" / "docx" / "2026-11-05"
OUT.mkdir(parents=True, exist_ok=True)
DOCX = OUT / "Leena_M_Senior_AI_Python_Developer_Resume.docx"

# Reuse the approved content in the referenced PDF builder.
spec = importlib.util.spec_from_file_location("resume_source", ROOT / "build_senior_ai_python_resume.py")
source = importlib.util.module_from_spec(spec)
spec.loader.exec_module(source)


def set_font(run, name="Arial", size=10, bold=False, italic=False, color=None):
    run.font.name = name
    run._element.get_or_add_rPr().rFonts.set(qn("w:ascii"), name)
    run._element.get_or_add_rPr().rFonts.set(qn("w:hAnsi"), name)
    run.font.size = Pt(size)
    run.bold = bold
    run.italic = italic
    if color:
        run.font.color.rgb = RGBColor(*color)


def add_markup(paragraph, text, size=9.2):
    parts = re.split(r"(<b>.*?</b>)", text)
    for part in parts:
        if not part:
            continue
        bold = part.startswith("<b>") and part.endswith("</b>")
        clean = part[3:-4] if bold else part
        run = paragraph.add_run(clean)
        set_font(run, size=size, bold=bold)


def set_keep_with_next(paragraph):
    paragraph.paragraph_format.keep_with_next = True


doc = Document()
section = doc.sections[0]
section.top_margin = Inches(0.55)
section.bottom_margin = Inches(0.55)
section.left_margin = Inches(0.68)
section.right_margin = Inches(0.68)

normal = doc.styles["Normal"]
normal.font.name = "Arial"
normal._element.rPr.rFonts.set(qn("w:ascii"), "Arial")
normal._element.rPr.rFonts.set(qn("w:hAnsi"), "Arial")
normal.font.size = Pt(9.2)

name = doc.add_paragraph()
name.alignment = WD_ALIGN_PARAGRAPH.CENTER
name.paragraph_format.space_after = Pt(3)
set_font(name.add_run("Leena M"), size=22, bold=True, color=(23, 50, 77))

contact = doc.add_paragraph()
contact.alignment = WD_ALIGN_PARAGRAPH.CENTER
contact.paragraph_format.space_after = Pt(8)
set_font(contact.add_run("Texas, US  |  +1 (972) 776-4448  |  leenakrishna94@gmail.com"), size=9.5, color=(52, 73, 94))


def heading(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(4)
    set_keep_with_next(p)
    set_font(p.add_run(text), size=12, bold=True, color=(23, 50, 77))
    return p


heading("Professional Summary")
p = doc.add_paragraph()
p.paragraph_format.space_after = Pt(5)
add_markup(p, source.summary, size=9.2)

heading("Technical Skills")
for category, items in source.skills:
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(2)
    set_font(p.add_run(f"{category}: "), size=9.1, bold=True)
    set_font(p.add_run(items), size=9.1)

heading("Professional Experience")
for employer, date, bullets in source.experiences:
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(1)
    set_keep_with_next(p)
    set_font(p.add_run(employer), size=10.5, bold=True, color=(23, 50, 77))

    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(2)
    set_keep_with_next(p)
    set_font(p.add_run(date), size=9, italic=True, color=(82, 96, 109))

    for bullet in bullets:
        p = doc.add_paragraph(style="List Bullet")
        p.paragraph_format.left_indent = Inches(0.18)
        p.paragraph_format.first_line_indent = Inches(-0.12)
        p.paragraph_format.space_after = Pt(2)
        add_markup(p, bullet, size=8.8)

heading("Education")
p = doc.add_paragraph()
p.paragraph_format.space_after = Pt(2)
set_font(p.add_run("Master's in Cybersecurity"), size=9.3, bold=True)
set_font(p.add_run(" | Saint Louis University"), size=9.3)
p = doc.add_paragraph()
p.paragraph_format.space_after = Pt(2)
set_font(p.add_run("May 2026"), size=9.3)

footer = section.footer.paragraphs[0]
footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
set_font(footer.add_run("Leena M  |  Senior AI/Python Developer"), size=7.5, color=(123, 135, 148))

doc.core_properties.title = "Leena M - Senior AI/Python Developer Resume"
doc.core_properties.author = "Leena M"
doc.save(DOCX)
print(DOCX)
