import os

# Base directory for docs
base_dir = r"c:\Users\anjan\dev\kaling\docs"

# Mapping of file path to specific string replacements
replacements = {
    # ----------------- TKK STANDARDS -----------------
    "tkk/1.md": [
        # EP 2
        (
            """2. Tersedia struktur organisasi klinik yang ditetapkan oleh pemilik/pejabat berwenang. 
   ::: tip Kelengkapan Bukti
    1. Terdapat struktur organisasi klinik \tdalam \tdokumen pendirian klinik ataupun dokumen lain yang sah 
    2. Terdapat \tbukti penyampaian \tinformasi struktur organisasi klinik  
    :::""",
            """2. Tersedia struktur organisasi klinik yang ditetapkan oleh pemilik/pejabat berwenang. 
   :::tip Kelengkapan Bukti
   1. Terdapat struktur organisasi klinik dalam dokumen pendirian klinik ataupun dokumen lain yang sah 
   2. Terdapat bukti penyampaian informasi struktur organisasi klinik  
   3. 📥 **Unduh Template:** [SK Struktur Organisasi, Tata Kerja, & Uraian Tugas (Word)](/templates/sk-struktur-organisasi-uraian-tugas.doc)
   :::"""
        ),
        # EP 3
        (
            """3. Tersedia uraian tugas, tanggung jawab, wewenang yang ditetapkan. 
   ::: tip Kelengkapan Bukti
   1. Terdapat dokumen yang sah yang mencantumkan uraian tugas, tanggung jawab dan wewenang 
   2. Melakukan wawancara terhadap petugas dalam memahami uraian tugas, tanggung jawab dan wewenang   
   :::""",
            """3. Tersedia uraian tugas, tanggung jawab, wewenang yang ditetapkan. 
   :::tip Kelengkapan Bukti
   1. Terdapat dokumen yang sah yang mencantumkan uraian tugas, tanggung jawab dan wewenang 
   2. Melakukan wawancara terhadap petugas dalam memahami uraian tugas, tanggung jawab dan wewenang   
   3. 📥 **Unduh Template:** [SK Struktur Organisasi, Tata Kerja, & Uraian Tugas (Word)](/templates/sk-struktur-organisasi-uraian-tugas.doc)
   :::"""
        )
    ],
    "tkk/2.md": [
        # EP 2
        (
            """2. Tersedia file kepegawaian seluruh SDM yang diperbaharui secara berkala. 
   :::tip Kelengkapan Bukti
    Terdapat dokumen file kepegawaian seluruh SDM yang diperbaharui secara berkala 
    :::""",
            """2. Tersedia file kepegawaian seluruh SDM yang diperbaharui secara berkala. 
   :::tip Kelengkapan Bukti
   1. Terdapat dokumen file kepegawaian seluruh SDM yang diperbaharui secara berkala.
   2. 📥 **Unduh Template:** [Checklist File Kepegawaian & Kualifikasi SDM (Word)](/templates/rencana-sdm-evaluasi-kinerja.doc)
   :::"""
        )
    ],
    "tkk/3.md": [
        # EP 1
        (
            """1. Tersedia bukti perizinan sesuai ketentuan peraturan perundang-undangan yang berlaku.  
   :::tip Kelengkapan Bukti
   Terdapat dokumen bukti perizinan sesuai ketentuan perundang-undangan yang berlaku
   :::""",
            """1. Tersedia bukti perizinan sesuai ketentuan peraturan perundang-undangan yang berlaku.  
   :::tip Kelengkapan Bukti
   1. Terdapat dokumen bukti perizinan sesuai ketentuan perundang-undangan yang berlaku
   2. 📥 **Unduh Template:** [Panduan Persyaratan Izin & Self-Assessment Klinik (Word)](/templates/program-mfk-manajemen-risiko.doc)
   :::"""
        ),
        # EP 3
        (
            """3. Tersedia daftar inventaris dan bukti pemeliharaan sarana yang tersedia di klinik. 
   :::tip Kelengkapan Bukti
   1. Terdapat dokumen daftar inventaris sarana yang tersedia di klinik 
   2. Terdapat SPO pemeliharaan sarana yang tersedia di klinik 
   3. Terdapat dokumen bukti pemeliharaan sarana yang tersedia di klinik 
   4. Melakukan observasi terhadap bukti pemeliharaan sarana  
   5. Melakukan wawancara terkait proses pemeliharaan sarana yang tersedia  
   :::""",
            """3. Tersedia daftar inventaris dan bukti pemeliharaan sarana yang tersedia di klinik. 
   :::tip Kelengkapan Bukti
   1. Terdapat dokumen daftar inventaris sarana yang tersedia di klinik 
   2. Terdapat SPO pemeliharaan sarana yang tersedia di klinik 
   3. Terdapat dokumen bukti pemeliharaan sarana yang tersedia di klinik 
   4. Melakukan observasi terhadap bukti pemeliharaan sarana  
   5. Melakukan wawancara terkait proses pemeliharaan sarana yang tersedia  
   6. 📥 **Unduh Template:** [Program MFK & Pemeliharaan Sarana Gedung (Word)](/templates/program-mfk-manajemen-risiko.doc)
   :::"""
        ),
        # EP 4
        (
            """4. Tersedia bukti pelaksanaan pengamanan dan pengawasan akses keluar masuk fasyankes. 
   :::tip Kelengkapan Bukti
   1. Terdapat SPO pelaksanaan pengamanan klinik 
   2. Terdapat dokumen bukti pelaksanaan pengamanan dan pengawasan akses keluar masuk klinik 
   3. Melakukan observasi dan wawancara terhadap pelaksanaan pengamanan dan pengawasan akses keluar masuk klinik 
   :::""",
            """4. Tersedia bukti pelaksanaan pengamanan dan pengawasan akses keluar masuk fasyankes. 
   :::tip Kelengkapan Bukti
   1. Terdapat SPO pelaksanaan pengamanan klinik 
   2. Terdapat dokumen bukti pelaksanaan pengamanan dan pengawasan akses keluar masuk klinik 
   3. Melakukan observasi dan wawancara terhadap pelaksanaan pengamanan dan pengawasan akses keluar masuk klinik 
   4. 📥 **Unduh Template:** [SPO Keamanan Gedung & Akses Keluar Masuk (Word)](/templates/program-mfk-manajemen-risiko.doc)
   :::"""
        ),
        # EP 6
        (
            """6. Tersedia bukti pengelolaan sampah domestik serta pengelolaan air limbah sesuai peraturan perundang-undangan. 
   :::tip Kelengkapan Bukti
   1. Terdapat SPO pengelolaan sampah domestik serta pengelolaan air limbah 
   2. Terdapat dokumen bukti pengelolaan sampah domestik serta pengelolaan air limbah sesuai dengan ketentuan peraturan perundang-undangan. 
   3. Melakukan observasi pengelolaan sampah domestik serta pengelolaan air limbah  
   4. Melakukan wawancara dengan petugas tentang proses pengelolaan sampah domestik serta pengelolaan air limbah""",
            """6. Tersedia bukti pengelolaan sampah domestik serta pengelolaan air limbah sesuai peraturan perundang-undangan. 
   :::tip Kelengkapan Bukti
   1. Terdapat SPO pengelolaan sampah domestik serta pengelolaan air limbah 
   2. Terdapat dokumen bukti pengelolaan sampah domestik serta pengelolaan air limbah sesuai dengan ketentuan peraturan perundang-undangan. 
   3. Melakukan observasi pengelolaan sampah domestik serta pengelolaan air limbah  
   4. Melakukan wawancara dengan petugas tentang proses pengelolaan sampah domestik serta pengelolaan air limbah
   5. 📥 **Unduh Template:** [SPO Pengelolaan Sampah & Air Limbah IPAL (Word)](/templates/program-mfk-manajemen-risiko.doc)"""
        ),
        # EP 10
        (
            """10. Tersedia daftar inventaris, bukti pemeliharaan dan bukti kalibrasi peralatan medis dan bukti izin Bapeten untuk yang memiliki pelayanan radiologi. 
    :::tip Kelengkapan Bukti
       1. Terdapat SPO pemeliharaan dan kalibrasi peralatan medis 
       2. Terdapat dokumen berupa daftar inventaris peralatan medis 
       3. Terdapat bukti pemeliharaan dan bukti kalibrasi peralatan medis 
       4. Terdapat bukti izin BAPETEN untuk yang memiliki pelayanan radiologi 
       5. Melakukan observasi untuk memastikan peralatan medis sesuai dengan daftar inventaris dan terpelihara dengan baik 
       6. Melakukan wawancara tentang proses pemeliharaan dan kalibrasi peralatan medis  
    :::""",
            """10. Tersedia daftar inventaris, bukti pemeliharaan dan bukti kalibrasi peralatan medis dan bukti izin Bapeten untuk yang memiliki pelayanan radiologi. 
    :::tip Kelengkapan Bukti
       1. Terdapat SPO pemeliharaan dan kalibrasi peralatan medis 
       2. Terdapat dokumen berupa daftar inventaris peralatan medis 
       3. Terdapat bukti pemeliharaan dan bukti kalibrasi peralatan medis 
       4. Terdapat bukti izin BAPETEN untuk yang memiliki pelayanan radiologi 
       5. Melakukan observasi untuk memastikan peralatan medis sesuai dengan daftar inventaris dan terpelihara dengan baik 
       6. Melakukan wawancara tentang proses pemeliharaan dan kalibrasi peralatan medis  
       7. 📥 **Unduh Template:** [Logbook Pemeliharaan & Kalibrasi Alat Medis (Word)](/templates/program-mfk-manajemen-risiko.doc)
    :::"""
        )
    ],
    "tkk/4.md": [
        # EP 2
        (
            """2. Dokumen kontrak memiliki indikator kinerja pihak yang melakukan kerjasama.  
   :::tip Kelengkapan Bukti
    Terdapat indikator kinerja pihak yang melakukan kerjasama dan tercantum pada dokumen kontrak.  
   :::""",
            """2. Dokumen kontrak memiliki indikator kinerja pihak yang melakukan kerjasama.  
   :::tip Kelengkapan Bukti
   * Terdapat indikator kinerja pihak yang melakukan kerjasama dan tercantum pada dokumen kontrak.  
   * 📥 **Unduh Template:** [Daftar KPI / Indikator Mutu Pihak Ketiga (Word)](/templates/mou-kontrak-kerja-sama-kpi.doc)
   :::"""
        ),
        # EP 3
        (
            """3. Ada bukti monitoring dan evaluasi serta tindak lanjut terhadap pemenuhan indikator kinerja yang tercantum di dalam kontrak. 
   :::tip Kelengkapan Bukti
   1. Terdapat dokumen bukti monitoring dan evaluasi serta tindak lanjut terhadap pemenuhan indikator kinerja yang tercantum di dalam kontrak. 
   2. Melakukan wawancara terkait monitoring dan evaluasi  serta tindak lanjut terhadap pemenuhan indikator kinerja yang tercantum di dalam kontrak 
   :::""",
            """3. Ada bukti monitoring dan evaluasi serta tindak lanjut terhadap pemenuhan indikator kinerja yang tercantum di dalam kontrak. 
   :::tip Kelengkapan Bukti
   1. Terdapat dokumen bukti monitoring dan evaluasi serta tindak lanjut terhadap pemenuhan indikator kinerja yang tercantum di dalam kontrak. 
   2. Melakukan wawancara terkait monitoring dan evaluasi  serta tindak lanjut terhadap pemenuhan indikator kinerja yang tercantum di dalam kontrak 
   3. 📥 **Unduh Template:** [Form Monev Kinerja Bulanan Rekanan Klinik (Word)](/templates/mou-kontrak-kerja-sama-kpi.doc)
   :::"""
        )
    ],

    # ----------------- PMKP STANDARDS -----------------
    "pmkp/1.md": [
        # EP 2
        (
            """2. Ada indikator mutu layanan yang diukur, dievaluasi, analisa dan tindak lanjut serta dilaporkan sesuai dengan ketentuan. 
   :::tip Kelengkapan Bukti
\t 1. Terdapat penetapan indikator mutu klinik 
\t 2. Terdapat Kebijakan terkait pengukuran dan pelaporan indikator mutu klinik 
\t 3. Terdapat dokumen bukti pengukuran, evaluasi, analisa, tindak lanjut dan pelaporan indikator mutu klinik yang dilaporkan kepada penanggung jawab klinik dan pemilik 
\t 4. Terdapat dokumen bukti umpan balik perbaikan dari penanggung jawab klinik and pemilik
\t 5. Terdapat dokumen bukti pengukuran, evaluasi, analisa, tindak lanjut dan pelaporan Indikator Nasional Mutu yang disampaikan kepada Kementerian Kesehatan 
\t 6. Melaksanakan wawancara untuk \tmemastikan pelaksanaan pengukuran indikator mutu 
\t :::""",
            """2. Ada indikator mutu layanan yang diukur, dievaluasi, analisa dan tindak lanjut serta dilaporkan sesuai dengan ketentuan. 
   :::tip Kelengkapan Bukti
   1. Terdapat penetapan indikator mutu klinik (INM, Prioritas Klinik, Prioritas Unit)
   2. Terdapat Kebijakan terkait pengukuran dan pelaporan indikator mutu klinik 
   3. Terdapat dokumen bukti pengukuran, evaluasi, analisa, tindak lanjut dan pelaporan indikator mutu klinik
   4. Terdapat dokumen bukti umpan balik perbaikan dari penanggung jawab klinik dan pemilik
   5. Terdapat dokumen bukti pengukuran, evaluasi, analisa, tindak lanjut dan pelaporan Indikator Nasional Mutu
   6. Melaksanakan wawancara untuk memastikan pelaksanaan pengukuran indikator mutu 
   7. 📥 **Unduh Template:** [SK PJ Mutu & Daftar Indikator Mutu Klinik (Word)](/templates/sk-pj-mutu-indikator-risiko.doc)
   :::"""
        ),
        # EP 3
        (
            """3. Insiden keselamatan pasien dilaporkan dan dilakukan investigasi sesuai dengan ketentuan. 
   :::tip Kelengkapan Bukti 
\t 1. Terdapat dokumen bukti pelaporan insiden keselamatan pasien sesuai dengan ketentuan yang berlaku  
\t 2. Melaksanakan wawancara dengan penanggung jawab mutu tentang pelaporan dan proses investigasi terhadap insiden keselamatan pasien 
\t :::""",
            """3. Insiden keselamatan pasien dilaporkan dan dilakukan investigasi sesuai dengan ketentuan. 
   :::tip Kelengkapan Bukti 
   1. Terdapat dokumen bukti pelaporan insiden keselamatan pasien sesuai dengan ketentuan yang berlaku (KNC/KTD/Sentinel)
   2. Melaksanakan wawancara dengan penanggung jawab mutu tentang pelaporan dan proses investigasi terhadap insiden keselamatan pasien 
   3. 📥 **Unduh Template:** [Form Pelaporan & Investigasi Insiden Keselamatan Pasien (Word)](/templates/sk-pj-mutu-indikator-risiko.doc)
   :::"""
        ),
        # EP 5
        (
            """5. Ada bukti tindak lanjut dari mitigasi resiko 
   :::tip Kelengkapan Bukti 
   1. Terdapat bukti tindak lanjut dari mitigasi risiko 
   2. Melakukan wawancara dengan penanggung jawab mutu tentang tindak lanjut dari mitigasi risiko 
\t :::""",
            """5. Ada bukti tindak lanjut dari mitigasi resiko 
   :::tip Kelengkapan Bukti 
   1. Terdapat bukti tindak lanjut dari mitigasi risiko 
   2. Melakukan wawancara dengan penanggung jawab mutu tentang tindak lanjut dari mitigasi risiko 
   3. 📥 **Unduh Template:** [Register Risiko & Rencana Mitigasi Klinik (Word)](/templates/sk-pj-mutu-indikator-risiko.doc)
   :::"""
        )
    ],
    "pmkp/2.md": [
        # EP 3 (Keamanan obat risiko tinggi)
        (
            """2. Tersedia bukti pengelolaan keamanan obat resiko tinggi. 
   :::tip Kelengkapan Bukti
   1. Terdapat SPO pengelolaan keamanan obat risiko tinggi 
   2. Terdapat daftar obat risiko tinggi yang diperbaharui secara berkala 
   3. Melaksanakan observasi dan wawancara dengan petugas terkait pengelolaan keamanan obat risiko tinggi 
   :::""",
            """2. Tersedia bukti pengelolaan keamanan obat resiko tinggi. 
   :::tip Kelengkapan Bukti
   1. Terdapat SPO pengelolaan keamanan obat risiko tinggi 
   2. Terdapat daftar obat risiko tinggi yang diperbaharui secara berkala 
   3. Melaksanakan observasi dan wawancara dengan petugas terkait pengelolaan keamanan obat risiko tinggi 
   4. 📥 **Unduh Template:** [SPO & Daftar Obat High Alert / LASA (Word)](/templates/pelayanan-kefarmasian-lengkap.doc)
   :::"""
        ),
        # EP 6 (Media kebersihan tangan)
        (
            """3. Ada media informasi penerapan kebersihan tangan sesuai ketentuan WHO. 
   :::tip Kelengkapan Bukti
   1. Terdapat SPO kebersihan tangan  
   2. Terdapat media informasi tentang penerapan kebersihan tangan  
   3. Melaksanakan \twawancara dengan \tpasien \tdan \tpetugas tentang penerapan kebersihan tangan  
   4. Simulasi kebersihan tangan oleh pasien dan petugas .    
   :::""",
            """3. Ada media informasi penerapan kebersihan tangan sesuai ketentuan WHO. 
   :::tip Kelengkapan Bukti
   1. Terdapat SPO kebersihan tangan  
   2. Terdapat media informasi tentang penerapan kebersihan tangan  
   3. Melaksanakan wawancara dengan pasien dan petugas tentang penerapan kebersihan tangan  
   4. Simulasi kebersihan tangan oleh pasien dan petugas 
   5. 📥 **Unduh Template:** [Kebijakan, Program Kerja, & SPO Hand Hygiene PPI (Word)](/templates/kebijakan-program-ppi.doc)
   :::"""
        ),
        # EP 8 (Implementasi pencegahan pasien jatuh)
        (
            """5. Ada bukti implementasi langkah-langkah pencegahan pasien jatuh. 
   :::tip Kelengkapan Bukti
   1. Melaksanakan observasi bukti implementasi pencegahan pasien jatuh. 
   2. Melaksanakan wawancara dengan petugas terkait implementasi pencegahan pasien jatuh. 
   :::""",
            """5. Ada bukti implementasi langkah-langkah pencegahan pasien jatuh. 
   :::tip Kelengkapan Bukti
   1. Melaksanakan observasi bukti implementasi pencegahan pasien jatuh. 
   2. Melaksanakan wawancara dengan petugas terkait implementasi pencegahan pasien jatuh. 
   3. 📥 **Unduh Template:** [Asesmen & Protokol Pencegahan Risiko Jatuh (Word)](/templates/form-pencegahan-risiko-jatuh.doc)
   :::"""
        )
    ],
    "pmkp/3.md": [
        # EP 2
        (
            """2. Ditetapkan program PPI di klinik. 
   :::tip Kelengkapan Bukti
   1. Terdapat Program PPI yang ditetapkan oleh Penanggung jawab klinik 
   2. Terdapat bukti pelaksanaan program PPI yang sesuai dengan dengan pelayanan kesehatan, risiko dan sumber daya yang ada di klinik 
   3. Observasi \tdan \twawancara  pelaksanaan program PPI  
   :::""",
            """2. Ditetapkan program PPI di klinik. 
   :::tip Kelengkapan Bukti
   1. Terdapat Program PPI yang ditetapkan oleh Penanggung jawab klinik 
   2. Terdapat bukti pelaksanaan program PPI yang sesuai dengan dengan pelayanan kesehatan, risiko dan sumber daya yang ada di klinik 
   3. Observasi dan wawancara pelaksanaan program PPI  
   4. 📥 **Unduh Template:** [Kebijakan, Program Kerja, & SPO Hand Hygiene PPI (Word)](/templates/kebijakan-program-ppi.doc)
   :::"""
        ),
        # EP 3
        (
            """3. Ada petugas yang kompeten yang bertanggung jawab melaksanakan, monitoring, mengevaluasi implementasi PPI di klinik serta melakukan edukasi dan sosialisasi secara berkala dan terdokumentasi. 
   :::tip Kelengkapan Bukti
   Terdapat SK penetapan penanggung jawab PPI 
   :::""",
            """3. Ada petugas yang kompeten yang bertanggung jawab melaksanakan, monitoring, mengevaluasi implementasi PPI di klinik serta melakukan edukasi dan sosialisasi secara berkala dan terdokumentasi. 
   :::tip Kelengkapan Bukti
   1. Terdapat SK penetapan penanggung jawab PPI 
   2. 📥 **Unduh Template:** [SK PJ Mutu & SK Penetapan Penanggung Jawab PPI (Word)](/templates/kebijakan-program-ppi.doc)
   :::"""
        ),
        # EP 5
        (
            """5. Tersedia bukti pelaksanaan program PPI di klinik. 
   :::tip Kelengkapan Bukti
   Terdapat bukti pelaksanaan program PPI dan telah dilaporkan kepada penanggung jawab klinik dan pemilik 
   :::""",
            """5. Tersedia bukti pelaksanaan program PPI di klinik. 
   :::tip Kelengkapan Bukti
   1. Terdapat bukti pelaksanaan program PPI dan telah dilaporkan kepada penanggung jawab klinik dan pemilik 
   2. 📥 **Unduh Template:** [Laporan Pelaksanaan Program PPI Klinik (Word)](/templates/kebijakan-program-ppi.doc)
   :::"""
        )
    ],

    # ----------------- PKP STANDARDS -----------------
    "pkp/1.md": [
        # EP 2
        (
            """2. Tersedia bukti petugas menjelaskan tentang hak dan kewajiban pasien beserta keluarganya.  
   :::tip Kelengkapan Bukti
   1. Terdapat dokumen bukti petugas telah menjelaskan tentang hak dan kewajiban pasien beserta keluarganya.  
   2. Melakukan observasi dan wawancara dengan petugas tentang cara menjelaskan hak dan kewajiban pasien beserta keluarganya.
   :::""",
            """2. Tersedia bukti petugas menjelaskan tentang hak dan kewajiban pasien beserta keluarganya.  
   :::tip Kelengkapan Bukti
   1. Terdapat dokumen bukti petugas telah menjelaskan tentang hak dan kewajiban pasien beserta keluarganya.  
   2. Melakukan observasi dan wawancara dengan petugas tentang cara menjelaskan hak dan kewajiban pasien beserta keluarganya.
   3. 📥 **Unduh Template:** [SK Kepala Klinik tentang Hak & Kewajiban Pasien (Word)](/templates/sk-hak-kewajiban.doc)
   :::"""
        ),
        # EP 3
        (
            """3. Pasien mengerti dan memahami hak dan kewajibannya. 
   :::tip Kelengkapan Bukti
   1. Terdapat dokumen bukti bahwa pasien mengerti dan memahami hak dan kewajibannya. 
   2. Melakukan wawancara dengan pasien apakah pasien mengerti dan memahami hak dan kewajibannya. 

   :::""",
            """3. Pasien mengerti dan memahami hak dan kewajibannya. 
   :::tip Kelengkapan Bukti
   1. Terdapat dokumen bukti bahwa pasien mengerti dan memahami hak dan kewajibannya. 
   2. Melakukan wawancara dengan pasien apakah pasien mengerti dan memahami hak dan kewajibannya. 
   3. 📥 **Unduh Template:** [SK Kepala Klinik tentang Hak & Kewajiban Pasien (Word)](/templates/sk-hak-kewajiban.doc)
   :::"""
        ),
        # EP 4
        (
            """4. Ada pemenuhan hak pasien berkebutuhan khusus atau dalam kondisi khusus. 
   :::tip Kelengkapan Bukti
   1. Terdapat SPO tentang pemenuhan hak pasien berkebutuhan khusus atau dalam kondisi khusus 
   2. Melakukan observasi dan wawancara kepada petugas dan pasien terkait proses pemenuhan hak pasien berkebutuhan khusus atau dalam kondisi khusus. 

   :::""",
            """4. Ada pemenuhan hak pasien berkebutuhan khusus atau dalam kondisi khusus. 
   :::tip Kelengkapan Bukti
   1. Terdapat SPO tentang pemenuhan hak pasien berkebutuhan khusus atau dalam kondisi khusus 
   2. Melakukan observasi dan wawancara kepada petugas dan pasien terkait proses pemenuhan hak pasien berkebutuhan khusus atau dalam kondisi khusus. 
   3. 📥 **Unduh Template:** [Panduan Pemenuhan Hak Pasien Berkebutuhan Khusus (Word)](/templates/sk-hak-kewajiban.doc)
   :::"""
        ),
        # EP 5
        (
            """5. Tersedia petugas, media atau tempat untuk menyampaikan keluhan pelayanan bagi pasien atau keluarga. 
   :::tip Kelengkapan Bukti
   1. Terdapat \tSPO \tpenanganan keluhan/komplain 
   2. Terdapat dokumen bukti tindak lanjut keluhan oleh klinik dan dikomunikasikan dengan pasien atau keluarga.  
   3. Melakukan observasi ketersediaan media atau sarana untuk menyampaikan keluhan pelayanan bagi pasien atau keluarga.
   4. Melakukan wawancara pasien terkait penanganan keluhan.  
   :::""",
            """5. Tersedia petugas, media atau tempat untuk menyampaikan keluhan pelayanan bagi pasien atau keluarga. 
   :::tip Kelengkapan Bukti
   1. Terdapat SPO penanganan keluhan/komplain 
   2. Terdapat dokumen bukti tindak lanjut keluhan oleh klinik dan dikomunikasikan dengan pasien atau keluarga.  
   3. Melakukan observasi ketersediaan media atau sarana untuk menyampaikan keluhan pelayanan bagi pasien atau keluarga.
   4. Melakukan wawancara pasien terkait penanganan keluhan.  
   5. 📥 **Unduh Template:** [SPO Penanganan Keluhan/Komplain Pasien (Word)](/templates/sk-hak-kewajiban.doc)
   :::"""
        ),
        # EP 6
        (
            """6. Ada tindak lanjut keluhan oleh klinik dan dikomunikasikan dengan pasien atau keluarga. 
   :::tip Kelengkapan Bukti
   1. Tersedia petugas, media atau tempat untuk menyampaikan keluhan pelayanan bagi pasien atau keluarga. 
   2. Ada tindak lanjut keluhan oleh klinik dan dikomunikasikan dengan pasien atau keluarga. 
 
   :::""",
            """6. Ada tindak lanjut keluhan oleh klinik dan dikomunikasikan dengan pasien atau keluarga. 
   :::tip Kelengkapan Bukti
   1. Tersedia petugas, media atau tempat untuk menyampaikan keluhan pelayanan bagi pasien atau keluarga. 
   2. Ada tindak lanjut keluhan oleh klinik dan dikomunikasikan dengan pasien atau keluarga. 
   3. 📥 **Unduh Template:** [Form Catatan Pengaduan & Tindak Lanjut (Word)](/templates/sk-hak-kewajiban.doc)
   :::"""
        ),
        # EP 7
        (
            """7. Ada dokumentasi pengaduan dan tindak lanjut yang telah dilakukan. 
   :::tip Kelengkapan Bukti
   1. Terdapat dokumen bukti pengaduan dan tindak lanjut yang telah dilakukan 
   2. Melakukan wawancara kepada petugas/manajemen \tklinik tentang proses tindak lanjut pengaduan    
   :::""",
            """7. Ada dokumentasi pengaduan dan tindak lanjut yang telah dilakukan. 
   :::tip Kelengkapan Bukti
   1. Terdapat dokumen bukti pengaduan dan tindak lanjut yang telah dilakukan 
   2. Melakukan wawancara kepada petugas/manajemen klinik tentang proses tindak lanjut pengaduan    
   3. 📥 **Unduh Template:** [Form Catatan Pengaduan & Tindak Lanjut (Word)](/templates/sk-hak-kewajiban.doc)
   :::"""
        )
    ],
    "pkp/2.md": [
        # EP 1
        (
            """1. Ada bukti pelaksanaan persetujuan tindakan kedokteran dan terdokumentasi di rekam medik pasien.  
   :::tip Kelengkapan Bukti
   1. Terdapat \tSPO \tpersetujuan tindakan kedokteran 
   2. Terdapat dokumen bukti persetujuan tindakan kedokteran dan terdokumentasi di rekam medik pasien. 
   3. 📥 **Unduh Template:** [Formulir Persetujuan Tindakan Kedokteran / Informed Consent (Word)](/templates/informed-consent.doc)
   :::""",
            """1. Ada bukti pelaksanaan persetujuan tindakan kedokteran dan terdokumentasi di rekam medik pasien.  
   :::tip Kelengkapan Bukti
   1. Terdapat SPO persetujuan tindakan kedokteran 
   2. Terdapat dokumen bukti persetujuan tindakan kedokteran dan terdokumentasi di rekam medik pasien. 
   3. 📥 **Unduh Template:** [Formulir Persetujuan Tindakan Kedokteran / Informed Consent (Word)](/templates/informed-consent.doc)
   :::"""
        ),
        # EP 2
        (
            """2. Pasien atau keluarga mengetahui rencana asuhan, diagnostik dan kemungkinan hasil asuhan yang diberikan. 
   :::tip Kelengkapan Bukti
   1. Terdapat dokumen bukti pasien atau keluarga mengetahui rencana asuhan, diagnostik dan kemungkinan hasil asuhan yang diberikan. 
   2. Melaksanakan wawancara kepada pasien atau keluarga apakah sudah mengetahui rencana asuhan, diagnostik dan kemungkinan hasil asuhan yang diberikan. 
   :::""",
            """2. Pasien atau keluarga mengetahui rencana asuhan, diagnostik dan kemungkinan hasil asuhan yang diberikan. 
   :::tip Kelengkapan Bukti
   1. Terdapat dokumen bukti pasien atau keluarga mengetahui rencana asuhan, diagnostik dan kemungkinan hasil asuhan yang diberikan. 
   2. Melaksanakan wawancara kepada pasien atau keluarga apakah sudah mengetahui rencana asuhan, diagnostik dan kemungkinan hasil asuhan yang diberikan. 
   3. 📥 **Unduh Template:** [Formulir Persetujuan Tindakan Kedokteran / Informed Consent (Word)](/templates/informed-consent.doc)
   :::"""
        )
    ],
    "pkp/3.md": [
        # EP 2
        (
            """2. Ada bukti pelaksanaan pendaftaran sesuai regulasi yang ditetapkan. 
   :::tip Kelengkapan Bukti
   1. Melakukan observasi terhadap pelaksanaan pendaftaran 
   2. Melakukan wawancara dengan petugas dan pasien terkait pelaksanaan pendaftaran 
   :::""",
            """2. Ada bukti pelaksanaan pendaftaran sesuai regulasi yang ditetapkan. 
   :::tip Kelengkapan Bukti
   1. Melakukan observasi terhadap pelaksanaan pendaftaran 
   2. Melakukan wawancara dengan petugas dan pasien terkait pelaksanaan pendaftaran 
   3. 📥 **Unduh Template:** [SPO Pendaftaran Pasien (Word)](/templates/spo-pendaftaran.doc)
   :::"""
        ),
        # EP 4
        (
            """4. Ada bukti pelaksanaan skrining sesuai regulasi yang ditetapkan. 
   :::tip Kelengkapan Bukti
   1. Terdapat \tdokumen \tbukti pelaksanaan skrining 
   2. Melaksanakan observasi dan wawancara petugas dan pasien terkait pelaksanaan skrining 
   :::""",
            """4. Ada bukti pelaksanaan skrining sesuai regulasi yang ditetapkan. 
   :::tip Kelengkapan Bukti
   1. Terdapat dokumen bukti pelaksanaan skrining 
   2. Melaksanakan observasi dan wawancara petugas dan pasien terkait pelaksanaan skrining 
   3. 📥 **Unduh Template:** [SPO Skrining Pasien (Word)](/templates/spo-skrining.doc)
   :::"""
        )
    ],
    "pkp/4.md": [
        # EP 1
        (
            """1. Ada bukti dilakukan kajian pasien oleh PPA dalam penetapan diagnosis yang dituangkan ke dalam rekam medis.  
   :::tip Kelengkapan Bukti
   1. Terdapat bukti dokumen pengkajian pasien oleh PPA dalam penetapan diagnosis yang dituangkan ke dalam rekam medis 
   2. Melaksanakan observasi pengkajian pasien oleh PPA  
   :::""",
            """1. Ada bukti dilakukan kajian pasien oleh PPA dalam penetapan diagnosis yang dituangkan ke dalam rekam medis.  
   :::tip Kelengkapan Bukti
   1. Terdapat bukti dokumen pengkajian pasien oleh PPA dalam penetapan diagnosis yang dituangkan ke dalam rekam medis 
   2. Melaksanakan observasi pengkajian pasien oleh PPA  
   3. 📥 **Unduh Template:** [Formulir Catatan Perkembangan Pasien Terintegrasi / CPPT (Word)](/templates/form-cppt.doc)
   :::"""
        ),
        # EP 2
        (
            """2. Kajian awal sekurang kurangnya memuat data angka `1.` sampai angka `5.`  
   :::tip Kelengkapan Bukti
   Terdapat bukti pengkajian awal sekurang kurangnya memuat data: 
   1. Status fisik 
   2. Psikososial-spiritual 
   3. Riwayat kesehatan pasien 
   4. Riwayat penggunaan obat 
   5. Screening gizi pasien 
   
   Pengkajian awal dilakukan 1x24 jam 
   :::""",
            """2. Kajian awal sekurang kurangnya memuat data angka `1.` sampai angka `5.`  
   :::tip Kelengkapan Bukti
   1. Terdapat bukti pengkajian awal sekurang-kurangnya memuat data: Status fisik, Psikososial-spiritual, Riwayat kesehatan, Riwayat penggunaan obat, dan Skrining gizi (dalam 1x24 jam).
   2. 📥 **Unduh Template:** [Form Kajian Awal Pasien Terintegrasi (Word)](/templates/form-cppt.doc)
   :::"""
        )
    ],
    "pkp/5.md": [
        # EP 2
        (
            """2. Ada bukti pelaksanaan asuhan dan terdokumentasi di rekam medik pasien. 
   :::tip Kelengkapan Bukti
   Terdapat dokumen bukti pelaksanaan asuhan dan terdokumentasi di rekam medis pasien. 
   :::""",
            """2. Ada bukti pelaksanaan asuhan dan terdokumentasi di rekam medik pasien. 
   :::tip Kelengkapan Bukti
   1. Terdapat dokumen bukti pelaksanaan asuhan dan terdokumentasi di rekam medis pasien. 
   2. 📥 **Unduh Template:** [Formulir Catatan Perkembangan Pasien Terintegrasi (CPPT) & Rencana Asuhan (Word)](/templates/form-cppt.doc)
   :::"""
        ),
        # EP 3
        (
            """3. Ada bukti rencana asuhan dievaluasi secara berkala oleh pemberi asuhan. 
   :::tip Kelengkapan Bukti
   1. Terdapat dokumen bukti rencana asuhan dievaluasi secara berkala oleh pemberi asuhan.   
   2. Melaksanakan \twawancara dengan petugas terkait evaluasi rencana asuhan secara berkala 
   :::""",
            """3. Ada bukti rencana asuhan dievaluasi secara berkala oleh pemberi asuhan. 
   :::tip Kelengkapan Bukti
   1. Terdapat dokumen bukti rencana asuhan dievaluasi secara berkala oleh pemberi asuhan.   
   2. Melaksanakan wawancara dengan petugas terkait evaluasi rencana asuhan secara berkala 
   3. 📥 **Unduh Template:** [Formulir Catatan Perkembangan Pasien Terintegrasi (CPPT) & Rencana Asuhan (Word)](/templates/form-cppt.doc)
   :::"""
        )
    ],
    "pkp/6.md": [
        # EP 2
        (
            """2. Ada bukti pelaksanaan dan laporan pelaksanaan program promotif dan preventif. 
   :::tip Kelengkapan Bukti
   1. Terdapat bukti pencatatan dan pelaporan pelaksanaan program promotif dan preventif  
   2. Terdapat bukti pencatatan dan pelaporan pelaksanaan Program \tNasional \t(Pelaporan \tTB-SITB/Stunting dan wasting/HIV-SIHA/Kesehatan Ibu Anak dll), disesuaikan dengan jenis pelayanan di klinik 
   :::""",
            """2. Ada bukti pelaksanaan dan laporan pelaksanaan program promotif dan preventif. 
   :::tip Kelengkapan Bukti
   1. Terdapat bukti pencatatan dan pelaporan pelaksanaan program promotif dan preventif  
   2. Terdapat bukti pencatatan dan pelaporan pelaksanaan Program Nasional (Pelaporan TB-SITB/Stunting/HIV-SIHA/KIA dll)
   3. 📥 **Unduh Template:** [Form Laporan Bulanan Program Nasional & Edukasi (Word)](/templates/program-promotif-preventif.doc)
   :::"""
        )
    ],
    "pkp/7.md": [
        # EP 1
        (
            """1. Ada penetapan pelayanan pasien risiko tinggi pada klinik. 
   :::tip Kelengkapan Bukti
   1. Terdapat penetapan pelayanan pasien risiko tinggi di klinik. 
   2. Terdapat penetapan pelayanan risiko tinggi di klinik
   :::""",
            """1. Ada penetapan pelayanan pasien risiko tinggi pada klinik. 
   :::tip Kelengkapan Bukti
   1. Terdapat penetapan pelayanan pasien risiko tinggi di klinik. 
   2. Terdapat penetapan pelayanan risiko tinggi di klinik
   3. 📥 **Unduh Template:** [SK & SPO Pelayanan Pasien Risiko Tinggi (Word)](/templates/spo-pelayanan-risiko-tinggi.doc)
   :::"""
        )
    ],
    "pkp/8.md": [
        # EP 2
        (
            """2. Pelayanan anestesi dan bedah dilakukan oleh tenaga medis yang kompeten sesuai dengan ketentuan peraturan perundang-undangan.  
   :::tip Kelengkapan Bukti
   1. Terdapat dokumen bukti bahwa pelayanan anestesi dan bedah dilakukan oleh tenaga medis yang kompeten sesuai dengan peraturan perundangan yang berlaku.  
   2. Melaksanakan wawancara dengan manajemen klinik, petugas anestesi dan bedah tentang kompetensi petugas anestesi dan bedah 
   :::""",
            """2. Pelayanan anestesi dan bedah dilakukan oleh tenaga medis yang kompeten sesuai dengan ketentuan peraturan perundang-undangan.  
   :::tip Kelengkapan Bukti
   1. Terdapat dokumen bukti bahwa pelayanan anestesi dan bedah dilakukan oleh tenaga medis yang kompeten sesuai dengan peraturan perundangan yang berlaku.  
   2. Melaksanakan wawancara dengan manajemen klinik, petugas anestesi dan bedah tentang kompetensi petugas anestesi dan bedah 
   3. 📥 **Unduh Template:** [Checklist Kualifikasi Kompetensi Tenaga Anestesi & Bedah (Word)](/templates/spo-anestesi-bedah-minor.doc)
   :::"""
        ),
        # EP 3
        (
            """3. Jenis, dosis dan teknik anestesi dan pemantauan status fisiologi pasien selama pemberian anestesi oleh petugas dicatat dalam rekam medis pasien.  
   :::tip Kelengkapan Bukti
   Terdapat dokumen bukti bahwa Jenis, dosis dan teknik anestesi dan pemantauan status fisiologi pasien selama pemberian anestesi oleh petugas dicatat dalam rekam medis pasien.
   :::""",
            """3. Jenis, dosis dan teknik anestesi dan pemantauan status fisiologi pasien selama pemberian anestesi oleh petugas dicatat dalam rekam medis pasien.  
   :::tip Kelengkapan Bukti
   1. Terdapat dokumen bukti bahwa Jenis, dosis dan teknik anestesi dan pemantauan status fisiologi pasien selama pemberian anestesi oleh petugas dicatat dalam rekam medis pasien.
   2. 📥 **Unduh Template:** [Form Pemantauan Fisiologis Intra & Pasca Anestesi (Word)](/templates/spo-anestesi-bedah-minor.doc)
   :::"""
        ),
        # EP 4
        (
            """4. Ada bukti pelaksanaan kajian pra bedah.  
   :::tip Kelengkapan Bukti
   Terdapat dokumen bukti pelaksanaan kajian pra bedah 
   :::""",
            """4. Ada bukti pelaksanaan kajian pra bedah.  
   :::tip Kelengkapan Bukti
   1. Terdapat dokumen bukti pelaksanaan kajian pra bedah 
   2. 📥 **Unduh Template:** [Form Kajian Pra-Bedah Terintegrasi (Word)](/templates/spo-anestesi-bedah-minor.doc)
   :::"""
        ),
        # EP 5
        (
            """5. Ada bukti pelaksanaan kajian pra anestesi. 
   :::tip Kelengkapan Bukti
   Terdapat dokumen bukti pelaksanaan kajian pra anestesi 
   :::""",
            """5. Ada bukti pelaksanaan kajian pra anestesi. 
   :::tip Kelengkapan Bukti
   1. Terdapat dokumen bukti pelaksanaan kajian pra anestesi 
   2. 📥 **Unduh Template:** [Form Kajian Pra-Anestesi Terintegrasi (Word)](/templates/spo-anestesi-bedah-minor.doc)
   :::"""
        ),
        # EP 6
        (
            """6. Ada bukti pemantauan dan evaluasi paska anestesi dan bedah. 
   :::tip Kelengkapan Bukti
   1. Terdapat dokumen bukti pemantauan dan evaluasi selama tindakan pembedahan. 
   2. Terdapat dokumen bukti pemantauan dan evaluasi paska anestesi dan bedah. 
   :::""",
            """6. Ada bukti pemantauan dan evaluasi paska anestesi dan bedah. 
   :::tip Kelengkapan Bukti
   1. Terdapat dokumen bukti pemantauan dan evaluasi selama tindakan pembedahan. 
   2. Terdapat dokumen bukti pemantauan dan evaluasi paska anestesi dan bedah. 
   3. 📥 **Unduh Template:** [Form Pemantauan Status Fisiologis Pasca Bedah & Anestesi (Word)](/templates/spo-anestesi-bedah-minor.doc)
   :::"""
        )
    ],
    "pkp/9.md": [
        # EP 1
        (
            """1. Asuhan gizi dilakukan oleh petugas yang berkompeten sesuai dengan ketentuan peraturan perundang-undangan. 
   :::tip Kelengkapan Bukti
   Terdapat dokumen penetapan petugas  yang berkompeten sesuai dengan aturan perundangan. 
   :::""",
            """1. Asuhan gizi dilakukan oleh petugas yang berkompeten sesuai dengan ketentuan peraturan perundang-undangan. 
   :::tip Kelengkapan Bukti
   1. Terdapat dokumen penetapan petugas yang berkompeten sesuai dengan aturan perundangan (Ahli Gizi/Nutrisionis ber-STR).
   2. 📥 **Unduh Template:** [Checklist Kualifikasi Kompetensi Staf Asuhan Gizi (Word)](/templates/asuhan-edukasi-gizi.doc)
   :::"""
        ),
        # EP 3
        (
            """3. Distribusi dan pemberian makanan dilakukan sesuai jadwal dan pemesanan dan di dokumentasikan.  
   :::tip Kelengkapan Bukti
   1. Terdapat dokumen bukti bahwa distribusi dan pemberian makanan dilakukan sesuai jadwal dan pemesanan. 
   2. Melaksanakan wawancara dengan petugas terkait distribusi dan pemberian makanan yang dilakukan sesuai jadwal dan pemesanan 
   :::""",
            """3. Distribusi dan pemberian makanan dilakukan sesuai jadwal and pemesanan dan di dokumentasikan.  
   :::tip Kelengkapan Bukti
   1. Terdapat dokumen bukti bahwa distribusi dan pemberian makanan dilakukan sesuai jadwal dan pemesanan. 
   2. Melaksanakan wawancara dengan petugas terkait distribusi dan pemberian makanan yang dilakukan sesuai jadwal dan pemesanan 
   3. 📥 **Unduh Template:** [Form Pemesanan & Lembar Kendali Distribusi Makanan Pasien (Word)](/templates/asuhan-edukasi-gizi.doc)
   :::"""
        ),
        # EP 4
        (
            """4. Pasien dan/atau keluarga diberi edukasi tentang pembatasan diet pasien dan keamanan atau kebersihan makanan.  
   :::tip Kelengkapan Bukti
   1. Terdapat dokumen bukti bahwa Pasien dan/atau keluarga diberi edukasi tentang pembatasan diet pasien dan keamanan atau kebersihan makanan.  
   2. Melaksanakan wawancara dengan pasien dan petugas terkait edukasi tentang pembatasan diet pasien dan keamanan atau kebersihan makanan. 
   :::""",
            """4. Pasien dan/atau keluarga diberi edukasi tentang pembatasan diet pasien dan keamanan atau kebersihan makanan.  
   :::tip Kelengkapan Bukti
   1. Terdapat dokumen bukti bahwa Pasien dan/atau keluarga diberi edukasi tentang pembatasan diet pasien dan keamanan atau kebersihan makanan.  
   2. Melaksanakan wawancara dengan pasien dan petugas terkait edukasi tentang pembatasan diet pasien dan keamanan atau kebersihan makanan. 
   3. 📥 **Unduh Template:** [Form Catatan Edukasi & Konseling Diet Pasien (Word)](/templates/asuhan-edukasi-gizi.doc)
   :::"""
        )
    ],
    "pkp/10.md": [
        # EP 1
        (
            """1. Dokter melaksanakan pemulangan dan menyusun rencana tindak lanjut sesuai dengan rencana yang disusun dan kriteria pemulangan. 
   :::tip Kelengkapan Bukti
   Terdapat dokumen bukti bahwa Dokter melaksanakan pemulangan dan menyusun rencana tindak lanjut sesuai dengan rencana yang disusun dan kriteria pemulangan. 
   :::""",
            """1. Dokter melaksanakan pemulangan dan menyusun rencana tindak lanjut sesuai dengan rencana yang disusun dan kriteria pemulangan. 
   :::tip Kelengkapan Bukti
   1. Terdapat dokumen bukti bahwa Dokter melaksanakan pemulangan dan menyusun rencana tindak lanjut sesuai dengan rencana yang disusun dan kriteria pemulangan. 
   2. 📥 **Unduh Template:** [SPO Pemulangan Pasien & Kriteria Pulang Rawat Inap (Word)](/templates/resume-medis-kriteria-pulang.doc)
   :::"""
        ),
        # EP 3
        (
            """3. Ada bukti pemberian informasi kepada pasien saat pulang. 
   :::tip Kelengkapan Bukti
   1. Terdapat dokumen bukti pemberian informasi kepada pasien saat pulang. 
   2. Melaksanakan wawancara kepada pasien dan/atau petugas terkait pemberian informasi kepada pasien saat pulang. 
   :::""",
            """3. Ada bukti pemberian informasi kepada pasien saat pulang. 
   :::tip Kelengkapan Bukti
   1. Terdapat dokumen bukti pemberian informasi kepada pasien saat pulang (Edukasi kontrol/obat). 
   2. Melaksanakan wawancara kepada pasien dan/atau petugas terkait pemberian informasi kepada pasien saat pulang. 
   3. 📥 **Unduh Template:** [Form Lembar Discharge Planning & Edukasi Pasien Pulang (Word)](/templates/resume-medis-kriteria-pulang.doc)
   :::"""
        )
    ],
    "pkp/11.md": [
        # EP 2
        (
            """2. Klinik yang merujuk pasien memastikan bahwa fasyankes yang dituju dapat memenuhi kebutuhan pasien. 
   :::tip Kelengkapan Bukti
   1. Terdapat dokumen bukti bahwa  Klinik memastikan fasyankes yang dituju dapat memenuhi kebutuhan pasien yang dirujuk. 
   2. Malaksanakan \twawancara dengan petugas terkait tatacara merujuk pasien ke fasyankes lain.    
   :::""",
            """2. Klinik yang merujuk pasien memastikan bahwa fasyankes yang dituju dapat memenuhi kebutuhan pasien. 
   :::tip Kelengkapan Bukti
   1. Terdapat dokumen bukti bahwa  Klinik memastikan fasyankes yang dituju dapat memenuhi kebutuhan pasien yang dirujuk. 
   2. Melaksanakan wawancara dengan petugas terkait tatacara merujuk pasien ke fasyankes lain.    
   3. 📥 **Unduh Template:** [SPO Rujukan Pasien, Surat Rujukan & MoU Ambulans (Word)](/templates/surat-rujukan-mou-ambulans.doc)
   :::"""
        ),
        # EP 3
        (
            """3. Pasien/keluarga memperoleh informasi rujukan dan memberi persetujuan untuk dilakukan rujukan berdasarkan kebutuhan pasien. 
   :::tip Kelengkapan Bukti
   1. Terdapat dokumen bukti pemberian informasi pada pasien dan keluarga yang akan dirujuk  
   2. Terdapat dokumen bukti persetujuan pasien/keluarga saat dilakukan rujukan  
   3. Melaksanakan wawancara dengan pasien dan/atau petugas terkait pemberian informasi sebelum dilakukan rujukan 
   :::""",
            """3. Pasien/keluarga memperoleh informasi rujukan dan memberi persetujuan untuk dilakukan rujukan berdasarkan kebutuhan pasien. 
   :::tip Kelengkapan Bukti
   1. Terdapat dokumen bukti pemberian informasi pada pasien dan keluarga yang akan dirujuk  
   2. Terdapat dokumen bukti persetujuan pasien/keluarga saat dilakukan rujukan  
   3. Melaksanakan wawancara dengan pasien dan/atau petugas terkait pemberian informasi sebelum dilakukan rujukan 
   4. 📥 **Unduh Template:** [Form Lembar Informasi & Persetujuan Rujukan (Word)](/templates/surat-rujukan-mou-ambulans.doc)
   :::"""
        ),
        # EP 4
        (
            """4. Ada sarana transportasi rujukan yang memenuhi syarat (khusus klinik yang menyelenggarakan pelayanan rawat inap). 
   :::tip Kelengkapan Bukti
   1. Melaksanakan observasi terkait sarana transportasi yang digunakan untuk merujuk pasien yang memenuhi syarat (khusus klinik yang menyelenggarakan pelayanan rawat inap). 
   2. Melaksanakan wawancara dengan petugas terkait sarana transportasi rujukan yang memenuhi syarat (khusus klinik yang menyelenggarakan pelayanan rawat inap). 
   :::""",
            """4. Ada sarana transportasi rujukan yang memenuhi syarat (khusus klinik yang menyelenggarakan pelayanan rawat inap). 
   :::tip Kelengkapan Bukti
   1. Melaksanakan observasi terkait sarana transportasi yang digunakan untuk merujuk pasien yang memenuhi syarat (khusus klinik yang menyelenggarakan pelayanan rawat inap). 
   2. Melaksanakan wawancara dengan petugas terkait sarana transportasi rujukan yang memenuhi syarat (khusus klinik yang menyelenggarakan pelayanan rawat inap). 
   3. 📥 **Unduh Template:** [MoU Penyediaan Mobil Ambulans Transportasi Rujukan 24 Jam (Word)](/templates/surat-rujukan-mou-ambulans.doc)
   :::"""
        ),
        # EP 5
        (
            """5. Ada daftar jejaring rujukan klinik. 
   :::tip Kelengkapan Bukti
    Terdapat dokumen daftar jejaring rujukan klinik.
   :::""",
            """5. Ada daftar jejaring rujukan klinik. 
   :::tip Kelengkapan Bukti
   1. Terdapat dokumen daftar jejaring rujukan klinik.
   2. 📥 **Unduh Template:** [Daftar Jejaring Rujukan Klinik (Word)](/templates/surat-rujukan-mou-ambulans.doc)
   :::"""
        )
    ],
    "pkp/12.md": [
        # EP 1
        (
            """1. Ada bukti penyelenggaraan rekam medis. 
   :::tip Kelengkapan Bukti
   Terdapat \tdokumen \tbukti penyelenggaraan rekam medis sesuai ketentuan yang berlaku 
   :::""",
            """1. Ada bukti penyelenggaraan rekam medis. 
   :::tip Kelengkapan Bukti
   1. Terdapat dokumen bukti penyelenggaraan rekam medis sesuai ketentuan yang berlaku 
   2. 📥 **Unduh Template:** [SPO Pengelolaan, Kerahasiaan, & Retensi Rekam Medis (Word)](/templates/spo-pengelolaan-rekam-medis.doc)
   :::"""
        ),
        # EP 2
        (
            """2. Ada bukti rekam medis diisi secara lengkap oleh Profesional Pemberi Asuhan (PPA). 
   :::tip Kelengkapan Bukti
   Terdapat dokumen bukti rekam medis diisi secara lengkap oleh Profesional Pemberi Asuhan (PPA).
   :::""",
            """2. Ada bukti rekam medis diisi secara lengkap oleh Profesional Pemberi Asuhan (PPA). 
   :::tip Kelengkapan Bukti
   1. Terdapat dokumen bukti rekam medis diisi secara lengkap oleh Profesional Pemberi Asuhan (PPA).
   2. 📥 **Unduh Template:** [SPO Tata Cara Pengisian Rekam Medis (SOAP) & Pembetulan Salah Tulis (Word)](/templates/spo-pengelolaan-rekam-medis.doc)
   :::"""
        ),
        # EP 4
        (
            """4. Ada bukti klinik menjaga kerahasiaan rekam medis pasien. 
   :::tip Kelengkapan Bukti
   1. Terdapat dokumen bukti klinik menjaga kerahasiaan rekam medis pasien. 
   2. Melaksanakan observasi dan wawancara terkait cara klinik menjaga kerahasiaan rekam medis pasien. 
   :::""",
            """4. Ada bukti klinik menjaga kerahasiaan rekam medis pasien. 
   :::tip Kelengkapan Bukti
   1. Terdapat dokumen bukti klinik menjaga kerahasiaan rekam medis pasien. 
   2. Melaksanakan observasi dan wawancara terkait cara klinik menjaga kerahasiaan rekam medis pasien. 
   3. 📥 **Unduh Template:** [Form Persetujuan Pelepasan Informasi Medis Pasien (Word)](/templates/spo-pengelolaan-rekam-medis.doc)
   :::"""
        )
    ],
    "pkp/13.md": [
        # EP 1
        (
            """1. Ada penetapan jenis-jenis pelayanan laboratorium yang disediakan. 
   :::tip Kelengkapan Bukti
   Terdapat SK penetapan jenis-jenis pelayanan laboratorium yang disediakan. 
   :::""",
            """1. Ada penetapan jenis-jenis pelayanan laboratorium yang disediakan. 
   :::tip Kelengkapan Bukti
   1. Terdapat SK penetapan jenis-jenis pelayanan laboratorium yang disediakan. 
   2. 📥 **Unduh Template:** [SK Jenis Layanan Laboratorium (Word)](/templates/spo-pelayanan-laboratorium.doc)
   :::"""
        ),
        # EP 2
        (
            """2. Terdapat Penanggung Jawab Laboratorium sesuai perundang-undangan yang berlaku. 
   :::tip Kelengkapan Bukti
   Terdapat dokumen SK Penanggung Jawab Laboratorium \tsesuai \tperundang-undangan yang berlaku. 
   :::""",
            """2. Terdapat Penanggung Jawab Laboratorium sesuai perundang-undangan yang berlaku. 
   :::tip Kelengkapan Bukti
   1. Terdapat dokumen SK Penanggung Jawab Laboratorium sesuai perundang-undangan yang berlaku. 
   2. 📥 **Unduh Template:** [SK Penanggung Jawab Laboratorium Klinik (Word)](/templates/spo-pelayanan-laboratorium.doc)
   :::"""
        ),
        # EP 3
        (
            """3. Klinik menetapkan rentang nilai normal untuk setiap jenis pemeriksaan yang disediakan. 
   :::tip Kelengkapan Bukti
   Terdapat penetapan rentang nilai normal untuk setiap jenis pemeriksaan yang disediakan. 
   :::""",
            """3. Klinik menetapkan rentang nilai normal untuk setiap jenis pemeriksaan yang disediakan. 
   :::tip Kelengkapan Bukti
   1. Terdapat penetapan rentang nilai normal untuk setiap jenis pemeriksaan yang disediakan. 
   2. 📥 **Unduh Template:** [SK Penetapan Rentang Nilai Normal Pemeriksaan Laboratorium (Word)](/templates/spo-pelayanan-laboratorium.doc)
   :::"""
        ),
        # EP 4
        (
            """4. Ada bukti reagensia esensial dan bahan lain tersedia sesuai dengan jenis pelayanan yang ditetapkan, pelabelan dan penyimpanannya. 
   :::tip Kelengkapan Bukti
   Tersedia reagensia esensial dan bahan lain sesuai dengan jenis pelayanan yang ditetapkan, pelabelan dan penyimpanannya 
   :::""",
            """4. Ada bukti reagensia esensial dan bahan lain tersedia sesuai dengan jenis pelayanan yang ditetapkan, pelabelan dan penyimpanannya. 
   :::tip Kelengkapan Bukti
   1. Tersedia reagensia esensial dan bahan lain sesuai dengan jenis pelayanan yang ditetapkan, pelabelan dan penyimpanannya.
   2. 📥 **Unduh Template:** [SPO Pelabelan & Penyimpanan Reagensia Esensial Laboratorium (Word)](/templates/spo-pelayanan-laboratorium.doc)
   :::"""
        ),
        # EP 6
        (
            """6. Ada prosedur rujukan spesimen dan/ atau pengguna layanan, jika pemeriksaan laboratorium tidak dapat dilakukan oleh klinik. 
   :::tip Kelengkapan Bukti
   Terdapat SPO rujukan spesimen dan/ atau pengguna layanan, jika pemeriksaan laboratorium tidak dapat dilakukan oleh klinik. 
   :::""",
            """6. Ada prosedur rujukan spesimen dan/ atau pengguna layanan, jika pemeriksaan laboratorium tidak dapat dilakukan oleh klinik. 
   :::tip Kelengkapan Bukti
   1. Terdapat SPO rujukan spesimen dan/ atau pengguna layanan, jika pemeriksaan laboratorium tidak dapat dilakukan oleh klinik. 
   2. 📥 **Unduh Template:** [SPO Rujukan Pemeriksaan Spesimen Laboratorium (Word)](/templates/spo-pelayanan-laboratorium.doc)
   :::"""
        ),
        # EP 7
        (
            """7. Ada bukti pelaksanaan Pemantapan Mutu Internal (PMI) dan Pemantapan Mutu Eksternal  (PME) secara berkala. 
   :::tip Kelengkapan Bukti
   1. Terdapat dokumen bukti pelaksanaan Pemantapan Mutu Internal (PMI) dan Pemantapan Mutu Eksternal (PME) secara berkala 
   2. Melaksanakan wawancara dengan petugas tentang pelaksanaan Pemantapan Mutu Internal (PMI) dan Pemantapan Mutu Eksternal (PME) secara berkala di klinik 
   :::""",
            """7. Ada bukti pelaksanaan Pemantapan Mutu Internal (PMI) dan Pemantapan Mutu Eksternal  (PME) secara berkala. 
   :::tip Kelengkapan Bukti
   1. Terdapat dokumen bukti pelaksanaan Pemantapan Mutu Internal (PMI) dan Pemantapan Mutu Eksternal (PME) secara berkala 
   2. Melaksanakan wawancara dengan petugas tentang pelaksanaan Pemantapan Mutu Internal (PMI) dan Pemantapan Mutu Eksternal (PME) secara berkala di klinik 
   3. 📥 **Unduh Template:** [Form Kendali Pemantauan Mutu Internal & Eksternal Lab (Word)](/templates/spo-pelayanan-laboratorium.doc)
   :::"""
        )
    ],
    "pkp/14.md": [
        # EP 2
        (
            """2. Ada bukti pelayanan radiologi sesuai dengan prosedur yang ada termasuk kepatuhan terhadap manajemen keamanan radiasi. 
   :::tip Kelengkapan Bukti
   1. Terdapat dokumen bukti pelayanan radiologi sesuai dengan prosedur yang ada termasuk kepatuhan terhadap manajemen keamanan radiasi. 
   2. Melaksanakan wawancara dengan petugas tentang pelaksanaan pelayanan radiologi yang sesuai dengan prosedur yang ada termasuk kepatuhan terhadap manajemen keamanan radiasi. 
   :::""",
            """2. Ada bukti pelayanan radiologi sesuai dengan prosedur yang ada termasuk kepatuhan terhadap manajemen keamanan radiasi. 
   :::tip Kelengkapan Bukti
   1. Terdapat dokumen bukti pelayanan radiologi sesuai dengan prosedur yang ada termasuk kepatuhan terhadap manajemen keamanan radiasi. 
   2. Melaksanakan wawancara dengan petugas tentang pelaksanaan pelayanan radiologi yang sesuai dengan prosedur yang ada termasuk kepatuhan terhadap manajemen keamanan radiasi. 
   3. 📥 **Unduh Template:** [SPO Pelayanan Radiologi & Proteksi Keamanan Radiasi (Word)](/templates/spo-pelayanan-radiologi.doc)
   :::"""
        )
    ],
    "pkp/15.md": [
        # EP 2
        (
            """2. Tersedia daftar formularium obat klinik. 
   :::tip Kelengkapan Bukti
   Terdapat daftar formularium obat  
   :::""",
            """2. Tersedia daftar formularium obat klinik. 
   :::tip Kelengkapan Bukti
   1. Terdapat daftar formularium obat  
   2. 📥 **Unduh Template:** [Formulir Obat Klinik / Daftar Obat Esensial (Word)](/templates/pelayanan-kefarmasian-lengkap.doc)
   :::"""
        ),
        # EP 3
        (
            """3. Ada kebijakan dan atau prosedur pengadaan obat sesuai dengan regulasi. 
   :::tip Kelengkapan Bukti
   Terdapat prosedur pengadaan obat sesuai dengan regulasi 
   :::""",
            """3. Ada kebijakan dan atau prosedur pengadaan obat sesuai dengan regulasi. 
   :::tip Kelengkapan Bukti
   1. Terdapat prosedur pengadaan obat sesuai dengan regulasi 
   2. 📥 **Unduh Template:** [SPO Pengadaan Obat Lewat Jalur Resmi (Word)](/templates/pelayanan-kefarmasian-lengkap.doc)
   :::"""
        ),
        # EP 5
        (
            """5. Tersedia bukti pemberian informasi obat dan konseling oleh Apoteker. 
   :::tip Kelengkapan Bukti
   1. Terdapat dokumen bukti pemberian informasi obat dan konseling oleh Apoteker
   2. Melaksanakan observasi dan wawancara pelaksanaan pemberian informasi obat dan konseling oleh Apoteker 
   :::""",
            """5. Tersedia bukti pemberian informasi obat dan konseling oleh Apoteker. 
   :::tip Kelengkapan Bukti
   1. Terdapat dokumen bukti pemberian informasi obat dan konseling oleh Apoteker
   2. Melaksanakan observasi dan wawancara pelaksanaan pemberian informasi obat dan konseling oleh Apoteker 
   3. 📥 **Unduh Template:** [Form Lembar Konseling & Pelayanan Informasi Obat / PIO (Word)](/templates/pelayanan-kefarmasian-lengkap.doc)
   :::"""
        ),
        # EP 6
        (
            """6. Tersedia bukti rekonsiliasi obat pada pelayanan rawat inap sesuai dengan ketentuan peraturan perundang-undangan. 
   :::tip Kelengkapan Bukti
   1. Terdapat dokumen bukti rekonsiliasi obat pada pelayanan rawat inap sesuai dengan peraturan perundang-undangan 
   2. Melaksanakan \tobservasi \tdan wawancara \tpetugas \tterhadap pelaksanaan rekonsiliasi obat pada pelayanan rawat inap  
   :::""",
            """6. Tersedia bukti rekonsiliasi obat pada pelayanan rawat inap sesuai dengan ketentuan peraturan perundang-undangan. 
   :::tip Kelengkapan Bukti
   1. Terdapat dokumen bukti rekonsiliasi obat pada pelayanan rawat inap sesuai dengan peraturan perundang-undangan 
   2. Melaksanakan observasi dan wawancara petugas terhadap pelaksanaan rekonsiliasi obat pada pelayanan rawat inap  
   3. 📥 **Unduh Template:** [Form Lembar Rekonsiliasi Obat Rawat Inap (Word)](/templates/pelayanan-kefarmasian-lengkap.doc)
   :::"""
        ),
        # EP 7
        (
            """7. Tersedia obat emergensi pada unit-unit dimana diperlukan, dan dapat diakses untuk memenuhi kebutuhan yang bersifat emergensi, dipantau, dan diganti tepat waktu setelah digunakan atau bila kadaluarsa.  
   :::tip Kelengkapan Bukti
   1. Terdapat daftar obat emergensi yang diperbaharui secara berkala 
   2. Terdapat dokumen bukti ketersediaan obat emergensi pada unit-unit dimana diperlukan, dan dapat diakses untuk memenuhi kebutuhan yang bersifat emergensi, dipantau, dan diganti tepat waktu setelah digunakan atau bila kadaluarsa. 
   3. Melaksanakan observasi dan wawancara terhadap ketersediaan obat emergensi pada unit-unit dimana diperlukan 
   :::""",
            """7. Tersedia obat emergensi pada unit-unit dimana diperlukan, dan dapat diakses untuk memenuhi kebutuhan yang bersifat emergensi, dipantau, dan diganti tepat waktu setelah digunakan atau bila kadaluarsa.  
   :::tip Kelengkapan Bukti
   1. Terdapat daftar obat emergensi yang diperbaharui secara berkala 
   2. Terdapat dokumen bukti ketersediaan obat emergensi pada unit-unit dimana diperlukan, dan dapat diakses untuk memenuhi kebutuhan yang bersifat emergensi, dipantau, dan diganti tepat waktu setelah digunakan atau bila kadaluarsa. 
   3. Melaksanakan observasi dan wawancara terhadap ketersediaan obat emergensi pada unit-unit dimana diperlukan 
   4. 📥 **Unduh Template:** [Daftar Obat Emergensi & Lembar Pemantauan Suhu/Kadaluarsa (Word)](/templates/pelayanan-kefarmasian-lengkap.doc)
   :::"""
        ),
        # EP 9
        (
            """9. Tersedia bukti penyimpanan obat termasuk obat *High Alert* yang baik, benar dan aman sesuai regulasi. 
   :::tip Kelengkapan Bukti
   1. Terdapat SPO penyimpanan obat termasuk obat *High Alert* yang baik, benar dan aman sesuai regulasi 
   2. Terdapat \tdokumen \tbukti penyimpanan obat termasuk obat *High Alert* yang baik, benar dan aman sesuai regulasi 
   3. Melaksanakan \tobservasi \tdan wawancara \tpetugas \ttentang penyimpanan obat termasuk obat *High Alert* yang baik, benar dan aman sesuai regulasi 
   :::""",
            """9. Tersedia bukti penyimpanan obat termasuk obat *High Alert* yang baik, benar dan aman sesuai regulasi. 
   :::tip Kelengkapan Bukti
   1. Terdapat SPO penyimpanan obat termasuk obat *High Alert* yang baik, benar dan aman sesuai regulasi 
   2. Terdapat dokumen bukti penyimpanan obat termasuk obat *High Alert* yang baik, benar dan aman sesuai regulasi 
   3. Melaksanakan observasi dan wawancara petugas tentang penyimpanan obat termasuk obat *High Alert* yang baik, benar dan aman sesuai regulasi 
   4. 📥 **Unduh Template:** [SPO Penyimpanan & Pelabelan Stiker Obat High Alert / LASA (Word)](/templates/pelayanan-kefarmasian-lengkap.doc)
   :::"""
        ),
        # EP 10
        (
            """10. Tersedia kebijakan dan atau prosedur penanganan obat kadaluarsa/rusak. 
   :::tip Kelengkapan Bukti
   1. Terdapat SPO penanganan obat kadaluarsa/ rusak 
   2. Terdapat dokumen bukti penanganan obat kadaluarsa/ rusak sesuai prosedur  
   3. Melaksanakan wawancara dengan petugas terkait penanganan obat kadaluarsa/ rusak  
   :::""",
            """10. Tersedia kebijakan dan atau prosedur penanganan obat kadaluarsa/rusak. 
   :::tip Kelengkapan Bukti
   1. Terdapat SPO penanganan obat kadaluarsa/ rusak 
   2. Terdapat dokumen bukti penanganan obat kadaluarsa/ rusak sesuai prosedur  
   3. Melaksanakan wawancara dengan petugas terkait penanganan obat kadaluarsa/ rusak  
   4. 📥 **Unduh Template:** [SPO & Berita Acara Pemusnahan Obat Kadaluarsa / Rusak (Word)](/templates/pelayanan-kefarmasian-lengkap.doc)
   :::"""
        ),
        # EP 11
        (
            """11. Terdapat pencatatan dan pelaporan MESO/Monitoring Efek Samping Obat. 
   :::tip Kelengkapan Bukti
   1. Terdapat dokumen bukti pencatatan dan pelaporan MESO/Monitoring Efek Samping Obat 
   2. Melaksanakan wawancara dengan petugas tentang pencatatan dan pelaporan MESO/Monitoring Efek Samping Obat di klinik 
   :::""",
            """11. Terdapat pencatatan dan pelaporan MESO/Monitoring Efek Samping Obat. 
   :::tip Kelengkapan Bukti
   1. Terdapat dokumen bukti pencatatan dan pelaporan MESO/Monitoring Efek Samping Obat 
   2. Melaksanakan wawancara dengan petugas tentang pencatatan dan pelaporan MESO/Monitoring Efek Samping Obat di klinik 
   3. 📥 **Unduh Template:** [Formulir Pelaporan Efek Samping Obat / MESO / Kartu Kuning (Word)](/templates/pelayanan-kefarmasian-lengkap.doc)
   :::"""
        ),
        # EP 12
        (
            """12. Ada kebijakan dan atau prosedur pemantauan dan pelaporan *medication error*. 
   :::tip Kelengkapan Bukti
   1. Terdapat SPO pemantauan dan pelaporan *medication error* 
   2. Terdapat dokumen bukti pelaksanaan pemantauan dan pelaporan *medication error* 
   3. Melaksanakan wawancara dengan petugas terkait pelaksanaan pemantauan dan pelaporan *medication error* di klinik 
   :::""",
            """12. Ada kebijakan dan atau prosedur pemantauan dan pelaporan *medication error*. 
   :::tip Kelengkapan Bukti
   1. Terdapat SPO pemantauan dan pelaporan *medication error* 
   2. Terdapat dokumen bukti pelaksanaan pemantauan dan pelaporan *medication error* 
   3. Melaksanakan wawancara dengan petugas terkait pelaksanaan pemantauan dan pelaporan *medication error* di klinik 
   4. 📥 **Unduh Template:** [SPO & Laporan Kejadian Nyaris Cedera / Medication Error (Word)](/templates/pelayanan-kefarmasian-lengkap.doc)
   :::"""
        ),
        # EP 13
        (
            """13. Dalam hal klinik tidak memiliki apoteker, sebagai penanggung jawab pelayanan kefarmasian, ada bukti bahwa klinik hanya mengelola obat darurat medis sesuai dengan ketentuan peraturan perundang-undangan. 
   :::tip Kelengkapan Bukti
   1. Terdapat dokumen bukti bahwa klinik hanya mengelola obat darurat medis sesuai \tperaturan \tperundang-undangan 
   2. Melaksanakan observasi dan wawancara tentang pengelolaan obat 
   :::""",
            """13. Dalam hal klinik tidak memiliki apoteker, sebagai penanggung jawab pelayanan kefarmasian, ada bukti bahwa klinik hanya mengelola obat darurat medis sesuai dengan ketentuan peraturan perundang-undangan. 
   :::tip Kelengkapan Bukti
   1. Terdapat dokumen bukti bahwa klinik hanya mengelola obat darurat medis sesuai peraturan perundang-undangan 
   2. Melaksanakan observasi dan wawancara tentang pengelolaan obat 
   3. 📥 **Unduh Template:** [Daftar Obat Darurat Medis bagi Klinik Tanpa Apoteker (Word)](/templates/pelayanan-kefarmasian-lengkap.doc)
   :::"""
        )
    ]
}

