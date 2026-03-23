import pickle

def save_model(model, vectorizer, path="models/model.pkl"):
    with open(path, "wb") as f:
        pickle.dump((model, vectorizer), f)

def load_model(path="models/model.pkl"):
    with open(path, "rb") as f:
        return pickle.load(f)