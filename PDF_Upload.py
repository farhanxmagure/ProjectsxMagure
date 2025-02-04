import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import PyPDF2
import webbrowser
import threading
import time

def upload_pdf():
    file_path = filedialog.askopenfilename(
        title="Select a PDF file",
        filetypes=[("PDF files", "*.pdf")]
    )
    
    if file_path:
        progress_bar.start(10) 
        status_label.config(text="Uploading PDF...", fg="blue")
        
        def process_file():
            try:
                time.sleep(2)  
                with open(file_path, "rb") as pdf_file:
                    reader = PyPDF2.PdfReader(pdf_file)
                    num_pages = len(reader.pages)
                    
                progress_bar.stop()
                status_label.config(text="Upload Complete!", fg="green")
                messagebox.showinfo("Success", f"PDF uploaded successfully!\nNumber of pages: {num_pages}")
                webbrowser.open(file_path)
                root.after(5000, reset_ui)  
            except Exception as e:
                progress_bar.stop()
                status_label.config(text="Upload Failed", fg="red")
                messagebox.showerror("Error", f"Failed to read the PDF file: {e}")
                root.after(5000, reset_ui)  
        
        thread = threading.Thread(target=process_file)
        thread.start()

def reset_ui():
    status_label.config(text="", fg="black")
    progress_bar.stop()


root = tk.Tk()
root.title("PDF Uploader")
root.geometry("800x400")
root.configure(bg="#f0f0f0")
root.protocol("WM_DELETE_WINDOW", lambda: reset_ui() or root.destroy())  

frame = tk.Frame(root, bg="#f0f0f0")
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

label = tk.Label(frame, text="Upload a PDF file", font=("Arial", 16), bg="#f0f0f0")
label.pack(pady=10)

upload_button = tk.Button(frame, text="Upload PDF", command=upload_pdf, font=("Arial", 14), bg="#007bff", fg="white", padx=10, pady=5)
upload_button.pack(pady=10)

progress_bar = ttk.Progressbar(frame, mode='indeterminate', length=300)
progress_bar.pack(pady=10)

status_label = tk.Label(frame, text="", font=("Arial", 12), bg="#f0f0f0")
status_label.pack()

root.mainloop()
