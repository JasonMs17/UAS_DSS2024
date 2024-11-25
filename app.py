import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from model import load_model, predict_stress_level
import seaborn as sns
from utils import generate_recommendation, guide_data, bmi_calculator
from sklearn.preprocessing import LabelEncoder

# Load trained model and encoders
model, encoders, accuracy = load_model()

# Load data to calculate average stress level
df = pd.read_csv("dataset.csv")
label_encoder = LabelEncoder()
factors = ['Sleep Duration', 'Quality of Sleep', 'Heart Rate', 'Daily Steps']
average_stress = df.groupby('Stress Level')[factors].mean()

# Styling
st.markdown("""
<style>
[data-testid="stMain"] {
    background-image: url("https://cdn.britannica.com/25/214625-050-A37D76CC/heart-rate-monitor-illustration-heartbeat.jpg");
    background-size: cover;
}
            
[data-testid="stMain"]::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.7);
}
            
h1, h2, h3, p {
    color: #fff;
}
</style>
""", unsafe_allow_html=True)

st.sidebar.title("Selamat Datang di Aplikasi Deteksi Stres ❤️‍🩹")
st.sidebar.markdown("---")
st.sidebar.write("""
Aplikasi ini dirancang untuk membantu dalam memahami hubungan antara berbagai faktor kesehatan dan tingkat stres. Model dikembangkan dengan metode Naive Bayes menggunakan dataset **[Sleep Health and Lifestyle Dataset](https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset)** 
""")

st.title("Deteksi Stress Level")
tab1, tab2, tab3 = st.tabs(["Beranda", "Formulir", "Hubungan Korelasi"])

# Tab Beranda
with tab1:

    st.write(f"""

### Akurasi Model:
Model ini telah diuji dengan data yang tersedia dan memiliki tingkat akurasi {accuracy * 100:.2f}%
""")

    st.table(pd.DataFrame(guide_data))

# Tab Formulir
with tab2:
    st.header("Jawab Pertanyaan Berikut")
    gender = st.selectbox("Jenis Kelamin Anda?", ["Male", "Female"])
    age = st.number_input("Usia Anda?", min_value=0, max_value=100, value=25)
    sleep_duration = st.number_input("Jam tidur per hari?", min_value=0.0, max_value=24.0, value=7.0)
    quality_of_sleep = st.slider("Kualitas tidur Anda?", 1, 10, 5)
    bmi_category = st.selectbox("Kategori BMI mana yang paling menggambarkan Anda?", ["Normal", "Overweight", "Obese"])

    with st.expander("Kalkulator BMI"):
        bmi = bmi_calculator()
        if bmi:
            st.write(f"BMI Anda adalah: {bmi:.2f}")

    # activity_level = st.number_input("Aktivitas fisik (dalam %)?", min_value=0, max_value=100, value=50)
    heart_rate = st.number_input("Berapa detak jantung Anda saat istirahat?", min_value=0, max_value=200, value=70)
    daily_steps = st.number_input("Berapa langkah rata-rata yang Anda ambil setiap hari?", min_value=0, max_value=50000, value=5000)
    sleep_disorder = st.selectbox("Apakah Anda memiliki gangguan tidur yang didiagnosis?", ['Sleep Apnea', 'Insomnia', 'Nothing'])


    if st.button("Prediksi Tingkat Stres"):
        input_data = {
            'Gender': [gender],
            'Age': [age],
            'Sleep Duration': [sleep_duration],
            'Quality of Sleep': [quality_of_sleep],
            # 'Physical Activity Level': [activity_level],
            'BMI Category': [bmi_category],
            'Heart Rate': [heart_rate],
            'Daily Steps': [daily_steps],
            'Sleep Disorder': [sleep_disorder]
        }
        stress_level = predict_stress_level(input_data, model, encoders)
        st.write(f"Tingkat stres Anda: **{stress_level}**")
        # recommendations = generate_recommendation(stress_level, sleep_duration, quality_of_sleep, activity_level, heart_rate)
        recommendations = generate_recommendation(stress_level, sleep_duration, quality_of_sleep, heart_rate)
        for rec in recommendations:
            st.write(f"- {rec}")
 
        factors = ['Sleep Duration', 'Quality of Sleep', 'Heart Rate', 'Daily Steps']
        values = [sleep_duration, quality_of_sleep, heart_rate, daily_steps]

        avg_values = [average_stress[factor].mean() for factor in factors]

        # Create separate bar charts for each category of factors
        fig, axs = plt.subplots(1, len(factors), figsize=(20, 5))
        bar_width = 0.35

        fig, axs = plt.subplots(2, 2, figsize=(10, 8))
        for i, factor in enumerate(factors):
            row = i // 2
            col = i % 2
            axs[row, col].bar(['Input Pengguna', 'Rata-rata Stress Level'], [values[i], avg_values[i]], bar_width, color=['blue', 'green'])
            axs[row, col].set_title(f'Perbandingan {factor}')
            axs[row, col].set_ylabel('Nilai')
            axs[row, col].set_xticklabels(['Input Pengguna', 'Rata-rata Stress Level'])
            axs[row, col].legend()

        plt.tight_layout()

        st.pyplot(fig)

