# 💓 Aplikasi Deteksi Stres

Aplikasi ini dirancang untuk membantu dalam memahami hubungan antara berbagai faktor kesehatan dan tingkat stres. Model prediksi stres dikembangkan dengan menggunakan metode Random Forest dan diterapkan pada **Sleep Health and Lifestyle Dataset** yang tersedia di Kaggle. Aplikasi ini mengklasifikasikan tingkat stres pada skala 3 hingga 8.

## Fitur Utama

- Menggunakan **Random Forest** untuk mendeteksi tingkat stres berdasarkan data kesehatan dan gaya hidup.
- Dataset yang digunakan: [Sleep Health and Lifestyle Dataset](https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset).
- Model ini diuji dengan dataset yang tersedia dan menghasilkan tingkat akurasi **97.33%**.
- Dikembangkan menggunakan **Streamlit** untuk antarmuka pengguna yang interaktif.

## Teknologi yang Digunakan

- **Random Forest**: Algoritma machine learning untuk prediksi tingkat stres.
- **Streamlit**: Framework untuk membuat aplikasi web interaktif dengan Python.
- **Pandas**: Untuk manipulasi data dan pemrosesan dataset.
- **Scikit-Learn**: Untuk implementasi model machine learning.
- **Matplotlib**: Untuk visualisasi data.
- **Seaborn**: Untuk visualisasi data.  
- **NumPy**: Untuk komputasi numerik dan manipulasi array.

## Anggota Tim

- **140810220051 - Jason Natanael Krisyanto**
- **140810220002 - Muhammad Faiz Fahri**
- **140810220026 - Muhammad Rumi Rifai**

## Panduan Penggunaan

1. **Install dependencies**:
   Pastikan Anda telah menginstall semua dependencies yang diperlukan dengan menjalankan perintah berikut:

   ```bash
   pip install -r requirements.txt

2. **Jalankan aplikasi Streamlit**:
   Setelah menginstal dependencies, jalankan aplikasi menggunakan perintah berikut di terminal atau command prompt:

   ```bash
   streamlit run app.py
   ```
  
3. **Masukkan Data**:
   Aplikasi ini akan meminta pengguna untuk menginput data terkait gaya hidup dan kesehatan. Berdasarkan input ini, model akan memprediksi tingkat stres berdasarkan hubungan yang ditemukan dalam dataset.

4. **Lihat Hasil**:
   Setelah memasukkan data, aplikasi akan menampilkan hasil prediksi tingkat stres serta analisis terkait faktor-faktor yang memengaruhi stres.
