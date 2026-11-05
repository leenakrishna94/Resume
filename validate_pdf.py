from pathlib import Path
from pypdf import PdfReader
import pypdfium2 as pdfium

pdf = Path('Resumes/pdf/2026-11-04/Leena_M_Outfitter_AI_Business_Development_Representative_Resume.pdf')
reader = PdfReader(str(pdf))
texts = [(page.extract_text() or '') for page in reader.pages]
full = '\n'.join(texts)
required = ['Leena M', 'Professional Summary', 'Technical Skills', 'Professional Experience', 'Education']
print('pages=', len(texts), 'chars=', len(full))
print('required=', {term: (term in full) for term in required})
print('bullet_count=', full.count('•'))
render_dir = Path('tmp/pdfs/outfitter')
render_dir.mkdir(parents=True, exist_ok=True)
doc = pdfium.PdfDocument(str(pdf))
for i, page in enumerate(doc):
    bitmap = page.render(scale=2)
    bitmap.to_pil().save(render_dir / f'page-{i+1}.png')
print('rendered=', len(doc))
