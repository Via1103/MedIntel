# 🏥 MedIntel

**An AI-powered Healthcare Analytics Platform built using Python, Power BI, Machine Learning, Streamlit, SQLite, and Google Gemini AI.**

MedIntel combines data analytics and machine learning to analyze healthcare data, predict diabetes risk, and generate AI-powered clinical summaries through an interactive web application.

---

## 📌 About the Project

Healthcare organizations generate a huge amount of patient data every day. The goal of this project was to build a complete analytics workflow that transforms raw healthcare data into meaningful insights and predictive models.

The project starts with cleaning and transforming patient records using Python, stores the processed data in SQLite, visualizes healthcare trends in Power BI, predicts diabetes risk using a Random Forest model, and uses Google's Gemini API to generate an easy-to-understand clinical summary for each prediction.

Instead of building separate dashboards and machine learning notebooks, I wanted to combine everything into one application that demonstrates the complete data analytics lifecycle.

---

## ✨ Features

- Healthcare ETL pipeline using Pandas
- Data cleaning and feature engineering
- SQLite database integration
- Interactive Power BI dashboard
- Diabetes risk prediction using Random Forest
- AI-generated clinical summaries using Gemini AI
- PDF clinical report generation
- Prediction history stored in SQLite
- Multi-page Streamlit web application

---

## 🛠 Tech Stack

| Category | Technologies |
|----------|--------------|
| Programming | Python |
| Data Processing | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| Database | SQLite |
| Dashboard | Power BI |
| Web App | Streamlit |
| AI | Google Gemini API |
| Reports | ReportLab |

---

## 🏗 Project Architecture

```
Raw Dataset
      │
      ▼
ETL Pipeline
      │
      ▼
SQLite Database
      │
 ┌────┴─────────┐
 │              │
 ▼              ▼
Power BI    Machine Learning
Dashboard   (Random Forest)
                  │
                  ▼
         Diabetes Prediction
                  │
                  ▼
         Gemini AI Summary
                  │
                  ▼
        PDF Clinical Report
                  │
                  ▼
          Streamlit Application
```

---

## 📊 Dashboard

The Power BI dashboard provides an overview of patient demographics and diabetes-related trends.

It includes:

- Diabetes prevalence
- BMI distribution
- Age group analysis
- Smoking history
- Hypertension analysis
- Blood glucose insights

> *(Dashboard screenshot goes here)*

---

## 🤖 Machine Learning

The prediction model was trained using a Random Forest Classifier.

### Model Performance

| Metric | Score |
|--------|-------|
| Accuracy | 95.84% |
| Precision | 78% |
| Recall | 74% |
| F1 Score | 76% |

### Most Important Features

- HbA1c Level
- Blood Glucose Level
- Age
- BMI
- Smoking History

---

## 🧠 AI Clinical Summary

After predicting diabetes risk, the application uses the Google Gemini API to generate a concise clinical summary.

The summary highlights:

- Possible risk factors
- Clinical interpretation
- Lifestyle recommendations
- Preventive suggestions

---

## 📄 PDF Report

Users can download a clinical report containing:

- Patient information
- Prediction result
- Risk probability
- AI-generated clinical summary
- Recommendations
- Report generation date and time

---

## 📂 Project Structure

```
MedIntel/
│
├── app.py
├── dashboard/
├── data/
├── models/
├── pages/
├── reports/
├── src/
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

Clone the repository

```bash
git clone https://github.com/yourusername/MedIntel.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 💡 Future Improvements

Some features I would like to add in the future:

- Batch prediction using CSV upload
- Explainable AI using SHAP
- REST API with FastAPI
- Docker support
- Cloud deployment on Azure
- User authentication
- Real-time healthcare analytics

---

## 👩‍💻 Author

**Vineeta Sharma**

B.Tech Computer Science Engineering (AI)

If you have any suggestions or feedback, feel free to connect with me on LinkedIn.