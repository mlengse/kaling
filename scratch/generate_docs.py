import os

# Create target directory if it doesn't exist
output_dir = r"c:\Users\anjan\dev\kaling\docs\public\templates"
os.makedirs(output_dir, exist_ok=True)

def get_html_doc_wrapper(title, content):
    return f"""<html xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:w="urn:schemas-microsoft-com:office:word" xmlns="http://www.w3.org/TR/REC-html40">
<head>
<meta charset="utf-8">
<title>{title}</title>
<style>
    @page {{
        size: 21cm 29.7cm;
        margin: 2.5cm 2.5cm 2.5cm 2.5cm;
        mso-page-orientation: portrait;
    }}
    body {{
        font-family: 'Arial', sans-serif;
        font-size: 10pt;
        line-height: 1.4;
        color: #000000;
    }}
    .kop-surat {{
        text-align: center;
        border-bottom: 3px double #000000;
        padding-bottom: 8px;
        margin-bottom: 15px;
    }}
    .kop-title {{
        font-size: 13pt;
        font-weight: bold;
        text-transform: uppercase;
        margin: 0;
    }}
    .kop-subtitle {{
        font-size: 9pt;
        margin: 3px 0 0 0;
        font-style: italic;
    }}
    .doc-title {{
        text-align: center;
        font-size: 11pt;
        font-weight: bold;
        text-transform: uppercase;
        margin-bottom: 15px;
        text-decoration: underline;
    }}
    .section-title {{
        font-weight: bold;
        margin-top: 10px;
        margin-bottom: 4px;
        font-size: 10pt;
        text-decoration: underline;
    }}
    table {{
        width: 100%;
        border-collapse: collapse;
        margin-top: 8px;
        margin-bottom: 8px;
    }}
    table, th, td {{
        border: 1px solid #000000;
    }}
    th {{
        background-color: #f2f2f2;
        font-weight: bold;
        text-align: center;
        padding: 5px;
        font-size: 9pt;
    }}
    td {{
        padding: 5px;
        vertical-align: top;
        font-size: 9pt;
    }}
    .text-center {{
        text-align: center;
    }}
    .signature-area {{
        margin-top: 30px;
        width: 100%;
    }}
    .signature-table {{
        border: none !important;
    }}
    .signature-table td {{
        border: none !important;
        width: 50%;
        text-align: center;
    }}
</style>
</head>
<body>
    <div class="kop-surat">
        <p class="kop-title">KLINIK PRATAMA / UTAMA KELUARGA SEHAT</p>
        <p class="kop-subtitle">Jl. Raya Pembangunan No. 123, Jakarta Selatan | Telp: (021) 555-1234 | Email: info@keluargasehat.com</p>
    </div>
    {content}
</body>
</html>"""

# ----------------- ORIGINAL 5 TEMPLATES (PKP 1 - 4) -----------------

# 1. SK Hak dan Kewajiban Pasien
sk_content = """
    <div class="doc-title">KEPUTUSAN KEPALA KLINIK KELUARGA SEHAT<br>NOMOR: 001/SK/DIR/2026</div>
    <div class="text-center" style="font-weight: bold; margin-bottom: 15px;">TENTANG<br>HAK DAN KEWAJIBAN PASIEN DI KLINIK KELUARGA SEHAT</div>
    
    <div class="text-center" style="font-weight: bold;">KEPALA KLINIK KELUARGA SEHAT,</div>
    
    <table style="border:none; margin-top:15px; width:100%;">
        <tr style="border:none;">
            <td style="border:none; width:15%; font-weight:bold;">Menimbang</td>
            <td style="border:none; width:5%; text-align:center;">:</td>
            <td style="border:none; width:80%;">
                a. bahwa untuk menjamin pelayanan kesehatan yang bermutu, profesional, bertanggung jawab, serta mengedepankan keselamatan pasien, perlu ditetapkan pemenuhan Hak dan Kewajiban Pasien di Klinik;<br>
                b. bahwa penetapan Hak dan Kewajiban Pasien merupakan perwujudan dari tata kelola pelayanan yang berfokus pada pasien di Klinik Pratama dan Utama;<br>
                c. bahwa berdasarkan pertimbangan sebagaimana dimaksud dalam huruf a dan b, perlu menetapkan Keputusan Kepala Klinik tentang Hak dan Kewajiban Pasien di Klinik Keluarga Sehat.
            </td>
        </tr>
        <tr style="border:none;">
            <td style="border:none; font-weight:bold; padding-top:10px;">Mengingat</td>
            <td style="border:none; text-align:center; padding-top:10px;">:</td>
            <td style="border:none; padding-top:10px;">
                1. Undang-Undang Republik Indonesia Nomor 17 Tahun 2023 tentang Kesehatan;<br>
                2. Peraturan Menteri Kesehatan Republik Indonesia Nomor 34 Tahun 2022 tentang Akreditasi Pusat Kesehatan Masyarakat, Klinik, Laboratorium Kesehatan, Unit Transfusi Darah, Tempat Praktik Mandiri Dokter, dan Tempat Praktik Mandiri Dokter Gigi;<br>
                3. Peraturan Menteri Kesehatan Republik Indonesia Nomor 14 Tahun 2021 tentang Standar Kegiatan Usaha dan Produk pada Penyelenggaraan Perizinan Berusaha Berbasis Risiko Sektor Kesehatan;<br>
                4. Keputusan Menteri Kesehatan Republik Indonesia Nomor HK.01.07/MENKES/1983/2022 tentang Standar Akreditasi Klinik.
            </td>
        </tr>
    </table>
    
    <div style="page-break-before: always;"></div>
    
    <div class="text-center" style="font-weight: bold; margin-bottom: 15px;">MEMUTUSKAN:</div>
    
    <table style="border:none; width:100%;">
        <tr style="border:none;">
            <td style="border:none; width:15%; font-weight:bold;">Menetapkan</td>
            <td style="border:none; width:5%; text-align:center;">:</td>
            <td style="border:none; width:80%; font-weight:bold;">KEPUTUSAN KEPALA KLINIK TENTANG HAK DAN KEWAJIBAN PASIEN DI KLINIK KELUARGA SEHAT.</td>
        </tr>
        <tr style="border:none;">
            <td style="border:none; font-weight:bold; padding-top:10px;">KESATU</td>
            <td style="border:none; text-align:center; padding-top:10px;">:</td>
            <td style="border:none; padding-top:10px;">Menetapkan Hak dan Kewajiban Pasien di Klinik Keluarga Sehat sebagaimana tercantum dalam Lampiran yang merupakan bagian tidak terpisahkan dari Keputusan ini.</td>
        </tr>
        <tr style="border:none;">
            <td style="border:none; font-weight:bold; padding-top:10px;">KEDUA</td>
            <td style="border:none; text-align:center; padding-top:10px;">:</td>
            <td style="border:none; padding-top:10px;">Seluruh PPA (Profesional Pemberi Asuhan) dan Staf Klinik Keluarga Sehat wajib mensosialisasikan, memahami, dan memfasilitasi pemenuhan Hak dan Kewajiban Pasien tersebut dalam pelaksanaan pelayanan sehari-hari.</td>
        </tr>
        <tr style="border:none;">
            <td style="border:none; font-weight:bold; padding-top:10px;">KETIGA</td>
            <td style="border:none; text-align:center; padding-top:10px;">:</td>
            <td style="border:none; padding-top:10px;">Keputusan ini mulai berlaku sejak tanggal ditetapkan, dan apabila di kemudian hari terdapat kekeliruan akan dilakukan perbaikan sebagaimana mestinya.</td>
        </tr>
    </table>
    
    <table class="signature-table" style="margin-top: 30px;">
        <tr>
            <td></td>
            <td>
                Ditetapkan di: Jakarta<br>
                Pada tanggal: 2 Januari 2026<br><br>
                <b>KEPALA KLINIK KELUARGA SEHAT</b><br><br><br><br>
                ( <b>dr. Ahmad Hidayat</b> )<br>
                SIP. 123/456/XX/2026
            </td>
        </tr>
    </table>

    <div style="page-break-before: always;"></div>
    
    <div style="font-weight:bold;">LAMPIRAN KEPUTUSAN KEPALA KLINIK KELUARGA SEHAT</div>
    <div>NOMOR: 001/SK/DIR/2026 TENTANG HAK DAN KEWAJIBAN PASIEN</div>
    <hr style="border-top:1px solid #000; margin-bottom:15px;">
    
    <div class="section-title">A. HAK PASIEN DI KLINIK</div>
    <p>Setiap pasien Klinik Keluarga Sehat mempunyai hak sebagai berikut:</p>
    <ol>
        <li>Mendapatkan informasi mengenai tata tertib dan peraturan yang berlaku di Klinik.</li>
        <li>Mendapatkan informasi tentang hak dan kewajiban pasien.</li>
        <li>Mendapatkan pelayanan yang manusiawi, adil, jujur, dan tanpa diskriminasi.</li>
        <li>Mendapatkan pelayanan kesehatan bermutu sesuai dengan standar profesi dan standar prosedur operasional (SPO).</li>
        <li>Mendapatkan pelayanan yang efektif dan efisien sehingga pasien terhindar dari kerugian fisik dan materi.</li>
        <li>Mengajukan pengaduan atas kualitas pelayanan yang didapatkan.</li>
        <li>Memilih dokter dan kelas perawatan sesuai dengan keinginannya dan peraturan yang berlaku di Klinik.</li>
        <li>Meminta konsultasi tentang penyakit yang dideritanya kepada dokter lain yang mempunyai Surat Izin Praktik (SIP) baik di dalam maupun di luar Klinik (second opinion).</li>
        <li>Mendapatkan privasi dan kerahasiaan penyakit yang diderita termasuk data-data medisnya (kerahasiaan Rekam Medis).</li>
        <li>Mendapatkan informasi yang meliputi diagnosis dan tata cara tindakan medis, tujuan tindakan medis, alternatif tindakan, risiko dan komplikasi yang mungkin terjadi, dan prognosis terhadap tindakan yang dilakukan serta perkiraan biaya pengobatan.</li>
        <li>Memberikan persetujuan atau menolak terhadap tindakan yang akan dilakukan oleh tenaga kesehatan (Informed Consent).</li>
        <li>Didampingi oleh keluarganya dalam keadaan kritis.</li>
        <li>Mendapatkan pemenuhan hak khusus bagi pasien lansia, berkebutuhan khusus, ibu hamil, dan menyusui.</li>
    </ol>
    
    <div class="section-title">B. KEWAJIBAN PASIEN DI KLINIK</div>
    <p>Setiap pasien Klinik Keluarga Sehat mempunyai kewajiban sebagai berikut:</p>
    <ol>
        <li>Mematuhi peraturan yang berlaku di Klinik Keluarga Sehat.</li>
        <li>Menggunakan fasilitas Klinik secara bertanggung jawab.</li>
        <li>Memberikan informasi yang jujur, lengkap, dan akurat tentang masalah kesehatannya kepada PPA.</li>
        <li>Mematuhi rencana asuhan yang direkomendasikan oleh PPA di Klinik.</li>
        <li>Menerima segala konsekuensi hukum atas keputusan penolakan tindakan medis atau rencana asuhan yang telah disarankan.</li>
        <li>Memberikan imbalan jasa atas pelayanan yang diterima sesuai ketentuan tarif Klinik.</li>
    </ol>
"""

# 2. SPO Pendaftaran Pasien
spo_pendaftaran_content = """
    <div class="doc-title">STANDAR PROSEDUR OPERASIONAL (SPO)</div>
    <div class="text-center" style="font-weight: bold; font-size: 11pt; margin-bottom: 15px;">PENDAFTARAN PASIEN</div>
    
    <table>
        <tr>
            <td style="width: 25%; font-weight: bold;">No. Dokumen</td>
            <td style="width: 25%;">010/SPO/ADM/2026</td>
            <td style="width: 25%; font-weight: bold;">No. Revisi</td>
            <td style="width: 25%;">00</td>
        </tr>
        <tr>
            <td style="font-weight: bold;">Tanggal Terbit</td>
            <td>2 Januari 2026</td>
            <td style="font-weight: bold;">Halaman</td>
            <td>1 dari 2</td>
        </tr>
        <tr>
            <td colspan="4" style="background-color:#f2f2f2; text-align:center; font-weight:bold; padding:3px;">KLINIK KELUARGA SEHAT</td>
        </tr>
    </table>
    
    <table style="margin-top: 10px;">
        <tr>
            <td style="width: 20%; font-weight: bold;">Pengertian</td>
            <td>Proses penerimaan, pencatatan data identitas sosial, dan pendaftaran pasien yang datang ke Klinik untuk mendapatkan pelayanan medis (rawat jalan, UGD, atau penunjang).</td>
        </tr>
        <tr>
            <td style="font-weight: bold;">Tujuan</td>
            <td>Sebagai acuan penerapan langkah-langkah dalam melaksanakan pendaftaran pasien secara tertib, cepat, dan akurat guna mendukung kelancaran proses asuhan terintegrasi.</td>
        </tr>
        <tr>
            <td style="font-weight: bold;">Kebijakan</td>
            <td>Surat Kebijakan Pendaftaran Pasien dan Hak Kewajiban Nomor: 005/SK/DIR/2026.</td>
        </tr>
        <tr>
            <td style="font-weight: bold;">Referensi</td>
            <td>1. Peraturan Menteri Kesehatan RI Nomor 34 Tahun 2022 tentang Akreditasi Klinik.<br>
            2. Peraturan Menteri Kesehatan RI Nomor 24 Tahun 2022 tentang Rekam Medis.</td>
        </tr>
        <tr>
            <td style="font-weight: bold;">Prosedur / Langkah-langkah</td>
            <td>
                1. <b>Salam dan Sapa:</b> Petugas admisi menyapa pasien/keluarga yang datang dengan senyum, sapa, dan salam.<br>
                2. <b>Skrining Awal:</b> Petugas memastikan pasien tidak dalam kondisi darurat medis (jika darurat, langsung arahkan ke Ruang Tindakan/UGD).<br>
                3. <b>Identifikasi Pasien:</b> Petugas menanyakan apakah pasien sudah pernah berkunjung sebelumnya (Pasien Lama atau Baru).<br>
                4. <b>Pasien Baru:</b><br>
                &nbsp;&nbsp;&nbsp;&nbsp;a. Petugas meminta kartu identitas resmi (KTP/KIA/Paspor) dan kartu asuransi (jika ada).<br>
                &nbsp;&nbsp;&nbsp;&nbsp;b. Petugas meminta pasien/keluarga mengisi Formulir Data Sosial Pasien Baru.<br>
                &nbsp;&nbsp;&nbsp;&nbsp;c. Petugas menginput data sosial pasien ke SIM-Klinik secara lengkap dan membuat nomor Rekam Medis (RM) baru.<br>
                5. <b>Pasien Lama:</b><br>
                &nbsp;&nbsp;&nbsp;&nbsp;a. Petugas meminta Kartu Identitas Berobat (KIB) atau KTP pasien.<br>
                &nbsp;&nbsp;&nbsp;&nbsp;b. Petugas mencari data Rekam Medis pasien pada sistem komputer SIM-Klinik.<br>
                6. <b>Penjelasan Hak & Kewajiban:</b> Petugas memberikan selebaran/menjelaskan hak dan kewajiban pasien kepada pasien baru, serta meminta persetujuan umum (*General Consent*).<br>
                7. <b>Tentukan Poli Tujuan:</b> Petugas menanyakan keluhan utama untuk menentukan PPA/Poli tujuan (Poli Umum, Poli Gigi, Poli Spesialis).<br>
                8. <b>Pemberian Antrean:</b> Petugas mencetak nomor antrean poli dan menyerahkannya kepada pasien.<br>
                9. <b>Ruang Tunggu:</b> Petugas mempersilakan pasien untuk menunggu di area ruang tunggu poli yang dituju.<br>
                10. <b>Distribusi RM:</b> Petugas admisi menyiapkan rekam medis fisik (jika manual) atau meneruskan rekam medis elektronik ke komputer poli tujuan.
            </td>
        </tr>
        <tr>
            <td style="font-weight: bold;">Unit Terkait</td>
            <td>1. Unit Pendaftaran / Admisi<br>
            2. Unit Rekam Medis<br>
            3. Poli Umum / Gigi / Spesialis<br>
            4. Ruang Tindakan / UGD</td>
        </tr>
    </table>
"""

