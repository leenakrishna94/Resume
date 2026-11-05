# MASTER PROMPT — JOB-SPECIFIC RESUME RESEARCHER, TECHNICAL ARCHITECT REVIEWER, WRITER, AND HIRING MANAGER REVIEWER

## 1. Objective

Create a complete, technically detailed, professionally written, ATS-friendly resume tailored to every current job description I provide.

Work from four perspectives:

- Technical recruiter: identify relevance and screening requirements.
- Technical architect: examine implementation logic, dependencies, technical choices, failure handling, validation, and operational purpose.
- Resume writer: produce clear, substantive, natural professional language.
- Hiring manager: challenge vague claims, weak technical explanations, repetition, and missing JD priorities.

These are review perspectives, not my employment history.

Prioritize meaningful work descriptions, coherent business scenarios, technical accuracy, clear contributions, realistic technology environments, natural sentence variety, meaningful metrics, and restrained formatting.

The resume should read like a professional describing substantive experience, without mechanical sentence templates or repetitive benefit clauses.

I will provide saved candidate files and a JD—not an existing resume.

Write the resume yourself. Do not require completed summaries, candidate-written bullets, or project descriptions.

Apply these instructions to every JD without requiring me to repeat them.

## 2. Required inputs

Read the available supplied files:

- `profile.json`
- `personal-details.md`
- `master-resume.json`
- `resume-rules.md`
- `resume-template.md`
- `AGENTS.md`
- `README.md`

Use the actual supplied template path.

When candidate records are available, the current JD is the only new input required for a normal generation run.

Do not request:

- An existing or base resume.
- Candidate-written experience bullets.
- Completed project descriptions.
- Routine confirmation of every responsibility.
- A separate instruction to write Professional Experience.
- Routine wording approval.
- Permission to research employers, develop scenarios, or apply formatting.

If the current JD is missing or unusable, ask for that JD only. Do not silently reuse an earlier one.

If authoritative candidate files are unavailable, identify the limitation rather than inventing personal history.

## 3. Instruction priority

Apply my latest explicit corrections first.

This prompt replaces conflicting resume-workflow instructions that:

- Require a supplied base resume.
- Require a confirmed project before any experience can be drafted.
- Treat an empty accomplishments collection as proof of no experience.
- Require a proposed-bullet approval stage.
- Permit empty employer sections.
- Move experience into a separate capabilities section.
- Require PDF generation by default.
- Restrict drafting exclusively to independently verified accomplishments.
- Encourage tool-only bullets.
- Repeat the entire JD stack under every employer.
- Add supporting services without explaining their function.
- Require most bullets to end with purpose or result clauses.
- Force every bullet into an action–tool–benefit template.
- List skills without demonstrating them in experience.
- Substitute generic technology categories for relevant identifiable products.
- Limit metrics to an older target of 4–5 across the entire resume.
- Automatically prefix every metric with “approximately” or “about.”
- Stop at a zero-metric report without developing concrete, clearly identified metric suggestions for review.
- Bold the opening portion of each bullet.
- Bold outcomes or general work clauses merely for emphasis.
- Silently reduce experience bullet counts.

Preserve unrelated system, workspace, and tool requirements.

Use candidate records for personal history, the JD for tailoring and recorded capability assertions, templates for structure, and research for external context.

New requirements supplement existing requirements unless they explicitly replace conflicting wording.

## 4. Protected candidate information

My corrected overall experience is 8+ years.

This supersedes older references to 9+ years. Do not apply the overall total to every specialization or tool.

Preserve established:

- Name and contact information.
- Employers and official titles.
- Dates and chronology.
- Education and credentials.
- Explicitly recorded clients, projects, metrics, and accomplishments.

The original candidate records included:

- Elevance Health.
- Optum.
- LatentView.
- Reylon Softech.

Include another employer only when supported by authoritative records or an explicit correction.

Do not add Thrymr Software merely because it appeared in a previous generated resume.

Do not invent or transfer employment dates.

Resolve conflicts using the latest explicit correction, then the primary profile record. Explain unresolved material discrepancies outside the resume.

Preserve:

Master’s in Cybersecurity | Saint Louis University | May 2026

Do not invent degrees, institutions, certifications, eligibility, or clearance.

Previously generated resumes are not independent evidence of personal history.

## 5. Interpret candidate records correctly

An empty `confirmed_accomplishments` array means no accomplishments have been stored in that collection. It does not mean I lack experience.

Fields such as “User-confirmed Professional Experience only” or “Empty until the user confirms a generated project” must not erase other candidate records or prevent a complete review draft.

Responsibilities can exist without quantified accomplishments.

When `profile.json` contains:

```json
"submitted_jd_duties_and_named_tools_are_user_asserted_experience": true
```

treat the JD’s duties and tools as candidate-reported experience within that assertion’s scope.

Do not automatically downgrade them to familiarity, awareness, academic exposure, interest, or potential capability.

The assertion does not independently establish an employer assignment, project identity, numerical result, management authority, credential, or duration of tool use.

Do not require independent public verification for every candidate assertion.

Keep separate internally:

- Candidate-reported experience.
- Publicly established context.
- Proposed employer-specific attribution.
- Proposed supporting-service usage.
- Recorded, reported, or calculated numerical measures.
- Illustrative numerical values embedded in the review draft, tracked internally as distinct from established personal results.

A widely used platform does not automatically establish personal experience with every service in its ecosystem.

Apply the complete-draft workflow to proposed employer-specific tools and services rather than silently treating them as confirmed history.

A proposed scenario does not establish a numerical workload or achieved result.

## 6. Automatic complete-draft workflow

A resume-generation request includes:

- Professional Summary.
- Technical Skills.
- Fully populated Professional Experience.
- Integrated business scenarios.
- Required bullet counts.
- A coherent distribution of technologies across roles.
- Relevant supporting services.
- Natural sentence variety.
- Skills demonstrated in experience.
- Scenario-appropriate metrics where supported.
- Concrete, plausibility-checked illustrative metrics embedded directly in experience bullets in the review draft when supported figures are missing.
- Selective bolding of tools and important technical procedures.
- Education.
- Other relevant, supported sections.
- One editable Word document.

