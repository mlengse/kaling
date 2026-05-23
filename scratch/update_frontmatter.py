import os
import re

base_dir = r"c:\Users\anjan\dev\kaling\docs"

# Hardcoded mappings of files to their titles and optimized descriptions
metadata_map = {
    # TKK
    "tkk/1.md": {
        "title": "1.1. Organisasi",
        "description": "Panduan dan template lengkap akreditasi Tata Kelola Klinik (TKK 1) tentang visi, misi, dan struktur organisasi klinik sesuai KMK 62/2026."
    },
    "tkk/2.md": {
        "title": "1.2. SDM",
        "description": "Panduan Tata Kelola SDM Klinik (TKK 2) mencakup perencanaan kebutuhan tenaga, kelengkapan file kepegawaian (STR/SIP), dan evaluasi kinerja berkala."
    },
    "tkk/3.md": {
        "title": "1.3. Fasilitas Keselamatan",
        "description": "Panduan Tata Kelola Fasilitas dan Keselamatan (TKK 3/MFK) mencakup program MFK, pengelolaan B3, evakuasi bencana, proteksi kebakaran, pemeliharaan APAR, dan alat medis."
    },
    "tkk/4.md": {
        "title": "1.4. Kerja Sama",
        "description": "Panduan Tata Kelola Kerja Sama Klinik (TKK 4) mencakup perjanjian kerja sama (MoU) eksternal dan pemantauan indikator kinerja (KPI) pihak ketiga secara berkala."
    },
    "tkk/index.md": {
        "title": "1. Tata Kelola Klinik",
        "description": "Kumpulan standar instrumen akreditasi kelompok Tata Kelola Klinik (Bab I: TKK) lengkap dengan penjelasan maksud, tujuan, dan template dokumen pendukung."
    },
    
    # PMKP
    "pmkp/1.md": {
        "title": "2.1. Upaya Peningkatan Mutu",
        "description": "Panduan Upaya Peningkatan Mutu dan Keselamatan Pasien (PMKP 1) mencakup penanggung jawab mutu, indikator nasional mutu (INM), register risiko terintegrasi, dan laporan IKP."
    },
    "pmkp/2.md": {
        "title": "2.2. SKP",
        "description": "Panduan penerapan 6 Sasaran Keselamatan Pasien (PMKP 2/SKP) seperti identifikasi pasien, SBAR/TBAK, WHO Surgical Safety Checklist, dan pencegahan risiko jatuh."
    },
    "pmkp/3.md": {
        "title": "2.3. PPI",
        "description": "Panduan Pencegahan dan Pengendalian Infeksi (PMKP 3/PPI) mencakup hand hygiene WHO, sterilisasi alat medis terstandar, dan laporan program tahunan PPI klinik."
    },
    "pmkp/index.md": {
        "title": "2. PMKP",
        "description": "Kumpulan standar instrumen akreditasi kelompok Peningkatan Mutu dan Keselamatan Pasien (Bab II: PMKP) lengkap dengan penjelasan standar dan template dokumen."
    },
    
    # PKP
    "pkp/1.md": {
        "title": "3. 1. Hak Pasien & Keluarga",
        "description": "Panduan Hak Pasien dan Keluarga (PKP 1) mencakup sosialisasi hak kewajiban pasien, penanganan keluhan/komplain pasien, dan pemenuhan akses berkebutuhan khusus."
    },
    "pkp/2.md": {
        "title": "3. 2. Proses Asuhan",
        "description": "Panduan Persetujuan Tindakan Kedokteran (PKP 2/Informed Consent) dan penjelasan hak pasien memahami rencana asuhan klinis serta alternatif pengobatan."
    },
    "pkp/3.md": {
        "title": "3. 3. Akses Pasien",
        "description": "Panduan Akses, Pendaftaran, dan Skrining Pasien (PKP 3) mencakup triase visual UGD, isolasi batuk infeksius, dan pendaftaran sistem informasi SIM-Klinik."
    },
    "pkp/4.md": {
        "title": "3. 4. Pengkajian Pasien",
        "description": "Panduan Pengkajian Awal Pasien (PKP 4) oleh Profesional Pemberi Asuhan (PPA) mencakup status fisik, riwayat obat, skrining gizi MST, dan form cppt."
    },
    "pkp/5.md": {
        "title": "3. 5. Pelaksanaan Asuhan",
        "description": "Panduan Pelaksanaan Asuhan Klinis Terintegrasi (PKP 5) dan evaluasi rencana asuhan secara berkala oleh PPA yang didokumentasikan di rekam medis terpadu."
    },
    "pkp/6.md": {
        "title": "3. 6. Promotif Preventif",
        "description": "Panduan Pelayanan Promotif dan Preventif (PKP 6) mencakup Program Prioritas Nasional (Proprinas) seperti tuberkulosis (SITB), HIV (SIHA), stunting, dan KIA."
    },
    "pkp/7.md": {
        "title": "3. 7. Pelayanan Risiko Tinggi",
        "description": "Panduan Pelayanan Pasien Risiko Tinggi dan Emergensi Gawat Darurat (PKP 7) di klinik, termasuk penularan airborne, pencegahan bunuh diri, dan populasi rentan."
    },
    "pkp/8.md": {
        "title": "3. 8. Anestesi dan Bedah",
        "description": "Panduan Pelayanan Anestesi Lokal dan Bedah Minor (PKP 8) mencakup kajian pra-bedah, pra-anestesi, pemantauan status fisiologis intra/pasca tindakan."
    },
    "pkp/9.md": {
        "title": "3. 9. Gizi",
        "description": "Panduan Pelayanan Gizi Klinik (PKP 9) mencakup skrining gizi MST rawat inap, pemesanan dan distribusi makanan higienis, serta edukasi gizi keluarga."
    },
    "pkp/10.md": {
        "title": "3.10. Pemulangan dan Tindak Lanjut",
        "description": "Panduan Pemulangan dan Tindak Lanjut Pasien (PKP 10) mencakup resume medis pulang (discharge summary), kriteria pulang rawat inap, dan kontrol pasca rawat."
    },
    "pkp/11.md": {
        "title": "3.11. Rujukan",
        "description": "Panduan Pelayanan Rujukan Pasien (PKP 11) mencakup surat rujukan terpadu, komunikasi rujukan antar fasyankes, daftar jejaring, dan MoU ambulans 24 jam."
    },
    "pkp/12.md": {
        "title": "3.12. Rekam Medis",
        "description": "Panduan Penyelenggaraan Rekam Medis (PKP 12) mencakup kerahasiaan rekam medis elektronik, peminjaman berkas, retensi, pemusnahan, dan cara pembetulan salah tulis."
    },
    "pkp/13.md": {
        "title": "3.13. Laboratorium",
        "description": "Panduan Pelayanan Laboratorium Klinik (PKP 13) mencakup jenis pemeriksaan, rentang nilai normal, pemantauan mutu internal/eksternal (PMI/PME), dan pelaporan nilai kritis."
    },
    "pkp/14.md": {
        "title": "3.14. Radiologi",
        "description": "Panduan Pelayanan Radiologi (PKP 14) mencakup prosedur keselamatan radiologi, proteksi paparan radiasi personal, penggunaan Pb apron, dan kalibrasi berkala."
    },
    "pkp/15.md": {
        "title": "3.15. Kefarmasian",
        "description": "Panduan Pelayanan Kefarmasian Lengkap (PKP 15) mencakup daftar formularium obat, resep obat High Alert/LASA, narkotika, rekonsiliasi, MESO, dan medication error."
    },
    "pkp/index.md": {
        "title": "3. PKP",
        "description": "Kumpulan standar instrumen akreditasi kelompok Penyelenggaraan Kesehatan Perseorangan (Bab III: PKP) lengkap dengan 15 standar klinis dan template dokumen."
    },
    
    # Pendahuluan & Survei & Home
    "index.md": {
        "title": "Home - Akreditasi Klinik",
        "description": "Platform referensi digital persiapan akreditasi Klinik Pratama dan Utama lengkap dengan instrumen TKK, PMKP, PKP, dan 25 template dokumen Word siap pakai."
    },
    "pendahuluan/index.md": {
        "title": "Pendahuluan",
        "description": "Selamat datang di panduan digital akreditasi Klinik Pratama dan Utama. Platform referensi terlengkap untuk mempersiapkan pemenuhan kelengkapan bukti instrumen."
    },
    "pendahuluan/referensi.md": {
        "title": "Referensi Regulasi",
        "description": "Daftar regulasi resmi, undang-undang, keputusan menteri kesehatan (KMK 62/2026), dan dasar hukum akreditasi klinik yang berlaku aktif di Indonesia saat ini."
    },
    "pendahuluan/tdd.md": {
        "title": "Kriteria TDD",
        "description": "Penjelasan kriteria kelulusan akreditasi klinik: Tidak Dapat Diterapkan (TDD), Tidak Terpenuhi (TT), Terpenuhi Sebagian (TS), dan Terpenuhi Penuh (TP)."
    },
    "survei/index.md": {
        "title": "Alur Survei",
        "description": "Panduan umum alur pelaksanaan survei akreditasi klinik oleh lembaga penyelenggara resmi yang ditunjuk oleh Kementerian Kesehatan RI."
    },
    "survei/metode.md": {
        "title": "Metode Survei",
        "description": "Rincian metode survei akreditasi klinik (Dokusimwawastaf) untuk memeriksa dokumen bukti, simulasi tindakan, wawancara staf, dan observasi lapangan."
    },
    "survei/surveior.md": {
        "title": "Kode Etik Surveior",
        "description": "Kode etik resmi, kewajiban, hak, wewenang, dan tanggung jawab tim surveior akreditasi klinik selama melaksanakan penilaian lapangan secara profesional."
    }
}

