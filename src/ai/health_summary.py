import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def generate_summary(patient, prediction, probability):
    prompt = f"""
    You are an experienced Healthcare Analytics Assistant helping clinicians interpret a machine learning prediction.

    The prediction comes from a trained Random Forest model.

    Patient Information

    Gender: {patient["gender"]}
    Age: {patient["age"]}

    BMI: {patient["bmi"]}

    HbA1c Level: {patient["hba1c_level"]}

    Blood Glucose Level: {patient["blood_glucose_level"]}

    Smoking History: {patient["smoking_history"]}

    Hypertension: {"Yes" if patient["hypertension"] else "No"}

    Heart Disease: {"Yes" if patient["heart_disease"] else "No"}

    Model Prediction:
    {"High Diabetes Risk" if prediction else "Low Diabetes Risk"}

    Probability:
    {probability*100:.2f}%

    Generate the response using exactly these sections:

    ## Clinical Summary

    Explain the overall risk.

    ## Major Risk Factors

    List the patient factors contributing to the prediction.

    ## Lifestyle Recommendations

    Provide 4 concise general wellness recommendations.

    ## Important Note

    Clearly state that this is an AI-generated educational summary and is not a medical diagnosis.
    """
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )   
    return response.text

from src.ml.predict import predict_patient

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

    summary = generate_summary(
        patient,
        prediction,
        probability
    )

    print(summary)