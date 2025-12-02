import tkinter as tk
from tkinter import simpledialog
import random
import time
from sorting.insert import creatingTheList, insertionSort

def draw_bars(canvas, array, active_index = None):
    canvas.delete("all")
    c_width = 400
    c_height = 300
    bar_width = c_width / len(array)
    for i, val in enumerate(array):
        x0 = i * bar_width
        y0 = c_height - val
        x1 = (i + 1) * bar_width
        y1 = c_height
        color = "red" if i == active_index else "blue"
        canvas.create_rectangle(x0, y0, x1, y1, fill=color)
    canvas.update_idletasks()

def visualizer(canvas, steps, delay=0.1):
    for state, active_index in steps:
        draw_bars(canvas, state, active_index)
        time.sleep(delay)


def insertion_sort_steps(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        # highlight the key
        yield array[:], i
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
            yield array[:], j+i  # yield after each shift
        array[j + 1] = key
        yield array[:], j+1  # yield after placing key

# main window
def main():
    root = tk.Tk()
    root.title("Algorithm Visualization")
    root.geometry("400x300")

    #creates the canvas
    canvas = tk.Canvas(root, width=400, height=300, bg="white")
    canvas.pack()

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

                # else add a list then call insertion sort with the number they wanted (mainly used for me to practice coding it)
                num = creatingTheList(n)
                num2 = num.copy()
                num2 = insertionSort(num2)
                print(num2)
                #goes through the universal method and also calling the steps
                steps = insertion_sort_steps(num.copy())
                visualizer(canvas, steps)
                #showing the differnace between unsorted and sorted
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