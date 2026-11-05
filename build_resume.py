from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, PageBreak, KeepTogether

ROOT = Path(__file__).parent
OUT = ROOT / 'Resumes' / 'doc' / '2026-11-04'
OUT.mkdir(parents=True, exist_ok=True)
PDF = OUT / 'Leena_M_Outfitter_AI_Business_Development_Representative_Resume.pdf'

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='Name', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=22, leading=25, alignment=TA_CENTER, textColor=colors.HexColor('#17324D'), spaceAfter=4))
styles.add(ParagraphStyle(name='Contact', parent=styles['Normal'], fontName='Helvetica', fontSize=9.5, leading=12, alignment=TA_CENTER, textColor=colors.HexColor('#34495E'), spaceAfter=8))
styles.add(ParagraphStyle(name='Section', parent=styles['Heading2'], fontName='Helvetica-Bold', fontSize=12, leading=14, textColor=colors.HexColor('#17324D'), spaceBefore=8, spaceAfter=5, keepWithNext=True))
styles.add(ParagraphStyle(name='Body', parent=styles['Normal'], fontName='Helvetica', fontSize=9.2, leading=12.2, textColor=colors.HexColor('#1F2933'), spaceAfter=5))
styles.add(ParagraphStyle(name='Skill', parent=styles['Normal'], fontName='Helvetica', fontSize=9.2, leading=12.2, textColor=colors.HexColor('#1F2933'), leftIndent=0, spaceAfter=3))
styles.add(ParagraphStyle(name='Employer', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=10.5, leading=13, textColor=colors.HexColor('#17324D'), spaceBefore=7, spaceAfter=1, keepWithNext=True))
styles.add(ParagraphStyle(name='Date', parent=styles['Normal'], fontName='Helvetica-Oblique', fontSize=9, leading=11, textColor=colors.HexColor('#52606D'), spaceAfter=3, keepWithNext=True))
styles.add(ParagraphStyle(name='ResumeBullet', parent=styles['Normal'], fontName='Helvetica', fontSize=8.9, leading=11.7, leftIndent=12, firstLineIndent=-8, bulletIndent=0, textColor=colors.HexColor('#1F2933'), spaceAfter=3))
styles.add(ParagraphStyle(name='Edu', parent=styles['Normal'], fontName='Helvetica', fontSize=9.4, leading=12, textColor=colors.HexColor('#1F2933'), spaceAfter=2))

summary = ('Senior Consultant with 8+ years of experience translating business needs into structured outreach, stakeholder conversations, and delivery plans. '
           'Brings a consultative approach to identifying decision-makers, personalizing communication, running discovery, and moving complex opportunities toward clear next steps. '
           'Comfortable working with owners and senior stakeholders through LinkedIn, email, and video calls, synthesizing market feedback, and coordinating the handoff from terms through launch. '
           'Relevant strengths include <b>partner development</b>, <b>multi-step deal progression</b>, and practical problem-solving across ambiguous business situations.')

skills = [
    ('Business Development', 'Target-market selection, owner prospecting, account research, consultative discovery, meeting generation'),
    ('Outreach Channels', 'LinkedIn, personalized email, video calls, AI-researched prospect lists, drafted outreach'),
    ('Partner Development', 'Partner qualification, founder-led presentations, terms discussion, signing coordination, market launch support'),
    ('Sales Process', 'Needs discovery, opportunity qualification, objection handling, follow-up, stakeholder alignment, next-step planning'),
    ('Market Intelligence', 'Voice-of-market capture, competitor and market scanning, feedback synthesis, territory prioritization'),
    ('Communication', 'Executive communication, presentation preparation, business writing, cross-functional coordination, documentation'),
]

