import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config(page_title="Mental Health Predictor", layout="centered")

st.set_page_config(page_title="Mental Health Predictor", layout="centered")

# 🔽 Background image CSS injected here
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1557683316-973673baf926");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Optional: Add a banner image (place a local image or link to hosted image)
st.image("https://images.unsplash.com/photo-1620147461831-a97b99ade1d3?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8bWVudGFsJTIwaGVhbHRofGVufDB8fDB8fHww", use_container_width =True)  # Replace with your own if needed

# Title and intro
st.title("🧠 Mental Health Treatment Predictor")
st.markdown("Welcome to the Mental Health Predictor App! 🚀")
st.markdown(
    "This tool helps estimate the likelihood of someone seeking mental health treatment based on workplace and personal factors."
)

st.divider()

# Load trained model
model = joblib.load("models/logreg_model.joblib")

# 👤 Personal & Work-Related Information
st.subheader("📋 User Information")

age = st.slider("📅 Age", 18, 65)

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("🧬 Gender", ["Male", "Female", "Other"])
    family_history = st.selectbox("👨‍👩‍👧‍👦 Family History of Mental Illness", ["Yes", "No"])
    remote_work = st.selectbox("🏠 Works Remotely", ["Yes", "No"])
    tech_company = st.selectbox("💻 Works in Tech Company", ["Yes", "No"])
    obs_consequence = st.selectbox("⚠️ Observed Negative Consequences", ["Yes", "No"])
    work_interfere = st.selectbox("💼 Mental Health Interference at Work", ["Never", "Rarely", "Sometimes", "Often"])
    benefits = st.selectbox("🎁 Mental Health Benefits", ["Yes", "No", "Don't know"])
    care_options = st.selectbox("🧑‍⚕️ Aware of Care Options", ["Yes", "No", "Not sure"])

with col2:
    wellness_program = st.selectbox("🏋️ Wellness Program", ["Yes", "No", "Don't know"])
    seek_help = st.selectbox("📞 Can Seek Help Easily", ["Yes", "No", "Don't know"])
    anonymity = st.selectbox("🕵️ Anonymity Protected", ["Yes", "No", "Don't know"])
    leave = st.selectbox("📝 Mental Health Leave Comfort", ["Very easy", "Somewhat easy", "Somewhat difficult", "Very difficult", "Don't know"])
    mental_health_consequence = st.selectbox("🧠 Mental Health Consequence", ["Yes", "No", "Maybe"])
    phys_health_consequence = st.selectbox("🏥 Physical Health Consequence", ["Yes", "No", "Maybe"])
    supervisor = st.selectbox("👔 Comfort with Supervisor", ["Yes", "No", "Some of them"])
    coworkers = st.selectbox("🤝 Comfort with Coworkers", ["Yes", "No", "Some of them"])

# Gender Encoding
gender_encoded = {
    "Male": [1, 0],
    "Female": [0, 1],
    "Other": [0, 0]
}[gender]

# Feature encoding
input_dict = {
    "Age": age,
    "family_history": 1 if family_history == "Yes" else 0,
    "remote_work": 1 if remote_work == "Yes" else 0,
    "tech_company": 1 if tech_company == "Yes" else 0,
    "obs_consequence": 1 if obs_consequence == "Yes" else 0,

    # Gender One-Hot
    "Gender_Male": gender_encoded[0],
    "Gender_Female": gender_encoded[1],

    # work_interfere One-Hot
    "work_interfere_Rarely": 1 if work_interfere == "Rarely" else 0,
    "work_interfere_Sometimes": 1 if work_interfere == "Sometimes" else 0,
    "work_interfere_Often": 1 if work_interfere == "Often" else 0,

    # benefits One-Hot
    "benefits_Yes": 1 if benefits == "Yes" else 0,
    "benefits_Don't know": 1 if benefits == "Don't know" else 0,

    # care_options One-Hot
    "care_options_Yes": 1 if care_options == "Yes" else 0,
    "care_options_Not sure": 1 if care_options == "Not sure" else 0,

    # wellness_program One-Hot
    "wellness_program_Yes": 1 if wellness_program == "Yes" else 0,
    "wellness_program_Don't know": 1 if wellness_program == "Don't know" else 0,

    # seek_help One-Hot
    "seek_help_Yes": 1 if seek_help == "Yes" else 0,
    "seek_help_Don't know": 1 if seek_help == "Don't know" else 0,

    # anonymity One-Hot
    "anonymity_Yes": 1 if anonymity == "Yes" else 0,
    "anonymity_Don't know": 1 if anonymity == "Don't know" else 0,

    # leave One-Hot
    "leave_Somewhat easy": 1 if leave == "Somewhat easy" else 0,
    "leave_Somewhat difficult": 1 if leave == "Somewhat difficult" else 0,
    "leave_Very difficult": 1 if leave == "Very difficult" else 0,
    "leave_Don't know": 1 if leave == "Don't know" else 0,

    # mental_health_consequence One-Hot
    "mental_health_consequence_Yes": 1 if mental_health_consequence == "Yes" else 0,
    "mental_health_consequence_Maybe": 1 if mental_health_consequence == "Maybe" else 0,

    # phys_health_consequence One-Hot
    "phys_health_consequence_Yes": 1 if phys_health_consequence == "Yes" else 0,
    "phys_health_consequence_Maybe": 1 if phys_health_consequence == "Maybe" else 0,

    # coworkers One-Hot
    "coworkers_Yes": 1 if coworkers == "Yes" else 0,
    "coworkers_Some of them": 1 if coworkers == "Some of them" else 0,

    # supervisor One-Hot
    "supervisor_Yes": 1 if supervisor == "Yes" else 0,
    "supervisor_Some of them": 1 if supervisor == "Some of them" else 0,
}


# Ensure all model columns are filled
all_features = model.feature_names_in_
input_df = pd.DataFrame([input_dict])
for col in all_features:
    if col not in input_df.columns:
        input_df[col] = 0
input_df = input_df[all_features]

st.divider()

# Prediction
if st.button("🔍 Predict"):
    result = model.predict(input_df)[0]
    st.subheader("🎯 Prediction Result")
    if result == 1:
        st.success("🛑 Likely to Seek Mental Health Treatment")
    else:
        st.info("✅ Unlikely to Seek Mental Health Treatment")

st.markdown("---")
st.caption("Built with ❤️ using Streamlit | Model: Logistic Regression")
