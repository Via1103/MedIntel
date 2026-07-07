import pandas as pd
from sqlalchemy import create_engine

# Extract
df = pd.read_csv("data/raw/diabetes_prediction_dataset.csv")

print(df.head())

# Transform

# Remove duplicates
df = df.drop_duplicates()

# Standardize column names
df.columns = [col.lower() for col in df.columns]

# Handle missing values
df = df.fillna(df.mean(numeric_only=True))

# Create BMI Category
def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

df["bmi_category"] = df["bmi"].apply(bmi_category)

# Create Age Group
def age_group(age):
    if age < 20:
        return "0-20"
    elif age < 40:
        return "21-40"
    elif age < 60:
        return "41-60"
    else:
        return "60+"

df["age_group"] = df["age"].apply(age_group)

# Risk Score Feature
df["risk_score"] = (
    df["bmi"] * 0.3 +
    df["blood_glucose_level"] * 0.5 +
    df["age"] * 0.2
)

# Load
engine = create_engine("sqlite:///../../healthcare.db")

# Save processed CSV
df.to_csv("data/processed/cleaned_healthcare_data.csv", index=False)

# Save processed SQL database
df.to_sql("data/processed/cleaned_healthcare_data.csv", engine, if_exists="replace", index=False)

print("ETL Pipeline Completed")
print(df.columns.tolist())

print(df[['bmi_category','age_group','risk_score']].head())