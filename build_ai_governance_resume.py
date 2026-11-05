from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import HRFlowable, KeepTogether, Paragraph, SimpleDocTemplate

ROOT = Path(__file__).parent
OUT = ROOT / "Resumes" / "pdf" / "2026-11-05"
OUT.mkdir(parents=True, exist_ok=True)
PDF = OUT / "Leena_M_Sr_IT_Governance_Analyst_AI_Resume.pdf"

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="Name", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=22, leading=25, alignment=TA_CENTER, textColor=colors.HexColor("#17324D"), spaceAfter=4))
styles.add(ParagraphStyle(name="Contact", parent=styles["Normal"], fontName="Helvetica", fontSize=9.5, leading=12, alignment=TA_CENTER, textColor=colors.HexColor("#34495E"), spaceAfter=8))
styles.add(ParagraphStyle(name="Section", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=12, leading=14, textColor=colors.HexColor("#17324D"), spaceBefore=8, spaceAfter=5, keepWithNext=True))
styles.add(ParagraphStyle(name="Body", parent=styles["Normal"], fontName="Helvetica", fontSize=9.0, leading=11.8, textColor=colors.HexColor("#1F2933"), spaceAfter=5))
styles.add(ParagraphStyle(name="Skill", parent=styles["Normal"], fontName="Helvetica", fontSize=8.9, leading=11.6, textColor=colors.HexColor("#1F2933"), spaceAfter=2.5))
styles.add(ParagraphStyle(name="Employer", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=10.5, leading=13, textColor=colors.HexColor("#17324D"), spaceBefore=7, spaceAfter=1, keepWithNext=True))
styles.add(ParagraphStyle(name="Date", parent=styles["Normal"], fontName="Helvetica-Oblique", fontSize=8.9, leading=11, textColor=colors.HexColor("#52606D"), spaceAfter=3, keepWithNext=True))
styles.add(ParagraphStyle(name="ResumeBullet", parent=styles["Normal"], fontName="Helvetica", fontSize=8.25, leading=10.6, leftIndent=11, firstLineIndent=-7, textColor=colors.HexColor("#1F2933"), spaceAfter=2.0))
styles.add(ParagraphStyle(name="Edu", parent=styles["Normal"], fontName="Helvetica", fontSize=9.1, leading=11.5, textColor=colors.HexColor("#1F2933"), spaceAfter=2))

summary = ("Senior Consultant with 8+ years of experience translating complex technology work into practical governance, control, documentation, and change-delivery practices. "
           "Brings a risk-focused approach to <b>AI governance and IT controls</b>, software development lifecycle process improvement, audit coordination, issue analysis, and cross-functional counsel. "
           "Experienced in mapping requirements to evidence, identifying systemic weaknesses, documenting remediation actions, and coordinating stakeholders across business, technology, cybersecurity, QA, architecture, and delivery teams. "
           "Prepared to apply <b>NIST-aligned risk thinking</b> to responsible AI development and enterprise control oversight.")

skills = [
    ("AI Governance and Controls", "AI governance, responsible AI, AI development standards, model and application controls, control design, control implementation, traceability"),
    ("IT Risk and Compliance", "IT risk management, risk assessment, control testing, issue management, remediation tracking, escalation, risk reporting"),
    ("Audit and Assurance", "Audit planning, evidence coordination, request management, walkthroughs, findings analysis, corrective actions, external-firm communication"),
    ("SDLC and Process Improvement", "Software development lifecycle, process mapping, policy and procedure development, standards, documentation, quality gates, continuous improvement"),
    ("Frameworks and Governance Operations", "NIST-aligned practices, governance forums, decision records, control inventories, operating procedures, portfolio prioritization"),
    ("Change and Stakeholder Leadership", "Complex change initiatives, dependency management, cross-division coordination, executive counsel, effective communication, future-state planning"),
]