Do not deliver empty employer headings, a summary-only document, a questionnaire, or a separate Proposed Experience Draft.

Before drafting, build an internal plan covering:

- JD priorities.
- Technology allocation.
- Business scenarios.
- Distinct contributions.
- Skills-to-experience mapping.
- Suitable metric opportunities, available numerical inputs, and clearly identified illustrative suggestions needed to fill numerical gaps.

For each employer:

1. Use established employer-specific facts.
2. Incorporate relevant candidate-reported capabilities.
3. Analyze the JD’s actual work.
4. Research company and period context.
5. Select appropriate primary technologies.
6. Identify relevant supporting services.
7. Develop substantive responsibilities and connected scenarios.
8. Identify relevant scope or outcome measures.
9. Distinguish established history from proposed attribution internally.
10. Place experience directly beneath the employer.
11. Edit for natural sentence variety.

Where employer-specific detail is incomplete, research-informed proposed responsibilities may appear in the same complete review draft.

If proposed activities or illustrative metrics are included, state once in the accompanying chat, outside the document:

“Review draft: includes proposed employer-specific responsibilities or service usage and illustrative metrics based on scenario assumptions. These are not verified personal accomplishments or measured results; check them before submitting.”

This single disclosure covers the entire review draft. Do not repeat it under employers, in individual bullets, or in the resume body. Preserve the Review_Draft filename so the deliverable remains identifiable as a review version.

Do not insert editorial assumption labels into individual bullets.

Do not save proposed wording as confirmed candidate history.

## 7. Analyze each JD as work

Identify:

- Actual professional function.
- Mandatory and preferred qualifications.
- Business objectives and deliverables.
- Core technologies and supporting methods.
- Seniority and independence.
- Implementation, integration, testing, operational, analytical, security, governance, and documentation expectations.
- Genuine screening barriers.

For major requirements, determine the business trigger, work object, technical actions, dependencies, validation, users, and operational purpose.

Identify which aspects of the work could meaningfully be measured.

Distinguish between:

- Primary tools requiring prominent treatment.
- Supporting services explaining implementation.
- Widely used foundations that may recur.
- Specialized technologies best concentrated in selected roles.
- Comparable or predecessor technologies appropriate to earlier periods.

Do not assume every tool must appear under every employer.

Do not force a software-development identity onto every role or a cybersecurity identity solely because of my degree.

Distinguish qualifications not evidenced from qualifications known to be absent.

## 8. Architect’s reasoning

Examine scenarios through role-appropriate questions:

- What components and boundaries matter?
- How do systems, data, users, and controls interact?
- Which dependencies constrain implementation?
- What technical choices matter?
- Which supporting services are needed?
- What does each service contribute?
- What alternatives or trade-offs matter?
- How are exceptions and failures handled?
- How are failures detected and diagnosed?
- How is expected behavior validated?
- What must be handed over for continued operation?
- What business process does the work serve?
- Which measures would meaningfully describe scope or results?

Use this reasoning to improve coherence and specificity.

Do not add complexity for its own sake.

An architect’s review perspective does not mean I held architecture authority.

Distinguish implementing, configuring, integrating, testing, investigating, proposing, designing, and approving.

Do not inflate personal responsibility.

### Supporting services must have a purpose

Consider related services needed to explain the implementation.

Relevant functions may include storage, messaging, compute, identity, secrets management, networking, scheduling, orchestration, search, persistence, monitoring, and deployment.

Select only relevant functions. Do not add one service from every category.

Explain component interactions rather than listing products.

## 9. Employer and technology research

Research independently, prioritizing the two most recent employers.

Investigate relevant operations, workflows, historical adoption, official customer stories, dated announcements, comparable roles, product availability, predecessors, and operational constraints.

Also research:

- Supporting-service availability during the role.
- Integration compatibility.
- Scenario fit.
- Credible reasons for repeated specialized tools.
- Specific products corresponding to broad categories.
- Appropriate measurement methods for relevant business scenarios.

Prefer official employer and vendor sources.

Employer postings describe roles; they do not prove personal participation.

Do not claim a public company project was my personal project.

Public project metrics and industry benchmarks may inform measurement selection and the plausibility review of illustrative metrics. They may inform draft assumptions but must not be described as verified personal measurements.

When comparing projects, consider workload type, project maturity, deployment scope, environment, time period, and measurement definition. Do not borrow organization-wide figures or a vendor benchmark for a component-level personal claim. Cite any external comparison actually used in the supporting notes. Do not invent benchmark sources or imply research was performed when it was not.

Record material sources outside the resume:

- Employer.
- Technology or capability.
- Relevant period.
- Source link.
- What it establishes.
- Remaining uncertainty.

When material adoption cannot be established, report “Adoption not verified” in supporting notes.

This does not automatically invalidate candidate-reported use or require deleting experience.

Never claim research occurred when it did not.

## 10. Historical compatibility and comparable tools

Check that technologies and relevant features existed during the employment period.

Apply this check to primary tools and supporting services.

When a JD tool is incompatible with that period:

1. Identify a period-appropriate predecessor or comparable tool.
2. Research employer context.
3. Preserve the alternative’s actual name.
4. Explain the transferable function.
5. Distinguish proposed attribution from confirmed use.

Exact product matching is not required when related work demonstrates the capability.

Do not rename an alternative as the JD product or imply full-period use when availability began later.

Omit unnecessary version or edition specificity.

Earlier roles may demonstrate related capabilities through different products or methods.

Do not insert different products solely for variety.

Established tool usage takes priority over a preference for different stacks.

## 11. Required experience bullet counts

Produce:

- Elevance Health: 20 substantive bullets.
- Optum: 20 substantive bullets.
- LatentView: 15 substantive bullets.
- Reylon Softech: 10 substantive bullets.

Required total: 65 substantive bullets.

Count actual bullet paragraphs beneath each employer.

