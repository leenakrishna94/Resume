from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import HRFlowable, KeepTogether, Paragraph, SimpleDocTemplate

ROOT = Path(__file__).parent
OUT = ROOT / "output" / "pdf" / "2026-11-05"
OUT.mkdir(parents=True, exist_ok=True)
PDF = OUT / "Leena_M_Sr_Developer_Randstad_Digital_Resume.pdf"

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

summary = ("Senior Consultant with 8+ years of experience analyzing requirements, developing software applications, and supporting large-scale IT delivery across UI, backend, API, database, and cloud concerns. "
           "Brings a full-stack delivery mindset across <b>C#/.NET services</b>, <b>Angular interfaces</b>, REST APIs, SQL, microservices, CI/CD, unit testing, and infrastructure automation. "
           "Experienced in researching complex technical problems, documenting decisions, and collaborating with business, QA, architecture, DevOps, and IT teams to deliver maintainable solutions with clear validation and operational handoffs.")

skills = [
    ("Application Development", "C#, .NET, backend services, Angular, TypeScript, full-stack development, object-oriented programming"),
    ("APIs and Architecture", "REST APIs, microservices, API integration, service contracts, authentication, error handling, distributed workflows"),
    ("Data and Databases", "SQL, DB2, relational databases, data access, schema-aware development, query optimization, data validation"),
    ("Cloud and Infrastructure", "AWS, Azure, cloud application support, Terraform, infrastructure as code, configuration and environment management"),
    ("Delivery and Source Control", "GitHub, Azure DevOps, CI/CD pipelines, code review, branching, build automation, deployment coordination"),
    ("Quality and Support", "Unit testing, development testing, integration testing, troubleshooting, technical research, documentation, production support"),
]

