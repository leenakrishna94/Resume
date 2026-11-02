# Resume generation rules

## Inputs and independence

Use only the saved candidate facts in `profile.json`, the current JD, and explicit candidate-background corrections from the user. The JD is the only new input required for a normal run. If it is missing, empty, or still a placeholder, request it before writing the resume.

The user has explicitly stated that submitting a JD confirms they have performed its duties, used its named tools, and used similar tools for the same job purpose. Apply this standing confirmation to JDs they submit for their own resume generation, without repeatedly asking the same experience questions. Treat these claims as user-reported, not independently verified, and retain the source when saving them in `profile.json`. Apply later user corrections first.

This confirmation does not supply past employers, credentials, quantified achievements, exact dates, or years with each technology. Do not turn the hiring company's description, benefits, product names, or future work arrangement into candidate history.

Every run is independent unless the user has confirmed a project into `master-resume.json`. Do not reuse earlier generated summaries, keywords, technology lists, or unconfirmed achievements. The persistent profile is a fact log; it is not a dump list for the resume. Previous generated PDFs are not evidence. After the user explicitly confirms a project, later runs may select and reorder those confirmed bullets for the current JD. Do not write generated copy into the master store without that confirmation.

Apply each section's rules only to that section. Do not use Professional Summary length limits for Technical Skills, and do not turn Technical Skills into a prose paragraph. Do not apply Technical Skills inventory format to Professional Experience bullets.

## Current output scope

Render exactly this order:

1. Leena M
2. Texas, US | +1 (972) 776-4448 | leenakrishna94@gmail.com
3. A prominent horizontal line across the content width
4. Professional Summary
5. One tailored summary paragraph
6. Technical Skills
7. Role-specific category lines in `Category: item, item` format
8. Professional Experience, when executed
9. The recorded employment blocks defined in that section
10. Education
11. The locked Saint Louis University Master's block

Do not print a literal "Details" heading. Do not add certifications, photograph, links, extra locations, skill bars, proficiency scores, other degrees, or employers the user has not provided.

Write Professional Experience content only when the user explicitly asks to execute Experience against a real JD. Until then, keep the Experience rules in this file and do not invent a project or bullets. Education facts are locked; print them whenever a resume PDF is generated, after Experience if Experience is present, otherwise after Technical Skills.

## Contact details

This block is fixed and is not tailored to the JD.

- Name: Leena M
- Contact line: Texas, US | +1 (972) 776-4448 | leenakrishna94@gmail.com
- Then a prominent horizontal rule across the content width

Do not add a "Details" heading, location, links, photograph, or extra contact fields. There is no word-count rule for this block.

## Professional Summary

This section is prose. Measure it in words, not in skill-category count.

Write exactly ONE paragraph, starting with "Cybersecurity professional with 9+ years of experience". Continue the sentence naturally; do not print a literal ellipsis.

Length limitation: normally 90-120 words. Choose a count inside that range for the current JD. Do not add a narrower standing target such as 100-110 words. Use a shorter paragraph only when the available candidate evidence cannot support the normal length without repetition, filler, or invented claims. Do not pad to hit a number.

Before writing, infer the JD's actual professional function from its duties and deliverables, rather than relying on its title or technology keywords. Use that function to select and prioritize relevant candidate evidence. A JD describes job requirements; under the user's explicit standing confirmation above, its duties and named tools also represent their self-reported experience.

Lead with enterprise software development, application integration, production delivery, and problem-solving. Name specialized tools (Claude, Argus, FileNet, and similar) only when they are material to this JD's function. Do not open a general engineering summary with a niche stack.

Summarize supported candidate strengths relevant to that function:

- Core work personally performed, including end-to-end delivery where the JD is implementation work.
- Tools and methods personally used, with reusable engineering skills before optional specialty tools.
- Problem-solving contribution.
- Relevant delivery or validation capability.
- Business value: faster process, greater reliability, easier maintenance, less manual effort, or better user experience. Prefer verified metrics from the master store; otherwise typical consultant metrics remain allowed.

