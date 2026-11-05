# Resume generator - initial setup

Create a JD-specific resume PDF for Leena M. This stage contains contact details, a Professional Summary, Technical Skills, and Professional Experience rules. Experience content is generated only when explicitly requested.

## Start here

Paste a job description into the conversation and save a copy in `inputs/` using a role-based filename. The only new input needed for a generation run is the current JD; saved candidate facts come from `profile.json`.

The assistant will use `resume-rules.md` and `templates/resume-template.md` to draft each in-scope section, then create a PDF when asked to generate. Each run starts from the saved profile and that JD, without using earlier generated resumes.

## Files

- `profile.json`: contact details, user-provided background, and confirmed technical experience.
- `resume-rules.md`: scope, tailoring rules, Technical Skills selection, factual limits, and PDF checks.
- `templates/resume-template.md`: contact, Professional Summary, Technical Skills, and Professional Experience structure.
- `inputs/`: submitted job descriptions, saved by role, employer, and date using `role-employer_YYYY-MM-DD.txt`.
- `AGENTS.md`: instructions for assistants working in this folder.

## Current status

Generation is currently assistant-guided using these profile, template, workflow files, and the selected JD from `inputs/`. PDFs are saved under `output/pdf/YYYY-MM-DD/`; editable Word resumes are saved under `output/docx/YYYY-MM-DD/`. Each new JD should be stored in `inputs/` before its matching resume is generated.

Summaries follow the quality standard in `resume-rules.md`: one paragraph, normally 90-120 words, prioritizing supported candidate strengths relevant to the JD's actual professional function.

Technical Skills are generated independently for each JD: exact named tools first, dependency and similar tools, foundation languages, and engineering practices. The profile records JD-named tools as user-reported; similar-only tools are not stored as a global stack. Employers, credentials, dates, and per-tool tenure are not inferred from a JD.

Professional Experience is generated only on an explicit execute request. STAR bullets use the four recorded employers: Elevance Health, Optum, LatentView, and Reylon Softech. Education is the locked Saint Louis University Master's block. ATS readability and recruiter relevance are design goals, not guarantees of screening results or interviews.
