import joblib
import pandas as pd

model = joblib.load("models/diabetes_model.pkl")
encoders = joblib.load("models/encoders.pkl")


def predict_patient(patient):
    patient_df = pd.DataFrame([patient])

    categorical_cols = [
        "gender",
        "smoking_history",
        "bmi_category",
        "age_group"
    ]

    for col in categorical_cols:
        patient_df[col] = encoders[col].transform(patient_df[col])

    prediction = model.predict(patient_df)[0]
    probability = model.predict_proba(patient_df)[0][1]

    return prediction, probability

if __name__ == "__main__":

    patient = {
        "gender": "Female",
        "age": 58,
        "hypertension": 1,
        "heart_disease": 0,
        "smoking_history": "former",
        "bmi": 32.5,
        "hba1c_level": 7.1,
        "blood_glucose_level": 185,
        "bmi_category": "Obese",
        "age_group": "41-60"
    }

    prediction, probability = predict_patient(patient)

    print("=" * 50)
    print("Diabetes Prediction")
    print("=" * 50)

    print(
        "Prediction:",
        "Diabetic" if prediction == 1 else "Non-Diabetic"
    )

    print(f"Risk Probability: {probability*100:.2f}%")