# 3. SPO Skrining Pasien
spo_skrining_content = """
    <div class="doc-title">STANDAR PROSEDUR OPERASIONAL (SPO)</div>
    <div class="text-center" style="font-weight: bold; font-size: 11pt; margin-bottom: 15px;">SKRINING PASIEN</div>
    
    <table>
        <tr>
            <td style="width: 25%; font-weight: bold;">No. Dokumen</td>
            <td style="width: 25%;">011/SPO/MED/2026</td>
            <td style="width: 25%; font-weight: bold;">No. Revisi</td>
            <td style="width: 25%;">00</td>
        </tr>
        <tr>
            <td style="font-weight: bold;">Tanggal Terbit</td>
            <td>2 Januari 2026</td>
            <td style="font-weight: bold;">Halaman</td>
            <td>1 dari 2</td>
        </tr>
        <tr>
            <td colspan="4" style="background-color:#f2f2f2; text-align:center; font-weight:bold; padding:3px;">KLINIK KELUARGA SEHAT</td>
        </tr>
    </table>
    
    <table style="margin-top: 10px;">
        <tr>
            <td style="width: 20%; font-weight: bold;">Pengertian</td>
            <td>Proses penyaringan awal secara cepat terhadap pasien saat kontak pertama kali di pintu masuk klinik, loket pendaftaran, atau UGD guna mengidentifikasi tingkat keparahan, kebutuhan medis, risiko penularan infeksi, dan risiko keselamatan lainnya.</td>
        </tr>
        <tr>
            <td style="font-weight: bold;">Tujuan</td>
            <td>1. Mengidentifikasi pasien dengan kondisi gawat darurat secara cepat agar segera mendapatkan tindakan.<br>
            2. Menilai kesesuaian kebutuhan pasien dengan kemampuan pelayanan klinik.<br>
            3. Mencegah penularan infeksi di ruang tunggu (skrining batuk/infeksius).<br>
            4. Menjamin keselamatan pasien (skrining risiko jatuh).</td>
        </tr>
        <tr>
            <td style="font-weight: bold;">Kebijakan</td>
            <td>Surat Keputusan Kepala Klinik Keluarga Sehat Nomor: 006/SK/DIR/2026 tentang Skrining Pasien dan Alur Pelayanan Klinis.</td>
        </tr>
        <tr>
            <td style="font-weight: bold;">Referensi</td>
            <td>1. Keputusan Menteri Kesehatan RI Nomor HK.01.07/MENKES/1983/2022 tentang Standar Akreditasi Klinik (PKP 3).<br>
            2. PMK No. 47 Tahun 2018 tentang Pelayanan Kegawatdaruratan.</td>
        </tr>
        <tr>
            <td style="font-weight: bold;">Prosedur / Langkah-langkah</td>
            <td>
                1. <b>Kontak Pertama:</b> Skrining dilakukan sejak kontak pertama kali pasien masuk ke klinik oleh petugas keamanan/penerima tamu atau perawat loket.<br>
                2. <b>Skrining Kegawatdaruratan (Triase Visual):</b><br>
                &nbsp;&nbsp;&nbsp;&nbsp;a. Petugas memperhatikan kesadaran pasien, pola napas (sesak), adanya nyeri dada hebat, perdarahan hebat, atau cedera kepala.<br>
                &nbsp;&nbsp;&nbsp;&nbsp;b. Jika ditemukan tanda kegawatdaruratan, pasien segera dibawa ke Ruang Tindakan/UGD menggunakan kursi roda/tandu. Pendaftaran dapat diselesaikan kemudian oleh keluarga.<br>
                3. <b>Skrining Risiko Jatuh:</b><br>
                &nbsp;&nbsp;&nbsp;&nbsp;a. Petugas memperhatikan cara berjalan pasien (limbung, tidak seimbang, menggunakan alat bantu).<br>
                &nbsp;&nbsp;&nbsp;&nbsp;b. Jika berisiko jatuh tinggi, pasangkan klip/gelang kuning (jika rawat inap) dan dampingi pasien menggunakan kursi roda.<br>
                4. <b>Skrining Batuk & Isolasi:</b><br>
                &nbsp;&nbsp;&nbsp;&nbsp;a. Petugas menanyakan gejala batuk, sesak, atau demam.<br>
                &nbsp;&nbsp;&nbsp;&nbsp;b. Jika pasien batuk, petugas memberikan masker medis dan mengarahkan pasien ke ruang tunggu khusus batuk (area terpisah) untuk mencegah transmisi udara.<br>
                5. <b>Skrining Kebutuhan Khusus:</b> Petugas mengidentifikasi jika pasien lansia, penyandang disabilitas, ibu hamil tua, atau anak-anak untuk diberikan prioritas antrean pendaftaran.<br>
                6. <b>Dokumentasi:</b> Perawat mendokumentasikan hasil skrining awal pada formulir skrining di Rekam Medis pasien.
            </td>
        </tr>
        <tr>
            <td style="font-weight: bold;">Unit Terkait</td>
            <td>1. Penerima Tamu / Security / Front Office<br>
            2. Unit Admisi / Pendaftaran<br>
            3. Ruang Tindakan / UGD<br>
            4. Poli Rawat Jalan</td>
        </tr>
    </table>
"""

# 4. Informed Consent
informed_consent_content = """
    <div class="doc-title">FORMULIR PERSETUJUAN TINDAKAN KEDOKTERAN<br>(INFORMED CONSENT)</div>
    
    <table style="width: 100%; border: 1px solid #000; margin-bottom: 15px;">
        <tr>
            <td style="width: 50%; font-weight: bold; background-color: #f2f2f2;">PEMBERIAN INFORMASI</td>
            <td style="width: 50%; font-weight: bold; background-color: #f2f2f2;">IDENTITAS PASIEN</td>
        </tr>
        <tr>
            <td>
                <b>Dokter Penanggung Jawab:</b> dr. ........................................<br>
                <b>Pemberi Informasi:</b> dr. ........................................<br>
                <b>Penerima Informasi:</b> ................................................
            </td>
            <td>
                <b>Nama Pasien:</b> ......................................................<br>
                <b>No. Rekam Medis:</b> ...............................................<br>
                <b>Tgl Lahir / Umur:</b> ................... / .......... Tahun<br>
                <b>Jenis Kelamin:</b> Laki-laki / Perempuan
            </td>
        </tr>
    </table>
    
    <div class="section-title">A. PEMBERIAN INFORMASI MEDIS</div>
    <table>
        <tr>
            <th style="width: 5%;">No</th>
            <th style="width: 25%;">Jenis Informasi</th>
            <th style="width: 60%;">Penjelasan Informasi Medis</th>
            <th style="width: 10%;">Tanda (V)</th>
        </tr>
        <tr>
            <td class="text-center">1</td>
            <td><b>Diagnosis (WD/DD)</b></td>
            <td>......................................................................................................</td>
            <td></td>
        </tr>
        <tr>
            <td class="text-center">2</td>
            <td><b>Dasar Diagnosis</b></td>
            <td>Pemeriksaan fisik, anamnesis, pemeriksaan penunjang (lab/rontgen)</td>
            <td></td>
        </tr>
        <tr>
            <td class="text-center">3</td>
            <td><b>Tindakan Kedokteran</b></td>
            <td>......................................................................................................</td>
            <td></td>
        </tr>
        <tr>
            <td class="text-center">4</td>
            <td><b>Indikasi Tindakan</b></td>
            <td>......................................................................................................</td>
            <td></td>
        </tr>
        <tr>
            <td class="text-center">5</td>
            <td><b>Tata Cara & Teknik</b></td>
            <td>Tindakan bedah minor / anestesi lokal / penjahitan luka / dll.</td>
            <td></td>
        </tr>
        <tr>
            <td class="text-center">6</td>
            <td><b>Tujuan & Manfaat</b></td>
            <td>......................................................................................................</td>
            <td></td>
        </tr>
        <tr>
            <td class="text-center">7</td>
            <td><b>Risiko & Komplikasi</b></td>
            <td>Nyeri, perdarahan, infeksi sekunder, alergi obat anestesi lokal.</td>
            <td></td>
        </tr>
        <tr>
            <td class="text-center">8</td>
            <td><b>Alternatif & Risiko</b></td>
            <td>Penolak tindakan berisiko memburuknya kondisi klinis pasien.</td>
            <td></td>
        </tr>
        <tr>
            <td class="text-center">9</td>
            <td><b>Prognosis</b></td>
            <td>Dubia ad bonam / Dubia ad malam</td>
            <td></td>
        </tr>
    </table>
    
    <div style="font-size: 8pt; font-style: italic; margin-bottom: 15px;">*Dengan membubuhkan tanda centang (V), Dokter menyatakan telah memberikan penjelasan secara lisan, dan Pasien/Keluarga menyatakan telah memahaminya.</div>
    
    <div style="page-break-before: always;"></div>
    
    <div class="section-title">B. PERNYATAAN PERSETUJUAN / PENOLAKAN TINDAKAN MEDIS</div>
    <p>Yang bertanda tangan di bawah ini:</p>
    <table style="border:none; width:100%;">
        <tr style="border:none;">
            <td style="border:none; width:25%;">Nama Lengkap</td>
            <td style="border:none; width:5%; text-align:center;">:</td>
            <td style="border:none; width:70%;">...........................................................................................................</td>
        </tr>
        <tr style="border:none;">
            <td style="border:none;">Umur / Tgl Lahir</td>
            <td style="border:none; text-align:center;">:</td>
            <td style="border:none;">.......... Tahun / .......................................................................................</td>
        </tr>
        <tr style="border:none;">
            <td style="border:none;">Alamat Lengkap</td>
            <td style="border:none; text-align:center;">:</td>
            <td style="border:none;">...........................................................................................................</td>
        </tr>
        <tr style="border:none;">
            <td style="border:none;">Hubungan dengan Pasien</td>
            <td style="border:none; text-align:center;">:</td>
            <td style="border:none;">Diri sendiri / Suami / Istri / Anak / Orang Tua / Wali</td>
        </tr>
    </table>
    
    <p>Menyatakan dengan sesungguhnya bahwa saya telah menerima <b>PENJELASAN DAN INFORMASI MEDIS</b> secara lisan dari Dokter Klinik Keluarga Sehat, memahami sepenuhnya, dan secara sadar tanpa paksaan menyatakan:</p>
    <p class="text-center" style="font-weight: bold; font-size: 11pt; margin: 10px 0;">
        [ &nbsp; ] MENYETUJUI &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; [ &nbsp; ] MENOLAK
    </p>
    <p>untuk dilakukan tindakan medis berupa: <b>........................................................................................................</b> terhadap diri saya sendiri / pasien yang bernama: <b>.................................................................</b>.</p>
    <p>Saya menyetujui bahwa tindakan tersebut merupakan ikhtiar medis yang memiliki risiko bawaan, dan saya bertanggung jawab atas pilihan yang saya tanda tangani di bawah ini.</p>
    
    <table class="signature-table" style="margin-top: 30px;">
        <tr>
            <td>
                Dokter yang Menjelaskan,<br><br><br><br>
                ( <b>dr. ........................................</b> )<br>
                SIP. ............................................
            </td>
            <td>
                Jakarta, Tgl ................................ Jam ...........<br>
                Pasien / Yang Membuat Pernyataan,<br><br><br><br>
                ( <b>................................................</b> )<br>
                Tanda Tangan & Nama Terang
            </td>
        </tr>
        <tr>
            <td style="padding-top: 15px;">
                Saksi dari Pihak Klinik,<br><br><br><br>
                ( <b>................................................</b> )<br>
                Staf Klinik / Perawat
            </td>
            <td style="padding-top: 15px;">
                Saksi dari Pihak Keluarga,<br><br><br><br>
                ( <b>................................................</b> )<br>
                Anggota Keluarga Pasien
            </td>
        </tr>
    </table>
"""

# 5. Form CPPT
form_cppt_content = """
    <div class="doc-title">CATATAN PERKEMBANGAN PASIEN TERINTEGRASI (CPPT)</div>
    
    <table style="width:100%; margin-bottom: 10px;">
        <tr>
            <td style="width: 50%; line-height: 1.5;">
                <b>Nama Pasien:</b> ....................................................<br>
                <b>No. Rekam Medis:</b> .............................................
            </td>
            <td style="width: 50%; line-height: 1.5;">
                <b>Tgl Lahir / Umur:</b> ................. / ........ Thn<br>
                <b>Jenis Kelamin:</b> L/P
            </td>
        </tr>
    </table>
    
    <p style="font-size: 8pt; font-style: italic; margin-top:0;">*Catatan perkembangan pasien ditulis menggunakan format SOAP (Subyektif, Obyektif, Asesmen, Plan) oleh seluruh PPA (Dokter, Perawat, Bidan, Apoteker, Ahli Gizi) secara terintegrasi.</p>
    
    <table>
        <tr>
            <th style="width: 12%;">Tanggal / Jam</th>
            <th style="width: 15%;">PPA (Profesi)</th>
            <th style="width: 45%;">Hasil Pengkajian Pasien & Perkembangan (SOAP)</th>
            <th style="width: 18%;">Instruksi PPA Termasuk Pasca Bedah/Terapi</th>
            <th style="width: 10%;">Paraf & Nama</th>
        </tr>
        <tr style="height: 120px;">
            <td class="text-center">
                ..../..../2026<br>
                Jam: ........ WIB
            </td>
            <td>
                <b>Perawat / Bidan</b>
            </td>
            <td>
                <b>S:</b> Pasien mengeluh nyeri luka di lengan kanan pasca terjatuh 2 jam yang lalu.<br>
                <b>O:</b> Tensi: 120/80 mmHg, Nadi: 84 x/mnt, Temp: 36.5C. Tampak luka robek sepanjang 4 cm di lengan kanan, perdarahan aktif minimal.<br>
                <b>A:</b> Nyeri akut b.d agen pencedera fisik (Vulnus Laceratum).<br>
                <b>P:</b><br>
                - Bersihkan luka dengan NaCl 0.9%<br>
                - Kolaborasi dokter untuk penjahitan luka (hecting).
            </td>
            <td>
                - Lakukan pembersihan luka.<br>
                - Siapkan hecting set dan anestesi lokal (Lidocain 2%).
            </td>
            <td class="text-center">
                <br><br><br>
                ( <b>Ns. Ani, S.Kep</b> )
            </td>
        </tr>
        <tr style="height: 150px;">
            <td class="text-center">
                ..../..../2026<br>
                Jam: ........ WIB
            </td>
            <td>
                <b>Dokter Umum / Spesialis</b>
            </td>
            <td>
                <b>S:</b> Nyeri lengan kanan terluka.<br>
                <b>O:</b> Luka robek 4x1 cm, batas tegas, tepi tidak rata, mengenai subkutis. TTV dbn.<br>
                <b>A:</b> Vulnus Laceratum regio antebrachii dextra.<br>
                <b>P:</b><br>
                - Lakukan anastesi lokal Lidocain 2% (2cc).<br>
                - Lakukan hecting (jahit situasi: 4 simpul catgut/silk).<br>
                - Berikan resep obat pulang.<br>
                - Edukasi ganti perban 2 hari lagi.
            </td>
            <td>
                - Hecting luka 4 jahitan.<br>
                - Terapi oral:<br>
                &nbsp;&nbsp;* Amoxicillin 3x500mg (10 tab)<br>
                &nbsp;&nbsp;* Paracetamol 3x500mg prn nyeri<br>
                - Kontrol poli 3 hari lagi.
            </td>
            <td class="text-center">
                <br><br><br><br>
                ( <b>dr. Ahmad H.</b> )<br>
                <span style="font-size:7pt;"><i>Verifikasi DPJP</i></span>
            </td>
        </tr>
        <tr style="height: 100px;">
            <td class="text-center">
                ..../..../2026<br>
                Jam: ........ WIB
            </td>
            <td>
                <b>Apoteker (Farmasi)</b>
            </td>
            <td>
                <b>S:</b> - <br>
                <b>O:</b> Pasien menerima obat Amoxicillin 500mg (10 tab) dan Paracetamol 500mg (10 tab).<br>
                <b>A:</b> Terapi obat pulang sesuai instruksi medis Dokter, tidak ada riwayat alergi.<br>
                <b>P:</b> Lakukan PIO (Pemberian Informasi Obat): Amoxicillin dihabiskan sebagai antibiotik, Paracetamol diminum hanya bila nyeri.
            </td>
            <td>
                - Jelaskan aturan minum obat.<br>
                - Edukasi efek samping mengantuk / gangguan lambung ringan.
            </td>
            <td class="text-center">
                <br><br><br>
                ( <b>Apt. Budi, S.Farm</b> )
            </td>
        </tr>
    </table>
"""

