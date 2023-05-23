import tkinter as tk
from tkinter import filedialog
from reportlab.pdfgen import canvas

def convert_to_pdf():
    text = label.cget("text")
    file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
    
    if file_path:
        c = canvas.Canvas(file_path)
        c.drawString(100, 750, text)
        c.save()

root = tk.Tk()
root.title("Label to PDF Converter")

# Create a Label widget
label = tk.Label(root, text="Hello, world!")
label.pack()

# Create a Button widget to convert to PDF
pdf_button = tk.Button(root, text="Save as PDF", command=convert_to_pdf)
pdf_button.pack()

root.mainloop()
