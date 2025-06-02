import os
import shutil
import tempfile
from fastapi import APIRouter, File, UploadFile
from app.services.azure_ocr import AzureOCR
from config import API_KEY, OCR_URL

router = APIRouter()

@router.post("/")
async def ocr_file(file: UploadFile = File(...)):
    try:
        temp_dir = tempfile.mkdtemp()
        file_path = os.path.join(temp_dir, file.filename)

        with open(file_path, "wb") as f:
            shutil.copyfileobj(file.file, f)

        ocr = AzureOCR(API_KEY, OCR_URL)

        if file.filename.lower().endswith(".pdf"):
            images = ocr.convert_pdf_to_images(file_path)
            text_results = []
            for i, image in enumerate(images):
                img_path = os.path.join(temp_dir, f"{file.filename}_page_{i}.png")
                image.save(img_path, "PNG")
                img_data = await ocr.image_to_bytes(img_path)
                json_result = await ocr.request_ocr(img_data)
                text_results.append(ocr.extract_text(json_result))
            return {"text": "\n".join(text_results)}
        else:
            img_data = await ocr.image_to_bytes(file_path)
            json_result = await ocr.request_ocr(img_data)
            text = ocr.extract_text(json_result)
            return {"text": text}

    except Exception as e:
        return {"error": str(e)}
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)
