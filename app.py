import streamlit as st
import pandas as pd
import pickle

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🏠 House Price Prediction App")

# Input form
GrLivArea = st.number_input("Above Ground Living Area (sq ft)", min_value=100, max_value=5000)
OverallQual = st.selectbox("Overall Quality (1-10)", list(range(1, 11)))
GarageCars = st.selectbox("Number of Garage Cars", [0, 1, 2, 3, 4])
TotalBsmtSF = st.number_input("Basement Area (sq ft)", min_value=0, max_value=3000)

# When the user clicks "Predict"
if st.button("Predict Price"):
    input_df = pd.DataFrame([[GrLivArea, OverallQual, GarageCars, TotalBsmtSF]],
                            columns=["GrLivArea", "OverallQual", "GarageCars", "TotalBsmtSF"])
    prediction = model.predict(input_df)[0]
    st.success(f"Estimated House Price: ${prediction:,.0f}")
