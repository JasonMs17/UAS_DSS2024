import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

def load_model():
    df = pd.read_csv("dataset.csv")
    # X = df[['Gender', 'Age', 'Sleep Duration', 'Quality of Sleep', 'Physical Activity Level', 'BMI Category', 'Heart Rate', 'Daily Steps', 'Sleep Disorder']]
    X = df[['Gender', 'Age', 'Sleep Duration', 'Quality of Sleep', 'BMI Category', 'Heart Rate', 'Daily Steps', 'Sleep Disorder']]
    X['BMI Category'] = X['BMI Category'].replace("Normal Weight", "Normal")
    X['Sleep Disorder'] = X['Sleep Disorder'].fillna("Nothing")
    y = df['Stress Level']

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

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    accuracy = accuracy_score(y_test, model.predict(X_test))
    return model, encoders, accuracy

def predict_stress_level(data, model, encoders):
    for col, encoder in encoders.items():
        data[col] = encoder.transform(data[col]) 

    df_input = pd.DataFrame(data)

    # Make a prediction
    prediction = model.predict(df_input)[0]
    return prediction
