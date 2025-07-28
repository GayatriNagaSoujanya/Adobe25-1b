import os
from extractor import extract_sections
from embedding import embed_query_and_chunks
from ranker import rank_chunks
from utils import save_json, load_input_json, timestamp

INPUT_DIR = "input/PDFs"
OUTPUT_DIR = "output"

def main():
    meta, persona, job, filenames = load_input_json()
    query = f"{persona}: {job}. Include cities, food, beach activities, culture, and fun spots."

    print(f"\n[INFO] Query: {query}")
    all_chunks = []

    for file in filenames:
        path = os.path.join(INPUT_DIR, file)
        print(f"[INFO] Processing file: {file}")
        sections = extract_sections(path)
        print(f"[DEBUG] Extracted {len(sections)} chunks from '{file}'")

        for s in sections:
            s["document"] = file
            all_chunks.append(s)

    print(f"\n[INFO] Total extracted chunks from all PDFs: {len(all_chunks)}")
    if not all_chunks:
        print("[ERROR] No chunks extracted. Check your PDFs and extractor.")
        return

    ranked, top_chunks = rank_chunks(all_chunks, query)

    print("\n[INFO] Top 5 Extracted Sections:")
    for sec in ranked:
        print(f"  - {sec['document']} (page {sec['page_number']}): {sec['section_title']}")

    output = {
        "metadata": {
            "input_documents": filenames,
            "persona": persona,
            "job_to_be_done": job,
            "processing_timestamp": timestamp()
        },
        "extracted_sections": ranked,
        "subsection_analysis": top_chunks
    }

    save_json(output, os.path.join(OUTPUT_DIR, "output.json"))
    print("\n✅ Output saved to 'output/output.json'")

if __name__ == "__main__":
    main()
