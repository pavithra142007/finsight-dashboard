import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page setup
st.set_page_config(page_title="Finance Dashboard", layout="wide")

st.title("📊 Revenue & Expense Dashboard")

# File upload
uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx"])

if uploaded_file is not None:
    try:
        df = pd.read_excel(uploaded_file, engine="openpyxl")

        # Clean column names
        df.columns = df.columns.str.strip()

        st.subheader("📄 Data Preview")
        st.dataframe(df)

        # Check required columns
        if "Revenue" not in df.columns or "Expense" not in df.columns:
            st.error("❌ Excel must contain 'Revenue' and 'Expense' columns")
        else:
            # Convert to numeric (safe)
            df["Revenue"] = pd.to_numeric(df["Revenue"], errors='coerce')
            df["Expense"] = pd.to_numeric(df["Expense"], errors='coerce')

            # Drop null values
            df = df.dropna(subset=["Revenue", "Expense"])

            # Calculations
            total_revenue = df["Revenue"].sum()
            total_expense = df["Expense"].sum()
            profit = total_revenue - total_expense

            # Metrics
            col1, col2, col3 = st.columns(3)
            col1.metric("💰 Total Revenue", f"{total_revenue:,.2f}")
            col2.metric("💸 Total Expense", f"{total_expense:,.2f}")
            col3.metric("📈 Profit", f"{profit:,.2f}")

            # Chart
            st.subheader("📊 Revenue vs Expense Chart")

            fig, ax = plt.subplots()
            df[["Revenue", "Expense"]].plot(kind="bar", ax=ax)
            plt.xticks(rotation=0)
            st.pyplot(fig)

    except Exception as e:
        st.error(f"⚠️ Error reading file: {e}")

else:
    st.info("📂 Please upload an Excel file to start")
