# 💳 Credit Card Prediction System

An end-to-end Machine Learning web application that predicts whether a bank customer is likely to take a credit card based on demographic and financial behavior.

The project includes:

* Data preprocessing & feature engineering
* Machine learning model training (Random Forest)
* Streamlit web interface
* Docker containerization for deployment

---

## 📊 Problem Statement

Banks want to identify customers who are most likely to accept a credit card offer.
Instead of marketing to everyone, this model helps target potential customers and reduce marketing cost.

---

## 🚀 Features

* Predict credit card acceptance probability
* Interactive web UI using Streamlit
* Trained ML model using Scikit-Learn
* Fully containerized using Docker
* Ready for cloud deployment

---

## 🧠 Machine Learning Pipeline

1. Data Cleaning
2. Outlier Handling (IQR Winsorization)
3. Feature Engineering
4. Handling Class Imbalance (SMOTE)
5. Model Training (Random Forest Classifier)
6. Model Serialization using Joblib

---

## 📁 Project Structure

```
credit-card-app/
│── main.py                # Streamlit App
│── credit_model.pkl       # Trained Model
│── train_model.ipynb      # Training Notebook
│── requirements.txt
│── Dockerfile
│── .gitignore
│── .dockerignore
│── README.md
```

---

## 🖥️ Run Locally

### 1️⃣ Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Linux/Mac
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run app

```bash
streamlit run main.py
```

Open browser:

```
http://localhost:8501
```

---

## 🐳 Run with Docker

### Build Image

```bash
docker build -t creditcard-app .
```

### Run Container

```bash
docker run -p 8501:8501 creditcard-app
```

Open:

```
http://localhost:8501
```

---

## 📦 Model Features Used

* Age
* Experience
* Income
* Family
* Education
* CCAvg
* Mortgage
* Online
* Securities Account
* CD Account
* Income per family
* Debt indicator
* Spending ratio

---

## 📈 Example Output

The app predicts:

* Whether customer will take credit card
* Probability percentage

---

## 🛠️ Tech Stack

* Python
* Scikit-Learn
* Pandas & NumPy
* Streamlit
* Docker
* Joblib

---

## 📌 Future Improvements

* Deploy to cloud (Render / AWS)
* Add database logging
* Add batch prediction upload
* Improve model using XGBoost

---

## 👨‍💻 Author

**Kalyan Sai Atchi**

Full Stack AI Developer

---

## ⭐ If you like this project

Give it a star on GitHub!
