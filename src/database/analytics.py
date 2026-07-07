import sqlite3
import pandas as pd

# Connect database
conn = sqlite3.connect("healthcare.db")

# 1. Total Patients
query1 = """
SELECT COUNT(*) AS total_patients
FROM patients
"""

# 2. Diabetes Distribution
query2 = """
SELECT diabetes, COUNT(*) AS count
FROM patients
GROUP BY diabetes
"""

# 3. Average Glucose by Diabetes
query3 = """
SELECT diabetes,
       AVG(blood_glucose_level) AS avg_glucose
FROM patients
GROUP BY diabetes
"""

# 4. Smoking vs Diabetes
query4 = """
SELECT smoking_history,
       COUNT(*) AS patient_count,
       AVG(diabetes) AS diabetes_rate
FROM patients
GROUP BY smoking_history
"""

# 5. BMI Risk Categories
query5 = """
SELECT
    CASE
        WHEN bmi < 18.5 THEN 'Underweight'
        WHEN bmi BETWEEN 18.5 AND 24.9 THEN 'Normal'
        WHEN bmi BETWEEN 25 AND 29.9 THEN 'Overweight'
        ELSE 'Obese'
    END AS bmi_category,
    COUNT(*) AS patient_count,
    AVG(diabetes) AS diabetes_rate
FROM patients
GROUP BY bmi_category
"""
# Execute queries
print("\nTOTAL PATIENTS")
print(pd.read_sql(query1, conn))

print("\nDIABETES DISTRIBUTION")
print(pd.read_sql(query2, conn))

print("\nAVERAGE GLUCOSE")
print(pd.read_sql(query3, conn))

print("\nSMOKING ANALYSIS")
print(pd.read_sql(query4, conn))

print("\nBMI ANALYSIS")
print(pd.read_sql(query5, conn))

#export clean data for powerbi 

full_df = pd.read_sql("SELECT * FROM patients", conn)

full_df.to_csv("data/processed/cleaned_healthcare_data.csv", index=False)

print("Processed CSV exported")