These are evidence-selection criteria, not a checklist to fill with unsupported claims. If a category lacks evidence, omit it and emphasize supported transferable strengths.

Check that the summary communicates relevant work or deliverables, rather than relying only on seniority, collaboration, and continuous learning. Those general qualities alone do not establish meaningful alignment to the JD's professional function. For an evaluation role, distinguish supported comparison, validation, analytical judgment, and documentation work from software implementation; do not imply direct chatbot-evaluation experience without evidence.

If facts outside the user's confirmed background and standing confirmation are essential to meaningful tailoring, identify the specific missing facts and prepare a clearly labeled proposed draft for review. Ask only about those missing details before turning them into experience claims. Do not present a generic fallback as a completed role-specific summary. Reuse background once confirmed so normal generation remains JD-only. Reviewer recommendations, scores, and sample paragraphs are suggestions unless the user explicitly confirms their activities as personal experience.

Technical depth must match both the work expectations and candidate evidence. Preserve real engineering contributions when job-relevant without automatically putting full-stack implementation first. Do not turn noncoding roles into coding portfolios. In the summary, prefer specifically named tools and the JD's core business problem; do not turn the paragraph into a skill inventory. General software delivery experience does not establish experience solving a specific JD problem.

DO:

- Be concrete, accurate, concise, and recruiter-readable, using third-person resume voice and natural keywords.
- Communicate differentiators through supported details about contributions, methods, delivery, validation, or business value.
- Connect relevant tools and methods to concrete deliverables and the JD's core business problem. Explain what the candidate produces or validates with those tools and how that work supports the needed business outcome. Avoid tool lists without an application, and do not invent implementations, results, or metrics to make the connection.
- Make each sentence add a distinct point. Prioritize relevant work and evidence over generic collaboration or learning statements.
- Include stakeholder and team collaboration, delivery progress, and continuous learning where relevant and supported.

DON'T:

- List employers, dates, or education in the summary, or name Truist, the project, or the hiring company.
- Describe the candidate as "interested in", "seeking", "hoping to", or "looking for" a role.
- Copy job requirements verbatim or narrate the target role instead of describing the candidate. Select and synthesize activities supported by the saved profile or the user's standing confirmation.
- List unrelated frameworks, technologies, or tools, or turn the paragraph into a keyword inventory.
- Claim unverified vendor platforms, certifications, domains, projects, metrics, degrees, leadership duties, or technical experience.
- Use generic "passionate" language, buzzwords, filler, repeated claims, or unsupported adjectives such as "expert" and "proven".
- Include scoring, research, evaluation-process commentary, or generation notes in the resume. This does not exclude supported professional evaluation or validation work when relevant to the job.

If a JD is outside the saved background, keep the professional identity accurate and briefly explain material gaps in the conversation, outside the resume. The workflow can accept any JD, but cannot manufacture qualifications for every job.

When Professional Experience has been generated for the current JD, the summary may use Truist-derived strengths (tools, problem-solving, design or evaluation work, integration, technical ownership, and outcomes) without naming Truist or the project. Do not describe a proposed design as a completed accomplishment. The summary presents professional strengths; it does not explain how the JD was matched.

## Technical Skills

This section is an ATS inventory. Do not apply a word count. Measure it in categories and items.

Generate a unique, technically precise, ATS-friendly Technical Skills section for every job description. Design it independently for the target position. Do not copy a previous resume's skill list. Do not dump `profile.json` confirmed technologies. Do not pause to ask the user to reconfirm tools.

The section must primarily reflect:

1. Exact JD technologies: relevant tools, platforms, languages, and frameworks named in the JD.
2. Closely related technologies that directly support the same job function.
3. A small, consistent foundation of general software and IT engineering capabilities usable across developers, admins, consultants, and analysts.
4. Engineering and product lifecycle practices that fit the duties.

Infer the job function from duties and deliverables first, not from the job title. A Software Engineer JD may be APIs, frontend, AI integration, or infrastructure. Extract named tools and methods from the current JD. Then select four tiers:

