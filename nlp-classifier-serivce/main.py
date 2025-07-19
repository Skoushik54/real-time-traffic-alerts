# nlp-classifier-service/main.py

from fastapi import FastAPI # Import the FastAPI class

# Create an instance of the FastAPI application.
# This `app` object is the core of your FastAPI service.
app = FastAPI()

# Define a simple GET endpoint.
# The '@app.get("/")' decorator tells FastAPI that the function below
# should handle HTTP GET requests made to the root URL ("/").
@app.get("/")
async def read_root():
    """
    Root endpoint of the NLP Classifier Service.
    Returns a welcome message to confirm the service is running.
    """
    # FastAPI automatically converts Python dictionaries to JSON responses.
    return {"message": "Welcome to the NLP Classifier Service! (Hello World)"}

# This is where your future NLP classification endpoints will go.
# Example for a future endpoint (just for illustration, DO NOT uncomment yet):
# from pydantic import BaseModel
# class TextToClassify(BaseModel):
#     text: str

# @app.post("/classify")
# async def classify_text(item: TextToClassify):
#     # Placeholder for NLP classification logic
#     classified_type = "unknown"
#     confidence_score = 0.5
#     if "accident" in item.text.lower():
#         classified_type = "accident"
#         confidence_score = 0.9
#     return {"type": classified_type, "confidence": confidence_score}