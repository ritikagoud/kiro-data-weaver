import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Weather vs Ice Cream Sales", layout="centered")

st.title("🍦 Weather vs Ice Cream Sales Dashboard")

st.write("This dashboard shows how temperature impacts ice cream sales.")

# Create fake weather data
data = {
    "Temperature (°C)": [20, 22, 25, 28, 30, 32, 35],
    "Ice Cream Sales": [120, 150, 180, 230, 280, 320, 380]
}

df = pd.DataFrame(data)

st.subheader("📊 Data Table")
st.dataframe(df)

st.subheader("📈 Temperature vs Ice Cream Sales")
st.line_chart(df.set_index("Temperature (°C)"))

st.success("Insight: Ice cream sales increase as temperature rises ☀️🍦")