# ----------------- NEW TKK TEMPLATES -----------------

# 6. SK Struktur Organisasi & Uraian Tugas (TKK 1)
sk_struktur_content = """
    <div class="doc-title">KEPUTUSAN KEPALA KLINIK KELUARGA SEHAT<br>NOMOR: 002/SK/DIR/2026</div>
    <div class="text-center" style="font-weight: bold; margin-bottom: 15px;">TENTANG<br>STRUKTUR ORGANISASI, TATA KERJA, DAN URAIAN TUGAS KLINIK KELUARGA SEHAT</div>
    
    <div class="text-center" style="font-weight: bold;">KEPALA KLINIK KELUARGA SEHAT,</div>
    
    <table style="border:none; margin-top:10px; width:100%;">
        <tr style="border:none;">
            <td style="border:none; width:15%; font-weight:bold;">Menimbang</td>
            <td style="border:none; width:5%; text-align:center;">:</td>
            <td style="border:none; width:80%;">
                a. bahwa agar penyelenggaraan pelayanan di Klinik Keluarga Sehat dapat berjalan secara efektif, efisien, bermutu, dan bertanggung jawab, perlu disusun pengorganisasian yang jelas;<br>
                b. bahwa struktur organisasi dan uraian tugas merupakan instrumen penting untuk menjamin kejelasan alur tanggung jawab, wewenang, komunikasi, dan pembagian tugas kerja seluruh staf;<br>
                c. bahwa berdasarkan pertimbangan tersebut pada huruf a dan b, perlu menetapkan Keputusan Kepala Klinik tentang Struktur Organisasi, Tata Kerja, dan Uraian Tugas Klinik Keluarga Sehat.
            </td>
        </tr>
        <tr style="border:none;">
            <td style="border:none; font-weight:bold; padding-top:10px;">Mengingat</td>
            <td style="border:none; text-align:center; padding-top:10px;">:</td>
            <td style="border:none; padding-top:10px;">
                1. Undang-Undang Republik Indonesia Nomor 17 Tahun 2023 tentang Kesehatan;<br>
                2. Peraturan Menteri Kesehatan Nomor 14 Tahun 2021 tentang Standar Kegiatan Usaha Sektor Kesehatan;<br>
                3. Keputusan Menteri Kesehatan Nomor HK.01.07/MENKES/1983/2022 tentang Standar Akreditasi Klinik.
            </td>
        </tr>
    </table>
    
    <div style="page-break-before: always;"></div>
    
    <div class="text-center" style="font-weight: bold; margin-bottom: 15px;">MEMUTUSKAN:</div>
    
    <table style="border:none; width:100%;">
        <tr style="border:none;">
            <td style="border:none; width:15%; font-weight:bold;">Menetapkan</td>
            <td style="border:none; width:5%; text-align:center;">:</td>
            <td style="border:none; width:80%; font-weight:bold;">KEPUTUSAN KEPALA KLINIK TENTANG STRUKTUR ORGANISASI, TATA KERJA, DAN URAIAN TUGAS KLINIK KELUARGA SEHAT.</td>
        </tr>
        <tr style="border:none;">
            <td style="border:none; font-weight:bold; padding-top:10px;">KESATU</td>
            <td style="border:none; text-align:center; padding-top:10px;">:</td>
            <td style="border:none; padding-top:10px;">Menetapkan Visi, Misi, dan Tujuan Klinik Keluarga Sehat sebagaimana tercantum dalam Lampiran I Keputusan ini.</td>
        </tr>
        <tr style="border:none;">
            <td style="border:none; font-weight:bold; padding-top:10px;">KEDUA</td>
            <td style="border:none; text-align:center; padding-top:10px;">:</td>
            <td style="border:none; padding-top:10px;">Menetapkan Bagan Struktur Organisasi Klinik Keluarga Sehat sebagaimana tercantum dalam Lampiran II Keputusan ini.</td>
        </tr>
        <tr style="border:none;">
            <td style="border:none; font-weight:bold; padding-top:10px;">KETIGA</td>
            <td style="border:none; text-align:center; padding-top:10px;">:</td>
            <td style="border:none; padding-top:10px;">Menetapkan Uraian Tugas, Tanggung Jawab, dan Wewenang masing-masing jabatan di lingkungan Klinik Keluarga Sehat sebagaimana tercantum dalam Lampiran III Keputusan ini.</td>
        </tr>
        <tr style="border:none;">
            <td style="border:none; font-weight:bold; padding-top:10px;">KEEMPAT</td>
            <td style="border:none; text-align:center; padding-top:10px;">:</td>
            <td style="border:none; padding-top:10px;">Keputusan ini mulai berlaku sejak tanggal ditetapkan, dan apabila di kemudian hari terdapat kekeliruan akan dilakukan perbaikan sebagaimana mestinya.</td>
        </tr>
    </table>
    
    <table class="signature-table" style="margin-top: 40px;">
        <tr>
            <td></td>
            <td>
                Ditetapkan di: Jakarta<br>
                Pada tanggal: 2 Januari 2026<br><br>
                <b>KEPALA KLINIK KELUARGA SEHAT</b><br><br><br><br>
                ( <b>dr. Ahmad Hidayat</b> )
            </td>
        </tr>
    </table>

    <div style="page-break-before: always;"></div>
    
    <div style="font-weight:bold; text-align:center; text-transform:uppercase;">LAMPIRAN I: VISI, MISI, DAN TUJUAN KLINIK KELUARGA SEHAT</div>
    <hr style="border-top:1px solid #000; margin-bottom:15px;">
    
    <p><b>A. VISI</b><br>
    Menjadi Klinik Pratama dan Utama terpercaya dalam menyelenggarakan pelayanan kesehatan yang bermutu, profesional, dan berorientasi pada keselamatan pasien di wilayah Jakarta Selatan pada tahun 2030.</p>
    
    <p><b>B. MISI</b><br>
    1. Menyelenggarakan pelayanan kesehatan perorangan yang komprehensif, bermutu, dan terjangkau.<br>
    2. Menerapkan tata kelola klinis dan manajemen fasilitas yang aman, suportif, dan ramah lingkungan.<br>
    3. Meningkatkan kompetensi berkelanjutan bagi seluruh Profesional Pemberi Asuhan (PPA) dan staf.<br>
    4. Mengaktifkan peran serta pasien dan keluarga dalam keselamatan asuhan pasien.</p>
    
    <p><b>C. TUJUAN</b><br>
    1. Mewujudkan derajat kesehatan perorangan yang optimal bagi pasien/pengguna layanan.<br>
    2. Menjamin keselamatan pasien, staf, dan pengunjung melalui manajemen mutu PPI dan SKP secara berkesinambungan.<br>
    3. Membangun lingkungan kerja klinik yang harmonis, profesional, dan berorientasi kepuasan pelanggan.</p>

    <div style="page-break-before: always;"></div>
    
    <div style="font-weight:bold; text-align:center; text-transform:uppercase;">LAMPIRAN II: BAGAN STRUKTUR ORGANISASI KLINIK KELUARGA SEHAT</div>
    <hr style="border-top:1px solid #000; margin-bottom:15px;">
    
    <p class="text-center" style="font-weight:bold; margin-bottom:15px;">BAGAN ALUR PENGORGANISASIAN</p>
    
    <table class="text-center" style="width:100%; border:1px solid #000;">
        <tr>
            <td colspan="4" style="background-color:#eaeaea; font-weight:bold; font-size:11pt; padding:10px;">PEMILIK KLINIK<br>(PT Sumber Sehat Keluarga)</td>
        </tr>
        <tr>
            <td colspan="4" style="padding:10px; font-weight:bold; background-color:#f9f9f9; font-size:10pt;">KEPALA / PENANGGUNG JAWAB KLINIK<br>(dr. Ahmad Hidayat)</td>
        </tr>
        <tr>
            <td style="width:25%; font-weight:bold; background-color:#f0f0f0;">Koordinator Mutu, Keselamatan & PPI<br>(PPA Utama)</td>
            <td style="width:25%; font-weight:bold; background-color:#f0f0f0;">Penanggung Jawab Medis & Keperawatan<br>(PPA Medis)</td>
            <td style="width:25%; font-weight:bold; background-color:#f0f0f0;">Penanggung Jawab Farmasi & Penunjang<br>(Apoteker/Analis)</td>
            <td style="width:25%; font-weight:bold; background-color:#f0f0f0;">Penanggung Jawab Administrasi & MFK<br>(Non-Nakes/Staf Adm)</td>
        </tr>
        <tr>
            <td>
                - Tim PMKP<br>
                - SKP & IKP<br>
                - Tim PPI
            </td>
            <td>
                - Poli Umum<br>
                - Poli Spesialis<br>
                - Ruang Tindakan/UGD<br>
                - Poli Gigi
            </td>
            <td>
                - Depo Farmasi<br>
                - Laboratorium<br>
                - Unit Gizi/Dietetik<br>
                - Radiologi (jika ada)
            </td>
            <td>
                - Admisi & RM<br>
                - Keuangan & SDM<br>
                - Tim Keamanan & APAR<br>
                - Pengelolaan B3 & Limbah
            </td>
        </tr>
    </table>

    <div style="page-break-before: always;"></div>
    
    <div style="font-weight:bold; text-align:center; text-transform:uppercase;">LAMPIRAN III: URAIAN TUGAS, TANGGUNG JAWAB, DAN WEWENANG JABATAN</div>
    <hr style="border-top:1px solid #000; margin-bottom:15px;">
    
    <p><b>1. KEPALA / PENANGGUNG JAWAB KLINIK (Tenaga Medis)</b><br>
    - <b>Tugas Pokok:</b> Memimpin, mengawasi, dan mengoordinasikan seluruh operasional, pelayanan klinis, tata usaha, serta mutu akreditasi klinik.<br>
    - <b>Tanggung Jawab:</b> Menjamin tersedianya perizinan usaha aktif, kepatuhan hukum, pemenuhan standar nasional, ketersediaan SDM, sarana prasarana yang aman, serta memberikan laporan tahunan kepada pemilik.<br>
    - <b>Wewenang:</b> Menetapkan kebijakan internal (SK/SPO), menandatangani perjanjian kerja sama, memutuskan sanksi/penghargaan pegawai, dan mengesahkan rencana kerja anggaran.</p>
    
    <p><b>2. KOORDINATOR MUTU, KESELAMATAN PASIEN, DAN PPI</b><br>
    - <b>Tugas Pokok:</b> Mengoordinasikan penyusunan program mutu (PMKP), pemantauan indikator mutu nasional (INM), manajemen risiko klinik (register risiko), pelaporan keselamatan pasien, dan kepatuhan pencegahan infeksi (PPI).<br>
    - <b>Tanggung Jawab:</b> Terlaksananya program pemantauan cuci tangan staf, kebersihan lingkungan, sterilisasi alat medis, penanganan tumpahan cairan tubuh, keselamatan bedah minor, pencegahan risiko jatuh, serta pelaporan IKP/KTD ke Kemenkes.<br>
    - <b>Wewenang:</b> Mengajukan rekomendasi perbaikan/tindak lanjut hasil audit mutu kepada Kepala Klinik, meminta laporan insiden keselamatan dari seluruh unit.</p>
    
    <p><b>3. PENANGGUNG JAWAB FARMASI (Apoteker)</b><br>
    - <b>Tugas Pokok:</b> Mengelola perencanaan, pengadaan lewat jalur resmi, penyimpanan obat, penanganan obat <i>High Alert</i>/LASA, narkotika/psikotropika, obat emergensi, peresepan, pengkajian resep, PIO, rekonsiliasi obat, serta pelaporan MESO dan <i>medication error</i>.<br>
    - <b>Tanggung Jawab:</b> Menjamin ketersediaan obat bermutu, kesesuaian formularium klinik, penanganan aman obat kadaluarsa, keakuratan pelabelan obat, serta keselamatan penggunaan obat.<br>
    - <b>Wewenang:</b> Menolak resep dokter apabila terdapat ketidaksesuaian klinis yang fatal setelah dikonfirmasi, mengawasi akses depo farmasi.</p>
"""

