import streamlit as st
import pandas as pd
import pickle

# Load model
with open("rf_delay_model.pkl", "rb") as file:
    model = pickle.load(file)

# Load test data with metadata
df = pd.read_csv("test_data.csv")

# Fill NaNs if any project names were missing in original data
df['name'] = df['name'].fillna("Unnamed Task")
df['project_name'] = df['project_name'].fillna("Unknown Project")

st.title("🚀 Task Delay Prediction Interface")
st.write("Select a task to view its predicted and actual delay.")

# Create custom display string
df['display_name'] = df['name'] + " (Project: " + df['project_name'] + ")"

# Dropdown with index=1 as default
selected_index = st.selectbox(
    "Choose a Task",
    options=df.index,
    format_func=lambda i: df.loc[i, "display_name"],
    index=1
)

# Display prediction results
row = df.loc[selected_index]
st.subheader("📊 Prediction Results")
st.write(f"**Task Name:** {row['name']}")
st.write(f"**Project Name:** {row['project_name']}")
st.write(f"**Predicted Delay:** `{row['predicted_delay']:.2f}` days")
st.write(f"**Actual Delay:** `{row['actual_delay']:.2f}` days")
st.metric(label="Prediction Error", value=f"{row['predicted_delay'] - row['actual_delay']:.2f} days")
