# 🐳 RenangPedia – Chatbot Informasi Gaya dan Aturan Dasar Renang

RenangPedia adalah aplikasi chatbot berbasis web yang dikembangkan menggunakan **Python dan Flask** untuk memberikan informasi seputar dunia renang, khususnya gaya renang, teknik dasar, serta aturan perlombaan renang.

Chatbot ini dirancang sebagai teman belajar virtual yang membantu pengguna memperoleh informasi mengenai olahraga renang melalui percakapan interaktif.

## 📌 Tentang Project

RenangPedia dikembangkan sebagai proyek Chatbot Tematik dengan pendekatan Natural Language Processing (NLP) dan pencocokan intent untuk mengenali pertanyaan pengguna berdasarkan basis pengetahuan yang telah disiapkan.

Aplikasi ini memiliki tampilan bertema **Cute Aquatic** dengan ilustrasi paus dan nuansa warna biru yang menggambarkan dunia perairan.

## ✨ Fitur Utama

### 1. Chatbot Informasi Renang
- Menjawab pertanyaan seputar gaya renang.
- Memberikan informasi teknik dasar renang.
- Menjelaskan aturan dan ketentuan perlombaan renang.
- Mengenali berbagai variasi pertanyaan pengguna.
- Memberikan respons berdasarkan basis pengetahuan chatbot.

### 2. Mode Belajar
- Menampilkan informasi tambahan mengenai hasil pencocokan pertanyaan.
- Membantu pengguna memahami proses pengenalan pertanyaan oleh chatbot.

### 3. Riwayat Percakapan
- Menyimpan riwayat percakapan pengguna.
- Menampilkan percakapan selama sesi berlangsung.
- Menyediakan fitur untuk menghapus riwayat percakapan.

### 4. Dashboard Admin
- Menampilkan jumlah pertanyaan yang masuk.
- Menampilkan persentase pertanyaan yang berhasil dikenali.
- Menampilkan jumlah pertanyaan yang tidak dikenali.
- Menampilkan jumlah sesi percakapan.
- Menampilkan statistik pertanyaan berdasarkan intent.
- Menampilkan pertanyaan yang belum dikenali chatbot.

## 📚 Ruang Lingkup Informasi

Basis pengetahuan RenangPedia mencakup 43 intent yang membahas beberapa kategori berikut:

- Gaya renang dan perbedaannya.
- Aturan start perlombaan renang.
- Teknik dan gerakan dasar renang.
- Aturan perlombaan renang.
- Ketentuan diskualifikasi.
- Informasi umum mengenai olahraga renang.

## 🛠️ Teknologi yang Digunakan

| Teknologi | Kegunaan |
|---|---|
| Python | Bahasa pemrograman utama |
| Flask | Framework pengembangan aplikasi web |
| HTML | Struktur halaman web |
| CSS | Desain dan tampilan antarmuka |
| JavaScript | Interaksi chatbot pada halaman web |
| JSON | Penyimpanan basis pengetahuan dan intent |
| SQLite | Penyimpanan riwayat percakapan |

## 📂 Struktur Project

```text
chatbot-RenangPedia-flask/
│
├── chatbot/
│   ├── __init__.py
│   ├── database.py
│   └── engine.py
│
├── evaluasi/
│   └── renang.csv
│
├── themes/
│   └── renang.json
│
├── templates/
│   ├── 404.html
│   ├── admin.html
│   ├── base.html
│   ├── chat.html
│   ├── index.html
│   └── welcome.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── chat.js
│
├── app.py
├── cli.py
├── evaluate.py
├── README.md
└── requirements.txt
```

## 🚀 Instalasi dan Menjalankan Aplikasi

Ikuti langkah-langkah berikut untuk menjalankan RenangPedia di komputer lokal.

### 1. Clone Repository

```bash
git clone https://github.com/della436/chatbot-RenangPedia-flask.git
```

### 2. Masuk ke Folder Project

```bash
cd chatbot-RenangPedia-flask
```

### 3. Buat Virtual Environment

```bash
python -m venv venv
```

### 4. Aktifkan Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**macOS / Linux:**
```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Jalankan Aplikasi

```bash
python app.py
```

### 7. Buka Aplikasi

Akses alamat berikut melalui browser:

```text
http://127.0.0.1:5000
```

## 🌐 Halaman Aplikasi

| Halaman | URL | Keterangan |
|---|---|---|
| Welcome | `/` | Halaman pembuka RenangPedia |
| Home | `/home` | Halaman utama chatbot |
| Chatbot | `/chat/renangpedia` | Halaman percakapan dengan chatbot |
| Admin | `/admin/renangpedia` | Dashboard statistik chatbot |

Jika menggunakan konfigurasi `ADMIN_KEY`, akses dashboard admin memerlukan parameter kunci admin.

## 📊 Evaluasi Chatbot

RenangPedia menyediakan file evaluasi untuk menguji kemampuan chatbot dalam mengenali pertanyaan berdasarkan intent yang telah ditentukan.

File evaluasi tersedia pada:

```text
evaluasi/renang.csv
```

Pengujian dapat dijalankan menggunakan:

```bash
python evaluate.py
```

Hasil evaluasi digunakan untuk mengetahui kemampuan chatbot dalam mengenali pertanyaan serta mengidentifikasi bagian basis pengetahuan yang perlu diperbaiki.

## 🎨 Tampilan Antarmuka

RenangPedia menggunakan konsep desain **Cute Aquatic** dengan karakteristik:
- Dominasi warna biru dan putih.
- Ilustrasi maskot paus.
- Elemen dekoratif gelembung air.
- Tampilan sederhana, interaktif, dan responsif.
- Antarmuka yang dirancang agar nyaman digunakan.

*RenangPedia – Learn swimming, one question at a time. 🐳*
