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
PDF = OUT / "Leena_M_Senior_AI_Python_Developer_Resume.pdf"

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

summary = (
    "Senior Consultant with 8+ years of experience translating enterprise workflows into production-oriented software, data, and integration solutions. "
    "Brings hands-on capability across <b>Python application development</b>, <b>Generative AI integration</b>, and <b>RAG and agentic workflows</b>, including prompt design, structured outputs, API contracts, retrieval, validation, testing, and secure data handling. "
    "Connects structured and unstructured data to usable services, investigates failure modes, and communicates trade-offs across application, data, DevOps, QA, cybersecurity, architecture, and business teams."
)

skills = [
    ("AI Application Engineering", "Python, Generative AI, LLM integration, Amazon Bedrock, boto3, prompt engineering, structured outputs, evaluation"),
    ("RAG and Intelligent Search", "RAG, embeddings, semantic search, vector retrieval, PostgreSQL, pgvector, intelligent search pipelines, citation grounding"),
    ("Agents and APIs", "AI agents, Strands Agents, agentic workflows, FastAPI, Pydantic, REST APIs, tool calling, schema validation"),
    ("Enterprise Data and Documents", "Structured and unstructured data integration, Amazon Textract, document extraction, data normalization, metadata and lineage"),
    ("Quality, Security, and Governance", "Automated testing, evaluation datasets, output validation, traceability, responsible AI, data protection, access controls, secure data handling"),
    ("Cloud and Operations", "AWS, Docker, PostgreSQL, observability, latency and token optimization, cost monitoring, reliability, deployment and support handoff"),
]