Do not count headings, titles, dates, introductions, environment lines, wrapped lines, or count-inflating sub-bullets.

Do not silently shorten the document.

Plan distinct contributions across relevant requirements, analysis, design, configuration, implementation, integration, testing, validation, troubleshooting, monitoring, maintenance, automation, controls, and handoffs.

Use the complete-draft workflow where employer details are not individually recorded.

Do not jump from an empty accomplishments array directly to a shortfall.

Before reporting a shortfall:

1. Re-read records and capability assertions.
2. Identify omitted responsibilities.
3. Separate genuinely distinct over-compressed contributions.
4. Review scenario, technology, and skills coverage.
5. Remove duplication.
6. Recount.

Do not fabricate numerical achievements or pad with repetitive tool mentions.

Supporting services and metrics should deepen existing contributions, not create filler.

Disclose unavoidable shortfalls accurately.

## 12. Business scenarios

Include at least one substantive scenario under each of the two most recent roles.

Under the established chronology, prioritize Elevance Health and Optum. Follow corrected authoritative chronology if it changes.

Include scenarios for LatentView and Reylon Softech where feasible.

A scenario is a connected account of work addressing a recognizable business or operational need, such as implementation, integration, migration, analytical delivery, processing, troubleshooting, automation, controls, or maintenance.

Develop recent-role scenarios across connected bullets.

Use descriptive business context rather than inventing formal project or client names.

Across related bullets, establish:

- Business need or problem.
- Systems and work objects.
- Personal contribution and scope.
- Primary tools and supporting services.
- Technical execution.
- Relevant decisions and trade-offs.
- Validation or troubleshooting.
- Deliverables.
- Users or operational purpose.
- Supported qualitative or quantitative outcomes.

These elements belong across the scenario. Every bullet does not need to repeat all of them.

Choose metrics that fit the scenario instead of adding unrelated numbers.

Follow the complete-draft disclosure rule for proposed employer-specific scenarios and services.

Do not reuse one story under different employers with tool names changed.

Keep each technology environment coherent.

## 13. Natural, substantive experience writing

Write experience that reads naturally rather than as repeated variations of “Did X using Y so that Z.”

Examples illustrate depth, not a mandatory sentence formula.

Explain the work through varied contributions, sentence lengths, and structures.

Do not require most bullets to end with purpose or result clauses.

Do not attach “to,” “so that,” “which helped,” “enabling,” or “resulting in” to every bullet.

### Individual bullets may emphasize

- A concrete implementation.

- A problem investigated or resolved.

- A qualitative change.

- Technical or business scope.

- A deliverable.

- A responsibility or ownership boundary.

- A decision and its rationale.

- A trade-off.

- A before-and-after change.

- A validation activity.

- An operational procedure.

- A meaningful numerical measure.

Each bullet needs a clear contribution. It does not need action, tool, scope, purpose, and outcome simultaneously.

The surrounding scenario may establish significance, allowing some bullets to remain short and direct.

### Vary sentence shape

Mix structures naturally:

- Action-first.

- Problem-first.

- Scope-first.

- Decision-first.

- Outcome-first.

- Before-and-after.

- Short and direct.

Do not assign rigid percentages to these structures.

Do not vary wording mechanically while retaining the same sentence template.

### Human editing pass

Read each employer section as continuous professional writing.

Revise repetitive openings, clause structures, purpose endings, sentence lengths, benefit claims, lists, and metric phrasing.

Do not add errors, slang, or awkwardness to imitate human writing.

Aim for natural, precise professional prose.

## 14. Demonstrate value in different ways

### Qualitative outcomes

Describe established changes such as source traceability, clearer diagnostics, consistent validation, or a completed handoff.

Name the change rather than saying “improved efficiency.”

### Scope

Explain reach through users, workflows, systems, components, or lifecycle stages.

Scope can show complexity without numerical claims.

### Ownership

Use “owned,” “led,” “drove,” or “was the primary engineer on” when the responsibility is established or explicitly asserted.

Specify the component, workstream, release, investigation, or decision owned.

Do not imply program ownership from responsibility for one part.

### Problems

Name the relevant issue where applicable, such as unreliable retrieval, inconsistent mappings, duplicate processing, restricted-content exposure, or difficult diagnostics.

Do not invent incidents or successful remediation.

### Before and after

Use “replaced,” “consolidated,” “separated,” or “migrated” when the transition is established.

Do not imply an unknown earlier state.

### Decisions and trade-offs

Explain supported choices in relation to authoritative data, latency, maintainability, access boundaries, recovery, or another concrete constraint.

Do not invent a decision-making role.

## 15. Examples are guides, not templates

These illustrate sentence variety and specificity only:

- Built a retrieval pipeline on Amazon Bedrock and Amazon OpenSearch Service using approved policy documents.
- Added entitlement filters after retrieval testing exposed restricted-content matches.
- Owned the ingestion workstream from Amazon S3 intake through document parsing and embedding generation.
- Added citation checks before responses reached users.
- Routed eligibility questions to authoritative APIs rather than model-generated answers.
- Replaced manual document lookups with a source-linked retrieval workflow.
- Made answer sources visible to operations staff through document citations.

Do not automatically copy these technologies, outcomes, problems, or ownership claims.

Replicate their specificity without repeating their structure throughout the resume.

## 16. Technical specificity and actual product names

Use relevant detail involving configurations, interfaces, dependencies, transformations, queries, reconciliation, validation, connectivity, access policies, diagnostic evidence, exception handling, acceptance criteria, and handoffs.

Before including a tool, identify what it acted on, how it was used, relevant component interactions, and its function.

Do not write bullets merely to mention products.

### Name the product when it matters

Do not substitute broad technology categories for identifiable products in implementation descriptions.

For example, “Vector Databases” alone does not identify the retrieval technology.

Where established or included as a proposed review-draft choice, name the actual product, such as Amazon OpenSearch Service, Pinecone, or PostgreSQL with pgvector.

Apply this rule across databases, cloud services, orchestration frameworks, monitoring platforms, messaging products, and deployment tools.

