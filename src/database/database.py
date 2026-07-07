import sqlite3
from datetime import datetime

def save_prediction(patient, prediction, probability):
    conn = sqlite3.connect("healthcare.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS prediction_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        gender TEXT,
        age INTEGER,
        bmi REAL,
        hba1c REAL,
        blood_glucose REAL,
        prediction TEXT,
        probability REAL
    )
    """)

    cursor.execute("""
    INSERT INTO prediction_history(
        timestamp,
        gender,
        age,
        bmi,
        hba1c,
        blood_glucose,
        prediction,
        probability
    )
    VALUES (?,?,?,?,?,?,?,?)
    """, (
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        patient["gender"],
        patient["age"],
        patient["bmi"],
        patient["hba1c_level"],
        patient["blood_glucose_level"],
        "High Risk" if prediction else "Low Risk",
        probability * 100
    ))

    conn.commit()
    conn.close()