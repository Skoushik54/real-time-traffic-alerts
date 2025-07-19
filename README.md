# Real-Time Smart Traffic Alert Web App

## Project Overview
This project aims to build a real-time web application that provides smart traffic alerts. It leverages a **microservices architecture** to separate core business logic from AI/ML functionalities.

### Key Components:
- **Frontend:** React.js (Future integration)
- **Main Backend (Traffic Orchestrator):** Spring Boot (Java) - Handles user management, overall report orchestration, and notifications.
- **NLP/ML Microservice (Classifier):** FastAPI (Python) - Specialized for classifying traffic reports using Natural Language Processing.
- **Database:** MongoDB Atlas - For storing traffic incidents (with geospatial data), user profiles, and alert configurations.
- **Notifications:** Firebase Cloud Messaging (FCM) - For real-time web push notifications.
- **Maps & Geolocation:** Google Maps JavaScript SDK.

## Getting Started (Developer Setup)

### 1. NLP/ML Classifier Service (`./nlp-classifier-service`)
This directory contains the Python FastAPI application responsible for classifying incoming traffic report text.

**Setup Steps:**
1.  Navigate into the `nlp-classifier-service` directory:
    ```bash
    cd nlp-classifier-service
    ```
2.  Create and activate a Python virtual environment:
    * **For Command Prompt (CMD):**
        ```bash
        python -m venv venv
        venv\Scripts\activate.bat
        ```
    * **For PowerShell:**
        ```powershell
        python -m venv venv
        .\venv\Scripts\Activate.ps1
        ```
3.  Install dependencies (will be populated in next steps):
    ```bash
    pip install -r requirements.txt
    ```

**Running the Application:**
(Instructions will be added here once we create the FastAPI app in the next steps of Sprint 1)

### 2. Main Backend Service (`./traffic-orchestrator-service`)
(This directory will contain the Spring Boot application. Setup and running instructions will be added here in a later sprint.)

---

## Overall Architecture Diagram
(A diagram illustrating the microservices interaction will be added here later.)

## Development & Contribution
(More sections like API Endpoints, Database Schema, Deployment, etc., will be added here as the project progresses.)