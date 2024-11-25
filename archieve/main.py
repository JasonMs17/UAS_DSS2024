import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# Memuat dataset
df = pd.read_csv('dataset.csv')

# Memproses kolom Tekanan Darah
df[['Sistolik', 'Diastolik']] = df['Blood Pressure'].str.split('/', expand=True)
df['Sistolik'] = df['Sistolik'].astype(float)
df['Diastolik'] = df['Diastolik'].astype(float)

# Menyiapkan data
X = df[['Gender', 'Age', 'Sleep Duration', 'Quality of Sleep', 
        'Physical Activity Level', 'BMI Category', 'Sistolik', 'Diastolik', 
        'Heart Rate', 'Daily Steps', 'Sleep Disorder']]
y = df['Stress Level']

# Mengenkripsi variabel kategori
le_gender = LabelEncoder()
X['Gender'] = le_gender.fit_transform(X['Gender'])

le_bmi = LabelEncoder()
X['BMI Category'] = le_bmi.fit_transform(X['BMI Category'])

le_sleep_disorder = LabelEncoder()
X['Sleep Disorder'] = le_sleep_disorder.fit_transform(X['Sleep Disorder'])

# Membagi dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Melatih model Naive Bayes
model = GaussianNB()
model.fit(X_train, y_train)

# Memprediksi data uji
y_pred = model.predict(X_test)

# Menghitung akurasi
accuracy = accuracy_score(y_test, y_pred)

# Tata letak aplikasi Streamlit
markdown_styling = """
<style>
[data-testid="stMain"] {
    background-image: url("https://wallpapercave.com/wp/wp2197012.jpg");
    background-size: cover;
}
h1, h2, h3, p {
    color: #fff;
}
[data-testid="stButton"] p {
    color: #949494 !important;
}
[data-testid="stHeader"] {
    background-color: rgba(0, 0, 0, 0);
}
[data-testid="stNumberInputContainer"] {
    width: 90%;
}
[data-testid="stSelectbox"] {
    width: 90% !important;
}
[data-testid="stAlertContainer"] {
    width: 90% !important;
}
</style>
"""

st.markdown(markdown_styling, unsafe_allow_html=True)
st.title("Penilaian Kesehatan Mental")

# Tab navigasi
tab1, tab2, tab3 = st.tabs(["Beranda", "Formulir", "Kalkulator BMI"])

# Tab Beranda
with tab1:
    st.header("Selamat Datang di Aplikasi Penilaian Kesehatan Mental")
    st.write("""
    Aplikasi ini membantu dalam menilai kesehatan mental dengan mengklasifikasikan tingkat stres berdasarkan berbagai parameter.
    Silakan pindah ke tab 'Formulir' untuk mengisi data Anda dan mendapatkan penilaian tingkat stres.
    """)
    st.write(f"Akurasi Model: {accuracy * 100:.2f}%")
    
    # Menampilkan tabel panduan
    st.subheader("Panduan untuk Kolom Input")
    guide_data = {
        "Kolom": [
            "Jenis Kelamin", "Usia", "Durasi Tidur", "Kualitas Tidur", 
            "Tingkat Aktivitas Fisik", "Kategori BMI", "Sistolik", "Diastolik",
            "Detak Jantung", "Langkah Harian", "Gangguan Tidur"
        ],
        "Deskripsi": [
            "Jenis kelamin biologis Anda (contoh: Pria, Wanita).",
            "Usia Anda dalam tahun.",
            "Jumlah rata-rata jam tidur Anda dalam sehari.",
            "Nilai kualitas tidur Anda pada skala 1 sampai 10.",
            "Tingkat aktivitas fisik harian Anda dalam persen.",
            "Kategori Indeks Massa Tubuh (contoh: Normal, Kelebihan Berat).",
            "Tekanan darah sistolik (angka atas, tekanan saat jantung berdetak).",
            "Tekanan darah diastolik (angka bawah, tekanan saat jantung istirahat).",
            "Detak jantung saat istirahat dalam denyut per menit (bpm).",
            "Jumlah rata-rata langkah yang Anda ambil setiap hari.",
            "Gangguan tidur yang didiagnosis (contoh: Insomnia, Tidak Ada)."
        ]
    }
    guide_df = pd.DataFrame(guide_data)
    st.table(guide_df)

