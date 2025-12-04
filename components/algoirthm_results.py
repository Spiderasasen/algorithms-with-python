import tkinter as tk

#resuable page
def show_algorithm(root, name, numbers, sorted_numbers):
    # If window already exists, reuse it
    if hasattr(root, "algo_window") and root.algo_window.winfo_exists():
        win = root.algo_window
        for widget in win.winfo_children():
            widget.destroy()  # clear old content
    else:
        win = tk.Toplevel(root)
        root.algo_window = win
        win.geometry("500x400")

    win.title(f"{name} Results")

    text_box = tk.Text(win, wrap="word", font=("Arial", 12))
    text_box.pack(expand=True, fill="both", padx=10, pady=10)
    text_box.insert(tk.END, f"Unsorted list:\n{numbers}\n\n")
    text_box.insert(tk.END, f"Sorted list:\n{sorted_numbers}\n")