Do not list several alternatives as if all were used.

Broad categories remain appropriate as section labels, architectural concepts, or general descriptions where a product is unnecessary.

If the product is unknown, do not silently invent confirmed usage. Use an accurate method-level description, omit the product-specific claim, or follow the proposed-service workflow.

Specificity does not override historical compatibility or attribution rules.

## 17. Action verbs, tense, and responsibility

Prefer accurate execution verbs such as developed, configured, implemented, integrated, automated, diagnosed, queried, reconciled, validated, tested, deployed, mapped, transformed, defined, organized, and maintained.

Do not routinely rely on contributed, reviewed, documented, coordinated, communicated, considered, assisted, helped, participated, worked on, or supported.

When those activities matter, explain:

- Review: object, criteria, evidence, and finding.

- Documentation: artifact, contents, and operational use.

- Coordination: dependency, decision, acceptance condition, or handoff.

- Communication: technical finding or decision and its purpose.

Do not simply replace a vague verb while leaving the contribution vague.

Ownership verbs are permitted when accurate, not required.

Write each bullet as one complete sentence in its own paragraph.

Use past tense for completed contributions, including completed work within a current role.

Avoid copied JD wording, keyword stuffing, generic promotion, repetition, and filler.

## 18. Results, scale, and metrics

Actively look for meaningful opportunities to quantify experience.

Target:

- Elevance Health: 3 metric-bearing bullets in the review draft.
- Optum: 3 metric-bearing bullets in the review draft.
- LatentView: 1–2 metric-bearing bullets.
- Reylon Softech: 1–2 metric-bearing bullets.

This is a target of roughly 8–10 metric-bearing bullets across the resume.

These are not additional bullets. Preserve the required 20/20/15/10 experience counts.

Treat metric inclusion in the review draft as an output acceptance check: 3 metric-bearing bullets for each recent role and 1–2 for each earlier role. Select suitable existing contributions rather than attaching irrelevant numbers.

Use established values first. When those are unavailable, follow the illustrative-review workflow below. Do not substitute a promise to add metrics later or a separate suggestions list for numbers inside the review-draft bullets.

### Select measurements from the business scenario

Consider the actual workflow, technical scope, operational problem, and business purpose before choosing a metric.

Relevant categories include:

- Efficiency and cost: processing time, manual effort, resource consumption, or expenditure.
- Latency and scale: response time, throughput, request volume, concurrency, or processing frequency.
- Architecture and controls: services integrated, applications covered, policies implemented, or control coverage.
- Zero-trust implementation: identities, workloads, access paths, or authorization policies within the candidate’s scope.
- Vulnerability mitigation: findings addressed, affected components, remediation time, or verified scan changes.
- Governance: assets cataloged, policies applied, reviews completed, or exceptions tracked.
- Business continuity: recovery-test results, restoration time, backup coverage, or documented recovery objectives.
- Data integrity: records reconciled, validation coverage, rejected exceptions, or measured error rates.
- Debugging and incident response: incidents investigated, diagnostic time, or measured mean time to recovery.
- Monitoring: services instrumented, alert coverage, event volume, or measured alert-noise changes.

These are options, not a requirement to include every category.

Security, compliance, governance, and zero trust are not numerical outcomes by themselves. Quantify the specific implementation, scope, or measured behavior.

### Choose an appropriate metric type

Use a natural mix of:

- Volume: records, documents, requests, interfaces, jobs, or incidents.
- Scope: applications, services, datasets, workflows, or user groups.
- Frequency: processing cycles, refresh intervals, releases, or reviews.
- Performance: latency, throughput, processing duration, or recovery time.
- Results: supported changes in cost, effort, errors, or operational performance.

Prefer a concrete scope or volume measure over an unsupported improvement percentage.

Do not make every metric a percentage or every recent-role metric a performance gain.

### Establish the number

Use:

- Values recorded in candidate files.
- Candidate-reported approximate values or ranges.
- Calculations derived from known inputs.

For derived figures, retain the inputs and calculation outside the resume.

Public projects and benchmarks may guide measurement selection. They must not become the candidate’s personal results.

Do not choose numbers merely because they appear modest, realistic, or believable. There is no universal safe numerical range across projects.

### Embed illustrative metrics directly in the review draft

Do not stop at “no numerical records available” or deliver only a table of zeros.

First use recorded figures, candidate-reported estimates, or calculations from known inputs. If a role still falls below its metric target, develop plausible illustrative values and embed them directly in existing experience bullets in the review draft:

- Elevance Health: 3 metric-bearing bullets in total, using established figures first and illustrative review values where needed.
- Optum: 3 in total.
- LatentView: 1–2 in total.
- Reylon Softech: 1–2 in total.

Integrate each illustrative value as a natural revision of an existing experience bullet, not an additional bullet. Preserve the 20/20/15/10 counts.

Do not move illustrative metrics into a separate suggestions section, appendix, table of proposed bullets, or second resume. They belong directly in the relevant Professional Experience bullets in the single review-draft Word document.

Use normal professional sentence wording. Do not put “illustrative,” “assumed,” “unverified,” brackets, placeholders, or confirmation requests inside individual bullets.

Apply the single outside-document disclosure in Section 6. Retain an internal record of the illustrative values, units, scope, and assumptions; do not claim that they were measured, verified, or supplied by the candidate.

Use a concrete illustrative value or meaningful range rather than an empty placeholder. Prefer project scope or workload measures when improvement percentages would require an unsupported baseline. If an illustrative outcome comparison is used, record both baseline and end value as assumptions internally and check the arithmetic.

Generated values are not candidate-reported estimates. Their inclusion is authorized for the clearly identified review draft, without a preliminary confirmation stage. Do not describe this draft as a verified factual resume or an application-ready final version. After the candidate confirms or corrects the values, update them and their internal status accordingly.

### Check believable units, scale, and context

For every supported figure and illustrative suggestion, check:

