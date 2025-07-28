from sklearn.metrics.pairwise import cosine_similarity
from collections import defaultdict

def rank_chunks(chunks, query):
    from embedding import embed_query_and_chunks

    query_embed, chunk_embeds = embed_query_and_chunks(query, chunks)
    sims = cosine_similarity([query_embed], chunk_embeds)[0]

    # Sort by similarity
    scored = sorted(zip(chunks, sims), key=lambda x: -x[1])

    seen_docs = set()
    extracted_sections = []
    refined = []

    for chunk, sim in scored:
        doc = chunk["document"]
        if doc in seen_docs:
            continue  # Skip if document already used
        seen_docs.add(doc)

        extracted_sections.append({
            "document": doc,
            "section_title": chunk["text"][:60] + "...",
            "importance_rank": len(extracted_sections) + 1,
            "page_number": chunk["page"]
        })

        refined.append({
            "document": doc,
            "refined_text": chunk["text"],
            "page_number": chunk["page"]
        })

        if len(extracted_sections) == 5:  # or however many top chunks you want
            break

    return extracted_sections, refined
