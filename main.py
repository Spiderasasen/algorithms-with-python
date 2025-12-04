import tkinter as tk
from tkinter import simpledialog
import time
from sorting.bubble import bubbleSort, bubble_sort_steps
from components.creat_list import creatingTheList
from sorting.insert import insertionSort, insertion_sort_steps
from sorting.selection import selection_sort, selection_sort_steps
from sorting.merge import mergeSort, merge_sort_steps

# Dictionary of complexities for each algorithm
COMPLEXITIES = {
    "Insertion Sort": "Best: O(n), \nAverage/Worst: O(n^2)",
    "Bubble Sort": "Best: O(n), \nAverage/Worst: O(n^2)",
    "Selection Sort": "Always: O(n^2)",
    "Merge Sort": "Best/Average/Worst: O(n log n)",
    "Quick Sort": "Best/Average: O(n log n), \nWorst: O(n^2)",
    "Heap Sort": "Best/Average/Worst: O(n log n)"
}

def draw_bars(canvas, array, active_index=None, compare_index=None, complexity=""):
    canvas.delete("all")
    c_width = 400
    c_height = 300
    bar_width = c_width / len(array)
    for i, val in enumerate(array):
        x0 = i * bar_width
        y0 = c_height - val
        x1 = (i + 1) * bar_width
        y1 = c_height
        if i == active_index:
            color = "red"
        elif i == compare_index:
            color = "green"
        else:
            color = "blue"
        canvas.create_rectangle(x0, y0, x1, y1, fill=color)
    canvas.create_text(10, 10, text=f"Time Complexity:\n{complexity}",
                       anchor="nw", font=("Arial", 12, "bold"), fill="black")
    canvas.update_idletasks()


def visualizer(canvas, steps, delay=0.1, complexity=""):
    for state, active_index, compare_index in steps:
        draw_bars(canvas, state, active_index=active_index, compare_index=compare_index, complexity=complexity)
        time.sleep(delay)

# main window
def main():
    root = tk.Tk()
    root.title("Algorithm Visualization")
    root.geometry("1000x900")

    #for exit button
    def on_exit():
        print('Exit button has been clicked')
        root.destroy()

    #title label
    root_label = tk.Label(root, text="Algorithm Visualization", font=("Arial", 20))
    root_label.pack(pady=20)
    print('title load')

    #creates the canvas
    canvas = tk.Canvas(root, width=400, height=300, bg="white")
    canvas.pack()
    print('canvas created')

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

    def how_many_elements() -> int:
        n = simpledialog.askinteger("Input", "How many numbers do you want to sort?", parent=root)
        print(n)
        return n

    # console log for buttons and also shows the results on the page
    def on_clicked(name: str):
        print(name, 'has been clicked')

        # checking what items will be accessed
        match name:
            case 'Insertion Sort':
                # asking the user how many number
                n = how_many_elements()

                # if nothing, then just return nothing
                if n is None:
                    return

                # else add a list then call insertion sort with the number they wanted (mainly used for me to practice coding it)
                num = creatingTheList(n)
                num2 = insertionSort(num.copy())
                #goes through the universal method and also calling the steps
                steps = insertion_sort_steps(num.copy())
                complexity = COMPLEXITIES.get(name, "")
                visualizer(canvas, steps, complexity=complexity)
                #showing the differnace between unsorted and sorted
                show_algorithm('Insertion Sort', num, num2)
            case "Bubble Sort":
                n = how_many_elements()
                if n is None:
                    return

                #does the sorting in the background first
                num = creatingTheList(n)
                num2 = bubbleSort(num.copy())
                #fixes the visulizer
                steps = bubble_sort_steps(num.copy())
                complexity = COMPLEXITIES.get(name, "")
                visualizer(canvas, steps, complexity=complexity)
                show_algorithm('Bubble Sort', num, num2)
            case "Selection Sort":
                n = how_many_elements()
                if n is None:
                    return

                #does sorting in the back ground
                num = creatingTheList(n)
                num2 = selection_sort(num.copy())
                #visualzer
                steps = selection_sort_steps(num.copy())
                complexity = COMPLEXITIES.get(name, "")
                visualizer(canvas, steps, complexity=complexity)
                show_algorithm('Selection Sort', num, num2)
            case 'Merge Sort':
                n = how_many_elements()
                if n is None:
                    return

                #does sorting in the background
                num = creatingTheList(n)
                num2 = mergeSort(num.copy())

                #visulizer
                steps = merge_sort_steps(num.copy())
                complexity = COMPLEXITIES.get(name, "")
                visualizer(canvas, steps, complexity=complexity)
                show_algorithm('Merge Sort', num, num2)

    #Insertion Sort
    insort_button = tk.Button(root, text="Insertion Sort", command=lambda: on_clicked('Insertion Sort'), width=20)
    insort_button.pack(pady=15)

    #bubble sort
    bubble_button = tk.Button(root, text="Bubble Sort", command=lambda: on_clicked('Bubble Sort'), width=20)
    bubble_button.pack(pady=15)

    #selection sort
    selection_button = tk.Button(root, text="Selection Sort", command=lambda: on_clicked('Selection Sort'), width=20)
    selection_button.pack(pady=15)

    #merge sort
    merge_button = tk.Button(root, text="Merge Sort", command=lambda: on_clicked('Merge Sort'), width=20)
    merge_button.pack(pady=15)

    # exit button
    exit_button = tk.Button(root, text="Exit", command=on_exit, width=20)
    exit_button.pack(pady=15)

    root.mainloop()

if __name__ == '__main__':
    main()