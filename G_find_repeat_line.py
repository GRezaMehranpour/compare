import tkinter as tk
from tkinter import scrolledtext
from collections import Counter

def find_repeated():
    # Get text from input area
    text = input_text.get("1.0", tk.END).strip()
    # Split into lines and remove empty lines
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    
    # Count line occurrences
    line_counts = Counter(lines)
    
    # Find repeated lines (lines that appear more than once)
    repeated_lines = [(line, count) for line, count in line_counts.items() if count > 1]
    
    # Clear output area
    output_text.delete("1.0", tk.END)
    
    # Display results
    if repeated_lines:
        output_text.insert(tk.END, "Repeated lines:\n\n")
        for line, count in repeated_lines:
            output_text.insert(tk.END, f"Line: '{line}' - Repeated {count} times\n")
    else:
        output_text.insert(tk.END, "No repeated lines found.")

# Create main window
root = tk.Tk()
root.title("Find Repeated Lines")
root.geometry("600x400")

# Create and pack input label
input_label = tk.Label(root, text="Enter your text (one line per entry):")
input_label.pack(pady=5)

# Create and pack input text area
input_text = scrolledtext.ScrolledText(root, height=10, width=60)
input_text.pack(pady=5)

# Create and pack find button
find_button = tk.Button(root, text="Find Repeated Lines", command=find_repeated)
find_button.pack(pady=5)

# Create and pack output label
output_label = tk.Label(root, text="Results:")
output_label.pack(pady=5)

# Create and pack output text area
output_text = scrolledtext.ScrolledText(root, height=10, width=60)
output_text.pack(pady=5)

# Start the main loop
root.mainloop()