- Tier A: exact JD technologies (required, preferred, or poster-added). Lead with these. Keep poster-added skills if they appear in the JD; place odd extras in a matching category, not the opening line.
- Tier B: closely related and dependency tools needed to do the job, about 2-4 companions per core JD platform or method. Exact JD names stay first. For a BSA JD this includes backlog and documentation tools (Jira, Confluence), process-mapping (Visio or equivalent), and Excel or SQL for analysis.
- Tier C: an IT foundation that does not contradict the role: SQL; Git where software delivery is in play; Java, Python, and other basic languages used to read, query, or discuss delivery; troubleshooting; technical documentation; stakeholder collaboration. This is a visible foundation line, not a second dump of the profile.
- Tier D: engineering and delivery practices that match the function. Developer JDs: unit testing, code review, CI/CD, debugging, release management. BSA JDs: BRD, process mapping, requirements traceability, UAT. Do not mix those sets.

Include an item only if at least one is true:

1. It is explicitly named in the JD.
2. It is directly used in the primary job function.
3. It is a close substitute, successor, or predecessor for a required technology.
4. It is commonly used alongside the required platform in the same job.
5. It is a relevant foundational software-engineering skill that does not contradict the role.

Allowed relatedness for Tier B: same product family or rebrand; successor or predecessor of a named platform; companion module of the same suite; standard protocol or format already implied by named integrations; delivery tools named or clearly required by the same lifecycle.

Do not include popular unrelated stacks, competitors with a different job purpose, hiring-company product names, certifications, leftover tools from earlier JDs, random web frameworks, analyst BI tools on an implementation JD unless named, or evaluation-only skills on a development JD (and the reverse). Do not invent vendor products, cloud brands, or languages that fail the five questions.

Record JD-named tools in `profile.json` as user-reported. Do not persist Tier B similar-only names into the global technology list.

Choose 5-7 function-specific category names designed for this JD. Do not reuse a permanent Programming Languages / Cloud / Tools template. Put the highest-value category first. Group each skill under its technical function. Prefer relevance over total keyword count. Cut unrelated stacks, redundant labels, vague fillers, leftover tools from earlier JDs, and hiring-company products.

Do not reuse a developer template for an analyst JD. Format each line as `Category Name: Tool, Tool, Tool` with no tables, bars, or ratings. Put the most important supported JD technologies first in their category. Put foundation and lifecycle last or in a Delivery Practices line. One section heading: Technical Skills. Keep overlapping soft items (collaboration, documentation, reporting) on one line, not repeated across categories. Specialized tools rise or fall with the JD; keep SQL, Git, APIs, testing, debugging, and security visible when they fit the function.

Use standard capitalization and grammar:

- Technical Skills items are sentence-case per item: capitalize the first letter of each comma-separated item; keep the rest lowercase unless it is a product name or acronym. Example: Requirements gathering, Functional analysis, Functional requirements, BRD, FRS, Gap analysis, Use cases, Impact analysis. Same pattern for User stories, Acceptance criteria, Stakeholder management, Communication, Documentation, Data mapping, Interface requirements, Adverse event intake.
- Product and language names: Jira, Confluence, Visio, Lucidchart, Azure DevOps, Excel, SharePoint, SQL, Java, Python, Git.
- Practices and domain labels: Agile, Scrum, SDLC, UAT, BRD, FRS, Patient Safety, Pharmacovigilance, Drug Safety, Life Sciences, Pharma.
- STAR bullets are sentence case with the first word capitalized, correct subject-verb agreement, and no misspellings (for example, requirements not “requierment”). Do not all-caps entire bullets. Do not write JIRA.

QA: each comma-separated skill item starts with an uppercase letter or an allowed acronym.

Before writing the PDF, check all of the following. Do not print this checklist in the resume:

1. The skills section alone identifies the target role.
2. The most important supported JD technologies appear prominently.
3. Selected similar technologies are closely related to the JD.
4. Unrelated frameworks, platforms, programming languages, and leftover tools from other JDs are removed.
5. Foundation languages and practices appear without drowning JD-named methods.
6. Engineering and product lifecycle practices are included where appropriate.
7. Category names match the specialization.
8. The content is different from resumes generated for unrelated positions.
9. The final result is technically coherent and ATS-readable.
10. Skill names use the capitalization and grammar rules above.
11. Each current JD Key Requirement appears in Technical Skills, and in Experience or Summary according to Case A–D.

