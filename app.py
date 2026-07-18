import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Finance Dashboard", layout="wide")

st.title("💰 Revenue & Expense Dashboard")

# Upload file
uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx", "csv"])

if uploaded_file:
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.subheader("📊 Data Preview")
    st.dataframe(df)

    # Assume columns: Month, Revenue, Expense
    st.subheader("📈 Chart")

    fig, ax = plt.subplots()
    ax.plot(df["Month"], df["Revenue"], marker='o', label="Revenue")
    ax.plot(df["Month"], df["Expense"], marker='o', label="Expense")
    ax.legend()

    st.pyplot(fig)

    # Profit
    df["Profit"] = df["Revenue"] - df["Expense"]

    st.subheader("💰 Profit Table")
    st.dataframe(df)

    st.success("Analysis Complete ✅")

else:
    st.info("Please upload a file to start")
