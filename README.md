# 🏥 Healthcare Insurance Cost Prediction using Machine Learning

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange.svg)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green.svg)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-blue.svg)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## 📖 Project Overview

Healthcare insurance providers need to estimate medical insurance costs based on an individual's demographic, lifestyle, and medical information. Manual estimation can be inconsistent and time-consuming.

This project develops a Machine Learning regression model capable of predicting healthcare insurance charges using patient information. It follows a complete end-to-end Machine Learning pipeline — from data preprocessing and exploratory data analysis to model training, evaluation, and deployment.

---

## 🎯 Problem Statement

Healthcare insurance costs are influenced by several factors such as:

- Age
- Gender
- BMI
- Smoking Habit
- Exercise Frequency
- Chronic Diseases
- Medical History
- Lifestyle Factors

The objective of this project is to build a regression model that accurately predicts insurance costs while identifying the most influential factors affecting medical expenses.

---

## 🎯 Project Objectives

- Analyze healthcare insurance data
- Understand factors affecting insurance charges
- Perform data cleaning and preprocessing
- Build multiple Machine Learning regression models
- Compare model performance
- Tune the best-performing model
- Predict insurance costs for new customers
- Deploy the final model using Streamlit

---

## 📊 Dataset

**Source:** Kaggle

The dataset contains healthcare insurance records with demographic, medical, and lifestyle information.

| Feature | Description |
|---|---|
| Age | Age of the individual |
| Gender | Male / Female |
| BMI | Body Mass Index |
| Smoking Status | Smoker / Non-smoker |
| Exercise Frequency | Activity level |
| Alcohol Consumption | Consumption level |
| Chronic Diseases | Presence of chronic illness |
| Blood Pressure | Blood pressure reading |
| Diabetes | Diabetic status |
| Region | Geographic region |
| Income | Income level |
| **Insurance Charges** | 🎯 Target variable |

---

## 📂 Project Structure

```text
Healthcare-Insurance-Cost-Prediction/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│
├── src/
│   ├── data/
│   ├── features/
│   ├── models/
│   └── utils/
│
├── models/
│
├── reports/
│
├── app/
│
├── README.md
├── requirements.txt
├── .gitignore
└── main.py
```

---

## 🚀 Machine Learning Workflow

```text
Dataset
   │
   ▼
Data Understanding
   │
   ▼
Data Cleaning
   │
   ▼
Exploratory Data Analysis
   │
   ▼
Feature Engineering
   │
   ▼
Data Preprocessing
   │
   ▼
Train-Test Split
   │
   ▼
Model Training
   │
   ▼
Model Evaluation
   │
   ▼
Hyperparameter Tuning
   │
   ▼
Final Model
   │
   ▼
Prediction
   │
   ▼
Streamlit Deployment
```

---

## 🔄 Full Pipeline Flow

```text
Raw Dataset (Kaggle)
        |
        | Load & Inspect
        v
  Data Understanding
        |
        | Handle missing values, duplicates, dtypes
        v
   Data Cleaning
        |
        |--------------------------------------------------|
        |                                                  |
        |  Exploratory Data Analysis                       |
        |  ----------------------------------------------  |
        |  1. Distribution analysis                        |
        |  2. Outlier detection                             |
        |  3. Correlation analysis                          |
        |  4. Feature relationship analysis                 |
        |  ----------------------------------------------  |
        |                                                  |
        |  Feature Engineering                             |
        |  ----------------------------------------------  |
        |  1. BMI categories                                |
        |  2. Age groups                                    |
        |  3. Lifestyle risk score                           |
        |  4. Medical risk indicators                        |
        |  ----------------------------------------------  |
        |
        v
  Data Preprocessing
        |
        | Encoding, scaling, train-test split
        v
  Model Training
        |
        |-----------------------------------------------|
        |                                               |
        |  Linear Regression   Decision Tree            |
        |  Random Forest       Gradient Boosting         |
        |  Extra Trees         XGBoost (optional)        |
        |-----------------------------------------------|
        |
        v
  Model Evaluation
        |
        |  MAE · MSE · RMSE · R² Score
        |
        v
  Hyperparameter Tuning
        |
        v
     Final Model
        |
        v
  ---------------- DEPLOYMENT ----------------
        |
        |  Streamlit Web Application
        |    - User input form
        |    - Real-time prediction
        |    - Results visualization
```