# 7. Rencana SDM & Evaluasi Kinerja (TKK 2)
rencana_sdm_content = """
    <div class="doc-title">DOKUMEN ANALISIS KEBUTUHAN SDM DAN EVALUASI KINERJA BERKALA</div>
    <div class="text-center" style="font-weight: bold; margin-bottom: 20px;">KLINIK KELUARGA SEHAT - TAHUN 2026</div>
    
    <div class="section-title">A. ANALISIS BEBAN KERJA (ABK) & REGULASI KETENAGAAN KLINIK</div>
    <p><b>PERSYARATAN MUTLAK PENANGGUNG JAWAB KLINIK (PerMenKes 14/2021):</b><br>
    1. Penanggung Jawab Klinik Pratama wajib merupakan Dokter, Dokter Gigi, atau Dokter Spesialis di bidang layanan primer.<br>
    2. Penanggung Jawab Klinik Utama wajib merupakan Dokter, Dokter Gigi, Dokter Spesialis, atau Dokter Gigi Spesialis.<br>
    3. Penanggung Jawab wajib memiliki <b>Surat Izin Praktik (SIP) yang aktif di klinik bersangkutan</b>, dapat merangkap sebagai pemberi layanan, dan <b>hanya diizinkan menjadi Penanggung Jawab untuk 1 (satu) klinik saja</b> (tidak boleh merangkap di fasyankes lain).</p>
    
    <p>Perencanaan ketenagaan disusun berdasarkan jenis layanan yang diselenggarakan, jam buka operasional klinik, serta analisis beban kerja harian rata-rata. Berikut tabel kebutuhan riil di Klinik Keluarga Sehat:</p>
    
    <table>
        <tr>
            <th>No</th>
            <th>Nama Jabatan / Profesi</th>
            <th>Kualifikasi Pendidikan</th>
            <th>Kebutuhan (Riil ABK)</th>
            <th>Ketersediaan (Aktif)</th>
            <th>Kesenjangan (Gap)</th>
            <th>Rencana Tindak Lanjut</th>
        </tr>
        <tr>
            <td class="text-center">1</td>
            <td>Dokter Umum / Penanggung Jawab</td>
            <td>Profesi Dokter + SIP + STR</td>
            <td class="text-center">3 Orang</td>
            <td class="text-center">3 Orang</td>
            <td class="text-center">0</td>
            <td>Mempertahankan & mengirim ke pelatihan ACLS berkala.</td>
        </tr>
        <tr>
            <td class="text-center">2</td>
            <td>Dokter Gigi</td>
            <td>Profesi Dokter Gigi + SIP + STR</td>
            <td class="text-center">2 Orang</td>
            <td class="text-center">1 Orang</td>
            <td class="text-center">-1</td>
            <td>Melakukan rekrutmen 1 Dokter Gigi tambahan kontrak paruh waktu.</td>
        </tr>
        <tr>
            <td class="text-center">3</td>
            <td>Perawat / Bidan</td>
            <td>D3/S1 Kep/Keb + SIPP/SIPB + STR</td>
            <td class="text-center">6 Orang</td>
            <td class="text-center">5 Orang</td>
            <td class="text-center">-1</td>
            <td>Rekrutmen 1 Perawat baru, diutamakan bersertifikat BTCLS.</td>
        </tr>
        <tr>
            <td class="text-center">4</td>
            <td>Apoteker</td>
            <td>Profesi Apoteker + SIPA + STRA</td>
            <td class="text-center">1 Orang</td>
            <td class="text-center">1 Orang</td>
            <td class="text-center">0</td>
            <td>Menambah asisten tenaga teknis kefarmasian (TTK).</td>
        </tr>
        <tr>
            <td class="text-center">5</td>
            <td>Analis Laboratorium</td>
            <td>D3 Analis Kesehatan + SIP + STR</td>
            <td class="text-center">1 Orang</td>
            <td class="text-center">1 Orang</td>
            <td class="text-center">0</td>
            <td>Pelatihan PME & PMI internal.</td>
        </tr>
    </table>

    <div style="page-break-before: always;"></div>
    
    <div class="section-title">B. FORM PENILAIAN KINERJA PEGAWAI BULANAN / TAHUNAN</div>
    <p><b>Nama Pegawai:</b> ........................................................ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <b>Unit Kerja:</b> ..............................................<br>
    <b>Jabatan / Profesi:</b> ................................................. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <b>Periode Evaluasi:</b> Tahun 2026</p>
    
    <table>
        <tr>
            <th style="width: 5%;">No</th>
            <th style="width: 30%;">Aspek Penilaian (Indikator Kinerja)</th>
            <th style="width: 45%;">Definisi Operasional / Standar Kerja</th>
            <th style="width: 10%;">Bobot (%)</th>
            <th style="width: 10%;">Skor (1-5)</th>
        </tr>
        <tr>
            <td class="text-center">1</td>
            <td><b>Kepatuhan SPO Pelayanan</b></td>
            <td>Melaksanakan asuhan klinis/administratif sesuai alur SPO klinis/non-klinis.</td>
            <td class="text-center">30%</td>
            <td></td>
        </tr>
        <tr>
            <td class="text-center">2</td>
            <td><b>Disiplin & Kehadiran</b></td>
            <td>Kehadiran masuk kerja tepat waktu minimal 95% dalam sebulan.</td>
            <td class="text-center">20%</td>
            <td></td>
        </tr>
        <tr>
            <td class="text-center">3</td>
            <td><b>Mutu & Keselamatan Pasien</b></td>
            <td>Melakukan 6 langkah cuci tangan, identifikasi pasien 2 cara, nihil insiden KTD.</td>
            <td class="text-center">20%</td>
            <td></td>
        </tr>
        <tr>
            <td class="text-center">4</td>
            <td><b>Kerja Sama & Komunikasi</b></td>
            <td>Menggunakan SBAR/TBAK saat serah terima pasien/pelaporan, ramah 5S.</td>
            <td class="text-center">15%</td>
            <td></td>
        </tr>
        <tr>
            <td class="text-center">5</td>
            <td><b>Pengembangan Kompetensi</b></td>
            <td>Aktif mengikuti sosialisasi internal, seminar eksternal, atau orientasi staf.</td>
            <td class="text-center">15%</td>
            <td></td>
        </tr>
        <tr>
            <th colspan="3" class="text-right">TOTAL SKOR AKHIR</th>
            <td class="text-center">100%</td>
            <td></td>
        </tr>
    </table>
    <p><b>Rekomendasi Pimpinan:</b> Perpanjang Kontrak / Kenaikan Golongan / Pelatihan Tambahan / Teguran Lisan / Tertulis.</p>
    
    <div style="page-break-before: always;"></div>
    
    <div class="section-title">C. CHECKLIST KEUTUHAN FILE KEPEGAWAIAN INDIVIDU</div>
    <p>Setiap staf wajib memiliki file kepegawaian fisik dan digital yang diperbarui secara berkala minimal setahun sekali. Gunakan checklist berikut:</p>
    
    <table>
        <tr>
            <th>No</th>
            <th>Jenis Dokumen Kepegawaian</th>
            <th>Ada (V)</th>
            <th>Tidak (X)</th>
            <th>Masa Berlaku / Keterangan</th>
        </tr>
        <tr>
            <td class="text-center">1</td>
            <td>Salinan Ijazah Terakhir dan Transkrip Nilai (legalisir)</td>
            <td></td>
            <td></td>
            <td>Seumur Hidup</td>
        </tr>
        <tr>
            <td class="text-center">2</td>
            <td>Surat Tanda Registrasi (STR) Aktif bagi Nakes</td>
            <td></td>
            <td></td>
            <td>Masa Berlaku: .......................................</td>
        </tr>
        <tr>
            <td class="text-center">3</td>
            <td>Surat Izin Praktik (SIP) Aktif di Klinik ini</td>
            <td></td>
            <td></td>
            <td>Masa Berlaku: .......................................</td>
        </tr>
        <tr>
            <td class="text-center">4</td>
            <td>Uraian Tugas Tertulis (ditandatangani Kepala Klinik & staf)</td>
            <td></td>
            <td></td>
            <td>Terbaru Tahun 2026</td>
        </tr>
        <tr>
            <td class="text-center">5</td>
            <td>Sertifikat Pelatihan Kompetensi (BTCLS, ACLS, PPI, MFK, RME, APAR)</td>
            <td></td>
            <td></td>
            <td>Terlampir minimal 2 sertifikat terbaru</td>
        </tr>
        <tr>
            <td class="text-center">6</td>
            <td>Hasil Penilaian Kinerja Karyawan berkala</td>
            <td></td>
            <td></td>
            <td>Tahun Buku 2025/2026</td>
        </tr>
        <tr>
            <td class="text-center">7</td>
            <td>Surat Keterangan Sehat Fisik & Mental Bebas Narkoba</td>
            <td></td>
            <td></td>
            <td>Diperbarui setiap 2 tahun sekali</td>
        </tr>
    </table>
"""

# 8. Program MFK & Manajemen Risiko (TKK 3)
program_mfk_content = """
    <div class="doc-title">PROGRAM KERJA MANAJEMEN FASILITAS DAN KESELAMATAN (MFK)</div>
    <div class="text-center" style="font-weight: bold; margin-bottom: 20px;">KLINIK KELUARGA SEHAT - TAHUN 2026</div>
    
    <div class="section-title">A. TUJUAN PROGRAM</div>
    <p>Menjamin tersedianya fasilitas klinik yang aman, berfungsi dengan baik, suportif, serta meminimalkan risiko kecelakaan, infeksi, kebakaran, tumpahan bahan beracun, kegagalan utilitas, kerusakan alat medis, dan pencemaran lingkungan bagi pasien, keluarga, pengunjung, serta seluruh staf Klinik Keluarga Sehat.</p>
    
    <div class="section-title">B. IMPLEMENTASI 7 AREA PROGRAM MFK SESUAI STANDAR</div>
    
    <p><b>1. Keselamatan dan Keamanan Fasilitas</b><br>
    - <b>Kegiatan:</b> Inspeksi berkala struktur fisik gedung (plafon bocor, lantai licin, tangga, pegangan tangan), pemeliharaan toilet pasien.<br>
    - <b>Parameter Lingkungan:</b> Pemantauan suhu ruangan (standar 20-26C), kelembapan (40-60%), pencahayaan ruang tindakan (minimal 300 lux), tingkat kebisingan koridor/tunggu (maksimal 45-55 dBA) diukur periodik dengan alat ukur portabel terkalibrasi.<br>
    - <b>Keamanan:</b> CCTV di titik rawan (loket obat, pintu keluar utama, koridor), penyediaan kartu pengenal staf, kartu akses rekam medis, patroli satpam malam.</p>
    
    <p><b>2. Bahan Berbahaya dan Beracun (B3) serta Limbah B3</b><br>
    - <b>Kegiatan:</b> Daftar inventarisasi B3 di Laboratorium, Farmasi, dan ruang tindakan. Menyediakan MSDS (Material Safety Data Sheet) yang mudah diakses petugas. Menyediakan lemari penyimpanan B3 ber-ventilasi dan berlabel simbol bahaya. Menyediakan APD dan <i>Spill Kit B3</i> (serbuk gergaji/pasir, kantong kuning, sekop kecil). Pengumpulan limbah medis di TPS B3 berizin sementara sebelum diangkut rekanan berizin.</p>
    
    <p><b>3. Penanggulangan Bencana (Disaster Plan)</b><br>
    - <b>Kegiatan:</b> Analisis risiko bencana. Menetapkan tim tanggap darurat (tim merah: pemadam, tim kuning: evakuasi pasien, tim hijau: penyelamat dokumen/aset). Rambu jalur evakuasi glow in the dark, penentuan Titik Kumpul (Assembly Point).</p>
    
    <p><b>4. Sistem Proteksi Kebakaran</b><br>
    - <b>Kegiatan:</b> Penyediaan APAR jenis Powder dan CO2 di area rawan (dapur, panel listrik, loket farmasi, laboratorium, poli umum). Melakukan inspeksi APAR bulanan. Melarang keras aktivitas merokok di seluruh area klinik.</p>
    
    <p><b>5. Peralatan Medis</b><br>
    - <b>Kegiatan:</b> Menyusun daftar inventaris alat medis. Pemeliharaan preventif harian (pembersihan) dan berkala (kalibrasi tahunan oleh lembaga penguji terakreditasi). Penarikan (recall) alat medis yang rusak atau tidak layak pakai.</p>
    
    <p><b>6. Sistem Utilitas (Listrik, Air, Gas Medis, Sanitasi)</b><br>
    - <b>Listrik:</b> Penyediaan Genset cadangan otomatis yang dipanaskan seminggu sekali untuk menjamin operasional RME, kulkas vaksin farmasi, dan lampu darurat tindakan.<br>
    - <b>Air Kesesuaian Kualitas:</b> Uji kualitas mikrobiologi & kimia air bersih laboratorium/tindakan ke Labkesda setahun sekali. Penyediaan toren air cadangan.<br>
    - <b>Gas Medis Rantai Pasok:</b> Pengaturan rantai pasok oksigen tabung lengkap dengan **braket pengaman dinding (rantai/holder)** agar tabung tidak roboh atau terbentur.</p>
    
    <p><b>7. Sampah Domestik dan Air Limbah</b><br>
    - <b>Kegiatan:</b> Penyediaan tong sampah domestik non-medis terpisah (organik-anorganik) berplastik hitam. Penyediaan IPAL fungsional untuk limbah cair laboratorium dan ruang tindakan, melakukan pemantauan kualitas outlet air limbah berkala ke lab eksternal terakreditasi.</p>
"""

# 9. Form Inspeksi APAR & B3 (TKK 3)
form_apar_b3_content = """
    <div class="doc-title">SPO DAN KARTU KONTROL INSPEKSI BULANAN APAR & REGISTER B3</div>
    
    <div class="section-title">A. STANDAR PROSEDUR OPERASIONAL (SPO) PEMELIHARAAN APAR</div>
    <p><b>Langkah-langkah Pemeliharaan:</b><br>
    1. Lakukan inspeksi visual setiap tanggal 1 awal bulan oleh petugas keamanan/sarpras.<br>
    2. Periksa tekanan manometer APAR, pastikan jarum berada di zona HIJAU (tekanan normal).<br>
    3. Periksa kondisi fisik tabung (tidak berkarat, tidak bocor), selang (tidak retak/pecah), nosel (tidak tersumbat), dan pin pengunci (masih tersegel aman).<br>
    4. Balik tabung APAR powder secara perlahan 2-3 kali untuk mencegah penggumpalan serbuk di dalam tabung.<br>
    5. Bersihkan tabung dari debu, catat hasil inspeksi pada Kartu Kontrol APAR di bawah ini.</p>
    
    <div class="section-title">B. KARTU KONTROL INSPEKSI APAR BULANAN - TAHUN 2026</div>
    <p><b>Nomor Unit APAR:</b> APAR-01 &nbsp;&nbsp;&nbsp;&nbsp; <b>Lokasi:</b> Depan Depo Farmasi &nbsp;&nbsp;&nbsp;&nbsp; <b>Jenis APAR:</b> Dry Chemical Powder (3 Kg)</p>
    <table>
        <tr>
            <th>Bulan</th>
            <th>Manometer (Hijau/Merah)</th>
            <th>Selang & Nosel (Baik/Retak)</th>
            <th>Pin & Segel (Utuh/Putus)</th>
            <th>Kebersihan (Bersih/Kotor)</th>
            <th>Paraf Pemeriksa</th>
            <th>Keterangan / Rencana Isi Ulang</th>
        </tr>
        <tr>
            <td class="text-center">Januari</td>
            <td class="text-center">Hijau</td>
            <td class="text-center">Baik</td>
            <td class="text-center">Utuh</td>
            <td class="text-center">Bersih</td>
            <td class="text-center"><br>Spt.</td>
            <td>Masa kadaluarsa s.d Des 2026.</td>
        </tr>
        <tr>
            <td class="text-center">Februari</td>
            <td class="text-center">Hijau</td>
            <td class="text-center">Baik</td>
            <td class="text-center">Utuh</td>
            <td class="text-center">Bersih</td>
            <td class="text-center"><br>Spt.</td>
            <td>Kondisi aman.</td>
        </tr>
        <tr>
            <td class="text-center">Maret</td>
            <td class="text-center">Hijau</td>
            <td class="text-center">Baik</td>
            <td class="text-center">Utuh</td>
            <td class="text-center">Bersih</td>
            <td class="text-center"><br>Spt.</td>
            <td>Kondisi aman.</td>
        </tr>
    </table>

    <div style="page-break-before: always;"></div>
    
    <div class="section-title">C. REGISTER INVENTARIS B3 & PROSEDUR SPILL KIT</div>
    <p><b>PROSEDUR PENANGANAN TUMPAHAN B3 (MENGGUNAKAN SPILL KIT B3):</b><br>
    1. Ambil kotak Spill Kit B3 terdekat. Pasang tanda peringatan "Awas Tumpahan Bahan Berbahaya".<br>
    2. Petugas wajib mengenakan APD lengkap (kacamata goggle, masker respirator, apron, sarung tangan nitril/karet).<br>
    3. Batasi area tumpahan dengan menaburkan serbuk gergaji/pasir penyerap secara melingkar di sekeliling tumpahan.<br>
    4. Taburkan serbuk gergaji/pasir di atas tumpahan secara merata hingga cairan terserap sepenuhnya.<br>
    5. Sapu dan sekop pasir hasil serapan menggunakan sekop plastik kecil, lalu masukkan ke dalam kantong plastik kuning limbah medis/B3. Ikat rapat, beri label B3, dan taruh di TPS B3 berizin.</p>
    
    <table>
        <tr>
            <th>No</th>
            <th>Nama Bahan B3</th>
            <th>Lokasi</th>
            <th>Jenis Bahaya</th>
            <th>Simbol Terpasang</th>
            <th>MSDS (Ya/No)</th>
            <th>APD Wajib</th>
            <th>Jumlah Stok Maks</th>
        </tr>
        <tr>
            <td class="text-center">1</td>
            <td><b>Alkohol 96% / 70%</b></td>
            <td>Gudang Farmasi & Poli</td>
            <td>Mudah Terbakar</td>
            <td class="text-center">Ya (Api)</td>
            <td class="text-center">Ya</td>
            <td>Masker medis, Handscoon latex</td>
            <td>5 Liter</td>
        </tr>
        <tr>
            <td class="text-center">2</td>
            <td><b>Klorin / Bayclin</b></td>
            <td>TPS / Ruang CS</td>
            <td>Korosif, Iritasi</td>
            <td class="text-center">Ya (Korosif)</td>
            <td class="text-center">Ya</td>
            <td>Masker, Goggle, Apron, Sarung tangan karet</td>
            <td>10 Liter</td>
        </tr>
        <tr>
            <td class="text-center">3</td>
            <td><b>Reagen Pewarna Gram</b></td>
            <td>Laboratorium</td>
            <td>Iritasi, Berwarna</td>
            <td class="text-center">Ya (Toksik)</td>
            <td class="text-center">Ya</td>
            <td>Jas lab, Masker, Handscoon nitril</td>
            <td>2 Botol @ 500 ml</td>
        </tr>
    </table>
"""

