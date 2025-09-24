import pickle
import pandas as pd


MODEL_VERSION = "1.0.0"



with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)

class_labels = model.classes_.tolist()

def predict(user_input: dict):

    input_df = pd.DataFrame([user_input])

    output = model.predict(input_df)[0]
    
    probabilities = model.predict_proba(input_df)[0]
    confidence = max(probabilities)
    
    class_probs = dict(zip(class_labels, map(lambda x: round(x, 4), probabilities)))
    return {
        "predicted_class": output,
        "confidence": round(confidence, 4),
        "class_probabilities": class_probs
    }