# Tab Formulir
with tab2:
    st.header("Jawab Pertanyaan Berikut")
    
    # Mengumpulkan input pengguna melalui pertanyaan
    gender = st.selectbox("Apa jenis kelamin Anda?", df['Gender'].unique())
    age = st.number_input("Berapa usia Anda?", min_value=0, max_value=100, value=25)
    sleep_duration = st.number_input("Berapa jam rata-rata Anda tidur dalam sehari?", min_value=0.0, max_value=24.0, value=7.0)
    quality_of_sleep = st.slider("Pada skala 1 sampai 10, bagaimana kualitas tidur Anda?", min_value=1, max_value=10, value=5)
    physical_activity_level = st.number_input("Seberapa aktif Anda secara fisik? (Masukkan persen antara 0-100)", min_value=0, max_value=100, value=50)
    bmi_category = st.selectbox("Kategori BMI mana yang paling menggambarkan Anda?", ["Normal", "Overweight", "Obese"])
    systolic = st.number_input("Berapa tekanan darah sistolik Anda?", min_value=50, max_value=200, value=120)
    diastolic = st.number_input("Berapa tekanan darah diastolik Anda?", min_value=30, max_value=130, value=80)
    heart_rate = st.number_input("Berapa detak jantung Anda saat istirahat?", min_value=0, max_value=200, value=70)
    daily_steps = st.number_input("Berapa langkah rata-rata yang Anda ambil setiap hari?", min_value=0, max_value=50000, value=5000)
    sleep_disorder = st.selectbox("Apakah Anda memiliki gangguan tidur yang didiagnosis?", df['Sleep Disorder'].unique())
    
    # Memproses input dan memprediksi
    if st.button("Prediksi Tingkat Stres"):
        # Mengubah input
        input_data = pd.DataFrame({
            'Gender': [le_gender.transform([gender])[0]],
            'Age': [age],
            'Sleep Duration': [sleep_duration],
            'Quality of Sleep': [quality_of_sleep],
            'Physical Activity Level': [physical_activity_level],
            'BMI Category': [le_bmi.transform([bmi_category])[0]],
            'Sistolik': [systolic],
            'Diastolik': [diastolic],
            'Heart Rate': [heart_rate],
            'Daily Steps': [daily_steps],
            'Sleep Disorder': [le_sleep_disorder.transform([sleep_disorder])[0]]
        })
        
        # Prediksi
        prediction = model.predict(input_data)
        st.success(f"Berdasarkan jawaban Anda, tingkat stres yang diprediksi adalah: {prediction[0]}")

# Tab Kalkulator BMI
with tab3:
    st.header("Kalkulator BMI")
    st.write("Masukkan berat badan dan tinggi badan Anda untuk menghitung Indeks Massa Tubuh (BMI).")
    
    # Input untuk berat badan dan tinggi badan
    weight = st.number_input("Berat badan Anda (kg):", min_value=1.0, max_value=200.0, value=70.0)
    height = st.number_input("Tinggi badan Anda (cm):", min_value=50.0, max_value=250.0, value=170.0)
    
    # Hitung BMI
    if st.button("Hitung BMI"):
        height_m = height / 100  # Konversi tinggi ke meter
        bmi = weight / (height_m ** 2)
        st.write(f"BMI Anda adalah: **{bmi:.2f}**")
        
        # Kategori BMI
        if bmi < 18.5:
            st.warning("Anda termasuk kategori: **Kekurangan Berat Badan**.")
        elif 18.5 <= bmi < 24.9:
            st.success("Anda termasuk kategori: **Normal**.")
        elif 25 <= bmi < 29.9:
            st.warning("Anda termasuk kategori: **Overweight**.")
        else:
            st.error("Anda termasuk kategori: **Obese**.")
