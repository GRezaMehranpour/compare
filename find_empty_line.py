import tkinter as tk
from tkinter import filedialog, messagebox

def browse_file():
    path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if path:
        entry_file.delete(0, tk.END)
        entry_file.insert(0, path)

def find_empty_lines():
    file_path = entry_file.get()

    if not file_path:
        messagebox.showwarning("هشدار", "لطفاً فایل را انتخاب کنید.")
        return

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        empty_lines = [i + 1 for i, line in enumerate(lines) if line.strip() == ""]

        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, f"تعداد خطوط خالی: {len(empty_lines)}\n\n")
        if empty_lines:
            result_text.insert(tk.END, "شماره خطوط خالی:\n")
            result_text.insert(tk.END, ", ".join(map(str, empty_lines)))
        else:
            result_text.insert(tk.END, "خط خالی پیدا نشد.")

    except Exception as e:
        messagebox.showerror("خطا", str(e))


# رابط کاربری
root = tk.Tk()
root.title("پیدا کردن خطوط خالی")
root.geometry("600x400")

tk.Label(root, text="مسیر فایل:").pack(pady=5)
entry_file = tk.Entry(root, width=70)
entry_file.pack()
tk.Button(root, text="انتخاب فایل", command=browse_file).pack(pady=5)

tk.Button(root, text="جستجوی خطوط خالی", command=find_empty_lines,
          bg="#F44336", fg="white", padx=10, pady=5).pack(pady=10)

result_text = tk.Text(root, height=15, width=75)
result_text.pack(pady=5)

root.mainloop()