---

## 📌 Project Status

| Phase | Status |
|--------|--------|
| Project Setup | ✅ Completed |
| Dataset Understanding | ⏳ In Progress |
| Exploratory Data Analysis | ⏳ Pending |
| Data Cleaning | ⏳ Pending |
| Feature Engineering | ⏳ Pending |
| Model Training | ⏳ Pending |
| Model Comparison | ⏳ Pending |
| Hyperparameter Tuning | ⏳ Pending |
| Model Evaluation | ⏳ Pending |
| Deployment | ⏳ Pending |

---

## 🛠 Technical Stack

| Category | Tools |
|-----------|------|
| **Programming** | Python |
| **Data Processing** | Pandas, NumPy |
| **Visualization** | Matplotlib, Seaborn |
| **Machine Learning** | Scikit-learn |
| **Model Saving** | Joblib |
| **Development** | Jupyter Notebook, VS Code |
| **Version Control** | Git, GitHub |
| **Deployment** | Streamlit (Upcoming) |

---

## 📚 Exploratory Data Analysis

The following analysis will be performed:

- Dataset overview
- Missing value analysis
- Duplicate detection
- Data type verification
- Distribution analysis
- Outlier detection
- Correlation analysis
- Feature relationship analysis

---

## 🧹 Data Preprocessing

The preprocessing pipeline will include:

- Missing value handling
- Duplicate removal
- Categorical encoding
- Feature scaling
- Train-test split
- Pipeline creation

---

## ⚙️ Feature Engineering

Planned feature engineering includes:

- BMI categories
- Age groups
- Lifestyle risk score
- Medical risk indicators
- Additional derived features

---

## 🤖 Machine Learning Models

The following regression models will be trained and compared:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor
- Extra Trees Regressor
- XGBoost (optional)

---

## 📈 Model Evaluation Metrics

The models will be evaluated using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

---

## 📊 Model Comparison

A detailed comparison of all trained models will be included after training.

| Model | MAE | RMSE | R² Score |
|-------|-----|------|-----------|
| Linear Regression | Coming Soon | Coming Soon | Coming Soon |
| Decision Tree | Coming Soon | Coming Soon | Coming Soon |
| Random Forest | Coming Soon | Coming Soon | Coming Soon |
| Gradient Boosting | Coming Soon | Coming Soon | Coming Soon |
| Extra Trees | Coming Soon | Coming Soon | Coming Soon |

---

## 💡 Prediction Example

### Input

```text
Age: 35
Gender: Male
BMI: 28.5
Smoker: Yes
Exercise Frequency: Regular
Region: Southeast
```

### Output

```text
Predicted Insurance Cost: Coming Soon...
```

---

## 📱 Streamlit Application

A user-friendly web application will allow users to:

- Enter healthcare information
- Predict insurance costs instantly
- View prediction results and key influencing factors

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/<your-username>/Healthcare-Insurance-Cost-Prediction.git
```

Navigate into the project

```bash
cd Healthcare-Insurance-Cost-Prediction
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the environment

**Windows**
```bash
.venv\Scripts\activate
```

**Linux / macOS**
```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

Open Jupyter Notebook

```bash
jupyter notebook
```

or run the main pipeline directly

```bash
python main.py
```

---

## 📋 Future Improvements

- Add feature selection
- Hyperparameter optimization
- SHAP explainability
- Cross validation
- Docker deployment
- FastAPI integration
- Cloud deployment
- Real-time prediction API

---

## 💼 Interview Talking Point

> Developed an end-to-end Machine Learning solution to predict healthcare insurance costs using patient demographic, lifestyle, and medical information. The project includes data preprocessing, exploratory data analysis, feature engineering, model comparison, hyperparameter tuning, and deployment planning following industry-standard machine learning practices.

---

## 📌 Current Progress

✅ Project setup completed

🚧 Currently working on:
- Dataset understanding
- Exploratory data analysis

---

## ⭐ Repository Goals

- Beginner friendly
- Recruiter friendly
- ATS friendly
- Industry-standard project structure
- End-to-end Machine Learning pipeline

---

## 👨‍💻 Author

**Siva**

AI & Data Science Student

Interested in:
- Data Analytics
- Machine Learning
- Python
- SQL
- Power BI

---

⭐ If you find this project useful, consider giving it a star!