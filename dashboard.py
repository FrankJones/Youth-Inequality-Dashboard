import streamlit as st
import pandas as pd

# Load your pupil counts and percentages
# (replace with your real CSV paths or DataFrames)
results = pd.read_csv("Results_2019_2024.csv")  # your % pass rates by Year & Ethnicity

# Merge the two
merged = results.merge(pupils, on=["Year","Ethnicity"], how="left")

st.title("GCSE Attainment Dashboard")

# Dropdown to select Ethnicity
ethnicity = st.selectbox("Select ethnicity:", sorted(merged["Ethnicity"].unique()))

# Filter by year
year = st.selectbox("Select year:", sorted(merged["Year"].unique()))

df = merged[(merged["Ethnicity"] == ethnicity) & (merged["Year"] == year)]

if not df.empty:
    fsm = df["FSM %"].values[0]
    nonfsm = df["Non-FSM %"].values[0]
    st.write(f"**FSM:** {fsm:.1f}%")
    st.write(f"**Non-FSM:** {nonfsm:.1f}%")
    st.write(f"**Gap:** {(nonfsm - fsm):.1f} percentage points")

    st.bar_chart(pd.DataFrame({
        "FSM": [fsm],
        "Non-FSM": [nonfsm]
    }, index=[ethnicity]))
