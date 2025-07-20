# nlp-classifier-service/main.py

from fastapi import FastAPI , HTTPException # Import the FastAPI class and HTTPException
from pydantic import BaseModel# Import the BaseModel class from Pydantic
import spacy # Import the spacy library
import os # Import the os library

# Create an instance of the FastAPI application.
# This `app` object is the core of your FastAPI service.
app = FastAPI(
    title=f"NLP Classifier Service",
    description=f"A microservice for classifying the traffic report text using NLP.",
    version="0.116.1"
)

# Global Resources (for spaCy model loading) 
# This ensures the spaCy model is loaded only once when the application starts.
# Loading it inside the endpoint function would make it load for every request, which is inefficient.
try:
    nlp=spacy.load("en_core_web_sm")
except OSError:
    print("SpaCy model 'en_core_web_sm' not found. Please run 'python -m  spacy download en_core_web_sm'")
    raise
# --- Pydantic Models ---
# Define the structure of the incoming request body
class TrafficReportRequest(BaseModel):
    """
    Request model for classifying a traffic report.
    """
    text: str  # The raw text of the traffic report
class ClassificationResponse(BaseModel):
    """
    Response model for the classified traffic report.
    """
    incident_type: str # e.g., "accident", "traffic_jam", "road_closure"
    confidence: float  # A confidence score (0.0 to 1.0) for the classification
    processed_text: str # The text after basic processing (e.g., lowercased)

# --- API Endpoints ---

@app.get("/")
async def read_root():
    """
    Root endpoint of the NLP Classifier Service.
    Returns a welcome message to confirm the service is running.
    """
    # FastAPI automatically converts Python dictionaries to JSON responses.
    return {"message": "Welcome to the NLP Classifier Service! (Hello World)"}

@app.post("/classify",response_model=ClassificationResponse)
async def classify_traffic_report(report:TrafficReportRequest):
    """
    Classifies an incoming traffic report text.

    Uses a rule-based approach with spaCy for initial classification.
    """
    # Process the text using spaCy (e.g., lowercasing, basic tokenization)
    doc = nlp(report.text.lower())  # Process text and convert to lowercase
    incident_type="other event" #Default type
    confidence=0.5 # Default condidence

    # --- Rule-Based Classification Logic ---
    # This is a simple example. More sophisticated rules or ML models would go here.

    # Keywords for Traffic Jam
    jam_keywords=["jam","traffic","heavy traffic","slow traffic", "standstill", "congested", "bottleneck"]
    if any(keyword in doc.text for keyword in jam_keywords):
        incident_type="traffic_jam"
        confidence=0.85
    
    # Keywords for Accident
    accident_keywords=["accident","crash","collision"]
    if any(keyword in doc.text for keyword in accident_keywords):
        incident_type="accident"
        confidence=0.95
    
    # Keywords for Road Closure
    closure_keywords=["closed","blocked","diversion"]
    if any(keyword in doc.text for keyword in closure_keywords):
        incident_type="road_closure"
        confidence=0.90

    return ClassificationResponse(
        incident_type=incident_type,
        confidence=confidence,
        processed_text=doc.text # Return the lowercased text for verification
    )