import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
import joblib

# Load dataset
data = pd.read_csv('depression.csv')

# Define features and target
X = data.drop(columns=['Number ', 'Depression State'])
y = data['Depression State']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = GaussianNB()
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, 'naive_bayes_model.pkl')

# Load the model
model = joblib.load('naive_bayes_model.pkl')

# Streamlit app
st.title("Depression Screening App")

# Create tabs
tab1, tab2 = st.tabs(["Home", "Form Mental Health"])

with tab1:
    st.header("Welcome to the Depression Screening App")
    st.write("This application helps you to identify the level of depression based on your symptoms.")

with tab2:
    st.header("Mental Health Form")
    # Collect user input
    sleep = st.selectbox("Sleep Disturbance", [1, 2, 3, 4, 5, 6], key='sleep')
    appetite = st.selectbox("Appetite Changes", [1, 2, 3, 4, 5, 6], key='appetite')
    interest = st.selectbox("Loss of Interest", [1, 2, 3, 4, 5, 6], key='interest')
    fatigue = st.selectbox("Fatigue", [1, 2, 3, 4, 5, 6], key='fatigue')
    worthlessness = st.selectbox("Worthlessness", [1, 2, 3, 4, 5, 6], key='worthlessness')
    concentration = st.selectbox("Concentration", [1, 2, 3, 4, 5, 6], key='concentration')
    agitation = st.selectbox("Agitation", [1, 2, 3, 4, 5, 6], key='agitation')
    suicidal_ideation = st.selectbox("Suicidal Ideation", [1, 2, 3, 4, 5, 6], key='suicidal_ideation')
    sleep_disturbance = st.selectbox("Sleep Disturbance", [1, 2, 3, 4, 5, 6], key='sleep_disturbance')
    aggression = st.selectbox("Aggression", [1, 2, 3, 4, 5, 6], key='aggression')
    panic_attacks = st.selectbox("Panic Attacks", [1, 2, 3, 4, 5, 6], key='panic_attacks')
    hopelessness = st.selectbox("Hopelessness", [1, 2, 3, 4, 5, 6], key='hopelessness')
    restlessness = st.selectbox("Restlessness", [1, 2, 3, 4, 5, 6], key='restlessness')
    low_energy = st.selectbox("Low Energy", [1, 2, 3, 4, 5, 6], key='low_energy')
    
    # Prediction
    if st.button("Submit"):
        user_input = [[sleep, appetite, interest, fatigue, worthlessness, concentration, agitation, suicidal_ideation, sleep_disturbance, aggression, panic_attacks, hopelessness, restlessness, low_energy]]
        prediction = model.predict(user_input)
        st.write(f"Predicted Depression Level: {prediction[0]}")