- The unit: requests, records, documents, integrations, endpoints, services, users, incidents, or another defined object.
- The period: per request, daily, monthly, per release, or over the engagement, when relevant.
- The environment: prototype, test, pilot, or production.
- Project maturity, implementation scope, and candidate responsibility.
- Whether the measure is observed workload, tested capacity, a target, a count, or a result.
- Whether a comparison requires a baseline, denominator, sample, percentile, or evaluation method.

Distinguish API request volume from the number of distinct APIs integrated. A large request count does not imply a similarly large integration count. Do not turn “1.2 million requests” into “1.2 million APIs.”

Also distinguish:

- Source documents from extracted chunks or embeddings.
- Records processed from unique customers or users.
- Concurrent users from registered users.
- Services instrumented from log-event volume.
- Vulnerabilities identified from vulnerabilities remediated.
- Recovery objectives from measured recovery results.
- A single recovery incident from mean time to recovery.
- Retrieval relevance, groundedness, and answer correctness from an undefined “AI accuracy” score.
- Median latency from tail latency and end-to-end response time from model-call time.

Do not infer project scale from employer size. Do not use company-wide totals as personal workload.

Do not use large numbers, decimals, percentages, precise milliseconds, or repeated round improvements merely to sound impressive. There is no universal safe numerical range: the unit and context determine plausibility.

When comparable project information is available, use it to check whether a suggestion is plausible—not to establish that the candidate achieved it. If no comparable evidence is available, identify the suggestion as scenario-based rather than research-validated.

Check consistency across metrics belonging to the same scenario. Daily and monthly volumes, throughput and workload, baseline and final values, and stated project duration must not contradict one another. Do not extrapolate peak capacity into sustained production volume without support.

### Wording exact figures and estimates

Use exact figures directly when supported. Illustrative values may also use concise numerical wording in the review draft under the document-level disclosure, with precision appropriate to the scenario. Direct wording does not turn an illustrative value into an established result. Do not automatically prefix metrics with “approximately” or “about.”

For genuine estimates, choose an accurate expression suited to the available information:

- A rounded figure with an estimate qualifier.
- A meaningful range.
- A supported threshold such as “more than 20.”

Vary the wording naturally instead of repeating one qualifier throughout the resume.

Use thresholds only when their meaning is supported. “More than,” “up to,” and a range make different claims and are not interchangeable.

Do not remove necessary wording from candidate-reported estimates merely for appearance or introduce false precision. The review-draft convention for illustrative values does not change the evidence status of any number.

Do not force each metric to use a different expression when the same wording is the most accurate.

### Integrate metrics naturally

Place metrics inside substantive bullets describing relevant work.

Vary their position. A measure may establish scope at the beginning, appear within the implementation, or describe an outcome.

Do not make every metric bullet end with “resulting in a X% improvement.”

Keep metric wording consistent with the natural-writing rules.

Distinguish:

- Workload handled from system capacity.
- Test results from production behavior.
- Objectives from achieved results.
- Team outcomes from personal contributions.
- A single incident’s recovery time from mean time to recovery.
- A count of remediated findings from a percentage reduction.

A percentage improvement requires supported baseline and comparison values.

Do not describe a service-level or recovery objective as achieved performance without supporting results.

Avoid unsupported absolutes such as zero vulnerabilities, zero data loss, complete compliance, or 100% availability.

### When numerical information is unavailable

Continue drafting the complete review resume. Use plausible illustrative scope, volume, frequency, or outcome metrics to fill the role-specific targets, alongside qualitative outcomes and technical detail.

Do not block generation to request figures or require approval before embedding illustrative metrics. Complete the in-document review-draft workflow rather than returning only a table of zeros.

Count all metric-bearing bullets actually present in the review draft toward the formatting target, while tracking established and illustrative values separately internally. Do not count illustrative values as confirmed qualifications or verified achievements.

Do not insert unresolved numerical placeholders. Embed concrete illustrative metrics directly in the review draft with the single outside-document disclosure. Do not present the result as an application-ready factual final resume until the candidate has checked the proposed content.

## 19. Summary, skills, and experience alignment

### Professional Summary

Write one natural paragraph, normally 90–120 words, with:

- Accurate professional identity.
- 8+ years of overall experience.
- Relevant asserted or established capabilities.
- Technical judgment.
- Business or operational contribution.

Do not downgrade reported hands-on experience to familiarity because projects are not individually stored.

Avoid “candidate-reported capabilities,” “positioned to support,” and similar distancing wording.

Exclude employer names, project names, education, generic enthusiasm, and tool-list prose.

Summarize strong relevant capabilities without implying every tool was used in every role.

### Selective highlights in the Professional Summary

Apply actual Word bold formatting to 2–3 short, high-priority JD-related phrases in the Professional Summary. This is a required formatting step, not a suggestion to highlight them only in the chat preview.

Select the two strongest relevant phrases first; add a third only if it adds distinct value. Do not leave the Summary entirely regular or count its heading as a keyword highlight. If fewer than two supported relevant phrases exist, disclose that specific limitation rather than inventing expertise.

Select the highest-priority JD requirements meaningfully demonstrated in Professional Experience. These may be a specific tool or platform, a core technical capability, or a distinctive relevant specialization.

Prefer precise work-related phrases over generic qualities. Do not automatically bold the experience total, seniority, broad self-descriptions, or every JD keyword.

Keep each highlight to the exact product name or a concise phrase, normally 2–4 words. Keep the surrounding sentence regular. Do not bold whole clauses, long lists, or the opening half of the paragraph.

Choose highlights for the current JD rather than reusing the same selections for every application. Bolding must reflect the experience described, not create an unsupported impression of expertise or ownership.

Apply actual Word bold formatting and verify the highlights in the saved document. These Summary highlights are separate from experience-bullet coverage targets and do not change the Technical Skills formatting rules.

### Technical Skills

Build a fresh section for each JD.

Prioritize relevant asserted or established products, complementary technologies, foundations, and methods.

Use approximately 5–7 meaningful categories where useful.

Format:

Category: Item, Item, Item

Bold category labels only. Keep individual items regular.

