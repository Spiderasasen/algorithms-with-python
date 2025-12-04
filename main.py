import tkinter as tk
from tkinter import simpledialog
from components.visulaize import visualizer
from components.algoirthm_results import show_algorithm
from sorting.bubble import bubbleSort, bubble_sort_steps
from components.creat_list import creatingTheList
from sorting.insert import insertionSort, insertion_sort_steps
from sorting.selection import selection_sort, selection_sort_steps
from sorting.merge import mergeSort, merge_sort_steps
from components.scroll import ScrollableFrame

# Dictionary of complexities for each algorithm
COMPLEXITIES = {
    "Insertion Sort": "Best: O(n), \nAverage/Worst: O(n^2)",
    "Bubble Sort": "Best: O(n), \nAverage/Worst: O(n^2)",
    "Selection Sort": "Always: O(n^2)",
    "Merge Sort": "Best/Average/Worst: O(n log n)",
    "Quick Sort": "Best/Average: O(n log n), \nWorst: O(n^2)",
    "Heap Sort": "Best/Average/Worst: O(n log n)"
}

# main window
def main():
    root = tk.Tk()
    root.title("Algorithm Visualization")
    root.geometry("1000x900")

    #adding the scroll bar
    main_frame = ScrollableFrame(root)
    main_frame.pack(fill="both", expand=True)

    #making a grid system
    content = tk.Frame(main_frame.scrollable_frame)
    content.grid(row=0, column=0, sticky="n")
    #making where they can center
    content.grid_rowconfigure(0, weight=1)

    #for exit button
    def on_exit():
        print('Exit button has been clicked')
        root.destroy()

    #title label
    root_label = tk.Label(content, text="Algorithm Visualization", font=("Arial", 20))
    root_label.grid(row=0, column=0 ,pady=20)
    print('title load')

    #creates the canvas
    canvas = tk.Canvas(content, width=400, height=300, bg="white")
    canvas.grid(row=1, column=0, pady=10)
    print('canvas created')

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
                show_algorithm(root, 'Insertion Sort', num, num2)
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
                show_algorithm(root ,'Bubble Sort', num, num2)
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
                show_algorithm(root, 'Selection Sort', num, num2)
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
                show_algorithm(root, 'Merge Sort', num, num2)

    #Insertion Sort
    insort_button = tk.Button(content, text="Insertion Sort", command=lambda: on_clicked('Insertion Sort'), width=20)
    insort_button.grid(row=2, column=0 ,pady=15)

    #bubble sort
    bubble_button = tk.Button(content, text="Bubble Sort", command=lambda: on_clicked('Bubble Sort'), width=20)
    bubble_button.grid(row=3, column=0 ,pady=15)

    #selection sort
    selection_button = tk.Button(content, text="Selection Sort", command=lambda: on_clicked('Selection Sort'), width=20)
    selection_button.grid(row=4, column=0, pady=15)

    #merge sort
    merge_button = tk.Button(content, text="Merge Sort", command=lambda: on_clicked('Merge Sort'), width=20)
    merge_button.grid(row=5, column=0, pady=15)

    # exit button
    exit_button = tk.Button(content, text="Exit", command=on_exit, width=20)
    exit_button.grid(row=6, column=0, pady=15)

    root.mainloop()

if __name__ == '__main__':
    main()