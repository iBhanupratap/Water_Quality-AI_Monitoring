import pandas as pd
import streamlit as st
import joblib

# Load trained model
model = joblib.load("model.pkl")

st.title("💧 Water Quality Monitoring System")

st.write("AI-powered Water Potability Prediction")

ph = st.number_input("pH", value=7.0)
hardness = st.number_input("Hardness", value=200.0)
solids = st.number_input("Solids", value=20000.0)
chloramines = st.number_input("Chloramines", value=7.0)
sulfate = st.number_input("Sulfate", value=300.0)
conductivity = st.number_input("Conductivity", value=400.0)
organic_carbon = st.number_input("Organic Carbon", value=14.0)
trihalomethanes = st.number_input("Trihalomethanes", value=70.0)
turbidity = st.number_input("Turbidity", value=4.0)



if st.button("Predict Water Quality"):

    input_data = pd.DataFrame({
    'ph': [ph],
    'Hardness': [hardness],
    'Solids': [solids],
    'Chloramines': [chloramines],
    'Sulfate': [sulfate],
    'Conductivity': [conductivity],
    'Organic_carbon': [organic_carbon],
    'Trihalomethanes': [trihalomethanes],
    'Turbidity': [turbidity]
    })

    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)

    score = round(probability[0][1] * 100, 2)

    st.write(f"Water Quality Score: {score}/100")

    
    if prediction[0] == 1:
     st.success("✅ Water is Safe to Drink")
    else:
     st.error("❌ Water is NOT Safe to Drink")

     st.subheader("Recommendations")

     st.write("• Boil water before drinking")
     st.write("• Use filtration systems")
     st.write("• Conduct laboratory testing")