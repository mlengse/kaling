import os
import re

base_dir = r"c:\Users\anjan\dev\kaling\docs"
folders = ["tkk", "pmkp", "pkp"]

print("Smart checking markdown files for missing templates in EPs...")
print("-" * 70)

total_eps = 0
missing_templates = []
all_checked_eps = []

for folder in folders:
    folder_path = os.path.join(base_dir, folder)
    if not os.path.exists(folder_path):
        continue
    
    # Get all .md files except index.md
    files = [f for f in os.listdir(folder_path) if f.endswith(".md") and f != "index.md"]
    # Sort files numerically
    files.sort(key=lambda x: int(os.path.splitext(x)[0]))
    
    for file in files:
        file_path = os.path.join(folder_path, file)
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Find the Elemen Penilaian section using a loose regex that supports various typos
        ep_section_match = re.search(r"##\s*Elemen\s*Penila[ia]*n\s*(.*)", content, re.DOTALL | re.IGNORECASE)
        if not ep_section_match:
            print(f"No 'Elemen Penilaian' section found in {folder}/{file}")
            continue
            
        ep_text = ep_section_match.group(1)
        
        # Parse EPs line-by-line
        lines = ep_text.split("\n")
        eps = []
        current_ep = None
        
        for line in lines:
            # Match top-level numbered list item like "1. " or "2. "
            # Must start with 0-2 spaces, a digit, dot, and space.
            m = re.match(r"^ {0,2}(\d+)\.\s+(.*)", line)
            if m:
                if current_ep:
                    eps.append(current_ep)
                current_ep = {
                    "num": m.group(1),
                    "title": m.group(2),
                    "lines": [line]
                }
            else:
                if current_ep:
                    current_ep["lines"].append(line)
        
        if current_ep:
            eps.append(current_ep)
            
        for ep in eps:
            ep_content = "\n".join(ep["lines"])
            total_eps += 1
            
            # Check for template download link
            has_template = "/templates/" in ep_content or "Unduh Template" in ep_content
            # Check if there is a Kelengkapan Bukti callout block
            has_callout = re.search(r":::\s*tip\s*Kel[ae]ngkapan\s*Bukti", ep_content, re.IGNORECASE) is not None
            
            all_checked_eps.append({
                "file": f"{folder}/{file}",
                "ep": ep["num"],
                "has_template": has_template,
                "has_callout": has_callout,
                "preview": ep["title"][:60]
            })
            
            if not has_template:
                missing_templates.append({
                    "file": f"{folder}/{file}",
                    "ep": ep["num"],
                    "has_callout": has_callout,
                    "preview": ep["title"][:60],
                    "content": ep_content
                })

print(f"Total top-level EPs parsed: {total_eps}")
print(f"EPs with missing templates: {len(missing_templates)}")
print("-" * 70)
for mt in missing_templates:
    callout_status = "Has Callout" if mt["has_callout"] else "NO Callout"
    print(f"- {mt['file']} EP {mt['ep']} ({callout_status}): {mt['preview']}")
