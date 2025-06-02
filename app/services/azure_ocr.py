import requests
from pdf2image import convert_from_path

class AzureOCR:
    def __init__(self, api_key, url):
        self.headers = {
            'Ocp-Apim-Subscription-Key': api_key,
            'Content-Type': 'application/octet-stream'
        }
        self.params = {'language': 'en'}
        self.url = url

    async def image_to_bytes(self, image_path):
        with open(image_path, 'rb') as f:
            return f.read()

    async def request_ocr(self, image_data):
        response = requests.post(self.url, headers=self.headers, params=self.params, data=image_data)
        return response.json()

    def extract_text(self, json_data):
        text = ''
        for region in json_data.get('regions', []):
            for line in region.get('lines', []):
                for word in line.get('words', []):
                    text += word['text'] + ' '
                text += '\n'
        return text.strip()
    

    def convert_pdf_to_images(self, pdf_path):
        return convert_from_path(pdf_path)
