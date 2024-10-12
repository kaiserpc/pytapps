import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger

def merge_pdfs(selected_files, output_path, status_label):
    try:
        merger = PdfMerger()

        # Add each selected file to the merger object
        for file_path in selected_files:
            if file_path.endswith('.pdf'):
                merger.append(file_path)
                print(f"Adding {os.path.basename(file_path)} to the final merged file.")

        # Save merged file
        merger.write(output_path)
        merger.close()

        print(f"PDF files merged at: {output_path}")
        messagebox.showinfo("Success", f"PDF files merged at: {output_path}")
        status_label.config(text="PDF merged successfully!", fg="light green")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
        status_label.config(text="An error occurred. Check the logs.", fg="red")


def select_files():
    # Open a window to select files
    files = filedialog.askopenfilenames(
        title="Select PDF files",
        filetypes=[("PDF Files", "*.pdf")],
        defaultextension=".pdf"
    )
    return list(files)


def save_file():
    # Open a window to select merged file destination
    output_file = filedialog.asksaveasfilename(
        title="Save merged PDF as",
        defaultextension=".pdf",
        filetypes=[("PDF Files", "*.pdf")]
    )
    return output_file


def merge_pdfs_gui(status_label):
    selected_files = select_files()
    if not selected_files:
        messagebox.showwarning("Warning", "No PDF files selected.")
        status_label.config(text="No PDF files selected", fg="orange")
        return
    if len(selected_files) == 1:
        messagebox.showwarning("Warning", "Only one PDF file selected, please select at least 2 files")
        merge_pdfs_gui(status_label)

    # Select merged file destination
    output_path = save_file()
    if not output_path:
        messagebox.showwarning("Warning", "No output file selected.")
        status_label.config(text="No output file selected", fg="orange")
        return

    merge_pdfs(selected_files, output_path, status_label)


# Create main window
root = tk.Tk()
root.title("K-PDFs Merger")
root.geometry("500x350")
root.configure(bg="#2e2e2e")

# Instructions label
instructions = tk.Label(
    root,
    text="Select PDF files to merge and choose a destination.",
    bg="#2e2e2e",
    fg="white",
    font=("Arial", 14)
)
instructions.pack(pady=10)

# Instructions label
instructions = tk.Label(
    root,
    text="Select PDF files to merge and choose a destination.",
    bg="#2e2e2e",
    fg="white",
    font=("Arial", 12)
)
instructions.pack(pady=10)

# Create the button to select and merge files
merge_button = tk.Button(
    root,
    text="Select PDF Files",
    command=lambda: merge_pdfs_gui(status_label),
    bg="#4a4a4a",
    fg="white",
    font=("Arial", 12),
    padx=10,
    pady=5
)
merge_button.pack(pady=20)

# Status Label
status_label = tk.Label(root, text="", bg="#2e2e2e", fg="white", font=("Arial", 10))
status_label.pack(pady=10)

# Status Bar at the bottom
status_bar = tk.Label(root, text="Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W, bg="#2e2e2e", fg="white")
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

# Start window loop
root.mainloop()