# 10. MoU Kerja Sama & KPI Rekanan (TKK 4)
mou_kontrak_content = """
    <div class="doc-title">PERJANJIAN KERJA SAMA (KONTRAK KERJA)</div>
    <div class="text-center" style="font-weight: bold; margin-bottom: 20px;">NOMOR: 050/PKS/ADM/I/2026</div>
    
    <p>Kami yang bertanda tangan di bawah ini:</p>
    <ol>
        <li><b>dr. Ahmad Hidayat</b>, selaku Kepala Klinik Keluarga Sehat, beralamat di Jl. Raya Pembangunan No. 123, Jakarta Selatan, selanjutnya disebut sebagai <b>PIHAK PERTAMA</b>.</li>
        <li><b>Ir. Bambang Wijaya</b>, selaku Direktur Utama PT Bio Lab Nusantara, beralamat di Jl. Kesehatan Raya No. 45, Jakarta Selatan, selanjutnya disebut sebagai <b>PIHAK KEDUA</b>.</li>
    </ol>
    <p>Kedua belah pihak secara bersama-sama sepakat mengikatkan diri dalam Perjanjian Kerja Sama Rujukan Pemeriksaan Laboratorium Spesialis dengan ketentuan sebagai berikut:</p>
    
    <div class="section-title">Pasal 1: Ruang Lingkup Kerja Sama</div>
    <p>PIHAK PERTAMA menunjuk PIHAK KEDUA sebagai laboratorium rekanan rujukan eksternal untuk melakukan pemeriksaan spesimen laboratorium yang tidak dapat dikerjakan secara mandiri di fasilitas laboratorium internal milik PIHAK PERTAMA.</p>
    
    <div class="section-title">Pasal 2: Standar Kompetensi & Mutu Pelayanan</div>
    <p>PIHAK KEDUA menjamin bahwa seluruh pemeriksaan dilakukan oleh analis kesehatan berkompeten di bawah pengawasan Dokter Spesialis Patologi Klinik berizin, serta menyelenggarakan PMI dan PME berkala.</p>

    <div style="page-break-before: always;"></div>
    
    <div class="section-title">Pasal 3: Indikator Kinerja Utama (Key Performance Indicators / KPI)</div>
    <table>
        <tr>
            <th>No</th>
            <th>Indikator Kinerja Mutu</th>
            <th>Target Mutu Disepakati</th>
            <th>Frekuensi</th>
            <th>Sanksi Ketidakpatuhan</th>
        </tr>
        <tr>
            <td class="text-center">1</td>
            <td><b>Waktu Tunggu Hasil (TAT)</b></td>
            <td>&ge; 98% hasil dikirimkan dalam 4 jam setelah sampel diterima.</td>
            <td class="text-center">Bulanan</td>
            <td>Teguran Tertulis I apabila 2 bulan berturut-turut gagal.</td>
        </tr>
        <tr>
            <td class="text-center">2</td>
            <td><b>Lapor Hasil Kritis</b></td>
            <td>100% hasil kritis dihubungi via telepon &le; 15 menit.</td>
            <td class="text-center">Insidentil</td>
            <td>Denda pemotongan biaya tagihan sebesar 5% per insiden.</td>
        </tr>
        <tr>
            <td class="text-center">3</td>
            <td><b>Keamanan Spesimen</b></td>
            <td>&le; 0.5% insiden spesimen lisis/rusak karena transportasi.</td>
            <td class="text-center">Bulanan</td>
            <td>PIHAK KEDUA wajib mengambil sampel ulang secara gratis.</td>
        </tr>
    </table>
    
    <div class="section-title">Pasal 4: Penutup</div>
    <p>Evaluasi berkala terhadap kinerja PIHAK KEDUA dilakukan oleh Tim PMKP Klinik Keluarga Sehat secara periodik.</p>
    
    <table class="signature-table" style="margin-top: 30px;">
        <tr>
            <td>
                <b>PIHAK PERTAMA</b><br>
                Kepala Klinik Keluarga Sehat<br><br><br><br>
                ( <b>dr. Ahmad Hidayat</b> )
            </td>
            <td>
                <b>PIHAK KEDUA</b><br>
                Direktur PT Bio Lab Nusantara<br><br><br><br>
                ( <b>Ir. Bambang Wijaya</b> )
            </td>
        </tr>
    </table>
"""

# ----------------- NEW PMKP TEMPLATES -----------------

# 11. SK Penanggung Jawab Mutu & Register Risiko (PMKP 1)
sk_pj_mutu_content = """
    <div class="doc-title">KEPUTUSAN KEPALA KLINIK KELUARGA SEHAT<br>NOMOR: 003/SK/DIR/2026</div>
    <div class="text-center" style="font-weight: bold; margin-bottom: 15px;">TENTANG<br>PENETAPAN PENANGGUNG JAWAB PROGRAM MUTU, KESELAMATAN PASIEN, DAN REGISTER RISIKO KLINIK</div>
    
    <div class="text-center" style="font-weight: bold;">KEPALA KLINIK KELUARGA SEHAT,</div>
    
    <table style="border:none; margin-top:10px; width:100%;">
        <tr style="border:none;">
            <td style="border:none; width:15%; font-weight:bold;">Menimbang</td>
            <td style="border:none; width:5%; text-align:center;">:</td>
            <td style="border:none; width:80%;">
                a. bahwa dalam rangka peningkatan mutu pelayanan kesehatan, pemenuhan sasaran keselamatan pasien, serta pengelolaan risiko klinis secara komprehensif, perlu ditunjuk seorang Penanggung Jawab/Koordinator Mutu Klinik;<br>
                b. bahwa penetapan penanggung jawab mutu merupakan wujud komitmen pimpinan klinik untuk mendukung sistem akreditasi berkelanjutan;<br>
                c. bahwa berdasarkan pertimbangan tersebut, perlu menetapkan Keputusan Kepala Klinik tentang Penanggung Jawab Program Mutu, Keselamatan Pasien, dan Register Risiko Klinik Keluarga Sehat.
            </td>
        </tr>
        <tr style="border:none;">
            <td style="border:none; font-weight:bold; padding-top:10px;">Mengingat</td>
            <td style="border:none; text-align:center; padding-top:10px;">:</td>
            <td style="border:none; padding-top:10px;">
                1. Peraturan Menteri Kesehatan Nomor 34 Tahun 2022 tentang Akreditasi Klinik;<br>
                2. Peraturan Menteri Kesehatan Nomor 30 Tahun 2022 tentang Indikator Nasional Mutu Pelayanan Kesehatan.
            </td>
        </tr>
    </table>
    
    <div style="page-break-before: always;"></div>
    
    <div class="text-center" style="font-weight: bold; margin-bottom: 15px;">MEMUTUSKAN:</div>
    
    <table style="border:none; width:100%;">
        <tr style="border:none;">
            <td style="border:none; width:15%; font-weight:bold;">Menetapkan</td>
            <td style="border:none; width:5%; text-align:center;">:</td>
            <td style="border:none; width:80%; font-weight:bold;">KEPUTUSAN KEPALA KLINIK TENTANG PENANGGUNG JAWAB PROGRAM MUTU, KESELAMATAN PASIEN, DAN REGISTER RISIKO KLINIK KELUARGA SEHAT.</td>
        </tr>
        <tr style="border:none;">
            <td style="border:none; font-weight:bold; padding-top:10px;">KESATU</td>
            <td style="border:none; text-align:center; padding-top:10px;">:</td>
            <td style="border:none; padding-top:10px;">Menunjuk <b>dr. Silvia Anggraeni</b> sebagai Penanggung Jawab Program Mutu dan Keselamatan Pasien di Klinik Keluarga Sehat.</td>
        </tr>
        <tr style="border:none;">
            <td style="border:none; font-weight:bold; padding-top:10px;">KEDUA</td>
            <td style="border:none; text-align:center; padding-top:10px;">:</td>
            <td style="border:none; padding-top:10px;">Penanggung Jawab Mutu wajib melakukan koordinasi pengukuran, evaluasi, pelaporan Indikator Nasional Mutu (INM) dan menyusun Register Risiko Klinik tahunan sebagaimana terlampir.</td>
        </tr>
    </table>
    
    <table class="signature-table" style="margin-top: 30px;">
        <tr>
            <td></td>
            <td>
                Ditetapkan di: Jakarta<br>
                Pada tanggal: 2 Januari 2026<br><br>
                <b>KEPALA KLINIK KELUARGA SEHAT</b><br><br><br><br>
                ( <b>dr. Ahmad Hidayat</b> )
            </td>
        </tr>
    </table>

    <div style="page-break-before: always;"></div>
    
    <div style="font-weight:bold; text-align:center; text-transform:uppercase;">LAMPIRAN: REGISTER RISIKO TAHUNAN KLINIK KELUARGA SEHAT</div>
    <hr style="border-top:1px solid #000; margin-bottom:15px;">
    
    <table>
        <tr>
            <th>No</th>
            <th>Unit Kerja</th>
            <th>Identifikasi Risiko</th>
            <th>Penyebab Risiko</th>
            <th>Dampak Klinis/Operasional</th>
            <th>Tingkat Risiko</th>
            <th>Tindakan Mitigasi</th>
            <th>PJ Mitigasi</th>
        </tr>
        <tr>
            <td class="text-center">1</td>
            <td>Pendaftaran</td>
            <td>Kesalahan rekam medis pasien (RME tertukar)</td>
            <td>Petugas tidak cek kartu ID pas berobat</td>
            <td>Salah diagnosis/pemberian obat</td>
            <td class="text-center" style="background-color:#ffcccc; font-weight:bold;">HIGH</td>
            <td>Terapkan minimal 2 cara identifikasi (Nama + Tgl Lahir) di loket secara ketat.</td>
            <td>Admisi</td>
        </tr>
        <tr>
            <td class="text-center">2</td>
            <td>Laboratorium</td>
            <td>Terpapar jarum suntik bekas infeksius</td>
            <td>Petugas terburu-buru, tidak pakai APD</td>
            <td>Penularan Hepatitis B / HIV</td>
            <td class="text-center" style="background-color:#ffcccc; font-weight:bold;">HIGH</td>
            <td>Edukasi teknik one-hand recapping, wajibkan safety box.</td>
            <td>Analis Lab</td>
        </tr>
        <tr>
            <td class="text-center">3</td>
            <td>Farmasi</td>
            <td>Salah pengambilan obat LASA (Look Alike)</td>
            <td>Penataan obat berdekatan tanpa stiker pembeda</td>
            <td>KTD/Efek samping merugikan</td>
            <td class="text-center" style="background-color:#ffe5cc; font-weight:bold;">MEDIUM</td>
            <td>Pasang stiker LASA berwarna jingga, pisahkan penyimpanan.</td>
            <td>Apoteker</td>
        </tr>
    </table>
"""

# 12. SPO Identifikasi & Komunikasi Efektif (PMKP 2)
spo_identifikasi_content = """
    <div class="doc-title">SPO IDENTIFIKASI PASIEN DAN KOMUNIKASI EFEKTIF (SBAR & TBAK)</div>
    
    <div class="section-title">A. STANDAR PROSEDUR OPERASIONAL (SPO) IDENTIFIKASI PASIEN</div>
    <p>1. Lakukan identifikasi pasien secara aktif sebelum melakukan pemberian obat, pengambilan sampel laboratorium, tindakan bedah minor, atau pemberian diit.<br>
    2. Mintalah pasien untuk menyebutkan **Nama Lengkap** dan **Tanggal Lahir / NIK** (bukan mencocokkan secara pasif seperti: "Apakah Anda Bpk. Budi?").<br>
    3. Cocokkan data sosial yang diucapkan pasien dengan label identitas yang tertempel pada berkas Rekam Medis (RME).<br>
    4. Jika pasien dalam kondisi penurunan kesadaran/koma, identifikasi dilakukan dengan mencocokkan data pada gelang identitas pasien atau menanyakan ke keluarga pengantar resmi secara verbal.</p>
    
    <div class="section-title">B. STANDAR PROSEDUR OPERASIONAL (SPO) KOMUNIKASI EFEKTIF (SBAR & TBAK)</div>
    <p><b>SOP SBAR (Melaporkan Kondisi Pasien via Telepon kepada Dokter DPJP):</b><br>
    - <b>S (Situation):</b> Laporkan nama pasien, umur, no rekam medis, lokasi, dan masalah klinis saat ini.<br>
    - <b>B (Background):</b> Jelaskan riwayat penyakit, diagnosis masuk, tindakan medis yang baru saja dilakukan, dan tanda vital.<br>
    - <b>A (Assessment):</b> Sampaikan hasil analisis atau kesimpulan klinis sementara.<br>
    - <b>R (Recommendation):</b> Usulkan tindakan segera.</p>
    
    <p><b>SOP TBAK (Menerima Instruksi Verbal / Telepon dari Dokter):</b><br>
    1. <b>TULIS (Write Down):</b> Tuliskan instruksi lengkap dokter pada lembar CPPT pasien secara jelas.<br>
    2. <b>BACA (Read Back):</b> Bacakan kembali instruksi tertulis tersebut secara lengkap kepada dokter via telepon.<br>
    3. <b>KONFIRMASI (Confirm):</b> Mintalah dokter mengonfirmasi kebenaran instruksi ("Apakah sudah benar Dok?"). Bubuhkan stempel "TBAK". Dokter wajib menandatangani verifikasi dalam waktu 24 jam.</p>
    
    <div class="section-title">C. FORMULIR CATATAN INSTRUKSI VERBAL (TBAK)</div>
    <table>
        <tr>
            <th>Tanggal / Jam</th>
            <th>Nama Pasien & No. RM</th>
            <th>Isi Instruksi Diterima</th>
            <th>Nama Dokter</th>
            <th>Nama Staf</th>
            <th>Status TBAK (Ya/Tidak)</th>
            <th>Tanda Tangan Dokter (24 Jam)</th>
        </tr>
        <tr>
            <td class="text-center">15/03/2026<br>Jam 14.15 WIB</td>
            <td>Ny. Aminah / 00-45-88</td>
            <td>Injeksi Ketorolac 30 mg IV / 8 jam (prn nyeri)</td>
            <td>dr. Ahmad Hidayat</td>
            <td>Ns. Rina</td>
            <td class="text-center" style="font-weight:bold; color:green;">YA (TBAK)</td>
            <td><br><br>...........................</td>
        </tr>
    </table>
"""

# 13. WHO Surgical Safety Checklist (PMKP 2)
surgical_safety_content = """
    <div class="doc-title">WHO SURGICAL SAFETY CHECKLIST & PENANDAAN LOKASI OPERASI</div>
    <div class="text-center" style="font-weight: bold; margin-bottom: 20px;">DIAPLIKASIKAN UNTUK TINDAKAN BEDAH MINOR KLINIK</div>
    
    <div class="section-title">A. SPO PENANDAAN LOKASI TINDAKAN (SURGICAL SITE MARKING)</div>
    <p>1. Penandaan sisi operasi wajib dilakukan untuk seluruh tindakan medis yang memiliki sisi kanan/kiri, beberapa struktur (jari tangan/kaki), atau tingkatan.<br>
    2. Penandaan dilakukan oleh dokter pemberi asuhan yang akan mengeksekusi langsung tindakan medis tersebut.<br>
    3. Penandaan dilakukan bersama pasien/keluarga dalam kondisi sadar sebelum dibawa ke ruang tindakan bedah.<br>
    4. Gunakan penanda spidol dermatografis tahan air berwarna biru/hitam berupa simbol **lingkaran (O)** atau **silang (X)** yang jelas pada daerah sayatan kulit.</p>
    
    <div class="section-title">B. FORMULIR CHECKLIST KESELAMATAN PASIEN BEDAH MINOR (ADAPTASI WHO)</div>
    <p><b>Nama Pasien:</b> ........................................................ &nbsp;&nbsp;&nbsp;&nbsp; <b>No. RM:</b> ..............................................<br>
    <b>Tindakan Bedah:</b> ........................................................ &nbsp;&nbsp;&nbsp;&nbsp; <b>Dokter Operator:</b> ............................................</p>
    
    <table>
        <tr>
            <th style="width: 33%; background-color:#ffcccc;">SIGN IN<br>(Sebelum Induksi Anestesi Lokal)</th>
            <th style="width: 34%; background-color:#ffe5cc;">TIME OUT<br>(Sebelum Insisi Kulit Mulai)</th>
            <th style="width: 33%; background-color:#ccffcc;">SIGN OUT<br>(Sebelum Pasien Keluar Ruang Bedah)</th>
        </tr>
        <tr>
            <td>
                <b>[ &nbsp; ] Konfirmasi Pasien:</b><br>
                - Identitas (Nama & No RM) sesuai.<br>
                - Sisi lokasi operasi benar.<br>
                - Prosedur tindakan dipahami.<br>
                - Informed Consent ditandatangani.<br><br>
                <b>[ &nbsp; ] Penandaan Sisi Lokasi:</b><br>
                - [ &nbsp; ] Ya, tanda spidol terverifikasi.<br>
                - [ &nbsp; ] Tidak diperlukan.<br><br>
                <b>[ &nbsp; ] Mesin & Obat Anestesi:</b><br>
                - Lidocain 2% siap.<br>
                - Oksimetri terpasang aktif.
            </td>
            <td>
                <b>[ &nbsp; ] Konfirmasi Anggota Tim Bedah:</b><br>
                - Seluruh tim medis menyebutkan nama dan peran masing-masing.<br><br>
                <b>[ &nbsp; ] Verbal Konfirmasi (Time Out):</b><br>
                - Nama Pasien: .......................................<br>
                - Prosedur Tindakan: ..........................<br>
                - Lokasi Sisi Sayatan: .........................<br><br>
                <b>[ &nbsp; ] Antisipasi Kejadian Kritis:</b><br>
                - <i>Dokter:</i> Langkah antisipasi perdarahan siap.<br>
                - <i>Perawat:</i> Sterilitas alat bedah set terverifikasi (OK).
            </td>
            <td>
                <b>[ &nbsp; ] Konfirmasi Verbal Perawat/Dokter:</b><br>
                - [ &nbsp; ] Prosedur tercatat secara tertulis.<br>
                - [ &nbsp; ] Hitungan Instrumen, Jarum Hecting, dan Kasa Medis: **LENGKAP & PAS** (tidak ada tertinggal).<br>
                - [ &nbsp; ] Spesimen patologi anatomi telah dilabeli identitas benar.<br><br>
                <b>[ &nbsp; ] Instruksi Pemulihan (Post-Op):</b><br>
                - Dokter menuliskan instruksi pasca bedah, manajemen nyeri, dan jadwal kontrol di lembar CPPT/Resume.
            </td>
        </tr>
        <tr>
            <td class="text-center"><b>Tanda Tangan Perawat</b><br><br><br>...........................................</td>
            <td class="text-center"><b>Tanda Tangan Dokter</b><br><br><br>...........................................</td>
            <td class="text-center"><b>Tanda Tangan Dokter</b><br><br><br>...........................................</td>
        </tr>
    </table>
"""

