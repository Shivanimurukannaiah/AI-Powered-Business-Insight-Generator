

import streamlit as st
from src.data_loader import load_data
from src.analyzer import summarize_data
from src.insight_generator import generate_insights

st.title("AI-Powered Business Insight Generator")

uploaded_file = st.file_uploader("Upload your CSV file", type="csv")

if uploaded_file:
    df = load_data(uploaded_file)
    st.write("### Data Preview", df.head())

    if st.button("Generate Insights"):
        summary = summarize_data(df)
        insights = generate_insights(summary)
        st.write("### Insights", insights)