experiences = [
    ("Senior Consultant | Elevance Health", "February 2026 - Present", [
        "Translate stakeholder workflows and exception paths into Python service requirements, acceptance criteria, and production delivery slices for enterprise AI-assisted applications.",
        "Design bounded Generative AI capabilities on <b>Amazon Bedrock</b> with explicit user goals, source boundaries, fallback behavior, and human review points.",
        "Create reusable prompt templates with versioned instructions, structured outputs, and evaluation cases so changes can be compared before release.",
        "Build retrieval flows using <b>embeddings</b>, metadata filters, and <b>PostgreSQL/pgvector</b> to ground answers in approved business content.",
        "Add <b>citation checks</b>, source freshness checks, and abstention behavior when retrieved evidence is incomplete or contradictory.",
        "Implement <b>FastAPI</b> endpoints with <b>Pydantic</b> request and response models, making validation and error contracts visible at the service boundary.",
        "Use <b>boto3</b> clients and least-privilege service permissions to connect application flows to AWS-managed AI and document-processing capabilities.",
        "Prototype <b>AI agents</b> and bounded tool workflows with explicit tool schemas, authorization checks, timeout behavior, and human escalation.",
        "Integrate structured records and unstructured documents, preserving identifiers and provenance as information moves through extraction and retrieval stages.",
        "Apply <b>Amazon Textract</b> for document extraction where layout-aware text and table capture are more reliable than plain text ingestion.",
        "Design validation paths for malformed model responses, unavailable dependencies, empty retrieval results, and conflicting source records.",
        "Create automated tests for prompt regressions, schema adherence, retrieval grounding, tool authorization, sensitive-data exposure, and API failure handling.",
        "Compare latency, token usage, retrieval depth, and response quality to identify optimization opportunities; an illustrative review target is a 20% reduction in avoidable model calls.",
        "Instrument request, retrieval, tool, and model stages with trace identifiers so reviewers can follow a response from input through evidence and final output.",
        "Define output-quality review criteria covering factual support, completeness, refusal behavior, tone, and safe handling of ambiguous requests.",
        "Use <b>Docker</b> to package repeatable local and test environments, reducing setup differences across application, QA, and integration work.",
        "Document data contracts, prompt versions, model assumptions, deployment dependencies, rollback steps, and operational ownership for support teams.",
        "Coordinate with architecture, cybersecurity, QA, DevOps, data, and business partners to resolve dependencies before production release.",
        "Investigate failed responses by separating retrieval, prompt, model, authorization, data-quality, and downstream-service causes rather than treating every issue as model drift.",
        "Deliver review-ready implementation notes and test evidence for an illustrative 30-case evaluation set spanning normal, edge, adversarial, and abstention scenarios.",
    ]),
    ("Senior Consultant | Optum", "October 2024 - February 2026", [
        "Develop Python components that connect business workflows, enterprise data, and AI-enabled assistance while keeping deterministic rules in control of high-risk decisions.",
        "Design <b>RAG</b> pipelines that split, enrich, embed, retrieve, and rank content before passing a bounded context to an LLM.",
        "Use <b>PostgreSQL</b> and <b>pgvector</b> schemas for document chunks, embedding metadata, source identifiers, and retrieval diagnostics.",
        "Build <b>FastAPI</b> services that expose stable REST contracts for ingestion, search, generation, evaluation, and reviewer feedback.",
        "Apply <b>Pydantic</b> models for request validation, typed structured outputs, field-level constraints, and predictable client errors.",
        "Implement prompt templates for classification, extraction, summarization, question answering, and tool selection with reusable variables and version history.",
        "Run prompt and retrieval evaluations against representative questions, measuring grounding, completeness, citation coverage, abstention, and invalid-output rates.",
        "Add response validation and repair logic for missing fields, unsupported claims, malformed JSON, and citations that do not match retrieved sources.",
        "Build agent-style workflows with explicit step boundaries, tool allowlists, retry limits, and escalation paths for unresolved tasks.",
        "Integrate document intake and <b>Amazon Textract</b> extraction with downstream normalization, confidence checks, and exception queues.",
        "Use <b>Amazon Bedrock</b> model calls through <b>boto3</b>, centralizing configuration for model selection, temperature, token limits, and request timeouts.",
        "Connect unstructured content to structured business records while preserving record keys, document versions, and processing status for traceability.",
        "Create automated unit, integration, regression, and negative tests covering prompt injection, unauthorized tools, sensitive data, empty context, and dependency failures.",
        "Add exponential backoff, idempotency keys, and dead-letter handling to ingestion and model-dependent workflows to avoid duplicate or silently lost work.",
        "Profile retrieval depth, token counts, service latency, and cache opportunities; an illustrative test goal is a 15% improvement in median response latency.",
        "Define structured logs and trace identifiers for request, retrieval, model, and tool stages while excluding sensitive payloads from routine telemetry.",
        "Review AI controls with cybersecurity and governance partners, including authorization, retention, data minimization, audit evidence, and responsible-use boundaries.",
        "Package services with <b>Docker</b> and document environment variables, secrets handling, health checks, and deployment prerequisites for DevOps handoff.",
        "Maintain architecture notes, evaluation results, prompt changes, known limitations, and support procedures so decisions remain explainable after delivery.",
        "Collaborate with application, data, QA, and business teams to move an illustrative evaluation from 25 representative cases to a repeatable release gate.",
    ]),
    ("Consultant | LatentView", "June 2022 - August 2024", [
        "Analyze business processes and data flows to identify where Python automation, search, or AI-assisted review can reduce manual investigation without removing accountable review.",
        "Develop reusable Python utilities for ingestion, normalization, validation, matching, comparison, and repeatable data preparation.",
        "Build REST integrations with explicit request contracts, response handling, timeout behavior, and actionable error messages.",
        "Support retrieval experiments using document metadata, text chunking, embeddings, and similarity search to improve access to unstructured information.",
        "Prepare prompt templates for extraction, classification, summarization, and question answering, keeping instructions separate from dynamic context.",
        "Evaluate generated outputs for factual support, completeness, consistency, safe refusal, and usefulness using representative examples and reviewer feedback.",
        "Implement schema checks and comparison rules that catch missing fields, unexpected types, duplicate records, and inconsistent source values.",
        "Create test cases for normal paths, empty inputs, malformed responses, unavailable services, and authorization failures across integrated workflows.",
        "Document source lineage, processing assumptions, data-quality exceptions, and reviewer decisions so outputs can be reproduced and challenged.",
        "Coordinate with data and application contributors to align API payloads, source identifiers, transformation logic, and downstream expectations.",
        "Investigate processing discrepancies by tracing inputs, transformations, service calls, and output records rather than relying on surface-level symptoms.",
        "Use containerized development patterns and repeatable configuration to reduce environment drift between implementation and QA activities.",
        "Summarize technical trade-offs, delivery risks, and unresolved dependencies for stakeholders making prioritization and rollout decisions.",
        "Measure illustrative workflow scope through a 10-source comparison set and document the assumptions behind any quality or time-saving estimate.",
        "Prepare deployment notes, troubleshooting guidance, rollback considerations, and support handoff materials for operational teams.",
    ]),
    ("Consultant | Reylon Softech", "June 2018 - June 2022", [
        "Gather requirements from business users and convert process needs into implementation tasks, validation rules, and testable acceptance criteria.",
        "Build and maintain <b>Python</b> application integrations and API consumers with explicit input contracts, error handling, and recovery paths.",
        "Develop SQL transformations for normalization, deduplication, comparison, reconciliation, and repeatable reporting workflows.",
        "Create data-quality checks for missing values, invalid formats, unexpected duplicates, and mismatched source records.",
        "Implement REST request and response handling with timeouts, status checks, logging, and clear escalation behavior for failed dependencies.",
        "Write unit and regression tests that trace delivered behavior to requirements, acceptance criteria, and known failure scenarios.",
        "Support document and text-processing workflows by preserving source identifiers, processing status, and reviewer-visible exception details.",
        "Document technical decisions, operating procedures, dependency assumptions, and support guidance for delivery and stakeholder teams.",
        "Communicate implementation trade-offs, risks, and unresolved issues clearly while escalating decisions requiring accountable business or security owners.",
        "Track an illustrative 12-case regression set across data, API, and validation paths to make repeatable checks part of the delivery handoff.",
    ]),
]


