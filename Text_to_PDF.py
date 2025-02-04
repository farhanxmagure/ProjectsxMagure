import tkinter as tk
from tkinter import filedialog, messagebox
from fpdf import FPDF
import threading
import time

class TextToPDFApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text to PDF Converter")
        self.root.geometry("500x400")
        self.root.config(bg="#212121")  
        
        self.main_frame = tk.Frame(self.root, bg="#212121")
        self.main_frame.pack(expand=True)
        
        self.title_label = tk.Label(self.main_frame, text="Text to PDF Converter", font=("Arial", 18, "bold"), fg="white", bg="#212121")
        self.title_label.pack(pady=20)

        self.text_box = tk.Text(self.main_frame, wrap="word", width=60, height=10, font=("Arial", 12), bg="#333333", fg="white", bd=2, relief="solid", insertbackground="white", padx=10, pady=10)
        self.text_box.pack(pady=20)
        
        self.button_frame = tk.Frame(self.main_frame, bg="#212121")
        self.button_frame.pack(pady=20)
        
        self.save_button = tk.Button(self.button_frame, text="Save to PDF", command=self.save_to_pdf, bg="#4CAF50", fg="white", font=("Arial", 12), bd=0, relief="flat", width=15)
        self.save_button.grid(row=0, column=0, padx=10)
        
        self.reset_button = tk.Button(self.button_frame, text="Reset Text", command=self.reset_text, bg="#f44336", fg="white", font=("Arial", 12), bd=0, relief="flat", width=15)
        self.reset_button.grid(row=0, column=1, padx=10)
        
        self.processing_label = tk.Label(self.main_frame, text="", bg="#212121", font=("Arial", 12), fg="white")
        self.processing_label.pack(pady=20)

    def save_to_pdf(self):
        text = self.text_box.get("1.0", "end-1c") 
        
        if not text.strip():
            messagebox.showwarning("Warning", "Text field cannot be empty!")
            return
        
        file_name = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
        
        if not file_name:
            return  
        
        self.processing_label.config(text="Saving PDF, please wait...", fg="blue")
        self.processing_label.update()  
        
        threading.Thread(target=self.create_pdf, args=(text, file_name)).start()

    def create_pdf(self, text, file_name):
        time.sleep(2)  
        
        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, text)
        pdf.output(file_name)
        
        self.processing_label.config(text="")
        messagebox.showinfo("Success", "PDF saved successfully!")

    def reset_text(self):
        self.text_box.delete("1.0", "end-1c")  

if __name__ == "__main__":
    root = tk.Tk()
    app = TextToPDFApp(root)
    root.mainloop()
