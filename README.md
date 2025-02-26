# 🚲 Bike Sharing Dashboard

## 📌 Deskripsi Proyek
Dashboard ini dibuat menggunakan **Streamlit** untuk menganalisis dataset "Bike Sharing". Dashboard ini menampilkan berbagai visualisasi data, analisis clustering, dan informasi statistik tentang pola penggunaan sepeda.

---

## 🛠️ Cara Menggunakan

### 1️⃣ **Unduh Repository**
Clone repository ini menggunakan Git atau unduh secara manual:
```sh
# Clone dengan Git
git clone https://github.com/username/repository.git
# Masuk ke folder proyek
cd repository
```
Atau jika diunduh secara manual, ekstrak file ZIP dan buka folder proyek di terminal.

### 2️⃣ **Buat Virtual Environment**
Sebelum menjalankan proyek, buat virtual environment untuk mengisolasi dependensi:
```sh
# Untuk pengguna Windows
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ **Instal Dependensi**
Setelah mengaktifkan environment, instal semua dependensi yang diperlukan:
```sh
pip install -r requirements.txt
```
Jika tidak ada file `requirements.txt`, instal paket utama secara manual:
```sh
pip install streamlit pandas matplotlib scikit-learn
```

### 4️⃣ **Menjalankan Dashboard**
Jalankan Streamlit untuk menampilkan dashboard:
```sh
streamlit run dashboard.py
```

Jika tidak ada error, terminal akan menampilkan URL seperti:
```
Running on local URL: http://localhost:8501
```
Buka URL tersebut di browser untuk melihat dashboard.

---

## 🔄 Troubleshooting
Jika mengalami error, coba langkah berikut:
1. Pastikan **Python** dan **pip** telah terinstal dengan versi terbaru.
   ```sh
   python --version
   pip --version
   ```
2. Pastikan **virtual environment aktif** sebelum menjalankan `streamlit run`.
3. Jika ada error terkait pustaka, coba hapus dan instal ulang environment.

## ✨ Kontributor
- **Nama:** Andreas Kevin  
- **Email:** kevinandreas913@gmail.com  
- **ID Dicoding:** andreas_kevin_6396  
