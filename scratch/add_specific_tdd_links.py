import os
import re

base_dir = r"c:\Users\anjan\dev\kaling\docs"
tdd_file = os.path.join(base_dir, "pendahuluan", "tdd.md")

# 1. Read and update docs/pendahuluan/tdd.md to add HTML anchors
print("Adding HTML anchors to docs/pendahuluan/tdd.md...")
print("-" * 75)

with open(tdd_file, "r", encoding="utf-8") as f:
    tdd_content = f.read()

tdd_lines = tdd_content.split("\n")
modified_tdd = False

for i, line in enumerate(tdd_lines):
    # Match pattern: e.g. "1. PMKP 2 ep 4: ..." or "2. PMKP 2 ep 5 ..." or "1. PKP 4 ep 3 Kajian..."
    m = re.match(r"^ {0,3}(\d+)\.\s+((PMKP|PKP)\s+(\d+)\s+ep\s+(\d+))", line, re.IGNORECASE)
    if m:
        code_str = m.group(2) # "PMKP 2 ep 4" or "PKP 4 ep 3"
        bab = m.group(3).lower() # "pmkp" or "pkp"
        std_num = m.group(4) # "2" or "4"
        ep_num = m.group(5) # "4" or "3"
        
        anchor_id = f"{bab}-{std_num}-ep-{ep_num}"
        anchor_tag = f'<a id="{anchor_id}"></a>'
        
        # Check if anchor is already there on the previous line or in the line
        has_anchor = False
        if i > 0 and anchor_tag in tdd_lines[i-1]:
            has_anchor = True
        elif anchor_tag in line:
            has_anchor = True
            
        if not has_anchor:
            # Insert the anchor tag on the line before the list item
            # Let's insert it inline or on the line before
            tdd_lines[i] = f'{anchor_tag}\n{line}'
            modified_tdd = True
            print(f"- Added anchor #{anchor_id} to tdd.md at line {i+1}")

if modified_tdd:
    new_tdd_content = "\n".join(tdd_lines)
    with open(tdd_file, "w", encoding="utf-8") as f:
        f.write(new_tdd_content)
    print("Successfully updated tdd.md with specific anchors!")
else:
    print("All anchors already exist in tdd.md.")

print("-" * 75)

# 2. Update specific standards files to target these new anchors
print("Updating standards files to target specific TDD anchors...")
folders = ["tkk", "pmkp", "pkp"]

# Map of standard code to file path
# Standard names like PMKP 2 -> pmkp/2.md, PKP 8 -> pkp/8.md
modified_files_count = 0

for folder in folders:
    folder_path = os.path.join(base_dir, folder)
    if not os.path.exists(folder_path):
        continue
    
    files = [f for f in os.listdir(folder_path) if f.endswith(".md") and f != "index.md"]
    for file in files:
        file_path = os.path.join(folder_path, file)
        
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        lines = content.split("\n")
        modified_file = False
        in_ep_section = False
        
        # Get standard number from file name, e.g. "2" from "2.md"
        std_num = os.path.splitext(file)[0]
        bab = folder.lower() # "pmkp" or "pkp"
        
        for i, line in enumerate(lines):
            # Detect start of Elemen Penilaian section
            if re.match(r"^##\s*Elemen\s*Penila[ia]*n", line, re.IGNORECASE):
                in_ep_section = True
                continue
                
            if in_ep_section:
                # Find EPs with the TDD notation
                # We look for a line containing "Bisa TDD"
                if "Bisa TDD" in line:
                    # Let's parse the EP number from the line
                    m = re.match(r"^ {0,2}(\d+)\.\s+(.*)", line)
                    if m:
                        ep_num = m.group(1)
                        # Construct the specific anchor ID, e.g. pmkp-2-ep-4
                        # Wait! For pmkp/2.md:
                        # In docs/pmkp/2.md, EP 1 is officially EP 4, EP 2 is officially EP 5.
                        # For other files (like pkp/8.md), EP 1 is EP 1, EP 2 is EP 2, etc.
                        # Let's handle the specific standard mapping for PMKP 2:
                        actual_ep_num = ep_num
                        if bab == "pmkp" and std_num == "2":
                            if ep_num == "1":
                                actual_ep_num = "4"
                            elif ep_num == "2":
                                actual_ep_num = "5"
                        
                        anchor_id = f"{bab}-{std_num}-ep-{actual_ep_num}"
                        
                        # Replace the general link (/pendahuluan/tdd) with the specific link (/pendahuluan/tdd#anchor_id)
                        old_link = "(/pendahuluan/tdd)"
                        new_link = f"(/pendahuluan/tdd#{anchor_id})"
                        
                        if old_link in line:
                            lines[i] = line.replace(old_link, new_link)
                            modified_file = True
                            print(f"- Updated link in {bab}/{file} EP {ep_num} -> #{anchor_id}")
                            
        if modified_file:
            new_content = "\n".join(lines)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            modified_files_count += 1

print("-" * 75)
print(f"Completed! Modified {modified_files_count} standards files with specific TDD anchor links.")