experiences = [
    ('Senior Consultant | Elevance Health', 'February 2026 - Present', [
        'Identify high-value stakeholder groups and prioritize outreach based on business need, timing, and likelihood of productive conversation.',
        'Translate ambiguous business questions into concise discovery topics, meeting objectives, and decision-ready follow-up actions.',
        'Personalize LinkedIn and email outreach around the recipient\'s operating context instead of relying on generic messaging.',
        'Run stakeholder conversations that surface goals, constraints, decision criteria, and the path required to move an opportunity forward.',
        'Prepare concise presentations that connect a proposed solution to the stakeholder\'s business priorities and practical next steps.',
        'Coordinate terms, open questions, and commitments across stakeholders so discussions progress toward a clear decision and launch plan.',
        'Capture market feedback from conversations and turn recurring themes into recommendations for positioning, outreach, and follow-up.',
        'Maintain disciplined follow-up across multi-step opportunities, documenting commitments and re-engaging stakeholders at appropriate points.',
    ]),
    ('Senior Consultant | Optum', 'October 2024 - February 2026', [
        'Built targeted stakeholder lists by researching organizations, roles, business priorities, and the owners or decision-makers most relevant to a conversation.',
        'Used structured outreach sequences across LinkedIn and email, adapting language to the prospect\'s business model and likely concerns.',
        'Qualified conversations through consultative questions covering current operating gaps, growth objectives, urgency, and fit.',
        'Facilitated video-call discussions with senior stakeholders and converted conversation notes into specific next steps and follow-up materials.',
        'Supported presentations by organizing the business case, anticipated objections, and proof points needed for an informed partner discussion.',
        'Advanced opportunities through review cycles by clarifying responsibilities, timing, decision criteria, and unresolved terms.',
        'Synthesized stakeholder feedback into concise internal updates that helped refine positioning and address patterns in the market.',
        'Balanced near-term meeting generation with long-cycle relationship development, keeping potential partners engaged between decision points.',
    ]),
    ('Consultant | LatentView', 'June 2022 - August 2024', [
        'Analyzed market and account information to identify priority segments, relevant organizations, and contacts worth pursuing.',
        'Developed personalized first-touch messaging that connected the conversation to the prospect\'s business context and likely value drivers.',
        'Conducted discovery conversations to understand operational pain points and determine whether a follow-up or partner discussion was warranted.',
        'Prepared meeting briefs and presentation content that made complex recommendations understandable to business owners and senior stakeholders.',
        'Managed follow-up across extended sales and partnership cycles, keeping open questions, commitments, and timing visible.',
        'Recorded voice-of-market observations and translated them into recommendations for target-market focus and outreach refinement.',
        'Coordinated with internal contributors to align proposed solutions, commercial considerations, and launch-readiness requirements.',
    ]),
    ('Consultant | Reylon Softech', 'June 2018 - June 2022', [
        'Researched prospective organizations and decision-makers to build focused outreach lists for business conversations.',
        'Engaged prospects through professional email and LinkedIn communication, tailoring messages to business needs and industry context.',
        'Used discovery questions to clarify objectives, current processes, constraints, and the people involved in a buying decision.',
        'Supported business presentations by organizing needs, proposed value, questions, and agreed follow-up actions.',
        'Maintained consistent follow-through across opportunities that required multiple conversations before a decision.',
        'Documented prospect feedback and recurring objections so future outreach could be more relevant and precise.',
    ]),
]

story = []
story.append(Paragraph('Leena M', styles['Name']))
story.append(Paragraph('Texas, US  |  +1 (972) 776-4448  |  leenakrishna94@gmail.com', styles['Contact']))
story.append(HRFlowable(width='100%', thickness=0.8, color=colors.HexColor('#7B8794'), spaceAfter=5))
story.append(Paragraph('Professional Summary', styles['Section']))
story.append(Paragraph(summary, styles['Body']))
story.append(Paragraph('Technical Skills', styles['Section']))
for cat, items in skills:
    story.append(Paragraph(f'<b>{cat}:</b> {items}', styles['Skill']))
story.append(Paragraph('Professional Experience', styles['Section']))
for employer, date, bullets in experiences:
    block = [Paragraph(employer, styles['Employer']), Paragraph(date, styles['Date'])]
    for bullet in bullets:
        block.append(Paragraph(f'• {bullet}', styles['ResumeBullet']))
    story.append(KeepTogether(block[:2]))
    story.extend(block[2:])
story.append(Paragraph('Education', styles['Section']))
story.append(Paragraph('<b>Master\'s in Cybersecurity</b> | Saint Louis University', styles['Edu']))
story.append(Paragraph('May 2026', styles['Edu']))

def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont('Helvetica', 7.5)
    canvas.setFillColor(colors.HexColor('#7B8794'))
    canvas.drawCentredString(LETTER[0] / 2, 0.38 * inch, f'Leena M  |  Business Development Representative  |  Page {doc.page}')
    canvas.restoreState()

doc = SimpleDocTemplate(str(PDF), pagesize=LETTER, rightMargin=0.68*inch, leftMargin=0.68*inch, topMargin=0.55*inch, bottomMargin=0.58*inch, title='Leena M - Outfitter AI Business Development Representative Resume', author='Leena M')
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print(PDF)