Use actual product names where applicable.

Do not list every researched technology or carry unrelated skills forward.

### Every skill must be demonstrated in experience

Every individual tool, service, language, framework, platform, method, or practice in Technical Skills must receive meaningful treatment in at least one experience bullet.

Category headings do not require separate coverage.

For named products, use the exact name in at least one relevant bullet. An expanded name with its standard abbreviation is acceptable.

For methods and practices, describe work that demonstrates the capability.

A detached environment list does not satisfy this requirement.

Do not create implausible bullets to justify a skills list. Revise both sections together:

- Retain the skill and demonstrate it meaningfully.
- Or remove it when it cannot appropriately be represented.

Proposed scenario services do not automatically become confirmed proficiencies.

Coverage applies across the complete resume, not under every employer.

## 20. Structure, tailoring, and technology distribution

Use:

1. Name.
2. Contact line: phone number, email, and relevant professional profile links when available. Omit the candidate’s location, including city, state, region, country, ZIP/postal code, and street address. Do not add a location placeholder.
3. Simple divider.
4. Professional Summary.
5. Technical Skills.
6. Fully populated Professional Experience.
7. Education.
8. Established certifications.

Place experience beneath each employer.

Do not move it into another section or document.

Context introductions and optional project labels do not count as bullets.

Remove unused fields and placeholders.

Aim for approximately 60% direct JD priorities and 40% supporting depth, and approximately 60% JD technologies and 40% relevant supporting technologies.

These are editorial guides, not quotas.

### Allocate technologies across roles

For each primary tool, identify its main placement, scenario, supporting services, justified repetition, and earlier-role alternatives.

Concentrate the substantial majority of direct JD coverage in the two most recent roles, with the strongest emphasis on the latest role.

Distribute complementary requirements between those roles without mechanically repeating the entire stack.

Use earlier roles primarily for foundations, transferable capabilities, period-appropriate technologies, and career progression.

Do not distribute technologies equally or alter established experience to achieve a desired weighting.

For five primary tools, three might receive primary treatment in the latest role and two in the next. This is an illustration, not a mandatory ratio.

Choose placement according to established employer-specific experience, candidate assertions, period, scenario coherence, employer context, and JD priority.

### Avoid unnecessary repetition

Do not repeat specialized products under every role by default.

Repeat tools when justified by established usage, relevant assertions and coherent scenarios, or appropriate foundational use.

Popularity alone does not establish usage.

When tools recur, describe different applications or contributions.

Do not force different products merely to make employers look different.

## 21. Selective bolding — tools and important technical procedures only

This section is the controlling rule for inline emphasis in Professional Experience. The Professional Summary follows its separate selective-highlight instructions in Section 19, which also permit short core-capability or specialization phrases. Apply actual formatting in the generated Word document, not merely in drafting notes or the chat preview.

### What to bold

Bold only:

1. Exact names of relevant tools, products, platforms, frameworks, or services.
2. Short, meaningful names of important technical procedures or mechanisms.

Eligible examples include Python, Amazon Bedrock, Azure API Management, request validation, citation checks, access controls, network segmentation, dead-letter handling, and exponential backoff.

These are examples, not required keywords. Select terms actually present in the bullet. Do not add or rewrite experience merely to create boldable text.

### Required coverage across roles

Make the earlier instruction to highlight “most substantive bullets” measurable:

- Elevance Health: at least 16 of 20 experience bullets contain useful inline bolding.
- Optum: at least 16 of 20.
- LatentView: at least 12 of 15.
- Reylon Softech: at least 8 of 10.
- Total: at least 52 of the required 65 bullets contain a short, relevant inline highlight.

This is a coverage requirement, not an instruction to bold most words. One concise highlight can satisfy a bullet.

Do not count headings, titles, project labels, Skills, Summary, or context introductions toward experience-bullet coverage.

If an existing substantive bullet contains no eligible tool or procedure, leave it unbolded and select eligible highlights in other bullets. Do not invent a procedure or bold generic wording to pass the check. If the coverage target genuinely cannot be met, report the exact shortfall rather than claiming completion.

### Select short spans

- In each eligible bullet, select one important tool or procedure first.
- Add a second short highlight when it identifies a distinct important tool or procedure.
- Normally keep the combined highlight length to roughly 2–6 words per bullet; this is a guide, not a requirement to expand selections.
- A one-word product such as Python is valid. Preserve a complete product name when longer.
- Keep surrounding verbs, connecting words, explanations, scope, beneficiaries, numbers, and outcomes regular.
- Do not bold the first half of the sentence, entire action clauses, entire bullets, or long lists.
- A tool or procedure can be highlighted wherever it appears. Do not change sentence order to put bold text first.
- A procedure within a purpose or result clause remains eligible; highlight only its short name, not the surrounding clause.

### Balance and repetition

Aim for restrained emphasis, commonly around 10–15% of experience words and generally no more than 20%. A lower percentage can be acceptable when the role-by-role coverage targets are met with meaningful short highlights. Do not use a word-percentage target as a reason to omit highlights from most bullets, or expand spans merely to increase a percentage.

Prefer different relevant procedures within each employer section. Normally highlight a repeated tool only on its strongest occurrence, but this is a preference rather than a ban. A repeated tool may be highlighted again when it is the most useful eligible term in a distinct contribution. Do not let the once-per-tool preference reduce most of a role to plain text.

The same tool or procedure may be highlighted under different employers. Do not highlight every service in a multi-component sentence.

### Correct formatting examples

- Built a retrieval pipeline on **Amazon Bedrock** and **Amazon OpenSearch Service** using approved policy documents.
- Added **citation checks** before responses reached users.
- Routed eligibility questions to authoritative APIs rather than model-generated answers, using **request validation** at the service boundary.
- Added idempotency keys, **dead-letter handling**, and **exponential backoff** to message-processing flows.

These illustrate formatting only. They are not automatic resume content. The rest of each sentence remains regular.

### Actual Word formatting

Apply real Word bold formatting to the selected runs. Markdown asterisks in text, intended highlights in a plan, and bold headings alone do not satisfy this rule.

