from fastapi import FastAPI
import joblib

app = FastAPI()

model, vectorizer = joblib.load("models/model.pkl")

@app.get("/")
def home():
    return {"message": "API de classificação de notícias"}

@app.post("/predict")
def predict(text: str):
    text_vec = vectorizer.transform([text])
    prediction = model.predict(text_vec)[0]
    return {"categoria": prediction}