## Professional Experience

This section is a job history block. Do not apply the summary word count. Do not format it as a skills inventory.

Generate Experience only after an explicit execute request and a usable current JD. Use the JD in the conversation or `inputs/job-description.txt`. Infer the JD's actual professional function from duties and deliverables. Do not reuse a previous resume's project, bullets, or technology list.

Employment facts come only from `profile.json` or explicit user corrections. Recorded roles, newest first:

- Employer: Truist Financial Corporation. Title: Senior Software Consultant. Dates: August 2024 – Present. 15–20 STAR bullets.
- Employer: PointClickCare. Title: Software Consultant. Dates: October 2022 – August 2024. 12–15 STAR bullets.
- Employer: Union Bank of India. Title: Software Consultant. Dates: December 2019 – June 2022. 7–10 STAR bullets. Technologies must have existed and been usable in that window.
- Employer: Scanet Trading PVT. LTD. Title: Software Consultant. Dates: June 2016 – November 2019. 5 STAR bullets. Technologies must have existed and been usable in that window. Do not make Scanet look like a modern cloud or AI-infrastructure engagement.

Do not add other employers. Do not infer these facts from a JD. Standing confirmation covers JD duties and named tools, not company industry. Represent ownership at Software Consultant level; do not invent direct reports, budgets, or company-wide authority. Generated project wording is user-directed resume copy; do not save it as confirmed background unless the user later confirms it. Do not store a generated project as the next run's template.

For every recorded employer, run this method independently. Do not hardcode a permanent project name per company.

1. Facts: name, title, and dates from `profile.json` only.
2. Domain: use the employment row's `domain` if present; otherwise research that employer publicly at generate time. Do not invent a new industry so the job matches the JD.
3. Timeline: only product types and tools that existed and were usable in that window.
4. JD capabilities, not JD industry: infer the current JD's professional function (for example technical demos, solution design, implementation, evaluation). Map those capabilities into a problem that employer would actually have.
5. Pick one problem: different users, systems, and operational reality from the other jobs on the same resume. Internally consider several domain-valid options, then keep one. Do not reuse another employer's story. Do not auto-select fraud, collections, inventory, or the hiring company's industry for every employer.
6. Tools: apply Case A–D before naming a JD tool.
7. Voice: no hiring-company name, no cloned JD sentences, no generation notes. If a tool is omitted, do not print that it was omitted. Typical resume-style quantified results are allowed when they are plausible for consultant-level work on that project. Do not invent awards, certifications, degrees, or employer names. Do not copy numbers from sample-resume sites.

Case A–D:

- Case A: available in that period and supported in that employer's domain — use the exact name.
- Case B: available but not a fit as named — use a comparable period-valid tool.
- Case C: released after that job ended — exclude it.
- Case D: does not fit the employer's domain — do not force it.

QA: if two jobs could swap company names and still read true, regenerate the weaker one. Summary and Technical Skills stay JD-tailored. Experience stays employer-domain-tailored.

Creativity preference is temperature 0.9 equivalent: internally consider several plausible problems inside that employer's domain and years, then keep one coherent story. Creativity must not invent awards, certifications, unrelated stacks, or the target hiring company's product names.

Internally convert the selected problem into a business requirement. Do not print this analysis on the resume:

- Situation: which process or application has the issue
- Problem: limitation, inefficiency, integration failure, or operational gap
- Impact: users, operations, data, reliability, or delivery
- Requirement: capability to introduce or improve
- Success criteria: what a successful solution must accomplish

Build one project using only steps that fit the JD function. Omit unused architecture:

