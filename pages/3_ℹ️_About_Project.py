import sqlite3
import pandas as pd
import streamlit as st

st.title("About Project")


st.markdown("---")
st.header("🛠 Technology Stack")

st.markdown("""
| Category | Technologies |
|-----------|--------------|
| Programming | Python |
| Data Processing | Pandas, NumPy |
| Database | SQLite |
| Data Visualization | Power BI |
| Machine Learning | Scikit-learn (Random Forest) |
| AI | Google Gemini API |
| Web Application | Streamlit |
| Report Generation | ReportLab |
""")

st.markdown("---")
st.header("🏗 Project Architecture")

st.code("""
Raw Healthcare Dataset
        │
        ▼
Python ETL Pipeline
(Data Cleaning + Feature Engineering)
        │
        ▼
SQLite Database
        │
        ├──────────────► Power BI Dashboard
        │
        ▼
Machine Learning Model
(Random Forest)
        │
        ▼
Risk Prediction
        │
        ▼
Gemini AI Clinical Summary
        │
        ▼
PDF Report Generation
        │
        ▼
Streamlit Web Application
""")


st.markdown("---")
st.header("✨ Key Features")

st.markdown("""
- Interactive Power BI Healthcare Dashboard
- Automated ETL Pipeline
- Feature Engineering
- Diabetes Risk Prediction using Machine Learning
- AI-generated Clinical Summary using Google Gemini
- Downloadable Clinical PDF Reports
- SQLite Prediction History
- Interactive Streamlit Interface
""")

st.markdown("---")
st.header("📈 Machine Learning Performance")

st.markdown("""
### Random Forest Classifier

| Metric | Score |
|---------|-------|
| Accuracy | **95.84%** |
| Precision | **78%** |
| Recall | **74%** |
| F1 Score | **76%** |

The model was trained on approximately **96,000 patient records** using clinical and demographic features including age, BMI, HbA1c level, blood glucose level, smoking history, hypertension, and heart disease.
""")

st.markdown("---")
st.header("🔬 Most Important Features")

st.markdown("""
Based on feature importance analysis from the Random Forest model:

1. 🩸 HbA1c Level
2. 🧪 Blood Glucose Level
3. 👤 Age
4. ⚖️ BMI
5. 🚬 Smoking History
6. ❤️ Hypertension
7. ❤️ Heart Disease

These variables contributed most significantly to diabetes risk prediction.
""")

st.markdown("---")
st.header("🔄 Complete Workflow")

st.markdown("""
1. Load healthcare dataset.
2. Clean and preprocess patient data.
3. Engineer clinical risk features.
4. Store processed data in SQLite.
5. Build interactive Power BI dashboard.
6. Train Random Forest prediction model.
7. Predict diabetes risk for new patients.
8. Generate AI-powered clinical interpretation using Gemini.
9. Export professional PDF clinical reports.
10. Save prediction history for future reference.
""")

st.markdown("---")
st.header("🚀 Future Enhancements")

st.markdown("""
- Batch prediction using uploaded CSV files
- REST API using FastAPI
- Docker containerization
- Cloud deployment on AWS/Azure
- Role-based authentication
- Integration with Electronic Health Records (EHR)
- Explainable AI (SHAP values)
- Real-time analytics dashboard
""")

st.markdown("---")

st.success(
"""
Developed as an end-to-end Healthcare Analytics and Machine Learning project demonstrating skills in Data Engineering, Business Intelligence, Predictive Analytics, Generative AI, and Full-Stack Data Application Development.
"""
)

st.markdown("---")
st.header("💼 Business Impact")

st.markdown("""
This platform demonstrates how healthcare organizations can combine analytics, machine learning, and generative AI to support clinical decision-making. By identifying high-risk patients, visualizing health trends, and generating AI-assisted clinical summaries, MedIntel showcases practical applications of data-driven healthcare solutions that can improve preventive care, optimize resource allocation, and assist healthcare professionals in making informed decisions.
""")