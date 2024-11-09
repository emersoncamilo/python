import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import os
import io

# Define the folder containing your PDFs and the output file
pdf_folder = 'C:/....' # Replace with the path to your folder
output_file = 'final_file.txt'  # The output text file name

# Initialize an empty string to store all the merged text
all_text = ""

# Loop through each file in the folder
for filename in os.listdir(pdf_folder):
    if filename.endswith(".pdf"):  # Only process PDF files
        pdf_path = os.path.join(pdf_folder, filename)
        print(f"Processing file: {filename}")
        
        # Open the PDF file
        with fitz.open(pdf_path) as pdf:
            # Iterate through each page
            for page_num in range(pdf.page_count):
                page = pdf[page_num]
                text = page.get_text()
                
                if text.strip():  # If selectable text exists, add it directly
                    all_text += text + "\n"
                else:  # No text detected, use OCR
                    # Convert the page to an image
                    pix = page.get_pixmap()
                    img = Image.open(io.BytesIO(pix.tobytes("png")))
                    
                    # Perform OCR on the image
                    ocr_text = pytesseract.image_to_string(img)
                    all_text += ocr_text + "\n"  # Append OCR text

# Write all extracted text to the output file
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(all_text)

print(f"All text from PDFs in {pdf_folder} has been saved to {output_file}")