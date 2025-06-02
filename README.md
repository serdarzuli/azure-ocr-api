# Azure OCR API

## 1. About the Work
This project is a FastAPI-based microservice for extracting text from images and PDF files using Microsoft Azure's Computer Vision OCR API. It allows users to upload images or PDFs and returns the extracted text using Azure's high-accuracy OCR capabilities.

## 2. Project Structure
```
azure-ocr-api/
│   README.md
│   requirement.txt
│   .env
│
├───app/
│   │   main.py                # FastAPI app entry point
│   ├───routes/
│   │   ocr_route.py           # API route for OCR
│   ├───services/
│   │   azure_ocr.py           # Azure OCR logic
│   │   pdf_utils.py           # PDF utility functions
│   └───utils/
│       logger.py              # Simple logger
│
└───data/                      # (Optional) For storing uploads or results
```

## 3. Getting Started
1. **Clone the repository**
2. **Install dependencies**
   ```powershell
   pip install -r requirement.txt
   ```
3. **Configure Azure Credentials**
   - Edit the `.env` file and set your Azure API key and endpoint:
     ```env
     API_KEY = "<your_azure_key>"
     OCR_URL = "https://<your-resource>.cognitiveservices.azure.com/vision/v3.2/ocr"
     ```

## 4. Usage
- **Run the API server:**
  ```powershell
  uvicorn app.main:app --reload
  ```
- **API Endpoint:** `POST /ocr/`
  - Upload an image or PDF file as form-data with the field name `file`.
  - The response will contain the extracted text in JSON format.

**Example using curl:**
```sh
curl -X POST "http://localhost:8000/ocr/" -F "file=@yourfile.pdf"
```

## 5. Technologies Used
- **FastAPI**: Web framework for building APIs
- **Uvicorn**: ASGI server for running FastAPI
- **Requests**: HTTP requests to Azure OCR API
- **pdf2image**: Convert PDF pages to images
- **Pillow**: Image processing
- **Azure Cognitive Services**: OCR engine

---
MIT License
