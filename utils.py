import streamlit as st

def generate_recommendation(stress_level, sleep_duration, quality_of_sleep, heart_rate):
    recommendations = []
    if stress_level >= 7:
        recommendations.append("Cobalah meditasi atau yoga untuk mengurangi stres.")
    if sleep_duration < 7:
        recommendations.append("Tidur lebih lama untuk meningkatkan kesehatan.")
    # if activity_level < 30:
    #     recommendations.append("Tingkatkan aktivitas fisik untuk keseimbangan mental.")
    if heart_rate > 100:
        recommendations.append("Latihan pernapasan dapat membantu menenangkan detak jantung Anda.")
    return recommendations

def bmi_calculator():
    weight = st.number_input("Berat badan Anda (kg)?", min_value=1.0, max_value=200.0, value=70.0)
    height = st.number_input("Tinggi badan Anda (cm)?", min_value=50.0, max_value=250.0, value=170.0)

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

guide_data = {
    "Kolom": [
        "Jenis Kelamin", 
        "Usia", 
        "Durasi Tidur", 
        "Kualitas Tidur", 
        "Kategori BMI",
        "Detak Jantung", 
        "Langkah Harian", 
        "Gangguan Tidur"
    ],
    "Deskripsi": [
        "Jenis kelamin biologis Anda (contoh: Pria, Wanita).",
        "Usia Anda dalam tahun.",
        "Jumlah rata-rata jam tidur Anda dalam sehari.",
        "Nilai kualitas tidur Anda pada skala 1 sampai 10.",
        "Kategori Indeks Massa Tubuh",
        "Detak jantung saat istirahat dalam denyut per menit (bpm).",
        "Jumlah rata-rata langkah yang Anda ambil setiap hari.",
        "Gangguan tidur yang didiagnosis"
    ]
}