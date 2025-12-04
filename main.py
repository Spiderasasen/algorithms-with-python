import tkinter as tk
from tkinter import simpledialog
import time
from sorting.bubble import bubbleSort
from components.creat_list import creatingTheList
from sorting.insert import insertionSort
from sorting.selection import selection_sort
from sorting.merge import mergeSort
from typing import List, Optional, Tuple

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


def insertion_sort_steps(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        # highlight the key
        yield array[:], i, j
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
            yield array[:], i, j  # yield after each shift
        array[j + 1] = key
        yield array[:], i, None  # yield after placing key

def bubble_sort_steps(array):
    n = len(array)
    swapped: bool = True
    while swapped:
        swapped = False
        for j in range (0, n-1):
            #yielding before comparison
            yield array[:], j, j+1
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
                #yield after swap
                yield array[:], j, j+1
        n -= 1

def selection_sort_steps(array):
    n = len(array)
    for i in range(n):
        minIndex = i
        for j in range(i + 1, n):
            # highlight i (red) and j (green)
            yield array[:], i, j
            if array[j] < array[minIndex]:
                minIndex = j
                # highlight new minIndex (could use green again)
                yield array[:], i, minIndex
        # swap the found minimum into place
        array[i], array[minIndex] = array[minIndex], array[i]
        yield array[:], i, minIndex

def merge_sort_steps(array: List[int]):
    yield array[:], None, None
    if len(array) <= 1:
        return array

    mid = len(array) // 2

    left = array[:mid]
    right = array[mid:]

    left_sorted: List[int] = yield from merge_sort_steps(left)   # get final sorted left
    right_sorted: List[int] = yield from merge_sort_steps(right) # get final sorted right

    merged:List[int] = []
    i = j = 0
    while i < len(left_sorted) and j < len(right_sorted):
        #makes a sythitic state of visual
        state = merged + left_sorted[i:] + right_sorted[j:]

        #computes highlight indices within state
        active_index = len(merged) #for left candiaite
        compare_index = len(merged) + (len(left_sorted) - i) #for right caniadate

        # highlight comparison
        yield state, active_index, compare_index

        if left_sorted[i] <= right_sorted[j]:
            merged.append(left_sorted[i])
            i += 1
        else:
            merged.append(right_sorted[j])
            j += 1
        yield merged + left_sorted[i:] + right_sorted[j:], i, j

        #post-append frame
        state = merged + left_sorted[i:] + right_sorted[j:]

        #recomputing the indeices
        active_index = len(merged)  # for left candiaite
        compare_index = len(merged) + (len(left_sorted) - i)  # for right caniadate

        yield state, active_index, compare_index

    #append finals
    merged.extend(left_sorted[i:])
    merged.extend(right_sorted[j:])

    #drawing the final vision
    yield merged, None, None
    return merged


# main window
def main():
    root = tk.Tk()
    root.title("Algorithm Visualization")
    root.geometry("900x800")

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
                num2 = num.copy()
                num2 = insertionSort(num2)
                print(num2)
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