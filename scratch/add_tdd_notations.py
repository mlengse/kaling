import os
import re

base_dir = r"c:\Users\anjan\dev\kaling\docs"

# Map of standard markdown files and the specific EP matches (search substrings)
tdd_map = {
    "pmkp/2.md": [
        "Penandaan sisi operasi/tindakan medis",
        "Surgical Safety Checklist"
    ],
    "pkp/4.md": [
        "Kajian ulang dibuat dalam bentuk CPPT"
    ],
    "pkp/8.md": [
        "Klinik menetapkan prosedur pelayanan anestesi",
        "Pelayanan anestesi dan bedah dilakukan oleh tenaga medis",
        "Jenis, dosis dan teknik anestesi dan pemantauan",
        "Ada bukti pelaksanaan kajian pra bedah",
        "Ada bukti pelaksanaan kajian pra anestesi",
        "Ada bukti pemantauan dan evaluasi paska"
    ],
    "pkp/9.md": [
        "Asuhan gizi dilakukan oleh petugas yang berkompeten",
        "Disusun rencana asuhan gizi",
        "distribusi dan pemberian makanan",
        "Pasien dan/atau keluarga diberi edukasi tentang pembatasan"
    ],
    "pkp/10.md": [
        "Ada bukti ringkasan pulang"
    ],
    "pkp/11.md": [
        "Ada sarana transportasi rujukan"
    ],
    "pkp/13.md": [
        "Ada penetapan jenis-jenis pelayanan laboratorium",
        "Terdapat Penanggung Jawab Laboratorium",
        "Klinik menetapkan rentang nilai normal",
        "Ada bukti reagensia esensial",
        "Ada prosedur pelaporan, pencatatan dan tindak lanjut hasil",
        "Ada bukti pelaksanaan Pemantapan Mutu Internal"
    ],
    "pkp/14.md": [
        "Klinik menerapkan prosedur pelayanan radiologi",
        "Ada bukti pelayanan radiologi sesuai dengan prosedur"
    ],
    "pkp/15.md": [
        "Tersedia bukti pengelolaan dan pelayanan sediaan farmasi",
        "Tersedia daftar formularium obat",
        "Ada kebijakan dan atau prosedur pengadaan obat",
        "Tersedia bukti dilakukan pengkajian resep",
        "Tersedia bukti pemberian informasi obat",
        "Tersedia bukti rekonsiliasi obat",
        "Tersedia obat emergensi pada unit-unit",
        "Tersedia bukti penyimpanan dan pelaporan obat",
        "Tersedia bukti penyimpanan obat termasuk obat",
        "Tersedia kebijakan dan atau prosedur penanganan obat",
        "Terdapat pencatatan dan pelaporan MESO",
        "Ada kebijakan dan atau prosedur pemantauan dan pelaporan",
        "Dalam hal klinik tidak memiliki apoteker"
    ]
}

print("Adding TDD notations and hyperlinks to relevant EPs...")
print("-" * 75)

modified_count = 0

for relative_path, queries in tdd_map.items():
    file_path = os.path.join(base_dir, relative_path.replace("/", os.sep))
    if not os.path.exists(file_path):
        print(f"Warning: File {file_path} not found.")
        continue
        
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Split content by line and process under Elemen Penilaian
    lines = content.split("\n")
    in_ep_section = False
    modified_file = False
    
    for i, line in enumerate(lines):
        # Detect start of Elemen Penilaian section
        if re.match(r"^##\s*Elemen\s*Penila[ia]*n", line, re.IGNORECASE):
            in_ep_section = True
            continue
            
        # If in EP section, look for top-level EP bullet/list items
        if in_ep_section:
            # We want to match top-level numbered list item: e.g., "1. " or "2. "
            m = re.match(r"^ {0,2}(\d+)\.\s+(.*)", line)
            if m:
                ep_text = m.group(2)
                # Check if this line matches any of our queries
                for query in queries:
                    # Let's do a case-insensitive check of query in ep_text
                    if query.lower() in ep_text.lower():
                        # Check if TDD notation is already in the line
                        if "Bisa TDD" not in line:
                            # Append the TDD notation before any trailing colons or directly at end of line
                            # Clean end of line spaces
                            clean_line = line.strip()
                            
                            # Determine where to add
                            if clean_line.endswith(":") or clean_line.endswith(".") or clean_line.endswith("*"):
                                # If it has a period, we can append it after or before the period
                                line_without_period = clean_line.rstrip(".")
                                lines[i] = f"{line_without_period} ⚠️ **[Bisa TDD](/pendahuluan/tdd)**."
                            else:
                                lines[i] = f"{clean_line} ⚠️ **[Bisa TDD](/pendahuluan/tdd)**"
                            
                            modified_file = True
                            print(f"- Added TDD link to {relative_path} EP {m.group(1)}: {query[:40]}...")
                            break
                            
    if modified_file:
        new_content = "\n".join(lines)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        modified_count += 1

print("-" * 75)
print(f"Completed! Added notations to {modified_count} out of {len(tdd_map)} files.")
