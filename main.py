import tkinter as tk
from tkinter import simpledialog
from sorting import *
from sorting.insert import creatingTheList, insertionSort


# main window
def main():
    root = tk.Tk()
    root.title("Algorithm Visualization")
    root.geometry("400x300")

    #for exit button
    def on_exit():
        print('Exit button has been clicked')
        root.destroy()

    #title label
    root_label = tk.Label(root, text="Algorithm Visualization", font=("Arial", 20))
    root_label.pack(pady=20)
    print('title load')

    #resuable page
    def show_algorithm(name, numbers, sorted_numbers):
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

    # console log for buttons and also shows the results on the page
    def on_clicked(name: str):
        print(name, 'has been clicked')

        # checking what items will be accessed
        match name:
            case 'Insertion Sort':
                # asking the user how many number
                n = simpledialog.askinteger("Input", "How many numbers do you want to sort?")

                # if nothing, then just return nothing
                if n is None:
                    return

                # else add a list then call insertion sort with the number they wanted
                num = creatingTheList(n)
                num2 = num.copy()
                num2 = insertionSort(num2)
                print(num2)
                show_algorithm('Insertion Sort', num, num2)

    #Insertion Sort
    insort_button = tk.Button(root, text="Insertion Sort", command=lambda: on_clicked('Insertion Sort'), width=20)
    insort_button.pack(pady=15)

    # exit button
    exit_button = tk.Button(root, text="Exit", command=on_exit, width=20)
    exit_button.pack(pady=15)

    root.mainloop()

if __name__ == '__main__':
    main()