experiences = [
    ("Senior Consultant | Elevance Health", "February 2026 - Present", [
        "Partner with technology and business stakeholders to translate emerging AI use cases into governance questions, control objectives, decision points, and accountable owners.",
        "Design <b>AI governance</b> review practices that connect intended use, data handling, human oversight, validation, monitoring, and escalation to the software delivery lifecycle.",
        "Document AI development standards, control expectations, approval paths, evidence requirements, and operating procedures for teams moving from experimentation toward production.",
        "Map software lifecycle activities to <b>IT controls</b> covering requirements, design, code changes, testing, deployment, access, logging, monitoring, and support handoff.",
        "Use <b>NIST-aligned risk thinking</b> to organize threats, affected assets, control responses, residual risk, and follow-up actions for AI-enabled workflows.",
        "Review proposed controls for clarity, ownership, testability, evidence quality, operating frequency, and the ability to detect systemic weaknesses.",
        "Coordinate audit and assurance requests by clarifying scope, assigning evidence owners, tracking due dates, and communicating open questions across technology teams.",
        "Prepare evidence narratives that connect policies, procedures, tickets, approvals, test results, logs, and remediation records without overstating what the evidence proves.",
        "Analyze control gaps by separating design deficiencies, operating failures, missing evidence, unclear ownership, and dependency problems that require different resolutions.",
        "Develop remediation plans with accountable owners, milestones, dependencies, interim safeguards, validation steps, and escalation criteria for overdue actions.",
        "Counsel leaders and business areas on practical control responses, explaining risk, business impact, implementation effort, and the consequences of accepting residual exposure.",
        "Facilitate cross-functional discussions with cybersecurity, architecture, application, data, QA, DevOps, legal, privacy, and business partners to resolve governance questions.",
        "Build control and issue tracking views that distinguish open risks, accepted risks, overdue actions, recurring findings, and evidence still required for closure.",
        "Lead process-improvement analysis for complex delivery workflows, identifying duplicate approvals, ambiguous handoffs, unowned controls, and inconsistent documentation.",
        "Prioritize an illustrative portfolio of 12 change initiatives by risk, business impact, dependency criticality, regulatory exposure, delivery capacity, and readiness.",
        "Create decision records that preserve the rationale for control exceptions, compensating actions, ownership changes, and future review dates.",
        "Assess whether AI-related documentation is sufficient to support traceability from use-case intent through requirements, testing, release approval, monitoring, and incident response.",
        "Identify recurring weaknesses across teams and escalate systemic issues with concise evidence, impact statements, recommended actions, and resource implications.",
        "Maintain clear status communication for leaders, including completed actions, blockers, decisions needed, upcoming audit commitments, and changes to risk posture.",
        "Deliver an illustrative control-review package covering 30 lifecycle evidence items across governance, development, testing, release, monitoring, and remediation paths.",
    ]),
    ("Senior Consultant | Optum", "October 2024 - February 2026", [
        "Assess technology processes and proposed changes against documented requirements, control objectives, risk considerations, and evidence expectations.",
        "Support <b>IT risk management</b> by identifying threats, affected business processes, control dependencies, risk owners, and actions needed to reduce exposure.",
        "Develop process maps and written procedures for software delivery, change control, access review, testing, incident handling, and evidence retention.",
        "Review AI-enabled workflow proposals for data use, human decision authority, output validation, monitoring, security boundaries, and accountable ownership.",
        "Translate <b>NIST</b> concepts into practical review questions and control language that delivery teams can apply during planning and implementation.",
        "Coordinate audit requests across application, infrastructure, data, security, QA, and business stakeholders, keeping scope, evidence, and response status visible.",
        "Prepare audit walkthrough materials that explain process steps, control intent, operating evidence, known limitations, and remediation commitments.",
        "Evaluate evidence for completeness, period coverage, approver identity, population scope, exception treatment, and consistency with the stated control.",
        "Track findings and corrective actions through closure, escalating overdue items and surfacing dependencies that prevent accountable owners from completing work.",
        "Analyze repeated findings to determine whether the underlying cause is policy ambiguity, process design, technology configuration, training, ownership, or monitoring.",
        "Advise stakeholders on control improvements that balance risk reduction, operational practicality, delivery timelines, and sustainable ownership.",
        "Document governance decisions, risk acceptances, exceptions, remediation plans, and review dates so future teams can understand the basis for prior actions.",
        "Lead process-change discussions involving multiple teams, sequencing dependencies and identifying interim controls when a full solution cannot land immediately.",
        "Maintain a prioritized change portfolio with status, risk, business impact, dependencies, resource needs, decision points, and expected outcomes.",
        "Use <b>effective communication</b> to convert complex control or audit issues into concise updates for technical contributors, business leaders, and external reviewers.",
        "Coordinate control testing and retesting, recording procedures performed, samples or evidence reviewed, exceptions identified, and conclusions reached.",
        "Build reusable templates for control narratives, evidence requests, issue logs, risk summaries, action plans, and governance meeting decisions.",
        "Support internal development standards by checking whether required reviews, testing, documentation, approvals, and operational handoffs occurred before release.",
        "Recommend future-state process changes using stakeholder input, recurring issue patterns, audit lessons, delivery constraints, and emerging AI risks.",
        "Track an illustrative 25-item audit and remediation worklist through status updates, owner follow-up, evidence review, and closure recommendations.",
    ]),
    ("Consultant | LatentView", "June 2022 - August 2024", [
        "Analyze business and technology workflows to identify control objectives, process risks, unclear ownership, evidence gaps, and opportunities for improvement.",
        "Document software development lifecycle steps, decision points, inputs, outputs, approvals, dependencies, and handoffs for stakeholder review.",
        "Support risk assessments by organizing assets, threats, vulnerabilities, existing safeguards, residual concerns, and recommended next actions.",
        "Review AI-related process proposals for data handling, review responsibilities, validation, traceability, monitoring, and escalation requirements.",
        "Prepare audit and control evidence requests with clear descriptions of the population, period, format, owner, due date, and expected support.",
        "Compare submitted evidence with control language to identify missing approvals, incomplete coverage, unexplained exceptions, and inconsistent documentation.",
        "Maintain issue logs and remediation trackers that distinguish root cause, interim action, target completion, validation evidence, and closure status.",
        "Facilitate working sessions with application, data, QA, security, and business contributors to resolve process ambiguity and assign accountable actions.",
        "Develop procedures and standards that make recurring control activities repeatable, reviewable, and easier to hand off to operational owners.",
        "Research complex process weaknesses by tracing requirements, implementation choices, testing evidence, change records, and operational outcomes.",
        "Recommend practical solutions that improve control coverage without creating unnecessary approvals, duplicate documentation, or unowned manual work.",
        "Support change initiatives by identifying critical dependencies, sequencing decisions, communication needs, and impacts across affected teams.",
        "Summarize risk themes, audit questions, open actions, and decisions needed for leaders managing competing priorities.",
        "Measure an illustrative 10-process review set through documented control objectives, evidence status, exceptions, and remediation recommendations.",
        "Prepare handoff materials covering process maps, control descriptions, issue status, evidence locations, review cadence, and escalation paths.",
    ]),
    ("Consultant | Reylon Softech", "June 2018 - June 2022", [
        "Gather requirements and document business processes, system dependencies, control expectations, and reviewable acceptance conditions.",
        "Support software lifecycle documentation by recording change scope, implementation tasks, test evidence, approvals, deployment steps, and support procedures.",
        "Identify process and technology risks involving data quality, access, change execution, dependency failure, incomplete testing, and unclear ownership.",
        "Create control checklists and evidence trackers for recurring reviews, approvals, validation steps, exception handling, and remediation follow-up.",
        "Coordinate audit-related questions with technical and business contributors, clarifying requested evidence and tracking responses to completion.",
        "Review documentation and test results for consistency with stated requirements, expected control behavior, and known exception paths.",
        "Research complex issues by comparing process descriptions, system behavior, records, logs, change history, and reproducible test outcomes.",
        "Recommend process improvements that make responsibilities, handoffs, evidence, and escalation paths clearer for delivery and support teams.",
        "Document technical decisions, operating procedures, dependencies, and unresolved risks so future work can begin from an auditable baseline.",
        "Track an illustrative 12-item control and remediation set through owner assignment, evidence collection, validation, and delivery handoff.",
    ]),
]

