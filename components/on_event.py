from tkinter import simpledialog
from components.visulaize import visualizer
from components.algoirthm_results import show_algorithm
from sorting.bubble import bubbleSort, bubble_sort_steps
from components.creat_list import creatingTheList
from sorting.insert import insertionSort, insertion_sort_steps
from sorting.selection import selection_sort, selection_sort_steps
from sorting.merge import mergeSort, merge_sort_steps


def how_many_elements(root) -> int:
    n = simpledialog.askinteger("Input", "How many numbers do you want to sort?", parent=root)
    print(n)
    return n

# Dictionary of complexities for each algorithm
COMPLEXITIES = {
    "Insertion Sort": "Best: O(n), \nAverage/Worst: O(n^2)",
    "Bubble Sort": "Best: O(n), \nAverage/Worst: O(n^2)",
    "Selection Sort": "Always: O(n^2)",
    "Merge Sort": "Best/Average/Worst: O(n log n)",
    "Quick Sort": "Best/Average: O(n log n), \nWorst: O(n^2)",
    "Heap Sort": "Best/Average/Worst: O(n log n)"
}

# console log for buttons and also shows the results on the page
def on_clicked(name: str, root, canvas):
    print(name, 'has been clicked')

    # checking what items will be accessed
    match name:
        case 'Insertion Sort':
            # asking the user how many number
            n = how_many_elements(root)

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
            n = how_many_elements(root)
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
            n = how_many_elements(root)
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
            n = how_many_elements(root)
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