story = [
    Paragraph("Leena M", styles["Name"]),
    Paragraph("Texas, US  |  +1 (972) 776-4448  |  leenakrishna94@gmail.com", styles["Contact"]),
    HRFlowable(width="100%", thickness=0.8, color=colors.HexColor("#7B8794"), spaceAfter=5),
    Paragraph("Professional Summary", styles["Section"]),
    Paragraph(summary, styles["Body"]),
    Paragraph("Technical Skills", styles["Section"]),
]
for category, items in skills:
    story.append(Paragraph(f"<b>{category}:</b> {items}", styles["Skill"]))

story.append(Paragraph("Professional Experience", styles["Section"]))
for employer, date, bullets in experiences:
    header = [Paragraph(employer, styles["Employer"]), Paragraph(date, styles["Date"])]
    story.append(KeepTogether(header + [Paragraph(f"- {bullets[0]}", styles["ResumeBullet"])]))
    for bullet in bullets[1:]:
        story.append(Paragraph(f"- {bullet}", styles["ResumeBullet"]))

story.extend([
    Paragraph("Education", styles["Section"]),
    Paragraph("<b>Master's in Cybersecurity</b> | Saint Louis University", styles["Edu"]),
    Paragraph("May 2026", styles["Edu"]),
])


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(colors.HexColor("#7B8794"))
    canvas.drawCentredString(LETTER[0] / 2, 0.38 * inch, f"Leena M  |  Senior AI/Python Developer  |  Page {doc.page}")
    canvas.restoreState()


doc = SimpleDocTemplate(
    str(PDF), pagesize=LETTER, rightMargin=0.66 * inch, leftMargin=0.66 * inch,
    topMargin=0.52 * inch, bottomMargin=0.58 * inch,
    title="Leena M - Senior AI/Python Developer Resume", author="Leena M",
)
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print(PDF)