# Apply all replacements
modified_count = 0
for relative_path, file_replacements in replacements.items():
    absolute_path = os.path.join(base_dir, relative_path.replace("/", os.sep))
    if not os.path.exists(absolute_path):
        print(f"Warning: File {absolute_path} not found.")
        continue
        
    with open(absolute_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    original_content = content
    for target, replacement in file_replacements:
        # Check if target exists in content
        if target in content:
            content = content.replace(target, replacement)
        else:
            # Let's do a loose check by replacing tabs and double spaces to make it match
            cleaned_target = target.replace("\t", " ").replace(" \n", "\n").replace("\r", "")
            # We can also clean content slightly for loose matching if needed
            print(f"Loose match attempting for a replacement chunk in {relative_path}...")
            # Let's try replacing direct variations
            target_variations = [
                target.replace("\t", " "),
                target.replace("Kelengkapan Bukti", "Kelangkapan Bukti"),
                target.replace("Kelangkapan Bukti", "Kelengkapan Bukti")
            ]
            matched = False
            for var in target_variations:
                if var in content:
                    content = content.replace(var, replacement)
                    matched = True
                    break
            if not matched:
                print(f"ERROR: Target content not found in {relative_path}!")
                print(f"Target: {target[:100]}...")
                
    if content != original_content:
        with open(absolute_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Successfully updated: {relative_path}")
        modified_count += 1
    else:
        print(f"No changes made to: {relative_path} (either already updated or target mismatch)")

print(f"\nCompleted! Modified {modified_count} out of {len(replacements)} files.")
