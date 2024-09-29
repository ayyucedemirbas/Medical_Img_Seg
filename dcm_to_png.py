import os
import pydicom
import numpy as np
from PIL import Image

def convert_dicom_to_png(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.dcm'):
            dicom_path = os.path.join(input_folder, filename)          
            dicom_file = pydicom.dcmread(dicom_path)               
            pixel_array = dicom_file.pixel_array
            normalized_array = (pixel_array - np.min(pixel_array)) / (np.max(pixel_array) - np.min(pixel_array)) * 255
            normalized_array = normalized_array.astype(np.uint8)
            image = Image.fromarray(normalized_array)
            output_filename = f"{os.path.splitext(filename)[0]}.png"
            output_path = os.path.join(output_folder, output_filename)
            image.save(output_path)
            print(f"Converted {filename} to PNG and saved to {output_path}")

input_folder = 'path_to_your_dicom_folder'
output_folder = 'path_to_your_png_folder'
convert_dicom_to_png(input_folder, output_folder)
