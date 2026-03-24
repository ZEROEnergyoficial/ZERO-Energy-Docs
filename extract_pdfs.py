import os
from pypdf import PdfReader

es_dir = r"c:\Users\cesar\Documents\Servidor\Zero\GitHub ZERO\01_Governance\02_Meeting_Minutes (Actas - Atas)\es"
out_file = r"c:\Users\cesar\Documents\Servidor\Zero\GitHub ZERO\actas_text.txt"

with open(out_file, "w", encoding="utf-8") as f:
    for filename in sorted(os.listdir(es_dir)):
        if filename.endswith(".pdf"):
            filepath = os.path.join(es_dir, filename)
            reader = PdfReader(filepath)
            text = f"--- {filename} ---\n"
            for page in reader.pages:
                extracted = page.extract_text()
                if extracted:
                    text += extracted + "\n"
            f.write(text + "\n======================\n")
