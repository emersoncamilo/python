# PDF Text Extraction Script

This Python script extracts and merges text from PDF files, using `pymupdf`, `pytesseract`, and `pillow` libraries. Additionally, Tesseract OCR is required for handling any images within PDFs that need text recognition.

## Setup Instructions

1. **Install Required Python Libraries**

   Use `pip` to install the required libraries:

   ```bash
   pip install pymupdf pytesseract pillow
## Install Tesseract OCR

Tesseract OCR must be installed on your system for OCR functionality.
Follow the steps below based on your operating system:

Windows: Download and install Tesseract from the official repository.

Linux:
Install Tesseract via the command line:
```bash
sudo apt install tesseract-ocr



macOS:
Install Tesseract using Homebrew:
```bash
brew install tesseract

Once you have installed both the Python libraries and Tesseract OCR, the script will be ready to process and extract text from PDF files.