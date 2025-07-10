import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

def compare_files():
    file1_path = entry_file1.get()
    file2_path = entry_file2.get()

    if not file1_path or not file2_path:
        messagebox.showwarning("Warning", "Please select both files.")
        return

    try:
        with open(file1_path, "r", encoding="utf-8") as f1:
            lines1 = set(line.strip() for line in f1)

        with open(file2_path, "r", encoding="utf-8") as f2:
            lines2 = set(line.strip() for line in f2)

        only_in_list2 = sorted(lines2 - lines1)

        result_box.delete(1.0, tk.END)
        if only_in_list2:
            result_box.insert(tk.END, "\n".join(only_in_list2))
        else:
            result_box.insert(tk.END, "No unique lines found in list2.txt")

    except Exception as e:
        messagebox.showerror("Error", str(e))

def browse_file1():
    path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if path:
        entry_file1.delete(0, tk.END)
        entry_file1.insert(0, path)

def browse_file2():
    path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if path:
        entry_file2.delete(0, tk.END)
        entry_file2.insert(0, path)

# GUI setup
root = tk.Tk()
root.title("Compare Two Text Files")
root.geometry("700x500")

tk.Label(root, text="File 1 (Base):").pack()
entry_file1 = tk.Entry(root, width=80)
entry_file1.pack()
tk.Button(root, text="Browse", command=browse_file1).pack()

tk.Label(root, text="File 2 (Compare With):").pack()
entry_file2 = tk.Entry(root, width=80)
entry_file2.pack()
tk.Button(root, text="Browse", command=browse_file2).pack()

tk.Button(root, text="Compare Files", command=compare_files, bg="#4CAF50", fg="white", padx=10, pady=5).pack(pady=10)

result_box = scrolledtext.ScrolledText(root, width=85, height=20)
result_box.pack()

root.mainloop()
