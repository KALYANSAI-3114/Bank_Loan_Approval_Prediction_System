import streamlit as st
import joblib
import pandas as pd

# ---------------- LOAD MODEL ---------------- #
@st.cache_resource
def load_model():
    data = joblib.load("credit_card_approval_model.pkl")
    return data["model"], data["features"]

model, features = load_model()

# ---------------- UI ---------------- #
st.title("💳 Credit Card Prediction")

Age = st.number_input("Age",18,80,30)
Experience = st.number_input("Experience",0,50,5)
Income = st.number_input("Income",10,500,50)
Family = st.selectbox("Family Members",[1,2,3,4])
Education = st.selectbox("Education",[1,2,3])
CCAvg = st.number_input("CC Average Spending",0.0,10.0,2.0)
Mortgage = st.number_input("Mortgage",0,1000,0)
Online = st.selectbox("Online Banking",[0,1])
Securities_Account = st.selectbox("Securities Account",[0,1])
CD_Account = st.selectbox("CD Account",[0,1])

Income_per_family = Income/Family
Debt_indicator = Mortgage/(Income+1)
Spending_ratio = CCAvg/(Income+1)

if st.button("Predict"):

    input_dict = {
        "Age":Age,
        "Experience":Experience,
        "Income":Income,
        "Family":Family,
        "Education":Education,
        "CCAvg":CCAvg,
        "Mortgage":Mortgage,
        "Online":Online,
        "Securities.Account":Securities_Account,
        "CD.Account":CD_Account,
        "Income_per_family":Income_per_family,
        "Debt_indicator":Debt_indicator,
        "Spending_ratio":Spending_ratio
    }

    input_df = pd.DataFrame([input_dict])
    input_df = input_df.reindex(columns=features, fill_value=0)

    pred = model.predict(input_df)[0]
    prob = model.predict_proba(input_df)[0][1]

    if pred == 1:
        st.success(f"Customer likely to take Credit Card ✅ ({prob*100:.2f}%)")
    else:
        st.error(f"Customer unlikely to take Credit Card ❌ ({prob*100:.2f}%)")
