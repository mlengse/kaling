import os
import re

base_dir = r"c:\Users\anjan\dev\kaling\docs"
folders = ["tkk", "pmkp", "pkp", "pendahuluan", "survei"]

print("Checking markdown files for title and description in frontmatter...")
print("-" * 75)

total_files = 0
files_missing_description = []

for folder in folders:
    folder_path = os.path.join(base_dir, folder)
    if not os.path.exists(folder_path):
        continue
    
    files = [f for f in os.listdir(folder_path) if f.endswith(".md")]
    
    for file in files:
        file_path = os.path.join(folder_path, file)
        total_files += 1
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Extract frontmatter
        fm_match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
        if not fm_match:
            files_missing_description.append({
                "file": f"{folder}/{file}",
                "reason": "No frontmatter found"
            })
            continue
            
        fm_text = fm_match.group(1)
        
        # Check for title
        title_match = re.search(r"^title:\s*(.*)", fm_text, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else None
        
        # Check for description
        desc_match = re.search(r"^description:\s*(.*)", fm_text, re.MULTILINE)
        description = desc_match.group(1).strip() if desc_match else None
        
        if not description:
            files_missing_description.append({
                "file": f"{folder}/{file}",
                "reason": "Missing description",
                "title": title
            })
        else:
            # We can print standard metadata if found
            pass

print(f"Total markdown files checked: {total_files}")
print(f"Files missing frontmatter description: {len(files_missing_description)}")
print("-" * 75)
for fmd in files_missing_description:
    title_str = f"'{fmd['title']}'" if "title" in fmd and fmd["title"] else "No Title"
    print(f"- {fmd['file']} ({title_str}): {fmd['reason']}")
