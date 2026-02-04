<div align="center">

# 🛡️ AuditSense Pro
### Enterprise Edition

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31%2B-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Status](https://img.shields.io/badge/Status-Production-success?style=for-the-badge)
![Organization](https://img.shields.io/badge/Organization-SPI%20PT%20PAL%20Indonesia-003366?style=for-the-badge)

**Sistem Otomasi Kertas Kerja Audit Internal (KKAI) Berbasis AI.**
<br>
Dikembangkan khusus untuk **Satuan Pengawasan Intern (SPI) - PT PAL Indonesia (Persero)**.

</div>

---

## 📖 Tentang Aplikasi

**AuditSense Pro** adalah platform analitik data tingkat lanjut yang dirancang untuk mengubah proses audit manual menjadi otomatis. Aplikasi ini berfokus pada **Rekonsiliasi Data Anggaran vs Realisasi PO** dengan kecepatan tinggi dan akurasi presisi.

> 🔒 **Security Note:** Aplikasi ini berjalan secara **Lokal (Local Processing)**, menjamin keamanan data keuangan perusahaan tanpa perlu mengunggah data ke *cloud* eksternal.

---

## ✨ Fitur Unggulan

### 1. ⚡ Analisis Performa Tinggi
* Mampu memproses ribuan baris data transaksi dalam hitungan detik.
* Algoritma pembersihan data cerdas (**Smart Cleaning**) yang mampu menangani format angka Excel, spasi, dan karakter non-standar.

### 2. 🎯 Deteksi Anomali Otomatis
* **Over Budget Detection:** Mengidentifikasi akun yang melebihi pagu anggaran secara otomatis.
* **Ghost Expense Detection:** Melacak transaksi PO yang tidak memiliki kode akun valid atau tidak terdaftar di anggaran.

### 3. 🎨 UI/UX Mewah (Enterprise Grade)
* **Glassmorphism Design:** Tampilan modern dengan efek kaca dan gradasi warna.
* **Dark Mode & Light Mode:** Tema yang dapat disesuaikan untuk kenyamanan mata auditor.
* **Smart KPI Cards:** Kartu statistik dengan format angka cerdas (Triliun/Miliar disingkat menjadi `4,7 T`, `10 M`) dilengkapi *Tooltip Instan* untuk melihat angka detail.

### 4. 📊 Laporan Eksekutif Cerdas
* Menghasilkan narasi laporan otomatis berdasarkan temuan data.
* Memberikan rekomendasi tindakan dan menyoroti 3 varians terbesar (*Top Findings*).
* Menampilkan persentase penyerapan anggaran dan status kesehatan keuangan (Sehat/Waspada/Kritis).

### 5. 📥 Ekspor Laporan
* Unduh hasil kerja (**KKA 1**, **KKA 2**, **KKA 2a**) dalam format Excel (`.xlsx`) yang rapi, dengan fitur *auto-width column* dan format akuntansi standar.

---

## 🛠️ Teknologi

| Komponen | Teknologi |
| :--- | :--- |
| **Bahasa Pemrograman** | Python 3.x |
| **Framework UI** | Streamlit |
| **Data Processing** | Pandas, Numpy |
| **Excel Engine** | Openpyxl, XlsxWriter |

---

## 🚀 Cara Menjalankan (Instalasi)

Ikuti langkah-langkah berikut untuk menjalankan aplikasi di komputer lokal Anda:

### 1. Clone Repository
Buka terminal (CMD/Git Bash) dan jalankan:
```bash
git clone https://github.com/SuryoMasduki/AuditSense.git
cd AuditSense
```

### 2. Buat Virtual Environment (Disarankan)
Langkah ini berguna agar instalasi tidak mengganggu Python utama di komputer Anda.

**Untuk Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Untuk Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
Pastikan Anda berada di dalam folder proyek yang memiliki file `requirements.txt`.
```bash
pip install -r requirements.txt
```

### 4. Jalankan Aplikasi
```bash
streamlit run app.py
```
Aplikasi akan otomatis terbuka di browser Anda (biasanya di `http://localhost:8501`).

---

## 📂 Struktur File

```plaintext
AuditSense/
├── .streamlit/
│   └── config.toml      # Konfigurasi tema & server Streamlit
├── logo/                # Folder aset gambar (Logo PAL, BUMN, Icon)
├── app.py               # Kode Utama Aplikasi (v5.4 Enterprise)
├── generate_dummy.py    # Script Python untuk membuat data dummy testing
├── requirements.txt     # Daftar library Python yang dibutuhkan
├── README.md            # Dokumentasi Proyek ini
└── .gitignore           # Daftar file yang diabaikan oleh Git
```

---

## 🧪 Testing dengan Data Dummy

Jika Anda belum memiliki data asli, Anda dapat membuat data simulasi untuk mencoba fitur aplikasi:

1. Buka terminal di folder proyek.
2. Jalankan perintah:
   ```bash
   python generate_dummy.py
   ```
3. Akan muncul dua file Excel baru: `budget_dummy.xlsx` dan `po_dummy.xlsx`.
4. Jalankan aplikasi (`streamlit run app.py`) dan upload kedua file tersebut.

---

## 🔒 Kebijakan Privasi & Keamanan

Aplikasi ini didesain dengan prinsip **Privacy First**:
* Semua pemrosesan data dilakukan di memori komputer pengguna (RAM).
* **Tidak ada data** yang dikirim, disimpan, atau dilacak ke server luar.
* Setelah browser ditutup atau di-refresh, sesi data akan dihapus otomatis dari memori.

---

<div align="center">

**Satuan Pengawasan Intern (SPI)**
<br>
PT PAL Indonesia (Persero)
<br>
Surabaya, Indonesia

<br>

**© 2026 All Rights Reserved.**

</div>