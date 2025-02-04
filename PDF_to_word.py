import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk
import PyPDF2
import threading
import time

def upload_pdf():
    file_path = filedialog.askopenfilename(
        title="Select a PDF file",
        filetypes=[("PDF files", "*.pdf")]
    )
    if file_path:
        status_label.config(text="Extracting text...", fg="blue")
        progress_bar.pack(pady=5)
        progress_bar.start(10)

        thread = threading.Thread(target=extract_text, args=(file_path,))
        thread.start()

def extract_text(file_path):
    try:
        time.sleep(2)
        
        with open(file_path, "rb") as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            text = ""

            for i, page in enumerate(reader.pages, start=1):
                extracted_text = page.extract_text()
                if extracted_text:
                    text += f"\n\n📄 Page {i}\n" + "-"*30 + "\n" + extracted_text.strip()
            
            root.after(0, lambda: display_text(text))

    except Exception as e:
        root.after(0, lambda: messagebox.showerror("Error", f"Failed to read the PDF file: {e}"))
    finally:
        time.sleep(1)
        root.after(0, lambda: progress_bar.stop())
        root.after(0, lambda: progress_bar.pack_forget())
        root.after(0, lambda: status_label.config(text="Extraction Complete!", fg="green"))

def display_text(text):
    text_area.delete(1.0, tk.END)
    text_area.insert(tk.INSERT, text)

def copy_to_clipboard():
    extracted_text = text_area.get(1.0, tk.END).strip()
    if extracted_text:
        root.clipboard_clear()
        root.clipboard_append(extracted_text)
        root.update()
        messagebox.showinfo("Copied", "Extracted text copied to clipboard!")

def save_text():
    extracted_text = text_area.get(1.0, tk.END).strip()
    if extracted_text:
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(extracted_text)
            messagebox.showinfo("Saved", "Extracted text saved successfully!")

def reset_text():
    text_area.delete(1.0, tk.END)
    status_label.config(text="", fg = "black")

root = tk.Tk()
root.title("📄 PDF Text Extractor")
root.geometry("700x500")
root.configure(bg="#f0f0f0")

frame = tk.Frame(root, bg="white", padx=20, pady=20, relief=tk.RIDGE, bd=2, highlightbackground="gray", highlightthickness=1)
frame.pack(expand=True, fill="both", padx=20, pady=20)

title_label = tk.Label(frame, text="📂 PDF Text Extractor", font=("Arial", 18, "bold"), bg="white", fg="black")
title_label.pack(pady=10)

upload_button = tk.Button(frame, text="📤 Upload PDF", command=upload_pdf, font=("Arial", 14), bg="#4CAF50", fg="white", padx=10, pady=5)
upload_button.pack(pady=10)

progress_bar = ttk.Progressbar(frame, mode="indeterminate", length=300)
progress_bar.pack_forget()

status_label = tk.Label(frame, text="", font=("Arial", 12), bg="white", fg="black")
status_label.pack()

text_area = scrolledtext.ScrolledText(
    frame, wrap=tk.WORD, width=75, height=15, font=("Arial", 12),
    borderwidth=2, relief=tk.SOLID, highlightbackground="gray", highlightthickness=2
)
text_area.pack(pady=15)

button_frame = tk.Frame(frame, bg="white")
button_frame.pack(pady=10)

copy_button = tk.Button(button_frame, text="📋 Copy Text", command=copy_to_clipboard, font=("Arial", 12), bg="#008CBA", fg="white", padx=10, pady=5)
copy_button.grid(row=0, column=0, padx=5)

save_button = tk.Button(button_frame, text="💾 Save as TXT", command=save_text, font=("Arial", 12), bg="#FFA500", fg="white", padx=10, pady=5)
save_button.grid(row=0, column=1, padx=5)

reset_button = tk.Button(button_frame, text="🔄 Reset", command=reset_text, font=("Arial", 12), bg="#FF6347", fg="white", padx=10, pady=5)
reset_button.grid(row=0, column=2, padx=5)

root.mainloop()
