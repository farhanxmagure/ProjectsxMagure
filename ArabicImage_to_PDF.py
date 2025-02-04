import tkinter as tk
from tkinter import filedialog, messagebox, ttk, scrolledtext
import pytesseract
from PIL import Image
from fpdf import FPDF
import os
import subprocess

def upload_image():
    
    pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
    
    status_label.config(text="Starting OCR process...", fg="blue")
    progress_bar.pack(pady=5)  
    progress_bar.start()
    
    file_path = filedialog.askopenfilename(
        title="Select an image file",
        filetypes=[("Image files", "*.jpg *.jpeg *.png")]
    )
    
    if file_path:
        try:
            img = Image.open(file_path)
            ocr_text = pytesseract.image_to_string(img, lang='ara')  # Arabic OCR
            
            text_display.delete('1.0', tk.END)  
            text_display.insert(tk.END, ocr_text) 
            
            status_label.config(text="OCR processing completed!", fg="green")
        except Exception as e:
            status_label.config(text=f"Error: {str(e)}", fg="red")
            messagebox.showerror("Error", f"Failed to process image: {e}")
    else:
        status_label.config(text="No image selected.", fg="red")
    
    progress_bar.stop()
    progress_bar.pack_forget()  
    
def save_to_pdf():
    text = text_display.get('1.0', tk.END).strip()
    if not text:
        messagebox.showwarning("Warning", "No text available to save!")
        return

    pdf_path = filedialog.asksaveasfilename(
        title="Save as PDF",
        defaultextension=".pdf",
        filetypes=[("PDF files", "*.pdf")]
    )
    
    if pdf_path:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_font("DejaVu", "", "DejaVuSans.ttf", uni=True)  
        pdf.set_font("DejaVu", "", 14)

        pdf.multi_cell(190, 10, text, align="R")  
        pdf.output(pdf_path)
        
        messagebox.showinfo("Success", "Text successfully saved as PDF!")
        
        try:
            if os.name == 'nt':  # Windows
                os.startfile(pdf_path)
            elif os.name == 'posix':  # macOS/Linux
                subprocess.Popen(["xdg-open", pdf_path])
        except Exception as e:
            messagebox.showerror("Error", f"Could not open PDF: {e}")

def reset_ui():
    text_display.delete('1.0', tk.END)
    status_label.config(text="")

root = tk.Tk()
root.title("Arabic Image to PDF Converter")
root.geometry("900x500")
root.configure(bg="#2c3e50") 

frame = tk.Frame(root, bg="#34495e", padx=20, pady=20)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

label = tk.Label(frame, text="Upload an image to extract Arabic text via OCR", font=("Arial", 16), bg="#34495e", fg="white")
label.pack(pady=10)

upload_button = tk.Button(frame, text="Upload Image", command=upload_image, font=("Arial", 14), bg="#3498db", fg="white", padx=10, pady=5)
upload_button.pack(pady=5)

save_button = tk.Button(frame, text="Save as PDF", command=save_to_pdf, font=("Arial", 14), bg="#2ecc71", fg="white", padx=10, pady=5)
save_button.pack(pady=5)

text_display = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=80, height=10, font=("Arial", 12))
text_display.pack(pady=10)

progress_bar = ttk.Progressbar(frame, orient=tk.HORIZONTAL, length=300, mode='indeterminate')
progress_bar.pack_forget() 

status_label = tk.Label(frame, text="", font=("Arial", 12), bg="#34495e", fg="white")
status_label.pack()

root.mainloop()
