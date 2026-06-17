import streamlit as st
import pandas as pd
import joblib
import os
import numpy as np

# Check current folder
st.write("Running from:", os.getcwd())

# Load model and columns
model = joblib.load("flight_model.pkl")
training_columns = joblib.load("columns.pkl")

st.set_page_config(page_title="Flight Price Predictor", page_icon="✈")

st.title("✈ Flight Price Prediction App")
st.write("Enter flight details below to predict ticket price.")

# -------- INPUT FIELDS 

airline = st.selectbox(
    "Select Airline",
    ["IndiGo", "Air India", "Jet Airways", "Vistara", "Air Asia", "SpiceJet"]
)

source = st.selectbox(
    "Select Source",
    ["Delhi", "Kolkata", "Banglore", "Mumbai", "Chennai"]
)

destination = st.selectbox(
    "Select Destination",
    ["Cochin", "Delhi", "New Delhi", "Banglore", "Hyderabad", "Kolkata"]
)

duration = st.number_input("Duration (in minutes)", min_value=0)
stops = st.number_input("Total Stops", min_value=0, max_value=4)

journey_day = st.number_input("Journey Day", min_value=1, max_value=31)
journey_month = st.number_input("Journey Month", min_value=1, max_value=12)

dep_hour = st.number_input("Departure Hour (0-23)", min_value=0, max_value=23)
arrival_hour = st.number_input("Arrival Hour (0-23)", min_value=0, max_value=23)

# -------- PREDICTION

if st.button("Predict Price"):

    input_df = pd.DataFrame([{
        "Airline": airline,
        "Source": source,
        "Destination": destination,
        "Duration": duration,
        "Total_Stops": stops,
        "Journey_day": journey_day,
        "Journey_month": journey_month,
        "Dep_hour": dep_hour,
        "Arrival_hour": arrival_hour
    }])

    # Apply encoding
    input_df = pd.get_dummies(input_df)

    # Match training columns
    input_df = input_df.reindex(columns=training_columns, fill_value=0)

    # Predict (log value)
    log_prediction = model.predict(input_df)

    # Convert back to original price
    actual_price = np.expm1(log_prediction[0])

    st.success(f"Estimated Flight Price: ₹ {actual_price:,.0f}")
