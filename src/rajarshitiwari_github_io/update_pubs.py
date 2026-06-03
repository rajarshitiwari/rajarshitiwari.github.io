import time
from scholarly import scholarly

def generate_markdown_pubs(scholar_id, output_file="publications.md", max_pubs=10):
    print(f"Fetching profile for ID: {scholar_id}...")
    
    # Fetch the author's basic profile
    author = scholarly.search_author_id(scholar_id)
    author = scholarly.fill(author, sections=['publications'])
    
    print(f"Found {len(author['publications'])} publications. Processing top {max_pubs}...")

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("### Selected Publications\n\n")

        for i, pub in enumerate(author['publications'][:max_pubs]):
            print(f"Fetching details for paper {i+1}...")
            
            # Fill individual publication details to get the venue and full authors
            pub_filled = scholarly.fill(pub)
            bib = pub_filled['bib']
            
            title = bib.get('title', 'Unknown Title')
            authors = bib.get('author', 'Unknown Authors')
            
            # Scholar sometimes uses 'venue', sometimes 'journal'
            venue = bib.get('venue', bib.get('journal', ''))
            year = bib.get('pub_year', '')
            citations = pub_filled.get('num_citations', 0)
            
            # Construct the direct Google Scholar link for the paper
            pub_id = pub_filled.get('author_pub_id', '')
            link = f"https://scholar.google.com/citations?view_op=view_citation&user={scholar_id}&citation_for_view={pub_id}"

            # Write standard Markdown (two spaces at the end of a line creates a hard break)
            f.write(f"**[{title}]({link})** \n")
            f.write(f"*{authors}* \n")
            
            # Build the metadata line dynamically
            meta = []
            if venue:
                meta.append(f"*{venue}*")
            if year:
                meta.append(str(year))
            if citations > 0:
                meta.append(f"**Cited by {citations}**")
                
            if meta:
                f.write(" · ".join(meta) + "  \n")
            f.write("\n")
            
            # Be polite to Google's servers to avoid IP blocks
            time.sleep(1.5)

    print(f"Successfully wrote {max_pubs} publications to {output_file}")

if __name__ == "__main__":
    # Your Google Scholar ID
    generate_markdown_pubs('zxrDxwEAAAAJ', max_pubs=-1)