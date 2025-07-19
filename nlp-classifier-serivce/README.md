# NLP Classifier Service (FastAPI)

## Overview
This is a dedicated microservice built with FastAPI in Python, responsible for performing Natural Language Processing (NLP) tasks, specifically classifying text-based traffic reports. It exposes API endpoints that the main Spring Boot backend will consume.

## Setup

### 1. Create and Activate Virtual Environment
Ensure you are in the `nlp-classifier-service` directory.
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

### 2. Install Dependencies
With your virtual environment activated, install the required Python packages from `requirements.txt`:
```bash
pip install -r requirements.txt