import streamlit as st
import pandas as pd

st.title("Revenue & Expense Dashboard")

data = {
    "Month": ["Jan", "Feb", "Mar"],
    "Revenue": [1000, 1500, 2000],
    "Expense": [800, 900, 1200]
}

df = pd.DataFrame(data)

st.line_chart(df.set_index("Month"))
