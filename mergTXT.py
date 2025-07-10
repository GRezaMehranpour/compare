import os
import tkinter as tk
from tkinter import filedialog, messagebox

class TextFileMergerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text File Merger")
        self.root.geometry("500x300")

        # Label and entry for folder path
        self.label_folder = tk.Label(root, text="Select Folder with .txt Files:")
        self.label_folder.pack(pady=10)

        self.entry_folder = tk.Entry(root, width=50)
        self.entry_folder.pack(pady=5)

        self.btn_browse = tk.Button(root, text="Browse", command=self.browse_folder)
        self.btn_browse.pack(pady=5)

        # Label and entry for output file
        self.label_output = tk.Label(root, text="Output File Name (e.g., merged.txt):")
        self.label_output.pack(pady=10)

        self.entry_output = tk.Entry(root, width=50)
        self.entry_output.insert(0, "merged.txt")
        self.entry_output.pack(pady=5)

        # Merge button
        self.btn_merge = tk.Button(root, text="Merge Files", command=self.merge_files)
        self.btn_merge.pack(pady=20)

        # Status label
        self.label_status = tk.Label(root, text="", wraplength=400)
        self.label_status.pack(pady=10)

    def browse_folder(self):
        folder = filedialog.askdirectory(title="Select Folder Containing .txt Files")
        if folder:
            self.entry_folder.delete(0, tk.END)
            self.entry_folder.insert(0, folder)
            self.label_status.config(text="Folder selected: " + folder)

    def merge_txt_files(self, input_folder, output_file):
        try:
            # Check if input folder exists
            if not os.path.isdir(input_folder):
                raise ValueError(f"The folder '{input_folder}' does not exist.")
            
            # Get list of .txt files in the folder
            txt_files = [f for f in os.listdir(input_folder) if f.endswith('.txt')]
            if not txt_files:
                raise ValueError(f"No .txt files found in '{input_folder}'.")
            
            # Ensure output file has .txt extension
            if not output_file.endswith('.txt'):
                output_file += '.txt'
            
            # Open output file in write mode
            with open(output_file, 'w', encoding='utf-8') as outfile:
                for i, txt_file in enumerate(txt_files, 1):
                    file_path = os.path.join(input_folder, txt_file)
                    try:
                        # Read content of each .txt file
                        with open(file_path, 'r', encoding='utf-8') as infile:
                            content = infile.read()
                            # Write header and content to output file
                            outfile.write(f"\n=== Content from {txt_file} ===\n")
                            outfile.write(content)
                            outfile.write("\n")  # Add newline for separation
                    except Exception as e:
                        self.label_status.config(text=f"Error reading {txt_file}: {e}")
                        return
                
            self.label_status.config(text=f"Success: Merged {len(txt_files)} files into '{output_file}'")
            messagebox.showinfo("Success", f"Merged {len(txt_files)} files into '{output_file}'")
        
        except Exception as e:
            self.label_status.config(text=f"Error: {e}")
            messagebox.showerror("Error", str(e))

    def merge_files(self):
        input_folder = self.entry_folder.get().strip()
        output_file = self.entry_output.get().strip()
        
        if not input_folder:
            self.label_status.config(text="Error: Please select a folder.")
            messagebox.showerror("Error", "Please select a folder.")
            return
        
        if not output_file:
            self.label_status.config(text="Error: Please enter an output file name.")
            messagebox.showerror("Error", "Please enter an output file name.")
            return
        
        self.merge_txt_files(input_folder, output_file)

def main():
    root = tk.Tk()
    app = TextFileMergerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()