# 14. Asesmen Pencegahan Risiko Jatuh (PMKP 2)
risiko_jatuh_content = """
    <div class="doc-title">SPO DAN ASESMEN PENCEGAHAN PASIEN JATUH</div>
    <div class="text-center" style="font-weight: bold; margin-bottom: 20px;">APLIKASI DI RAWAT JALAN & RAWAT INAP (DEWASA & ANAK)</div>
    
    <div class="section-title">A. STANDAR PROSEDUR OPERASIONAL (SPO) PENCEGAHAN RISIKO JATUH</div>
    <p>1. Lakukan skrining risiko jatuh visual pada seluruh pasien rawat jalan kontak pertama menggunakan metode get-up-and-go test.<br>
    2. Lakukan asesmen risiko jatuh komprehensif pada pasien rawat inap menggunakan **Skala Morse** (Dewasa) atau **Humpty Dumpty** (Anak) secara berkala.<br>
    3. Terapkan protokol pencegahan jatuh tinggi: pasang klip gelang warna KUNING, naikkan pagar pengaman bed tidur rawat inap, pastikan roda bed dalam posisi terkunci, dampingi pasien saat ke toilet.</p>
    
    <div class="section-title">B. ASESMEN RISIKO JATUH DEWASA (SKALA MORSE / MORSE FALL SCALE)</div>
    <table>
        <tr>
            <th>No</th>
            <th>Faktor Risiko Jatuh</th>
            <th>Skala Penilaian Klinis</th>
            <th>Skor Pasien</th>
        </tr>
        <tr>
            <td class="text-center">1</td>
            <td>Riwayat jatuh dalam 3 bulan terakhir</td>
            <td>Tidak (0) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Ya (25)</td>
            <td></td>
        </tr>
        <tr>
            <td class="text-center">2</td>
            <td>Diagnosis medis sekunder (&gt; 1 diagnosa aktif)</td>
            <td>Tidak (0) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Ya (15)</td>
            <td></td>
        </tr>
        <tr>
            <td class="text-center">3</td>
            <td>Alat bantu jalan (kruk/tongkat/kursi)</td>
            <td>Mandiri (0) &nbsp;&nbsp;&nbsp;&nbsp; Tongkat/Kruk (15) &nbsp;&nbsp;&nbsp;&nbsp; Kursi (30)</td>
            <td></td>
        </tr>
        <tr>
            <td class="text-center">4</td>
            <td>Terpasang cairan infus IV / obat penenang</td>
            <td>Tidak (0) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Ya (20)</td>
            <td></td>
        </tr>
        <tr>
            <td class="text-center">5</td>
            <td>Gaya berjalan / mobilitas</td>
            <td>Normal (0) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Lemah/Limbung (10) &nbsp;&nbsp;&nbsp;&nbsp; Terbatas (20)</td>
            <td></td>
        </tr>
        <tr>
            <td class="text-center">6</td>
            <td>Status mental pasien</td>
            <td>Sadar keterbatasan (0) &nbsp;&nbsp;&nbsp;&nbsp; Lupa keterbatasan/Agitasi (15)</td>
            <td></td>
        </tr>
        <tr>
            <th colspan="3" class="text-right">TOTAL SKOR MORSE</th>
            <td></td>
        </tr>
    </table>
    <p><b>Kategori Risiko:</b><br>
    - **0 - 24:** Risiko Rendah (Pencegahan jatuh standar, edukasi keluarga).<br>
    - **25 - 44:** Risiko Sedang (Pasang penanda segitiga kuning di bed, pastikan bel dekat).<br>
    - **&ge; 45:** Risiko Tinggi (Wajib pasangkan gelang kuning, kunci roda bed, dampingi total ke toilet).</p>
"""

# 15. Kebijakan & Program PPI (PMKP 3)
ppi_program_content = """
    <div class="doc-title">PROGRAM KERJA PENCEGAHAN DAN PENGENDALIAN INFEKSI (PPI)</div>
    <div class="text-center" style="font-weight: bold; margin-bottom: 20px;">KLINIK KELUARGA SEHAT - TAHUN 2026</div>
    
    <div class="section-title">A. PROGRAM KERJA UTAMA PPI SESUAI KEWASPADAAN STANDAR</div>
    <p><b>1. Kebersihan Tangan & Alat Pelindung Diri (APD)</b><br>
    Penyediaan sarana cuci tangan dan handrub di seluruh unit pelayanan. Penyediaan APD standar (masker medis, apron plastik pelindung badan, sarung tangan steril/non-steril).</p>
    
    <p><b>2. Dekontaminasi & Sterilisasi Peralatan Pasien</b><br>
    Penerapan desinfeksi dan sterilisasi autoklaf alat bedah minor gigi/medis secara sistematis.</p>
    
    <p><b>3. Penatalaksanaan Linen & Kebersihan Lingkungan</b><br>
    Linen kotor wajib dikumpulkan dalam wadah tertutup terpisah (linen infeksius plastik kuning, linen non-infeksius plastik hitam) untuk dicuci menggunakan cairan desinfektan klorin di ruang pencucian khusus.</p>
    
    <p><b>4. Perlindungan Kesehatan Petugas & Needle-Stick Injury</b><br>
    - **Program Imunisasi:** Staf medis wajib mendapatkan vaksinasi Hepatitis B lengkap secara berkala.<br>
    - **Pencegahan Tusukan Jarum Bekas:** Dilarang keras melakukan penutupan jarum suntik bekas secara dua tangan (strict no-recapping). Lakukan teknik satu tangan (*one-hand recapping*) dalam keadaan darurat medis, dan segera buang jarum suntik bekas ke dalam wadah baja/plastik tebal tahan tusukan (*safety box*).</p>
    
    <p><b>5. Penempatan Pasien & Etika Batuk</b><br>
    Isolasi sementara bagi pasien penularan infeksi airborne di ruang tunggu batuk terpisah yang berventilasi baik. Penyediaan masker bedah bagi pasien batuk.</p>
    
    <div class="section-title">B. SPO CUCI TANGAN 6 LANGKAH & 5 MOMEN (WHO HAND HYGIENE STANDARDS)</div>
    <p><b>5 MOMEN WAJIB CUCI TANGAN PETUGAS MEDIS (5 Moments):</b><br>
    1. Sebelum menyentuh pasien.<br>
    2. Sebelum melakukan tindakan aseptik/bersih.<br>
    3. Setelah terpapar cairan tubuh pasien.<br>
    4. Setelah menyentuh pasien.<br>
    5. Setelah menyentuh lingkungan sekitar pasien.</p>
    
    <p><b>6 LANGKAH CUCI TANGAN (WHO Standards):</b><br>
    1. Gosok kedua telapak tangan secara lembut dengan arah memutar.<br>
    2. Gosok punggung tangan kiri dengan telapak tangan kanan (lakukan bergantian).<br>
    3. Gosok sela-sela jari tangan secara menyeluruh hingga bersih.<br>
    4. Bersihkan ujung jari secara bergantian dengan posisi saling mengunci.<br>
    5. Gosok ibu jari kiri berputar dalam genggaman tangan kanan (lakukan bergantian).<br>
    6. Gosokkan memutar ujung jari-jari tangan kanan di telapak tangan kiri (lakukan bergantian).</p>
"""

# ----------------- NEW PKP TEMPLATES (6-15) -----------------

# 16. Program Promotif Preventif (PKP 6)
promotif_preventif_content = """
    <div class="doc-title">PROGRAM PELAYANAN PROMOTIF DAN PREVENTIF</div>
    <div class="text-center" style="font-weight: bold; margin-bottom: 20px;">KLINIK KELUARGA SEHAT - TAHUN 2026</div>
    
    <div class="section-title">A. TARGET PROGRAM PRIORITAS NASIONAL (PROPRINAS)</div>
    <p>Klinik menyusun program bulanan untuk berpartisipasi aktif dalam mendukung program prioritas nasional sektor kesehatan:</p>
    <ol>
        <li><b>Pencegahan dan Penatalaksanaan Tuberkulosis (TB):</b> Menyediakan ruang skrining batuk ber-ventilasi baik, berpartisipasi dalam penemuan kasus aktif melalui rujukan sampel dahak TCM ke Puskesmas, pencatatan di aplikasi SITB resmi Kemenkes.</li>
        <li><b>Pencegahan Penularan HIV/AIDS:</b> Edukasi sukarela kelompok berisiko (VCT/PITC), rujukan tes antibodi HIV terintegrasi (SIHA Kemenkes).</li>
        <li><b>Pencegahan Stunting dan Wasting Anak:</b> Melakukan posyandu balita dampingan berkala, edukasi gizi ASI eksklusif, PMT (Pemberian Makanan Tambahan) lokal.</li>
        <li><b>Kesehatan Ibu dan Anak (KIA):</b> Pemeriksaan ANC terpadu menggunakan USG dasar terakreditasi, program imunisasi bayi dasar lengkap.</li>
    </ol>
    
    <div class="section-title">B. FORMULIR PENCATATAN BULANAN PROGRAM TB-SITB & IMUNISASI</div>
    <table>
        <tr>
            <th>Bulan</th>
            <th>Jumlah Skrining Suspek TB</th>
            <th>Pasien TB Terkonfirmasi (BTA+)</th>
            <th>Pasien TB Mulai OAT</th>
            <th>Capaian Imunisasi Bayi</th>
            <th>Jumlah Edukasi Kelompok</th>
            <th>Status Pelaporan SITB/SIHA</th>
        </tr>
        <tr>
            <td class="text-center">Januari 2026</td>
            <td class="text-center">15 Orang</td>
            <td class="text-center">2 Orang</td>
            <td class="text-center">2 Orang</td>
            <td class="text-center">8 Bayi</td>
            <td class="text-center">1 Sesi (15 peserta)</td>
            <td class="text-center" style="color:green; font-weight:bold;">Selesai SITB</td>
        </tr>
        <tr>
            <td class="text-center">Februari 2026</td>
            <td class="text-center">10 Orang</td>
            <td class="text-center">0</td>
            <td class="text-center">0</td>
            <td class="text-center">12 Bayi</td>
            <td class="text-center">2 Sesi (25 peserta)</td>
            <td class="text-center" style="color:green; font-weight:bold;">Selesai SITB</td>
        </tr>
    </table>
"""

# 17. SPO Pelayanan Pasien Risiko Tinggi (PKP 7)
risiko_tinggi_content = """
    <div class="doc-title">STANDAR PROSEDUR OPERASIONAL (SPO) PELAYANAN PASIEN RISIKO TINGGI</div>
    
    <div class="section-title">A. KEBIJAKAN IDENTIFIKASI PASIEN RISIKO TINGGI</div>
    <p>Klinik Keluarga Sehat menetapkan kategori pasien risiko tinggi yang mampu ditangani di fasilitas primer klinik:</p>
    <ul>
        <li><b>Pasien Emergensi Gawat Darurat:</b> Pasien dengan ancaman henti napas/jantung, syok anafilaktik, perdarahan hebat, atau fraktur terbuka wajib ditangani di UGD tanpa hambatan administrasi.</li>
        <li><b>Pasien Penyakit Menular Airbone / Droplet (TBC Aktif, Covid-19):</b> Wajib diberikan masker bedah medis, didudukkan di ruang tunggu luar terpisah, diperiksa oleh dokter ber-APD level 2.</li>
        <li><b>Populasi Pasien Rentan (Lansia, Anak, Korban Kekerasan):</b> Berikan prioritas antrean, pastikan didampingi wali sah, cegah risiko tindak kekerasan, diskriminasi, eksploitasi, atau penelantaran di area klinik.</li>
        <li><b>Pasien dengan Risiko Bunuh Diri:</b> Dilakukan skrining kesehatan mental dasar (metode PHQ-9). Jika teridentifikasi risiko bunuh diri sedang/tinggi, amankan pasien dari alat tajam/koridor tinggi, dampingi terus oleh perawat, dan rujuk segera ke Rumah Sakit dengan layanan psikiatri.</li>
        <li><b>Koordinasi Layanan Dialisis & Kemoterapi:</b> Klinik tidak melakukan tindakan cuci darah (dialisis) atau kemoterapi secara mandiri di tingkat primer. Klinik berperan melakukan monitoring klinis berkala pasca tindakan dari RS rujukan, mengelola efek samping ringan obat kemoterapi oral, serta mengoordinasikan jadwal rujukan ulang terencana pasien ke RS tipe B/A mitra.</li>
    </ul>
    
    <div class="section-title">B. SPO PELAYANAN PASIEN GAWAT DARURAT (EMERGENSI) DI UGD</div>
    <p>1. Petugas triase UGD menerima pasien dan melakukan triase visual cepat (Merah/Kuning/Hijau).<br>
    2. Pasien kategori Merah langsung dibaringkan di bed resusitasi. Dokter UGD segera memimpin penanganan emergensi.<br>
    3. Pasang pulse oksimetri, lakukan oksigenasi masker nasal kanul 3-4 Lpm atau NRM 10 Lpm sesuai kebutuhan. Pasang jalur infus IV cairan NaCl 0.9% makro.<br>
    4. Lakukan penanganan primer (Airway, Breathing, Circulation). Petugas pendaftaran mengurus administrasi setelah pasien dalam kondisi klinis stabil.<br>
    5. Jika kondisi pasien tidak membaik dalam 30 menit atau membutuhkan ICU, siapkan rujukan ambulans segera ke RS jejaring sesuai SPO Rujukan.</p>
"""

