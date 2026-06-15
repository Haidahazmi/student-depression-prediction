import streamlit as st

st.set_page_config(
    page_title="Student Depression Prediction System",
    page_icon="🎓",
    layout="wide"
)

st.markdown("""
<style>
.block-container {
    padding-top: 1.5rem;
    padding-bottom: 0rem;
    max-width: 1150px;
}

h1 {
    font-size: 34px !important;
    text-align: center;
}

h3 {
    font-size: 22px !important;
}

.description {
    text-align: center;
    font-size: 15px;
    color: #555;
    margin-bottom: 20px;
}

.footer {
    text-align: center;
    font-size: 13px;
    color: #777;
    margin-top: 10px;
}
</style>
""", unsafe_allow_html=True)

st.title("🎓 Student Depression Prediction System")

st.markdown(
    '<p class="description">A machine learning web application to support early detection of student depression risk.</p>',
    unsafe_allow_html=True
)

st.markdown("---")

left, right = st.columns([1.4, 1])

with left:
    st.markdown("### 📋 Student Input")

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", min_value=15, max_value=50, value=20)

        academic_pressure = st.slider(
            "Academic Pressure",
            min_value=0,
            max_value=5,
            value=3
        )

        financial_stress = st.slider(
            "Financial Stress",
            min_value=0,
            max_value=5,
            value=3
        )

    with col2:
        work_study_hours = st.slider(
            "Work / Study Hours",
            min_value=0,
            max_value=24,
            value=6
        )

        study_satisfaction = st.slider(
            "Study Satisfaction",
            min_value=0,
            max_value=5,
            value=3
        )

    predict = st.button("🔍 Predict Depression Risk", use_container_width=True)

with right:
    st.markdown("### 📊 Risk Summary")

    risk_score = academic_pressure + financial_stress + work_study_hours - study_satisfaction

    st.metric("Risk Score", risk_score)

    st.markdown("### 🧠 Prediction Result")

    if predict:
        if risk_score >= 8:
            st.error("⚠️ Depression Risk Detected")
            st.progress(90)
            st.warning("Recommendation: Student may require early support or counselling attention.")
        else:
            st.success("✅ Low Depression Risk")
            st.progress(35)
            st.info("Recommendation: Student shows lower depression risk based on the selected factors.")
    else:
        st.info("Click the prediction button to generate the result.")

st.markdown("---")

st.markdown(
    '<p class="footer">Developed for BCI3333 Machine Learning Applications | Student Mental Health and Burnout Detection</p>',
    unsafe_allow_html=True
)