experiences = [
    ("Senior Consultant | Elevance Health", "February 2026 - Present", [
        "Analyze business and technical requirements for enterprise software changes, clarifying process rules, dependencies, exceptions, and acceptance conditions.",
        "Design full-stack delivery slices spanning <b>Angular</b> UI behavior, <b>C#/.NET</b> services, REST APIs, data access, and deployment configuration.",
        "Write and modify backend application code with clear service boundaries, input validation, error handling, and maintainable extension points.",
        "Build <b>REST APIs</b> that expose explicit request and response contracts for UI clients, downstream services, and integration workflows.",
        "Implement <b>microservices</b> patterns for independently deployable capabilities, separating domain logic from transport, persistence, and configuration concerns.",
        "Develop Angular components and TypeScript client logic that surface validation feedback, service states, and actionable errors to users.",
        "Create SQL queries and data-access routines for relational workflows, checking joins, null behavior, transaction boundaries, and result correctness.",
        "Support <b>DB2</b>-connected application flows by tracing schema definitions, stored behavior, query assumptions, and integration-side transformations.",
        "Add unit tests around business rules, service methods, controllers, validators, and data-mapping logic before changes move through the delivery pipeline.",
        "Perform development testing for normal, boundary, invalid-input, dependency-failure, and authorization scenarios, recording defects and retest evidence.",
        "Research complex technical problems by isolating UI, API, database, network, configuration, and deployment variables before recommending a solution.",
        "Use <b>GitHub</b> workflows for branching, pull requests, review feedback, merge coordination, and traceability between code and work items.",
        "Maintain <b>CI/CD pipelines</b> that build, test, package, and promote application changes with environment-specific configuration checks.",
        "Automate repeatable cloud configuration with <b>Terraform</b>, keeping infrastructure changes reviewable and aligned with application deployment needs.",
        "Coordinate <b>AWS</b> application support across configuration, identity, logging, networking, and managed-service dependencies.",
        "Investigate defects by comparing expected behavior with logs, request payloads, SQL results, deployed configuration, and reproducible test cases.",
        "Document API behavior, data assumptions, test coverage, technical decisions, deployment prerequisites, and support procedures for continued operation.",
        "Work with QA, DevOps, architecture, cybersecurity, business, and application teams to resolve delivery blockers and clarify ownership.",
        "Recommend implementation options by weighing maintainability, compatibility, performance, operational risk, and the effort required to change existing platforms.",
        "Deliver an illustrative development-test pack covering 30 representative UI, API, database, and failure-path cases for release review.",
    ]),
    ("Senior Consultant | Optum", "October 2024 - February 2026", [
        "Translate business requirements into technical work items, component responsibilities, acceptance criteria, and testable delivery increments.",
        "Develop <b>C#</b> and <b>.NET</b> backend functionality for complex application workflows, preserving existing contracts while adding new behavior.",
        "Implement service endpoints with request validation, structured responses, status handling, and consistent error messages for consuming applications.",
        "Build and maintain <b>Angular</b> screens that coordinate user input, API calls, loading states, validation messages, and recoverable failures.",
        "Design API integrations between application services and enterprise systems, documenting payloads, authentication assumptions, retries, and timeouts.",
        "Apply <b>microservices</b> decomposition where it improves ownership and release independence without hiding important transaction or data dependencies.",
        "Write SQL for data retrieval, updates, reconciliation, and exception analysis, checking query plans and result sets against business expectations.",
        "Support relational database work involving <b>DB2</b> schemas, legacy integration behavior, connection settings, and data-quality exceptions.",
        "Create unit tests for domain logic, controllers, API clients, mapping code, and negative paths, using failures to refine implementation boundaries.",
        "Perform development testing locally and in shared environments, validating code changes against representative records and documented acceptance criteria.",
        "Maintain <b>Azure DevOps</b> work items, pull-request context, build results, release notes, and evidence linking implementation to requirements.",
        "Use <b>CI/CD</b> automation to run builds, unit tests, packaging, and deployment checks consistently across development and test stages.",
        "Manage source changes through <b>GitHub</b> branching and review practices, resolving conflicts and incorporating technical feedback before merge.",
        "Support cloud-hosted services in <b>AWS</b> by reviewing configuration, logs, permissions, environment variables, and service dependencies.",
        "Define <b>Terraform</b> changes for repeatable infrastructure configuration, reviewing plan output and dependencies before applying environment updates.",
        "Research production-like defects by reproducing request paths, examining logs and database records, and separating code defects from configuration issues.",
        "Document setup steps, API contracts, database assumptions, troubleshooting decisions, and handoff information for developers and support teams.",
        "Collaborate with application, QA, DevOps, data, architecture, and business partners to prioritize fixes and resolve ambiguous requirements.",
        "Recommend solutions for complex technical problems, explaining trade-offs among short-term compatibility, long-term maintainability, and delivery risk.",
        "Track an illustrative 25-case regression suite across UI, service, database, and integration changes as a repeatable release-readiness gate.",
    ]),
    ("Consultant | LatentView", "June 2022 - August 2024", [
        "Analyze requirements and data flows to define application changes, integration points, validation rules, and measurable acceptance conditions.",
        "Develop reusable <b>C#/.NET</b> components for backend processing, service orchestration, and business-rule execution.",
        "Build REST integrations with explicit payload contracts, status checks, timeout behavior, and actionable diagnostic messages.",
        "Support <b>Angular</b> and TypeScript client behavior by connecting forms, API responses, validation, and user-facing exception states.",
        "Implement SQL transformations and data-access routines for normalization, comparison, reconciliation, and repeatable reporting workflows.",
        "Investigate <b>DB2</b> data issues by comparing source records, query behavior, integration mappings, and expected business outcomes.",
        "Create unit tests and development checks for service methods, data transformations, validators, and integration adapters.",
        "Use CI/CD build checks and pull-request reviews to catch compilation, test, packaging, and configuration issues before deployment.",
        "Maintain GitHub or equivalent source-control practices for branching, review comments, change traceability, and controlled merges.",
        "Support cloud application changes by documenting environment configuration, secrets assumptions, service dependencies, and rollback considerations.",
        "Research complex technical problems using logs, code paths, database results, dependency behavior, and focused reproduction cases.",
        "Prepare technical documentation covering component behavior, API contracts, data assumptions, test evidence, and operational troubleshooting.",
        "Coordinate with business, QA, application, and platform contributors to clarify defects, prioritize work, and confirm expected behavior.",
        "Recommend implementation alternatives by comparing effort, compatibility, performance, supportability, and the risk of changing shared components.",
        "Measure an illustrative 10-source comparison workflow through repeatable development tests and documented exception outcomes.",
    ]),
    ("Consultant | Reylon Softech", "June 2018 - June 2022", [
        "Gather software requirements and translate process needs into implementation tasks, validation rules, and testable acceptance criteria.",
        "Write and modify <b>C#</b> application code and service integrations with clear input contracts, error handling, and maintainable control flow.",
        "Develop SQL queries and transformations for validation, normalization, deduplication, comparison, and reconciliation workflows.",
        "Support relational database and <b>DB2</b>-connected processes by tracing schemas, data mappings, connection assumptions, and exceptions.",
        "Implement API request and response handling with status checks, timeouts, logging, and escalation behavior for failed dependencies.",
        "Create unit and regression tests that trace application behavior to requirements, acceptance criteria, and known failure scenarios.",
        "Use source control and review practices to organize changes, incorporate feedback, and preserve traceability across software releases.",
        "Document technical decisions, setup steps, operating procedures, dependencies, and support guidance for delivery and stakeholder teams.",
        "Research complex defects and recommend solutions by comparing code, data, configuration, logs, and reproducible test results.",
        "Track an illustrative 12-case regression set across API, data, and validation paths as part of the delivery handoff.",
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
    canvas.drawCentredString(LETTER[0] / 2, 0.38 * inch, f"Leena M  |  Sr Developer  |  Page {doc.page}")
    canvas.restoreState()

doc = SimpleDocTemplate(str(PDF), pagesize=LETTER, rightMargin=0.66 * inch, leftMargin=0.66 * inch, topMargin=0.52 * inch, bottomMargin=0.58 * inch, title="Leena M - Sr Developer Resume", author="Leena M")
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print(PDF)
