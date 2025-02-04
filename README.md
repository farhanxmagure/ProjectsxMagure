# Arabic OCR and PDF Utility

![Project Banner](https://dummyimage.com/900x300/000/fff&text=Arabic+OCR+and+PDF+Utility)

## 📜 Description
This project provides a set of Python-based GUI applications for working with PDF and image files. The applications leverage **Tesseract OCR** for extracting Arabic text from images, **PyPDF2** for handling PDFs, and **Tkinter** for a user-friendly interface. The utilities included are:

1. **Arabic OCR to PDF Converter**: Extracts Arabic text from images and saves it as a PDF.
2. **PDF Text Extractor**: Extracts text from PDFs and allows saving as a `.txt` file.
3. **PDF Uploader**: Uploads and previews PDFs while displaying page count.

## 🚀 Features
- Extract **Arabic** text from images using Tesseract OCR.
- Save extracted text as **PDF** with proper right-to-left (RTL) formatting.
- Extract text from **PDFs** and save it as a `.txt` file.
- **Threaded processing** for smooth UI interaction.
- **Modern GUI** using Tkinter.
- **Progress indicators** for OCR and PDF extraction processes.

## 📂 Installation

### 1️⃣ Install Python
Ensure you have **Python 3.8+** installed. You can download it from [Python Official Website](https://www.python.org/downloads/).

### 2️⃣ Install Dependencies
Run the following command to install required libraries:

```sh
pip install pytesseract pillow fpdf tkinter PyPDF2
```

### 3️⃣ Install Tesseract OCR
Tesseract is required for OCR functionality. Download and install it from:
- **Windows:** [Tesseract OCR Download](https://github.com/UB-Mannheim/tesseract/wiki)
- **Linux/macOS:** Install via package manager:
  ```sh
  sudo apt install tesseract-ocr   # Ubuntu/Debian
  brew install tesseract           # macOS
  ```

### 4️⃣ Configure Tesseract Path (Windows Only)
Update the Tesseract path in the script:
```python
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
```

## 🛠️ Usage

### 1️⃣ Run the Arabic OCR to PDF Converter
```sh
python arabic_ocr_to_pdf.py
```
- Click **Upload Image** to select an image containing Arabic text.
- The text will be extracted using **OCR** and displayed.
- Click **Save as PDF** to save the extracted text as a **right-aligned Arabic PDF**.

### 2️⃣ Run the PDF Text Extractor
```sh
python pdf_text_extractor.py
```
- Click **Upload PDF** to select a file.
- The text will be extracted and displayed.
- Click **Save as TXT** to save the extracted text.

### 3️⃣ Run the PDF Uploader
```sh
python pdf_uploader.py
```
- Click **Upload PDF** to select a file.
- The PDF will be opened and the page count will be displayed.

## 🖼️ Screenshots
![Arabic Image to PDF](https://github.com/farhanxmagure/ProjectsxMagure/blob/main/Images/Screenshot%202025-02-04%20183922.png)
![Text to PDF](https://github.com/farhanxmagure/ProjectsxMagure/blob/main/Images/Screenshot%202025-02-04%20174810.png)
![PDF Text Extractor](https://github.com/farhanxmagure/ProjectsxMagure/blob/main/Images/Screenshot%202025-02-04%20132654.png)
![PDF Text Extractor 2](https://github.com/farhanxmagure/ProjectsxMagure/blob/main/Images/Screenshot%202025-02-04%20132426.png)

## ❓ Troubleshooting
- If **Tesseract is not detected**, verify its installation and update the script path.
- For **missing fonts in PDFs**, ensure `DejaVuSans.ttf` is available in your system.
- If the **GUI freezes**, restart the application and avoid selecting large files.

## 📜 License
This project is licensed under the **MagurexMIT License**.

---

🔹 Developed by **[Farhan]** | 📧 Contact: [farhan.k@magureinc.com]