# 18. SPO Anestesi Bedah Minor (PKP 8)
anestesi_bedah_content = """
    <div class="doc-title">STANDAR PROSEDUR OPERASIONAL (SPO) ANESTESI LOKAL DAN BEDAH MINOR</div>
    
    <div class="section-title">A. TAHAPAN PROSEDUR ANESTESI LOKAL DAN BEDAH MINOR</div>
    <p>1. **Kajian Pra-Bedah & Pra-Anestesi:** Lakukan anamnesis alergi obat anestesi (lidokain), ukur TTV (tensi wajib &lt; 140/90 mmHg), periksa riwayat perdarahan/koagulopati.<br>
    2. **Informed Consent:** Berikan penjelasan risiko nyeri pasca bedah, perdarahan, infeksi sekunder, tanda tangani formulir persetujuan medis.<br>
    3. **Penandaan Lokasi (Marking):** Tandai sisi operasi menggunakan spidol penanda kulit tahan air bersama pasien.<br>
    4. **Infiltrasi Anestesi Lokal:** Lakukan penyuntikan Lidocain 2% subkutis di sekitar tepi luka secara melingkar (infiltrasi). Tunggu 3-5 menit hingga baal.<br>
    5. **Tindakan Bedah Kecil:** Lakukan pembersihan debridement luka dengan NaCl, lakukan penjahitan (hecting) kulit/subkutis secara steril.<br>
    6. **Edukasi & Pemantauan:** Pantau tanda vital pasca tindakan, berikan resep analgetik/antibiotik, edukasi luka tidak boleh terkena air kotor.</p>
    
    <div class="section-title">B. FORMULIR KAJIAN PRA-ANESTESI & PRA-BEDAH TERINTEGRASI</div>
    <p><b>Nama Pasien:</b> ........................................................ &nbsp;&nbsp;&nbsp;&nbsp; <b>No. Rekam Medis:</b> ..............................................<br>
    <b>Tgl / Jam Tindakan:</b> ................................................ &nbsp;&nbsp;&nbsp;&nbsp; <b>Jenis Tindakan Bedah:</b> ..........................................</p>
    
    <table>
        <tr>
            <th colspan="2" style="background-color:#eaeaea; font-weight:bold;">I. KAJIAN PRA-ANESTESI (LOKAL)</th>
            <th colspan="2" style="background-color:#eaeaea; font-weight:bold;">II. KAJIAN PRA-BEDAH (MINOR)</th>
        </tr>
        <tr>
            <td style="width:25%;"><b>Tanda-Tanda Vital</b></td>
            <td style="width:25%;">TD: ........ mmHg &nbsp;&nbsp; Nadi: ........ x/m<br>Suhu: ........ C &nbsp;&nbsp; Napas: ........ x/m</td>
            <td style="width:25%;"><b>Diagnosis Pra-Bedah</b></td>
            <td style="width:25%;">....................................................................</td>
        </tr>
        <tr>
            <td><b>Riwayat Alergi Obat</b></td>
            <td>[ &nbsp; ] Tidak Ada<br>[ &nbsp; ] Ada, sebutkan: .........................</td>
            <td><b>Rencana Tindakan Bedah</b></td>
            <td>....................................................................</td>
        </tr>
        <tr>
            <td><b>Riwayat Penyakit</b></td>
            <td>[ &nbsp; ] DM &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [ &nbsp; ] Asma<br>[ &nbsp; ] Hipertensi &nbsp;&nbsp; [ &nbsp; ] Jantung</td>
            <td><b>Sisi Penandaan Operasi</b></td>
            <td>[ &nbsp; ] Sudah ditandai (O/X spidol)<br>[ &nbsp; ] Tidak diperlukan</td>
        </tr>
        <tr>
            <td><b>Status Fisiologis Pra-Tindakan</b></td>
            <td>[ &nbsp; ] ASA I (Normal)<br>[ &nbsp; ] ASA II (Ringan)</td>
            <td><b>Jenis Anestesi Direncanakan</b></td>
            <td>Lidocain 2% secara infiltrasi lokal</td>
        </tr>
    </table>
"""

# 19. Asuhan & Edukasi Gizi (PKP 9)
gizi_content = """
    <div class="doc-title">DOKUMEN ASUHAN GIZI & CATATAN EDUKASI DIET PASIEN</div>
    <div class="text-center" style="font-weight: bold; margin-bottom: 20px;">KLINIK KELUARGA SEHAT - TAHUN 2026</div>
    
    <div class="section-title">A. SPO PELAYANAN ASUHAN GIZI RAWAT INAP</div>
    <p>1. **Skrining Gizi Awal:** Dilakukan oleh perawat rawat inap saat pasien masuk menggunakan metode MST (Malnutrition Screening Tool) &le; 24 jam.<br>
    2. **Pemesanan Makanan (Diet):** Perawat menuliskan instruksi pemesanan diet ke tim gizi sesuai advis dokter DPJP.<br>
    3. **Penyediaan & Distribusi:** Makanan disediakan secara higienis, didistribusikan sesuai jadwal regular (Pagi 07.00, Siang 12.00, Malam 18.00).<br>
    4. **Edukasi Gizi Pasien:** Ahli gizi/perawat memberikan edukasi pembatasan diet makanan pembawa luar oleh keluarga demi kelancaran pemulihan.<br>
    5. **PENCEGAHAN KONTAMINASI MAKANAN DARI LUAR:**<br>
    Apabila keluarga pasien membawa makanan sendiri dari luar klinik (atas seizin dan sepengetahuan Ahli Gizi / PPA yang merawat):<br>
    &nbsp;&nbsp;&nbsp;&nbsp;a. Makanan wajib disimpan dalam wadah tertutup rapat dan higienis.<br>
    &nbsp;&nbsp;&nbsp;&nbsp;b. Berikan label penanda identitas pasien (Nama & No RM) pada wadah makanan.<br>
    &nbsp;&nbsp;&nbsp;&nbsp;c. Letakkan makanan pada kulkas penyimpanan khusus makanan pasien rawat inap yang telah disediakan di pantry.<br>
    &nbsp;&nbsp;&nbsp;&nbsp;d. Bersihkan dan buang makanan dari luar yang telah melebihi batas waktu 24 jam untuk mencegah tumbuhnya bakteri kontaminan.</p>
    
    <div class="section-title">B. FORMULIR ASUHAN GIZI & DIET PASIEN (MST)</div>
    <p><b>Nama Pasien:</b> ........................................................ &nbsp;&nbsp;&nbsp;&nbsp; <b>No. Rekam Medis:</b> ..............................................<br>
    <b>Tgl Masuk:</b> ............................................................. &nbsp;&nbsp;&nbsp;&nbsp; <b>Diagnosis Medis:</b> .................................................</p>
    
    <table>
        <tr>
            <th>No</th>
            <th>Kriteria Skrining Gizi Awal (MST)</th>
            <th>Pilihan Jawaban Penilaian</th>
            <th>Skor</th>
        </tr>
        <tr>
            <td class="text-center">1</td>
            <td>Apakah pasien mengalami penurunan berat badan secara tidak sengaja dalam 3 bulan terakhir?</td>
            <td>- Tidak (0)<br>- Tidak yakin (2)<br>- Ya, ada penurunan 1-5 kg (1) / 6-10 kg (2) / &gt;15 kg (4)</td>
            <td></td>
        </tr>
        <tr>
            <td class="text-center">2</td>
            <td>Apakah asupan makanan menurun karena tidak nafsu makan?</td>
            <td>- Tidak (0)<br>- Ya (1)</td>
            <td></td>
        </tr>
        <tr>
            <th colspan="3" class="text-right">TOTAL SKOR MST</th>
            <td></td>
        </tr>
    </table>
    <p><b>Tindak Lanjut Skor MST:</b><br>
    - **Skor &lt; 2:** Risiko Malnutrisi Rendah (Asuhan gizi standar, evaluasi ulang 3 hari sekali).<br>
    - **Skor &ge; 2:** Risiko Malnutrisi Sedang/Tinggi (Konsultasikan ke Ahli Gizi untuk penyusunan rencana asuhan gizi spesifik).</p>
"""

# 20. Resume Medis Kriteria Pulang (PKP 10)
resume_medis_content = """
    <div class="doc-title">RESUME MEDIS PASIEN PULANG (DISCHARGE SUMMARY)</div>
    <div class="text-center" style="font-weight: bold; margin-bottom: 20px;">KLINIK KELUARGA SEHAT - TAHUN 2026</div>
    
    <table style="width:100%; border:1px solid #000; margin-bottom:15px;">
        <tr>
            <td style="width:50%;">
                <b>Nama Pasien:</b> ........................................................<br>
                <b>No. Rekam Medis:</b> ...............................................<br>
                <b>Jenis Kelamin / Umur:</b> L / P &nbsp;&nbsp; .......... Tahun
            </td>
            <td style="width:50%;">
                <b>Tanggal Masuk Rawat:</b> ......................................<br>
                <b>Tanggal Keluar / Pulang:</b> ..................................<br>
                <b>Dokter Penanggung Jawab (DPJP):</b> dr. .......................
            </td>
        </tr>
    </table>
    
    <div class="section-title">A. BATAS MAKSIMAL RAWAT INAP KLINIK SESUAI REGULASI NASIONAL</div>
    <p style="background-color:#ffe5cc; padding:8px; border:1px solid #ff9900; font-weight:bold; font-size:9.5pt;">
        ⚠️ PENTING: Sesuai dengan regulasi akreditasi nasional, klinik hanya dapat memberikan pelayanan rawat inap paling lama 5 (lima) hari. Apabila memerlukan rawat inap lebih dari 5 hari, maka pasien harus secara terencana dirujuk ke Rumah Sakit yang bermitra.
    </p>
    
    <div class="section-title">B. RINGKASAN KLINIS PASIEN</div>
    <p><b>1. Keluhan Utama saat Masuk:</b> ..............................................................................................................................................<br>
    <b>2. Temuan Fisik & Penunjang Penting (Lab/Ekg):</b> ............................................................................................................................<br>
    <b>3. Diagnosis Utama (Akhir):</b> .................................................... <b>Diagnosis Sekunder:</b> .............................................................<br>
    <b>4. Tindakan Medis / Bedah Minor:</b> .............................................................................................................................</p>
    
    <div class="section-title">C. TERAPI OBAT PULANG & ATURAN PAKAI</div>
    <table>
        <tr>
            <th>No</th>
            <th>Nama Obat Pulang</th>
            <th>Dosis Obat (mg/ml)</th>
            <th>Frekuensi Minum</th>
            <th>Rute</th>
            <th>Jumlah</th>
            <th>Aturan Minum (Habiskan/prn)</th>
        </tr>
        <tr>
            <td class="text-center">1</td>
            <td>Amoxicillin 500 mg</td>
            <td class="text-center">500 mg</td>
            <td class="text-center">3 x 1 Tablet</td>
            <td class="text-center">Oral</td>
            <td class="text-center">10 Tablet</td>
            <td>Wajib DIHABISKAN (Antibiotik).</td>
        </tr>
        <tr>
            <td class="text-center">2</td>
            <td>Paracetamol 500 mg</td>
            <td class="text-center">500 mg</td>
            <td class="text-center">3 x 1 Tablet</td>
            <td class="text-center">Oral</td>
            <td class="text-center">10 Tablet</td>
            <td>Diminum bila demam / nyeri (prn).</td>
        </tr>
    </table>
    
    <div class="section-title">D. INSTRUKSI PASCA PULANG (EDUKASI KONTROL)</div>
    <p>1. **Jadwal Kontrol Poli:** Hari/Tanggal ............................................................ Pukul ............... WIB.<br>
    2. **Kondisi Emergensi Segera ke UGD jika:** Mengalami demam mendadak tinggi, perdarahan hebat pada luka, muntah berulang, sesak napas berat.</p>
    
    <table class="signature-table" style="margin-top: 30px;">
        <tr>
            <td>
                Pasien / Keluarga Penerima Penjelasan,<br><br><br><br>
                ( <b>................................................</b> )
            </td>
            <td>
                Jakarta, Tgl ................................ Jam ...........<br>
                Dokter Penanggung Jawab (DPJP),<br><br><br><br>
                ( <b>dr. ........................................</b> )<br>
                SIP. ............................................
            </td>
        </tr>
    </table>
"""

# 21. Surat Rujukan & MoU Ambulans (PKP 11)
surat_rujukan_content = """
    <div class="doc-title">SURAT RUJUKAN PASIEN KELUAR / ANTAR FASYANKES</div>
    <div class="text-center" style="font-weight: bold; margin-bottom: 20px;">NOMOR: 095/SRU/MED/2026</div>
    
    <p><b>Kepada Yth. Dokter Spesialis / DPJP UGD</b><br>
    <b>Fasilitas Rujukan Penerima:</b> RSUD Jakarta Selatan<br>
    Dengan hormat, bersama surat ini kami rujuk pasien demi kelangsungan pelayanan medis komprehensif lebih lanjut:</p>
    
    <table style="width:100%; border:1px solid #000; margin-bottom:15px;">
        <tr>
            <td style="width:50%;">
                <b>Nama Lengkap Pasien:</b> ....................................................<br>
                <b>No. Rekam Medis:</b> ...................................................<br>
                <b>Jenis Kelamin / Umur:</b> L / P &nbsp;&nbsp; .......... Tahun
            </td>
            <td style="width:50%;">
                <b>Alamat Lengkap:</b> ........................................................<br>
                <b>Masa Asuransi / BPJS:</b> Umum / BPJS No. ....................<br>
                <b>Tanggal / Jam Dirujuk:</b> ......................... Pukul ............ WIB
            </td>
        </tr>
    </table>
    
    <div class="section-title">A. RESUME DATA KLINIS PASIEN SAAT DIKIRIM</div>
    <p><b>1. Anamnesis Ringkas & Keluhan:</b> ..............................................................................................................................................<br>
    <b>2. Hasil Pemeriksaan Fisik Terkini:</b> Tensi: ......... mmHg, Nadi: ......... x/m, Suhu: ......... C, Napas: ......... x/m, SpO2: ......... %.<br>
    <b>3. Hasil Laboratorium / Penunjang Terlampir:</b> ................................................................................................................................<br>
    <b>4. Tindakan Medis Sementara di Klinik:</b> .......................................................................................................................................<br>
    <b>5. Diagnosis Kerja Utama:</b> ..............................................................................................................................................................<br>
    <b>6. Alasan Rujukan Keluar:</b> [ &nbsp; ] Kompetensi Dokter Spesialis Tidak Tersedia &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [ &nbsp; ] ICU/Fasilitas Rawat Inap Penuh</p>
    
    <table class="signature-table" style="margin-top: 30px;">
        <tr>
            <td>
                Persetujuan Keluarga Pasien,<br><br><br><br>
                ( <b>................................................</b> )
            </td>
            <td>
                Jakarta, Tgl ................................ Jam ...........<br>
                Dokter Klinik yang Merujuk,<br><br><br><br>
                ( <b>dr. ........................................</b> )<br>
                SIP. ............................................
            </td>
        </tr>
    </table>

    <div style="page-break-before: always;"></div>
    
    <div style="font-weight:bold; text-align:center; text-transform:uppercase;">LAMPIRAN: MOU PENYEDIAAN MOBIL AMBULANS TRANSPORTASI RUJUKAN</div>
    <hr style="border-top:1px solid #000; margin-bottom:15px;">
    
    <p><b>Dasar Kerja Sama Ambulans Rekanan (Apabila Klinik Belum Memiliki Unit Mandiri):</b><br>
    Klinik Keluarga Sehat bersepakat mengadakan perjanjian penyediaan sarana transportasi rujukan medis darurat (Ambulans) 24 Jam dengan **Yayasan Ambulans Gawat Darurat Indonesia (AGD Jakarta)**. Ambulans rekanan wajib memenuhi persyaratan kelengkapan medis minimal (oksigen sentral, monitor TTV portable, DC Shock portable, obat emergensi dasar, resusitator kit) dan dipandu oleh 1 perawat tersertifikasi PPGD/BTCLS aktif pendamping rujukan luar fasyankes.</p>
"""

