
# 🏊 RenangPedia

### Chatbot Informasi Gaya dan Aturan Dasar Renang

RenangPedia merupakan aplikasi chatbot berbasis web yang dikembangkan menggunakan Python dan Flask. Aplikasi ini dirancang untuk memberikan informasi seputar gaya renang, teknik dasar, serta aturan dalam perlombaan renang.

Chatbot menggunakan pendekatan pencocokan intent untuk mengenali pertanyaan pengguna dan memberikan jawaban berdasarkan basis pengetahuan yang telah disediakan.

---

## ✨ Fitur Utama

- **Informasi Gaya Renang** – Penjelasan mengenai gaya bebas, gaya dada, gaya punggung, dan gaya kupu-kupu.
- **Aturan Start** – Informasi mengenai aturan dan prosedur start dalam perlombaan renang.
- **Diskualifikasi** – Penjelasan mengenai pelanggaran yang dapat menyebabkan diskualifikasi.
- **Aturan Perlombaan** – Informasi mengenai sentuhan dinding, putaran balik, estafet, dan ketentuan perlombaan lainnya.
- **Riwayat Percakapan** – Menyimpan dan menampilkan riwayat percakapan pengguna.
- **Mode Penjelasan** – Menampilkan kandidat intent dan skor pencocokan pertanyaan.
- **Statistik Chatbot** – Menampilkan statistik penggunaan dan hasil pengenalan pertanyaan.

---

## 🛠️ Teknologi yang Digunakan

| Teknologi | Kegunaan |
|---|---|
| Python | Bahasa pemrograman utama |
| Flask | Framework aplikasi web |
| HTML | Struktur halaman web |
| CSS | Tampilan antarmuka |
| JavaScript | Interaksi chatbot |
| SQLite | Penyimpanan riwayat percakapan |
| JSON | Penyimpanan basis pengetahuan |
| CSV | Dataset evaluasi chatbot |

---

## 📂 Struktur Proyek

```text
chatbox-RenangPedia-flask/
│
├── chatbot/
│   ├── __init__.py
│   ├── database.py
│   └── engine.py
│
├── evaluasi/
│   └── renang.csv
│
├── screenshots/
│   ├── 01-halaman-utama.png
│   ├── 02-halaman-chatbot.png
│   ├── 03-percakapan-chatbot.png
│   └── 04-halaman-statistik.png
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── chat.js
│
├── templates/
│   ├── 404.html
│   ├── admin.html
│   ├── base.html
│   ├── chat.html
│   └── index.html
│
├── themes/
│   └── renang.json
│
├── app.py
├── cli.py
├── evaluate.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🚀 Instalasi dan Menjalankan Aplikasi

### 1. Clone Repository

```bash
git clone URL_REPOSITORY
```

### 2. Masuk ke Folder Proyek

```bash
cd chatbox-RenangPedia-flask
```

### 3. Buat Virtual Environment

```bash
python -m venv venv
```

### 4. Aktifkan Virtual Environment

**macOS / Linux:**

```bash
source venv/bin/activate
```

**Windows (PowerShell):**

```powershell
venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**

```cmd
venv\Scripts\activate.bat
```

### 5. Instal Dependensi

```bash
pip install -r requirements.txt
```

### 6. Jalankan Aplikasi

```bash
python app.py
```

### 7. Buka Aplikasi

Buka browser dan akses alamat berikut:

```text
http://127.0.0.1:5000/
```

---

## 💬 Menjalankan Chatbot Melalui Terminal

Selain melalui browser, chatbot juga dapat dijalankan melalui terminal menggunakan perintah:

```bash
python cli.py
```

Untuk menampilkan kandidat intent:

```bash
python cli.py --debug
```

---

## 📊 Evaluasi Chatbot

Evaluasi chatbot dapat dilakukan menggunakan dataset yang tersedia pada folder `evaluasi/`.

Jalankan perintah:

```bash
python evaluate.py
```

Untuk menguji beberapa nilai ambang pencocokan:

```bash
python evaluate.py --sweep
```
---

## 👩‍💻 Pengembangan

**RenangPedia – Chatbot Informasi Gaya dan Aturan Dasar Renang**

Dikembangkan sebagai proyek praktikum aplikasi web.