story = [Paragraph("Leena M", styles["Name"]), Paragraph("Texas, US  |  +1 (972) 776-4448  |  leenakrishna94@gmail.com", styles["Contact"]), HRFlowable(width="100%", thickness=0.8, color=colors.HexColor("#7B8794"), spaceAfter=5), Paragraph("Professional Summary", styles["Section"]), Paragraph(summary, styles["Body"]), Paragraph("Technical Skills", styles["Section"])]
for category, items in skills:
    story.append(Paragraph(f"<b>{category}:</b> {items}", styles["Skill"]))
story.append(Paragraph("Professional Experience", styles["Section"]))
for employer, date, bullets in experiences:
    story.append(KeepTogether([Paragraph(employer, styles["Employer"]), Paragraph(date, styles["Date"]), Paragraph(f"- {bullets[0]}", styles["ResumeBullet"])]))
    for bullet in bullets[1:]:
        story.append(Paragraph(f"- {bullet}", styles["ResumeBullet"]))
story.extend([Paragraph("Education", styles["Section"]), Paragraph("<b>Master's in Cybersecurity</b> | Saint Louis University", styles["Edu"]), Paragraph("May 2026", styles["Edu"])])

def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(colors.HexColor("#7B8794"))
    canvas.drawCentredString(LETTER[0] / 2, 0.38 * inch, f"Leena M  |  Sr IT Governance Analyst for AI  |  Page {doc.page}")
    canvas.restoreState()

doc = SimpleDocTemplate(str(PDF), pagesize=LETTER, rightMargin=0.66 * inch, leftMargin=0.66 * inch, topMargin=0.52 * inch, bottomMargin=0.58 * inch, title="Leena M - Sr IT Governance Analyst for AI Resume", author="Leena M")
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print(PDF)
