import streamlit as st
import pandas as pd
import pickle

# Load model
with open("rf_delay_model.pkl", "rb") as file:
    model = pickle.load(file)

# Load test data with metadata
df = pd.read_csv("test_data.csv")

st.title("🚀 Task Delay Prediction Interface")
st.write("Select a task to view the predicted vs actual delay in days.")

# Combine name + project for display
df['display_name'] = df['name'] + " " +" (Project: " + df['project_name'] + ")"

# Dropdown with default index = 1
selected_index = st.selectbox(
    "Choose a Task",
    options=df.index,
    format_func=lambda i: df.loc[i, "display_name"],
    index=2,
    key="task_selector"
)


# Show results
row = df.loc[selected_index]
st.subheader("📊 Prediction Results")
st.write(f"**Task Name:** {row['name']}")
st.write(f"**Project Name:** {row['project_name']}")
st.write(f"**Predicted Delay:** `{row['predicted_delay']:.2f}` days")
st.write(f"**Actual Delay:** `{row['actual_delay']:.2f}` days")
st.metric(label="Prediction Error", value=f"{row['predicted_delay'] - row['actual_delay']:.2f} days")
