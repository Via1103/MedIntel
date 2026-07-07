import streamlit as st

from src.ml.predict import predict_patient
from src.ai.health_summary import generate_summary
from reports.pdf_report import generate_pdf

st.title("🩺 Diabetes Risk Prediction")

st.markdown("Enter patient clinical information.")

col1, col2 = st.columns(2)

with col1:

    gender = st.selectbox(
        "Gender",
        ["Male","Female"]
    )

    age = st.slider(
        "Age",
        1,
        100,
        40
    )

    bmi = st.number_input(
        "BMI",
        10.0,
        60.0,
        25.0
    )

    smoking = st.selectbox(
        "Smoking History",
        [
            "never",
            "former",
            "current",
            "ever",
            "not current",
            "No Info"
        ]
    )

with col2:

    hba1c = st.number_input(
        "HbA1c",
        3.0,
        15.0,
        5.5
    )

    glucose = st.number_input(
        "Blood Glucose",
        50,
        350,
        120
    )

    hypertension = st.selectbox(
        "Hypertension",
        [0,1]
    )

    heart = st.selectbox(
        "Heart Disease",
        [0,1]
    )

if bmi < 18.5:
    bmi_category = "Underweight"

elif bmi < 25:
    bmi_category = "Normal"

elif bmi < 30:
    bmi_category = "Overweight"

else:
    bmi_category = "Obese"

if age <=20:
    age_group="0-20"

elif age<=40:
    age_group="21-40"

elif age<=60:
    age_group="41-60"

else:
    age_group="60+"

patient = {

    "gender": gender,

    "age": age,

    "hypertension": hypertension,

    "heart_disease": heart,

    "smoking_history": smoking,

    "bmi": bmi,

    "hba1c_level": hba1c,

    "blood_glucose_level": glucose,

    "bmi_category": bmi_category,

    "age_group": age_group
}

if st.button("🔍 Predict Diabetes Risk"):

    prediction, probability = predict_patient(patient)

    st.subheader("Prediction Result")

    col1, col2 = st.columns(2)

    with col1:

        if prediction:
            st.error("🔴 High Risk")
        else:
            st.success("🟢 Low Risk")

    with col2:

        st.metric(
            "Risk Probability",
            f"{probability*100:.2f}%"
        )

    st.progress(probability)

    with st.spinner("Generating AI Clinical Summary..."):
        summary = generate_summary(
            patient,
            prediction,
            probability
        )

    with st.expander("AI Clinical Summary", expanded=True):

        st.markdown(summary)

    from datetime import datetime

    filename = f"MedIntel_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"

    generate_pdf(
        patient,
        prediction,
        probability,
        summary,
        filename
    )

    with open(filename, "rb") as file:

        st.download_button(
            label="📄 Download Clinical Report",
            data=file,
            file_name="MedIntel_Report.pdf",
            mime="application/pdf"
        )

    from src.database.database import save_prediction

    save_prediction(patient, prediction, probability)

st.info(
    "⚠️ This application is intended for educational and research purposes only and is not a substitute for professional medical advice."
)