1. Requirements analysis
2. Technical architecture
3. Technology selection: tools that pass Case A–D for this employer; JD-named tools only when they pass; companions only if needed and allowed by Technical Skills relatedness rules
4. Implementation: depth must match the role. For a BA or evaluation JD, core work is requirements, analysis, evaluation, documentation, and UAT, not a coding portfolio. For an implementation JD, core work is design, build, and integrate
5. Integration
6. Security and reliability, only if relevant
7. Testing and validation
8. Deployment or operational readiness, only if relevant
9. Business outcome. Typical quantified results are allowed when plausible; do not copy sample-resume percentages or invent awards.

For each major JD technology used in the project, internally know why it is needed, what it does, which component uses it, how it interacts with other tools, what work it requires, and which problem it helps solve. Use exact technology names. Do not repeat tools only for ATS. Do not claim personal implementation of a platform that fails the inclusion rules.

Leadership must be technical ownership appropriate to a Senior Software Consultant: owning design of a feature or component, translating requirements into deliverables, guiding architecture or approach, leading design discussions, breaking work into tasks, collaborating with business, architecture, QA, and engineering, performing design or code reviews, resolving cross-system dependencies, driving root-cause analysis, setting test and release-readiness criteria, knowledge transfer, and coordinating critical milestones. Do not claim people-management or company-wide authority unless the user provided those facts.

Printed structure, newest employer first. Each job is one consistent technical story:

- Heading: Professional Experience (once)
- `Title | Employer`
- Dates
- Project: a specific business-oriented name
- Business Context: one concise paragraph
- Project Solution: one technically substantial paragraph
- Technology Environment: comma-separated list grounded in this employer's domain, period, and JD tools that pass Case A–D
- Responsibilities: STAR bullets in descending count (Truist 15-20, PointClickCare 12-15, Union Bank 7-10, Scanet 5). Prefer a shorter set of strong bullets over filler. Most bullets follow problem, action with a named tool or method, deliverable, and a business result (speed, reliability, maintainability, less manual work, or UX). Prefer verified metrics from `master-resume.json`; otherwise typical consultant metrics remain allowed. Not every line must use the same sentence template.

Show end-to-end delivery at JD-appropriate depth: gather requirements, design, implement, test, deploy, and maintain. Show technical ownership of components, decisions, code reviews, integration issues, and release readiness. Do not claim unconfirmed people-management.

Do not clone the same testing, stakeholder, documentation, or integration theme across employers. Banking, healthcare, and trading jobs must show different problems and solutions. Include troubleshooting and production support (root-cause analysis, incidents, defects, monitoring, performance) where Case A–D allows.

Do not use Hire IT People or other public resume databases as candidate facts or as text to copy. Use them only as style for action, tool, and outcome.

Every Technical Skills item, including similar and dependency tools, must appear in Experience (Technology Environment or a STAR bullet) on at least one employer where it passes Case A–D. Fold extra names into Technology Environment when a new bullet would be filler. If a skill fails Case A–D for every employer, keep it in Skills and Summary only; do not force it onto the wrong domain.

DO:

- Use only recorded employer blocks with their titles, dates, and descending STAR ranges.
- Use exact JD tool names only when they pass Case A–D for that employer.
- Match technical depth to the JD function mapped onto that employer's domain.
- Show senior-consultant technical ownership.
- Generate independently for each JD and each employer.
- Research each recorded employer publicly at execute time if needed for a realistic, period-valid problem.

DON'T:

- List employers the user did not provide.
- Copy JD sentences as bullets or name the hiring company.
- Invent awards, certifications, or degrees beyond the locked Education block, or copy sample-resume metrics.
- Reuse a previous resume's project or bullets.
- Dump unrelated profile technologies.
- Print generation process, scores, temperature, or research notes on the resume.
- Claim platforms that fail the five inclusion questions.
- Copy JD launch channels, industries, or product names into jobs when they fail the period or domain test.
- Clone the same problem, testing story, stakeholder story, or integration story across employers with only the company name changed.
- Print defensive process lines such as unused-tool disclaimers or "without inventing metrics".
- Turn a noncoding JD into a coding portfolio, or an implementation JD into evaluation-only work.

## Education

