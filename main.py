from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Cargar modelo y scaler
model = joblib.load('modelo_clasificador.pkl')
scaler = joblib.load('scaler.pkl')

app = FastAPI(title="API de Clasificación Summa")

class InputData(BaseModel):
    SeniorCity: int
    Partner: str
    Dependents: str
    Service1: str
    Service2: str
    Security: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    Charges: float
    Demand: float

@app.get("/")
def home():
    return {"message": "API de Clasificación Alpha/Betha activa"}

@app.post("/predict")
def predict_class(data: InputData):
    
    df_input = pd.DataFrame([data.dict()])
    
    for col in df_input.select_dtypes(include=['object']).columns:
        df_input[col] = df_input[col].astype('category').cat.codes

    # Escalar y Predecir
    data_scaled = scaler.transform(df_input)
    prediction = model.predict(data_scaled)
    
    res = "Alpha" if prediction[0] == 0 else "Betha"
    return {"class_prediction": res}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8005)