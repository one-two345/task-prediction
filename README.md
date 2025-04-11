

```markdown
# 🚀 Task Delay Prediction App

This project is a machine learning web application built with **Streamlit** to predict delays in project tasks using a trained **Random Forest Regression** model. It provides a user-friendly interface to compare actual vs predicted delay days for project tasks, based on historical task data.

---

## 📁 Project Structure

```
task-delay-prediction/
│
├── rf_delay_model.pkl       # Trained Random Forest model
├── test_data.csv            # Test set with actual + predicted delay and metadata
├── app.py                   # Streamlit app
├── preprocess_and_train.py  # Script for data cleaning, encoding, training and exporting
├── README.md                # This file
```

---

## ⚙️ Features

- Predict delay in days for any project task.
- Interactive dropdown to select a task.
- Displays:
  - Task Name
  - Project Name
  - Predicted vs Actual Delay
  - Prediction Error metric
- Automatically handles missing values and encodes categorical data.

---

## 🧪 Dataset

The dataset includes project task records with features such as:
- `status`, `milestone_name`, `project_name`
- `planned_start`, `delay_days`, etc.

The target variable is `delay_days`.

---

## 🚀 How to Run the App

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/task-delay-prediction.git
cd task-delay-prediction
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt`, install manually:
```bash
pip install streamlit pandas numpy scikit-learn
```

### 3. Run the App

```bash
streamlit run app.py
```

Then open the provided `localhost` URL in your browser.

---

## 🛠️ How It Works

- `preprocess_and_train.py` handles:
  - Cleaning the dataset
  - Encoding categorical variables
  - Splitting data into training/test sets
  - Training the Random Forest model
  - Making predictions
  - Saving the model and test results (with task name and project name)

- `app.py` loads the model and the test data, and displays the prediction results interactively via Streamlit.

---

## 📦 Model Info

- Model: `RandomForestRegressor`
- Trained using `scikit-learn`
- Features include one-hot encoded task statuses, milestone names, and project names.

---

## 🧑‍💻 Author

**Tekilemaryam Shewamnil Sisay**

Feel free to reach out via [teklemariamshewamnil@gmail.com](mailto:teklemariamshewamnil@gmail.com) for questions or collaboration.

---