This section is a fixed academic block. Do not tailor it to the JD. Do not apply the summary word count. Do not format it as skills or STAR bullets.

Locked facts, unless the user explicitly updates them:

- University: Saint Louis University
- Degree: Master's in Cybersecurity
- Duration: May 2026

Print after Professional Experience when Experience is on the resume. If Experience has not been executed, print Education after Technical Skills.

Printed structure:

- Heading: Education (once)
- `Master's in Cybersecurity | Saint Louis University`
- Dates: May 2026 (ASCII hyphen)

Keep one entry. Do not add a second school, bachelor's degree, GPA, coursework, thesis, honors, clubs, or location line beyond the provided institution name. Do not infer this degree from a JD.

DO:

- Use the locked university, degree, and dates exactly.
- Keep Education independent of the current JD.
- Place it last on the resume.

DON'T:

- Invent GPA, coursework, honors, thesis, or additional degrees.
- Change the university name, degree wording, or dates to match a JD.
- Add certifications or training under Education unless the user later records them as Education facts.
- Use Education as a keyword dump for ATS.
- Print research notes or "locked" labels on the resume.

## PDF layout

Use a single column, US Letter page, equal 0.7-inch margins on all four sides, black text on white, and Times New Roman. Initial defaults: 20-point bold name, 10-11-point contact line, 12-point bold section heading, and 11-point body text with comfortable line spacing.

Justify Professional Summary, skill lines, project narrative, and STAR bullets. Keep the name, section headings, job titles, and date lines left-aligned. Bold named tools, JD methods, domain labels, and quantified results inside bullets and Technology Environment; do not bold entire sentences.

Use a roughly 1.5-point horizontal rule below the contact block. Keep the name and contact details in the document body, not a page header or footer. Use real selectable text in a logical reading order. Avoid tables, text boxes, icons, images, multi-column layouts, hidden keywords, and decorative elements other than the requested divider. Do not shrink text or pad the summary merely to fill the page. After Experience is executed, additional pages are allowed; do not shrink font or margins to force a page count.

Until Experience is executed, keep contact details, Professional Summary, Technical Skills, and Education on one US Letter page at the default fonts. That one-page target is not a word-count rule for skills. If that document does not fit, trim weak Tier B or Tier C skill items first. After Experience is executed, additional pages are allowed. Do not shrink summary text to force Experience or Education onto one page.

## Generation and delivery

1. Check that the current JD contains usable job information.
2. Infer the JD's actual professional function from duties and deliverables.
3. Draft Professional Summary using that section's rules, including one paragraph, the required opening, and a length chosen inside 90-120 words. Do not name Truist or the project in the summary.
4. Independently design Technical Skills using that section's four tiers, five inclusion questions, category/item limits, and nine-point QA. Do not interrupt the user for tool confirmation. Do not apply the summary word count here.
5. Generate Professional Experience only when the user explicitly asks to execute it. Follow that section's problem-to-requirement process, printed structure, descending STAR ranges (18 / 14 / 8 / 5 as typical targets inside 15-20 / 12-15 / 7-10 / 5), and DO/DON'T list. Do not generate Experience during a rules-only pass.
6. Print Education from the locked facts in `profile.json`. Do not tailor it. Do not invent academic extras.
7. Check every experience claim against its candidate source. Confirm appropriate technical depth, natural keywords, and no prohibited content. Remove unsupported claims; mention material gaps briefly outside the PDF when needed.
8. Fill the template without leaving placeholders or process notes in the resume.
9. Create `output/pdf/YYYY-MM-DD/` from the run date when needed and save a descriptive file such as `Deep_G_<role>_<unique-run-id>.pdf`. Same-day runs share that folder. Keep previous files unless the user requests replacement, and do not read them as input.
10. Extract the PDF text and confirm the exact contact details, correct reading order, complete summary, Technical Skills lines, Experience content when present, and the locked Education block.
11. Render and inspect the PDF for clipping, overlap, broken characters, and readable spacing.
12. Deliver the PDF link. Do not claim that an ATS will accept it or that it guarantees an interview.