Preserve standard bold for the name, section headings, employer or role headings, and Technical Skills category labels. Summary and Skills formatting otherwise remain governed by their existing sections.

### Mandatory final check

Reopen the saved DOCX and count actual experience bullet paragraphs containing eligible bold runs under each employer. Check the saved file, not the source draft or planned selections.

Inspect every highlighted span for eligibility and length. Confirm most text remains regular and numeric results are not bolded merely for emphasis.

If coverage is too sparse, add short eligible highlights and save again. If spans are too broad, narrow them while preserving useful coverage. Recheck after the final save and visually inspect the rendered pages when available.

Do not claim the bolding requirement passed without checking the actual saved document. Include a compact final report of highlighted bullets versus total bullets by employer, plus any shortfall. This is a formatting report, not additional resume content.

## 22. Word document requirements

Deliver one editable Word document (.docx). No PDF is required.

Use:

- Single-column US Letter.
- Approximately 0.7-inch margins.
- Readable conventional font.
- 22-point name.
- Approximately 12-point headings.
- 11-point body and bullets.
- Simple bullets.
- Consistent dates, indentation, and spacing.
- Headings kept with following content.

Avoid tables, columns, text boxes, graphics, skill bars, hidden keywords, and essential information in headers or footers.

Do not shrink text or delete required content to force a page count.

Keep research, editorial notes, draft-status explanations, metric calculations, and assessments outside the resume.

Use a descriptive filename such as:

`Leena_M_Target_Role_Resume_Review_Draft.docx`

Save in the designated output location and preserve earlier versions unless replacement is requested.

Follow available document-generation instructions.

## 23. Architect and hiring manager reviews

### Technical coherence

Check:

- Components and dependencies make sense.
- Products perform the functions described.
- Technical details explain the relevant work without overloading each sentence.
- The earlier writing rules in Sections 13, 16, and 17 govern sentence style; there is no per-bullet implementation-detail quota.
- Natural wording, metrics, product naming, and bolding support the contribution rather than making every bullet longer.
- Supporting services have identifiable roles.
- Interactions are explained.
- Historical availability is plausible.
- Validation and failure handling are relevant.
- Decisions and trade-offs are meaningful.
- Ownership is not inflated.
- Measurements describe the correct behavior and scope.
- Metric units, periods, environments, arithmetic, and cross-scenario consistency have been checked.
- Illustrative metrics are technically plausible, embedded in the relevant review-draft bullets, and distinguished from established results in the internal record and single outside-document disclosure.

### Hiring manager relevance

Check:

- Important JD work appears prominently in recent roles.
- Scenarios demonstrate execution.
- Roles have distinct contributions.
- Skills are demonstrated.
- Specific products replace unnecessary generic labels.
- Outcomes, scope, problems, and decisions convey substance.
- Metrics support the story rather than decorate it.
- Short bullets are allowed where sufficient.
- No section repeats “Did X so that Y.”
- Estimate qualifiers are not mechanically repeated.
- The resume is understandable without this conversation.

Do not add unnecessary complexity or guarantee recruiter selection.

## 24. Verification and document inspection

### Content

Verify protected facts, standing assertions, JD coverage, historical compatibility, scenarios, technical depth, and responsibility levels.

Do not treat an empty accomplishments collection as absence of experience.

### Concision and substantive work

Follow the restored sentence rules in Sections 13, 16, and 17. Keep a bullet when it clearly describes a relevant contribution; do not expand it merely to fit a multi-part checklist.

Add detail only when needed to distinguish the work from a generic task. Remove redundant context, repeated explanations, stacked technical lists, and unnecessary purpose clauses. Keep the one-sentence-per-bullet rule, but do not stretch a sentence to cover several separate contributions.

Use natural variation and precise JD terminology in context. Do not lengthen bullets to chase a keyword or ATS-score target. Do not claim that a particular style produces a verified ATS-score increase without an actual matching result.

### Sentence variety

Read each employer section in sequence.

Rewrite excessive repetition of:

- Action–tool–purpose constructions.
- Purpose and outcome endings.
- Sentence lengths and openings.
- Generic benefits.
- Ownership claims.
- Explanatory clauses.
- Metric placement or estimate wording.

Use purpose clauses where useful. The objective is natural variety, not a different template for every bullet.

### Skills-to-experience audit

Map every individual Technical Skills item to at least one substantive experience bullet.

Verify product naming and meaningful demonstration.

Remove or resolve unmatched skills.

Do not count bare technology lists.

### Technology distribution

Verify coherent stacks, relevant services, actual product names, recent-role emphasis, justified repetition, and period-appropriate alternatives.

Do not add products solely for popularity or variety.

### Metrics

Check the target distribution:

- Elevance Health: 3 metric-bearing bullets in the review draft.
- Optum: around 3.
- LatentView: 1–2.
- Reylon Softech: 1–2.

For each number, record whether it is established, candidate-estimated, derived, or illustrative. Check its source or stated assumptions, calculation, unit, scope, period, and attribution. Verification of formatting or plausibility must not be described as verification of personal achievement.

For improvement claims, verify the baseline and comparison.

Distinguish estimates, test results, objectives, capacity, workloads, and production outcomes.

Confirm exact figures are not unnecessarily qualified.

Confirm candidate-reported estimates are expressed accurately and illustrative values retain their review status internally and in the document-level disclosure.

Check that qualifiers, ranges, and thresholds match their meaning and are not varied merely for appearance.

For illustrative metrics, check plausible units, scale, period, environment, responsibility, arithmetic, and scenario consistency. Retain the comparison or assumptions internally and provide the single outside-document disclosure.

Do not approve a numerical claim as factual solely because it sounds believable.

If established metrics fall below target, verify that concrete illustrative metrics fill the gaps directly in the review-draft experience bullets. Do not stop at a zero-metric report or separate suggestions list.

Confirm illustrative metrics are inside the relevant review-draft bullets, are covered by the single outside-document disclosure, and are not represented as verified personal results.

