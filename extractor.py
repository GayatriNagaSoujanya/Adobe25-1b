import fitz  # PyMuPDF

def extract_sections(pdf_path):
    doc = fitz.open(pdf_path)
    sections = []
    for i, page in enumerate(doc):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if block["type"] == 0:
                text = " ".join(span["text"] for line in block["lines"] for span in line["spans"]).strip()
                if len(text) > 20:
                    sections.append({"text": text, "page": i + 1})
    return sections
