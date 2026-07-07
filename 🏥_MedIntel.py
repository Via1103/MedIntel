import streamlit as st

st.set_page_config(
    page_title="MedIntel",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 MedIntel")
st.subheader("AI-Powered Healthcare Analytics Platform")

st.markdown("---")

st.markdown("""
Welcome to **MedIntel**, an end-to-end Healthcare Analytics Platform.

This project combines:

- 📊 Power BI Dashboard
- 🤖 Machine Learning
- 🧠 Gemini AI
- 🗄️ SQL Database
- ⚙️ Python ETL Pipeline

Use the navigation menu on the left to explore the application.
""")

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Model Accuracy", "96%")

with col2:
    st.metric("Patients", "96K")

with col3:
    st.metric("Prediction Model", "Random Forest")



st.success("Project developed for Healthcare Analytics & Clinical Decision Support.")