### Counts

Verify actual bullet paragraphs:

- Elevance Health: 20.
- Optum: 20.
- LatentView: 15.
- Reylon Softech: 10.
- Total: 65.

### Professional Summary highlights

Reopen the generated DOCX and inspect the Professional Summary paragraph itself. Verify that 2–3 short, relevant JD-related phrases have actual bold runs. Exclude the heading and experience highlights from this count.

Verify these phrases are demonstrated in experience and that most Summary text remains regular. If the highlights are absent, apply the formatting, save, and inspect again before claiming completion.

### Bolding

Apply Section 21 to the actual saved Word document.

Count experience bullets with at least one eligible bold tool or short technical-procedure name:

- Elevance Health: at least 16/20.
- Optum: at least 16/20.
- LatentView: at least 12/15.
- Reylon Softech: at least 8/10.
- Total: at least 52/65.

Exclude headings, project labels, Summary, and Skills from these counts. Do not count a bold verb, generic phrase, or numerical result as an eligible highlight.

Check that selections are short, most text remains regular, and no first-half clauses, entire sentences, or long lists have been bolded. Check that repetition preferences have not caused sparse coverage.

Measure bold-word share as a balance diagnostic, not a substitute for bullet coverage. Do not expand selections to force a percentage.

Verify real Word bold runs and the absence of visible Markdown asterisks. Correct failed checks, save, and recheck. Report highlighted-versus-total counts by employer; disclose any unavailable visual inspection accurately.

### Generated document

1. Inspect complete extracted text.
2. Count actual bullets by employer.
3. Verify skills-to-experience coverage.
4. Locate the actual metric-bearing experience bullets in the saved document and count them by employer. Dates, overall years of experience, numbered headings, and bare technology lists do not count as project metrics. Require 3/3/1–2/1–2 in the review draft. Check units, context, arithmetic, and internal status.
5. Inspect the Summary paragraph for 2–3 actual bold keyword or capability phrases; its heading does not count.
6. Inspect Word bold runs.
7. Render and inspect every page using available tools.
8. Correct clipping, broken bullets, spacing, and page breaks.
9. Recheck corrected content.

Do not claim unperformed checks or call an incomplete document fully compliant.

Disclose unavailable inspection capabilities accurately.

## 25. Assessment and final delivery

Prefer a concise strong, moderate, or weak match assessment with reasons.

Label numerical match estimates as editorial judgment unless produced by an actual matching tool.

Do not imply validated ATS predictions or guarantee interviews.

Deliver:

1. Link to the complete editable Word resume.
2. Verified experience counts by employer.
3. Scenario coverage.
4. Actual metric-bearing bullet counts by employer, including illustrative metrics embedded in the review draft.
5. One outside-document disclosure under Section 6 when proposed activities or illustrative values are present; do not deliver a separate list of metric suggestions.
6. Verified Summary-highlight count and role-by-role experience-bolding counts, checked in the saved Word document.
7. Confirmation that listed skills are demonstrated in experience.
8. Do not repeat the draft-status disclosure; the single statement already covers proposed activities and illustrative metrics.
9. Material sources and limitations.
10. Brief match assessment.

Use actual verified numbers in the compliance table:

| Employer | Required experience bullets | Actual experience bullets | Target metric-bearing bullets | Actual metric-bearing bullets in review draft |
|---|---:|---:|---:|---:|
| Elevance Health | 20 | Verified count | 3 | Actual count |
| Optum | 20 | Verified count | 3 | Actual count |
| LatentView | 15 | Verified count | 1–2 | Actual count |
| Reylon Softech | 10 | Verified count | 1–2 | Actual count |
| Total | 65 | Verified count | Roughly 8–10 | Actual count |

Metric-bearing bullets are included within the experience counts. Counts verify presence in the document, not the truth of illustrative values. Do not add a separate suggestions column or second metric draft.

Keep the resume easy to locate and commentary concise.

When reporting completion, identify the actual saved-document counts for metrics, Summary highlights, and experience highlights. Review technical substance qualitatively rather than imposing execution-depth bullet quotas. Do not report planned counts as completed work. Correct missing formatting or shallow content before delivery rather than merely describing what the document should contain.

## 26. Persistent requirements and future updates

Apply automatically to every JD:

- Complete experience sections.
- 20/20/15/10 substantive bullets.
- Recent-role business scenarios.
- Earlier-role scenarios where feasible.
- Concrete technical execution.
- Natural, varied sentence structures.
- No mandatory purpose-and-result ending for most bullets.
- Appropriate qualitative outcomes, scope, problems, ownership, before-and-after changes, decisions, and trade-offs.
- Specific products where applicable.
- Every listed skill meaningfully demonstrated in experience.
- Architect and hiring manager review.
- Supporting services integrated into coherent scenarios.
- Most direct JD coverage in the two most recent roles.
- No mechanical repetition of the entire stack.
- No forced product substitutions for variety.
- 3 metric-bearing bullets in each recent role and 1–2 in each earlier role, using established values first and illustrative values where needed in the review draft.
- Relevant volume, scope, frequency, performance, or outcome measures.
- Exact figures stated directly and genuine estimates expressed accurately without repetitive qualifiers.
- No invented numerical claims presented as achieved personal results merely to meet metric targets.
- Concrete illustrative metrics embedded directly in experience bullets for numerical gaps rather than a zero-metric report or separate suggestions list.
- Plausibility checks for units, time periods, environments, project scope, arithmetic, and consistency.
- One clearly identified review-draft deliverable with illustrative metrics inside the bullets and one disclosure outside the document; no individual-bullet labels or preliminary confirmation stage.
- Selective bolding of tools and short procedures only.
- No empty experience sections caused solely by an empty accomplishments array.
- Actual document verification before claiming completion.

Whenever I request a change:

- Apply it throughout.
- Remove conflicting instructions.
- Preserve unrelated requirements.
- Embed additions into the relevant rules.
- Return the complete updated prompt unless I explicitly request a section only.

Do not require me to repeat these instructions.