# Tab Hubungan Correlation
with tab3:
    st.header("Hubungan dan Correlation Antar Faktor")
    
    # Display the correlation values directly
    correlation_values = {
        'Gender': 0.396018,
        'Age': -0.422344,
        'Sleep Duration': -0.811023,
        'Quality of Sleep': -0.898752,
        'BMI Category': 0.163665,
        'Heart Rate': 0.670026,
        'Daily Steps': 0.186829,
        'Sleep Disorder': -0.036058
    }
    
    # Display the correlation values
    st.write("Nilai Korelasi terhadap Tingkat Stres:")
    st.write(pd.DataFrame(list(correlation_values.items()), columns=["Faktor", "Korelasi"]))
    
    # Explanation in Bahasa Indonesia
    st.write("""
    Berdasarkan analisis korelasi terhadap tingkat stres, berikut adalah hubungan antara beberapa faktor dan tingkat stres:
    
    - **Jenis Kelamin (0.396)**: Terdapat korelasi positif antara jenis kelamin dengan tingkat stres. Ini menunjukkan bahwa jenis kelamin tertentu mungkin memiliki kecenderungan untuk mengalami stres lebih tinggi, meskipun ini bukanlah hubungan yang sangat kuat.
    
    - **Usia (-0.422)**: Korelasi negatif menunjukkan bahwa semakin tua usia seseorang, semakin rendah kemungkinan mereka mengalami stres. Hal ini bisa terkait dengan pengalaman hidup yang membuat orang lebih mampu mengelola stres seiring bertambahnya usia.
    
    - **Durasi Tidur (-0.811)**: Korelasi negatif yang sangat kuat antara durasi tidur dengan tingkat stres. Orang yang tidur lebih sedikit cenderung memiliki tingkat stres lebih tinggi, menunjukkan pentingnya tidur yang cukup untuk kesehatan mental.
    
    - **Kualitas Tidur (-0.898)**: Korelasi negatif yang sangat kuat juga ditemukan antara kualitas tidur dan tingkat stres. Semakin buruk kualitas tidur, semakin tinggi tingkat stres yang dialami. Tidur yang berkualitas sangat berpengaruh pada kesejahteraan mental.
    
    - **Kategori BMI (0.163)**: Korelasi positif yang lemah menunjukkan bahwa orang dengan BMI lebih tinggi mungkin memiliki kecenderungan sedikit lebih tinggi untuk mengalami stres. Namun, hubungan ini tidak terlalu kuat.
    
    - **Detak Jantung (0.670)**: Korelasi positif yang cukup kuat menunjukkan bahwa semakin tinggi detak jantung saat istirahat, semakin tinggi tingkat stres. Detak jantung yang tinggi sering kali menjadi indikator stres atau kecemasan.
    
    - **Langkah Harian (0.186)**: Korelasi positif yang lemah menunjukkan bahwa orang yang lebih banyak bergerak atau berjalan cenderung memiliki tingkat stres yang lebih rendah, meskipun ini bukan hubungan yang sangat kuat.
    
    - **Gangguan Tidur (-0.036)**: Korelasi sangat lemah menunjukkan bahwa gangguan tidur tidak memiliki pengaruh signifikan terhadap tingkat stres, meskipun gangguan tidur dapat mempengaruhi kualitas tidur yang berhubungan erat dengan stres.
    """)

    # Optional: You can also add a brief sentence to summarize the most influential factors
    st.write("""
    Dari faktor-faktor di atas, **durasi tidur** dan **kualitas tidur** memiliki korelasi yang sangat kuat dengan tingkat stres. Oleh karena itu, menjaga tidur yang cukup dan berkualitas adalah salah satu cara yang paling efektif untuk mengelola stres.
    """)