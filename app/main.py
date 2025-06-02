from fastapi import FastAPI
from app.routes.ocr_route import router as ocr_router

app = FastAPI(title="Azure OCR API")

# Include the OCR router
app.include_router(ocr_router, prefix="/ocr", tags=["OCR"])