print("Starting frontmatter descriptions enrichment...")
print("-" * 75)

modified_count = 0

for relative_path, metadata in metadata_map.items():
    file_path = os.path.join(base_dir, relative_path.replace("/", os.sep))
    if not os.path.exists(file_path):
        print(f"Warning: File {file_path} not found.")
        continue
        
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    title = metadata["title"]
    description = metadata["description"]
    
    # Check if file has frontmatter
    fm_match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    
    if fm_match:
        fm_text = fm_match.group(1)
        original_fm_text = fm_text
        
        # Check if description already exists in frontmatter
        if "description:" in fm_text:
            # Replace existing description with quotes
            fm_text = re.sub(r"^description:\s*(.*)", f'description: "{description}"', fm_text, flags=re.MULTILINE)
        else:
            # Add description with quotes
            fm_text = fm_text.strip() + f'\ndescription: "{description}"\n'
            
        # Update title with quotes
        if "title:" in fm_text:
            fm_text = re.sub(r"^title:\s*(.*)", f'title: "{title}"', fm_text, flags=re.MULTILINE)
        else:
            fm_text = f'title: "{title}"\n' + fm_text
            
        new_content = content.replace(original_fm_text, fm_text)
    else:
        # Create brand new frontmatter block with quotes
        new_content = f"""---
title: "{title}"
description: "{description}"
---
""" + content

    if new_content != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Enriched: {relative_path}")
        modified_count += 1
    else:
        print(f"No changes (already correct): {relative_path}")

print("-" * 75)
print(f"Completed! Enriched {modified_count} out of {len(metadata_map)} files.")
