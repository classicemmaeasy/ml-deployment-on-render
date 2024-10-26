from fastapi import FastAPI
import pickle
import pandas as pd
from data_model import Water

app=FastAPI(
    title="Water Potability Prediction",
    description="Predicting Water Potability Prediction"
)


with open("mod.pkl","rb") as f:
    model=pickle.load(f)

@app.get("/")

def index():
    return "welcome to water potability prediction"


@app.post("/predict")

def model_predict(water:Water):
    sample=pd.DataFrame({
        'ph':[water.ph],
        'Hardness':[water.Hardness],
        'Solids':[water.Solids],
        'Chloramines':[water.Chloramines],
        'Sulfate':[water.Sulfate],
        'Conductivity':[water.Conductivity],
        'Organic_carbon':[water.Organic_carbon],
        'Trihalomethanes':[water.Trihalomethanes],
        'Turbidity':[water.Turbidity]
    })


    pred_val=model.predict(sample)


    if pred_val==1:
     return 'water is consummable'

    else:
     return 'water is not consummable'
