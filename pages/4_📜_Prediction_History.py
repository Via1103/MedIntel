import sqlite3
import pandas as pd
import streamlit as st

st.title("📜 Prediction History")

conn = sqlite3.connect("healthcare.db")

df = pd.read_sql(
    "SELECT * FROM prediction_history ORDER BY id DESC",
    conn
)

conn.close()

st.dataframe(df, use_container_width=True)