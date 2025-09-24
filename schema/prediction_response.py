from pydantic import BaseModel, Field
from typing import Dict

class PredictionResponse(BaseModel):
    predicted_category: str = Field(..., description="The predicted insurance premium category", example="Medium")
    
    confidence: float = Field(..., description="Confidence score of the predicted class (range: 0 to 1)", example=0.85)
    
    class_probabilities: Dict[str, float] = Field(..., description="Probabilities for each insurance premium category", example={"Low": 0.1, "Medium": 0.15, "High": 0.84})
    