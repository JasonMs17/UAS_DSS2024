import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# **Fungsi untuk memuat model Random Forest**
def load_model():
    """
    Fungsi untuk memuat model Random Forest menggunakan dataset.
    - Dataset diproses untuk encoding fitur kategori.
    - Dataset dibagi menjadi data latih dan data uji.
    - Model dilatih menggunakan data latih dan akurasi dihitung pada data uji.
    
    Returns:
        model: Model Random Forest yang telah dilatih.
        encoders: Dictionary berisi LabelEncoders untuk fitur kategori.
        accuracy: Akurasi model pada data uji.
    """
    
    # Membaca dataset
    df = pd.read_csv("dataset.csv")
    
    # Memilih fitur dan target
    # X = df[['Gender', 'Age', 'Sleep Duration', 'Quality of Sleep', 'Physical Activity Level', 'BMI Category', 'Heart Rate', 'Daily Steps', 'Sleep Disorder']]
    X = df[['Gender', 'Age', 'Sleep Duration', 'Quality of Sleep', 'BMI Category', 'Heart Rate', 'Daily Steps', 'Sleep Disorder']]
    X['BMI Category'] = X['BMI Category'].replace("Normal Weight", "Normal")
    X['Sleep Disorder'] = X['Sleep Disorder'].fillna("Nothing")
    y = df['Stress Level']

    # Encoding fitur kategori
    encoders = {}

    le_gender = LabelEncoder()
    X['Gender'] = le_gender.fit_transform(X['Gender'])
    encoders['Gender'] = le_gender

    le_bmi = LabelEncoder()
    X['BMI Category'] = le_bmi.fit_transform(X['BMI Category'])
    encoders['BMI Category'] = le_bmi

    le_sleep_disorder = LabelEncoder()
    X['Sleep Disorder'] = le_sleep_disorder.fit_transform(X['Sleep Disorder'])
    encoders['Sleep Disorder'] = le_sleep_disorder

    # Membagi data menjadi latih dan uji
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Melatih model Random Forest
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    
    # Menghitung akurasi model
    accuracy = accuracy_score(y_test, model.predict(X_test))
    return model, encoders, accuracy


# **Fungsi untuk prediksi tingkat stres**
def predict_stress_level(data, model, encoders):
    """
    Fungsi untuk memprediksi tingkat stres berdasarkan data input pengguna.
    
    Args:
        data: Dictionary berisi data input pengguna.
        model: Model Random Forest yang telah dilatih.
        encoders: Dictionary LabelEncoders untuk fitur kategori.
    
    Returns:
        prediction: Prediksi tingkat stres pengguna.
    """

    # Melakukan encoding data input menggunakan LabelEncoders
    for col, encoder in encoders.items():
        data[col] = encoder.transform(data[col]) 

    # Membuat DataFrame dari data input
    df_input = pd.DataFrame(data)

    # Prediksi tingkat stres
    prediction = model.predict(df_input)[0]
    return prediction
