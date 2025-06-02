import os

def save_temp_image(file_path, page_number, image):
    temp_path = f"{file_path}_page_{page_number}.png"
    image.save(temp_path, 'PNG')
    return temp_path