# 22. SPO Pengelolaan Rekam Medis (PKP 12)
pengelolaan_rm_content = """
    <div class="doc-title">SPO TATA CARA PENYIMPANAN, PEMINJAMAN, DAN PEMUSNAHAN REKAM MEDIS</div>
    
    <div class="section-title">A. SPO PENYIMPANAN REKAM MEDIS & KERAHASIAAN</div>
    <p>1. Rekam Medis Elektronik (RME) disimpan pada server lokal klinik ter-enkripsi aman dengan sistem backup cloud mingguan.<br>
    2. Akses RME dilindungi password pribadi untuk setiap PPA. Staf dilarang keras membagikan password login SIM-Klinik.<br>
    3. Rekam Medis Fisik diletakkan pada lemari penyimpanan terkunci di ruang khusus rekam medis yang terisolasi. Pintu ruang RM wajib terkunci 24 jam selain petugas rekam medis resmi.</p>
    
    <div class="section-title">B. TATA CARA PEMBETULAN KESALAHAN PENCATATAN REKAM MEDIS</div>
    <p style="background-color:#ffffcc; padding:8px; border:1px solid #e6b800; font-weight:bold; font-size:9.5pt;">
        ⚠️ ATURAN PEMBETULAN PENULISAN (PMK 24/2022):<br>
        1. Dilarang keras menghapus, menutup tulisan asli dengan cairan koreksi (tip-ex/correction fluid), menyobek, atau melaminasi rekam medis yang salah tulis.<br>
        2. Pembetulan kesalahan pencatatan hanya dilakukan dengan <b>mencoret sekali (misal: <strike>salah tulis</strike>) tanpa menghilangkan/mengaburkan tulisan asli</b>.<br>
        3. Bubuhkan paraf PPA (Dokter/Perawat) yang melakukan pembetulan tepat di atas atau di samping coretan beserta keterangan waktu koreksi.
    </p>
    
    <div class="section-title">C. SPO PEMINJAMAN BERKAS REKAM MEDIS</div>
    <p>1. Peminjaman berkas rekam medis fisik hanya diizinkan untuk kepentingan pelayanan asuhan medis langsung pasien di klinik, kepentingan hukum/pengadilan (advis Kepala Klinik), atau kepentingan pendidikan internal.<br>
    2. Peminjam wajib mengisi Formulir Buku Peminjaman RM. Berkas wajib dikembalikan ke rak penyimpanan semula &le; 24 jam kerja.</p>
    
    <div class="section-title">D. SPO RETENSI & PEMUSNAHAN REKAM MEDIS</div>
    <p>1. Rekam medis wajib disimpan sekurang-kurangnya untuk jangka waktu **2 (dua) tahun** terhitung dari tanggal terakhir pasien berobat/berkunjung.<br>
    2. Lakukan retensi (pemindahan berkas aktif ke inaktif) setelah 2 tahun tanpa kunjungan.<br>
    3. Setelah berkas dinyatakan inaktif selama 2 tahun lanjutan, berkas rekam medis dapat dimusnahkan secara aman menggunakan mesin penghancur kertas dokumen atau dibakar habis yang dibuktikan dengan Berita Acara Pemusnahan.</p>
    
    <div class="section-title">E. FORMULIR BUKU KENDALI PEMINJAMAN BERKAS REKAM MEDIS</div>
    <table>
        <tr>
            <th>Tanggal Peminjaman</th>
            <th>No. Rekam Medis</th>
            <th>Nama Pasien</th>
            <th>Peminjam (Nama/Poli)</th>
            <th>Tujuan Peminjaman</th>
            <th>Tanggal Pengembalian</th>
            <th>Paraf Petugas RM</th>
        </tr>
        <tr>
            <td class="text-center">10/04/2026</td>
            <td class="text-center">00-33-21</td>
            <td>Tn. Suprapto</td>
            <td>Ns. Ani (Poli Gigi)</td>
            <td>Pelayanan asuhan tambal gigi</td>
            <td class="text-center">10/04/2026</td>
            <td class="text-center"><br>Rudi</td>
        </tr>
    </table>
"""

# 23. SPO Pelayanan Laboratorium & Nilai Kritis (PKP 13)
pelayanan_lab_content = """
    <div class="doc-title">SPO PELAPORAN HASIL LABORATORIUM KRITIS (NILAI KRITIS)</div>
    
    <div class="section-title">A. REGISTER JENIS PEMERIKSAAN LABORATORIUM & RENTANG NILAI NORMAL</div>
    <p>Klinik menyelenggarakan pelayanan pemeriksaan laboratorium penunjang berikut:</p>
    <table>
        <tr>
            <th>No</th>
            <th>Jenis Pemeriksaan Laboratorium</th>
            <th>Spesimen / Sampel</th>
            <th>Rentang Nilai Normal (Rujukan)</th>
            <th>Jangka Waktu Hasil Jadi (TAT)</th>
            <th>Kategori Nilai Kritis (Wajib Lapor)</th>
        </tr>
        <tr>
            <td class="text-center">1</td>
            <td><b>Hemoglobin (Hb)</b></td>
            <td>Darah EDTA</td>
            <td>Pria: 13-17 g/dL<br>Wanita: 12-15 g/dL</td>
            <td class="text-center">30 Menit</td>
            <td class="text-center" style="font-weight:bold; color:red;">&lt; 7.0 g/dL atau &gt; 20.0 g/dL</td>
        </tr>
        <tr>
            <td class="text-center">2</td>
            <td><b>Gula Darah Sewaktu (GDS)</b></td>
            <td>Darah Kapiler</td>
            <td>&lt; 140 mg/dL</td>
            <td class="text-center">15 Menit</td>
            <td class="text-center" style="font-weight:bold; color:red;">&lt; 40 mg/dL atau &gt; 400 mg/dL</td>
        </tr>
        <tr>
            <td class="text-center">3</td>
            <td><b>Waktu Pembekuan (Clotting Time)</b></td>
            <td>Darah Segar</td>
            <td>2 - 6 Menit</td>
            <td class="text-center">20 Menit</td>
            <td class="text-center" style="font-weight:bold; color:red;">&gt; 15 Menit</td>
        </tr>
    </table>
    
    <div class="section-title">B. SPO PELAPORAN HASIL LABORATORIUM KRITIS (NILAI KRITIS)</div>
    <p>1. Jika analis mendapati hasil pemeriksaan masuk kategori Nilai Kritis, **segera lakukan running ulang (recheck)** spesimen tersebut untuk verifikasi internal.<br>
    2. Hubungi langsung PPA/Dokter pengirim pasien via telepon **dalam waktu &le; 15 menit** setelah hasil terverifikasi.<br>
    3. Laporkan nama pasien, no rekam medis, jenis parameter uji, dan angka hasil kritis secara jelas menggunakan komunikasi efektif TBAK.<br>
    4. Dokumentasikan waktu pelaporan hasil kritis pada register nilai kritis laboratorium.</p>
"""

# 24. SPO Pelayanan Radiologi (PKP 14)
pelayanan_radiologi_content = """
    <div class="doc-title">SPO PELAYANAN RADIOLOGI DAN PROTEKSI KEAMANAN RADIASI</div>
    
    <div class="section-title">A. PANDUAN PROTEKSI RADIASI UNTUK STAF DAN PASIEN</div>
    <p>Khusus klinik yang menyelenggarakan pelayanan Radiologi (Rontgen Dental / X-Ray Umum):</p>
    <ul>
        <li><b>Untuk Staf Radiografer:</b> Wajib mengenakan apron pelindung timbal (Pb) tebal minimum 0.25 mm selama pemaparan sinar X. Wajib menggunakan TLD badge personal. Dilarang berada di ruang tembak saat eksposur dilakukan.</li>
        <li><b>Untuk Pasien & Keluarga:</b> Wajib dipasangkan apron Pb pada area gonad/leher (tiroid) jika tidak mengganggu visual rontgen. Tanyakan status kehamilan pada pasien wanita subur.</li>
        <li><b>Lingkungan Fisik:</b> Dinding ruang rontgen wajib dilapisi Pb tebal minimum 2 mm, pintu berlapis timbal lengkap dengan lampu indikator merah menyala saat eksposur berlangsung di atas pintu.</li>
    </ul>
    
    <div class="section-title">B. LOGBOOK PEMELIHARAAN ALAT RADIOLOGI & KALIBRASI</div>
    <table>
        <tr>
            <th>Tanggal Pemeliharaan</th>
            <th>Nama Alat Radiologi</th>
            <th>Merek & No Seri</th>
            <th>Uji Paparan Kebocoran Alat (Lolos/Gagal)</th>
            <th>Masa Berlaku Sertifikat Kalibrasi BPFK</th>
            <th>Masa Berlaku Izin BAPETEN</th>
            <th>Paraf Teknisi</th>
        </tr>
        <tr>
            <td class="text-center">05/01/2026</td>
            <td>X-Ray Dental Panoramic</td>
            <td>Carestream CS8100</td>
            <td class="text-center" style="color:green; font-weight:bold;">Lolos Uji</td>
            <td class="text-center">Hingga 12 Desember 2026</td>
            <td class="text-center">Aktif s.d 2028</td>
            <td class="text-center"><br>BPFK P.</td>
        </tr>
    </table>
"""

# 25. Pelayanan Kefarmasian Lengkap (PKP 15)
kefarmasian_lengkap_content = """
    <div class="doc-title">DOKUMEN INTEGRASI PELAYANAN KEFARMASIAN LENGKAP</div>
    <div class="text-center" style="font-weight: bold; margin-bottom: 20px;">KLINIK KELUARGA SEHAT - TAHUN 2026</div>
    
    <div class="section-title">A. FORMULIR OBAT KLINIK (CONTOH DAFTAR OBAT AKTIF)</div>
    <table>
        <tr>
            <th>No</th>
            <th>Nama Generik Obat</th>
            <th>Kekuatan Sediaan</th>
            <th>Rute Pemberian</th>
            <th>Kategori Obat (LASA / High Alert / Regular)</th>
            <th>Batas Stok Maksimal</th>
        </tr>
        <tr>
            <td class="text-center">1</td>
            <td><b>Lidocain Injeksi 2%</b></td>
            <td>2% ampul @ 2ml</td>
            <td>Infiltrasi Subkutis</td>
            <td class="text-center" style="background-color:#ffe5cc; font-weight:bold;">HIGH ALERT</td>
            <td>50 Ampul</td>
        </tr>
        <tr>
            <td class="text-center">2</td>
            <td><b>Epinefrin Injeksi (Adrenalin)</b></td>
            <td>1 mg/ml ampul</td>
            <td>Intramuskular / IV</td>
            <td class="text-center" style="background-color:#ffcccc; font-weight:bold;">HIGH ALERT (EMERGENCY)</td>
            <td>10 Ampul</td>
        </tr>
        <tr>
            <td class="text-center">3</td>
            <td><b>Amlodipin 5 mg & 10 mg</b></td>
            <td>Tablet 5mg/10mg</td>
            <td>Oral</td>
            <td class="text-center" style="background-color:#ffffcc; font-weight:bold;">LASA (Look Alike)</td>
            <td>200 Tablet</td>
        </tr>
        <tr>
            <td class="text-center">4</td>
            <td><b>Paracetamol 500 mg</b></td>
            <td>Tablet 500 mg</td>
            <td>Oral</td>
            <td class="text-center">Regular</td>
            <td>500 Tablet</td>
        </tr>
    </table>
    
    <div class="section-title">B. FORM LEMBAR REKONSILIASI OBAT RAWAT INAP</div>
    <p>Wajib diisi dalam 24 jam pertama saat pasien dipindahkan antar unit / masuk rawat inap:</p>
    <table>
        <tr>
            <th>Nama Obat dari Rumah / Luar</th>
            <th>Dosis & Rute</th>
            <th>Frekuensi Minum</th>
            <th>Tgl Mulai Minum</th>
            <th>Tindak Lanjut DPJP (Lanjutkan / Stop / Ubah Dosis)</th>
            <th>Nama Obat Baru Klinik (Substitusi)</th>
            <th>Paraf Apoteker</th>
        </tr>
        <tr>
            <td>Amlodipin 10 mg</td>
            <td>10 mg / Oral</td>
            <td>1 x sehari</td>
            <td>10/12/2025</td>
            <td class="text-center" style="font-weight:bold; color:blue;">LANJUTKAN</td>
            <td>Amlodipin 10 mg (Klinik)</td>
            <td class="text-center"><br>Apt. Budi</td>
        </tr>
    </table>
    
    <div class="section-title">C. FORMULIR PELAPORAN EFEK SAMPING OBAT (MESO / KARTU KUNING)</div>
    <p><b>Nama Pasien:</b> ........................................................ &nbsp;&nbsp;&nbsp;&nbsp; <b>No. RM:</b> .....................................................<br>
    <b>Gejala Efek Samping Timbul:</b> ......................................................................................................................<br>
    <b>Nama Obat Diduga Kuat Penyebab:</b> ......................................................................................................................</p>
    
    <div class="section-title">D. BERITA ACARA PEMUSNAHAN OBAT KADALUARSA / RUSAK</div>
    <p>Pada hari ini ................. Tanggal ................. Bulan ................. Tahun 2026, telah dilakukan pemusnahan obat kadaluarsa dan rusak milik Klinik Keluarga Sehat oleh Panitia Pemusnah Farmasi Klinik dengan cara dibakar/dilebur secara aman, disaksikan oleh Dinas Kesehatan setempat.</p>
"""

# Write all template documents
templates = [
    # Phase 1 Templates (PKP 1 - 4)
    ("sk-hak-kewajiban.doc", sk_content, "SK Hak dan Kewajiban Pasien"),
    ("spo-pendaftaran.doc", spo_pendaftaran_content, "SPO Pendaftaran Pasien"),
    ("spo-skrining.doc", spo_skrining_content, "SPO Skrining Pasien"),
    ("informed-consent.doc", informed_consent_content, "Informed Consent"),
    ("form-cppt.doc", form_cppt_content, "Form CPPT"),
    
    # TKK Templates
    ("sk-struktur-organisasi-uraian-tugas.doc", sk_struktur_content, "SK Struktur Organisasi dan Uraian Tugas"),
    ("rencana-sdm-evaluasi-kinerja.doc", rencana_sdm_content, "Rencana SDM dan Evaluasi Kinerja"),
    ("program-mfk-manajemen-risiko.doc", program_mfk_content, "Program MFK dan Manajemen Risiko"),
    ("form-inspeksi-apar-b3.doc", form_apar_b3_content, "Form Inspeksi APAR and B3"),
    ("mou-kontrak-kerja-sama-kpi.doc", mou_kontrak_content, "MoU Kontrak Kerja Sama dan KPI"),
    
    # PMKP Templates
    ("sk-pj-mutu-indikator-risiko.doc", sk_pj_mutu_content, "SK PJ Mutu Indikator Mutu dan Register Risiko"),
    ("spo-identifikasi-komunikasi-efektif.doc", spo_identifikasi_content, "SPO Identifikasi dan Komunikasi SBAR TBAK"),
    ("surgical-safety-checklist.doc", surgical_safety_content, "SPO Bedah Minor dan WHO Surgical Safety Checklist"),
    ("form-pencegahan-risiko-jatuh.doc", risiko_jatuh_content, "Asesmen dan Pencegahan Risiko Jatuh"),
    ("kebijakan-program-ppi.doc", ppi_program_content, "Kebijakan dan Program PPI"),
    
    # PKP Templates (6-15)
    ("program-promotif-preventif.doc", promotif_preventif_content, "Program Promotif Preventif dan Proprinas"),
    ("spo-pelayanan-risiko-tinggi.doc", risiko_tinggi_content, "SPO Pelayanan Pasien Risiko Tinggi"),
    ("spo-anestesi-bedah-minor.doc", anestesi_bedah_content, "SPO Anestesi dan Kajian Bedah Minor"),
    ("asuhan-edukasi-gizi.doc", gizi_content, "Asesmen MST dan Pelayanan Gizi"),
    ("resume-medis-kriteria-pulang.doc", resume_medis_content, "Resume Medis Kriteria Pulang"),
    ("surat-rujukan-mou-ambulans.doc", surat_rujukan_content, "Surat Rujukan Pasien dan MoU Ambulans"),
    ("spo-pengelolaan-rekam-medis.doc", pengelolaan_rm_content, "SPO Pengelolaan dan Retensi Rekam Medis"),
    ("spo-pelayanan-laboratorium.doc", pelayanan_lab_content, "SPO Pelayanan Laboratorium dan Nilai Kritis"),
    ("spo-pelayanan-radiologi.doc", pelayanan_radiologi_content, "SPO Pelayanan Radiologi Keselamatan Radiasi"),
    ("pelayanan-kefarmasian-lengkap.doc", kefarmasian_lengkap_content, "Formulir Obat dan Pelayanan Kefarmasian Lengkap")
]

for filename, content, title in templates:
    full_path = os.path.join(output_dir, filename)
    wrapped_html = get_html_doc_wrapper(title, content)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(wrapped_html)
    print(f"Generated {filename} successfully at {full_path}")

print("\nSuccess! Generated all 25 enriched Word-compatible templates (.doc) in docs/public/templates/")
