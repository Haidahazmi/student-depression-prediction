import streamlit as st

st.title("Student Depression Prediction System")

st.write("Enter student information below:")

age = st.number_input("Age", min_value=15, max_value=50, value=20)
academic_pressure = st.slider("Academic Pressure", 0, 5, 3)
study_satisfaction = st.slider("Study Satisfaction", 0, 5, 3)
work_study_hours = st.number_input("Work/Study Hours", min_value=0, max_value=24, value=6)
financial_stress = st.slider("Financial Stress", 0, 5, 3)

if st.button("Predict"):
    risk_score = academic_pressure + financial_stress + work_study_hours - study_satisfaction

    if risk_score >= 8:
        st.error("Prediction Result: Depression")
    else:
        st.success("Prediction Result: Not Depression")