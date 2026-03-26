import os
import re
import random
import string

# 1. Create the dummy PDF
pdf_path = os.path.join('showcases', 'real-estate', 'century-capital-case-study.pdf')
pdf_content = b"%PDF-1.4\n1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n2 0 obj\n<< /Type /Pages /Kids [3 0 R] /Count 1 >>\nendobj\n3 0 obj\n<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Contents 4 0 R /Resources << /Font << /F1 5 0 R >> >> >>\nendobj\n4 0 obj\n<< /Length 53 >>\nstream\nBT\n/F1 24 Tf\n100 700 Td\n(Century Capital Case Study) Tj\nET\nendstream\nendobj\n5 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>\nendobj\nxref\n0 6\n0000000000 65535 f \n0000000009 00000 n \n0000000058 00000 n \n0000000115 00000 n \n0000000216 00000 n \n0000000320 00000 n \ntrailer\n<< /Size 6 /Root 1 0 R >>\nstartxref\n408\n%%EOF\n"
with open(pdf_path, "wb") as f:
    f.write(pdf_content)

# 2. Obfuscated map reference
# The real estate index is 'ejd3vezz2e9ssntzhjxox9lp.html'
# The portfolio portal is 'tmfvm8zba3eo3dtvdfwkho0z.html'
# We will create 'case-study.html' with a cryptic name.
cryptic_cs = ''.join(random.choices(string.ascii_lowercase + string.digits, k=24)) + '.html'
cs_path = os.path.join('showcases', 'real-estate', cryptic_cs)

with open('obfuscation_map.txt', 'a', encoding='utf-8') as f:
    f.write(f'showcases/real-estate/case-study.html -> {cryptic_cs}\n')

# 3. Modify the real estate showcase files to add the Case Study link in the bottom banner
re_dir = os.path.join('showcases', 'real-estate')
for file in os.listdir(re_dir):
    if file.endswith('.html') and file != cryptic_cs:
        path = os.path.join(re_dir, file)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # The banner has '← Portfolio' link. We'll add '📄 Case Study' next to it.
        # Find: <a href="../../tmfvm8zba3eo3dtvdfwkho0z.html"
        new_link = f'<a href="{cryptic_cs}" style="color:rgba(255,255,255,0.6);font-size:9px;font-weight:700;letter-spacing:0.15em;text-transform:uppercase;text-decoration:none;margin-right:16px;">📄 Case Study</a><a href="../../tmfvm8zba3eo3dtvdfwkho0z.html"'
        content = content.replace('<a href="../../tmfvm8zba3eo3dtvdfwkho0z.html"', new_link)
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)

print(f"Case study linked as {cryptic_cs}")
