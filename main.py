import streamlit as st
from dotenv import load_dotenv
import os
import pandas as pd
import matplotlib.pyplot as plt
import google.generativeai as genai
from utils.data_cleaning import clean_financial_data

# Load API key
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

# Page title and header
st.set_page_config(page_title="Financial Simplified", layout="wide")
st.title("Finance Simplified")
st.markdown("Upload your raw financial CSV data to get AI insights and interactive visualizations.")
st.divider()

# Sidebar for controls
st.sidebar.header("Upload & Settings")
uploaded_file = st.sidebar.file_uploader("Upload CSV file", type=["csv"])

# Only show the rest if a file is uploaded
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    processed_df = clean_financial_data(df)

    # Tabs
    tab1, tab2, tab3, tab4 = st.tabs(
        ["Raw Data", "Processed Data", "Graphical Illustrations", "AI Insights"]
    )

    # ---------------- Tab 1: Raw Data ----------------
    with tab1:
        with st.expander("Show Raw Data"):
            st.dataframe(df)
        st.caption(f"Columns detected: {', '.join(df.columns)}")

    # ---------------- Tab 2: Processed Data ----------------
    with tab2:
        with st.expander("Show Cleaned Data"):
            st.dataframe(processed_df)
        st.caption(f"Columns detected: {', '.join(processed_df.columns)}")

        # Display basic metrics
        numeric_cols = processed_df.select_dtypes(include="number").columns
        if len(numeric_cols) > 0:
            st.markdown("### Key Metrics")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Min Value", processed_df[numeric_cols].min().min())
            with col2:
                st.metric("Max Value", processed_df[numeric_cols].max().max())
            with col3:
                st.metric("Mean Value", round(processed_df[numeric_cols].mean().mean(), 2))

    # ---------------- Tab 3: Graphical Illustrations ----------------
    with tab3:
        st.subheader("Interactive Graphs")

        numeric_cols = processed_df.select_dtypes(include="number").columns
        if len(numeric_cols) > 0:
            x_col = st.selectbox("Select X-axis", numeric_cols, key="x_axis")
            y_col = st.selectbox("Select Y-axis", numeric_cols, key="y_axis")
            chart_type = st.selectbox(
                "Select Chart Type",
                ("Line", "Bar", "Area", "Scatter", "Pie"),
                key="chart_type"
            )

            fig, ax = plt.subplots(figsize=(8, 5))

            if chart_type == "Line":
                ax.plot(processed_df[x_col], processed_df[y_col], marker='o', linestyle='-')
            elif chart_type == "Bar":
                ax.bar(processed_df[x_col], processed_df[y_col], color='skyblue')
            elif chart_type == "Area":
                ax.fill_between(processed_df[x_col], processed_df[y_col], color='orange', alpha=0.6)
            elif chart_type == "Scatter":
                ax.scatter(processed_df[x_col], processed_df[y_col], color='green')
            elif chart_type == "Pie":
                counts = processed_df.groupby(x_col)[y_col].sum()
                ax.pie(counts.values, labels=counts.index, autopct="%1.1f%%", startangle=90)
                ax.axis("equal")  # Keep pie chart circular

            ax.set_title(f"{chart_type} Plot of {y_col} vs {x_col}")
            ax.set_xlabel(x_col)
            ax.set_ylabel(y_col)
            st.pyplot(fig)
        else:
            st.warning("No numeric columns found to generate plots.")

    # ---------------- Tab 4: AI Insights ----------------
    with tab4:
        st.subheader("AI Analysis")
        prompt = f"""
You are a financial data analyst AI. Analyze the following dataset provided in CSV format.
Your analysis should include:

1. A concise summary of the dataset (number of rows, columns, and types of data).
2. Key statistics for numeric columns (min, max, mean, totals).
3. Detection of trends, anomalies, or outliers.
4. Insights on categorical columns, including top categories or most frequent values.
5. Suggestions for interesting visualizations or patterns to explore.

Provide your response in a clear, structured, and reader-friendly format.

Dataset:
{processed_df.to_csv(index=False)}

Data:
{processed_df.to_csv(index=False)}
"""
        try:
            model = genai.GenerativeModel("models/gemini-2.5-pro")
            response = model.generate_content(prompt)
            st.markdown("### AI Suggestions")
            st.write(response.text)
        except Exception as e:
            st.error(f"Error from Gemini: {str(e)}")

else:
    st.info("Please upload a CSV file in the sidebar to get started.")
