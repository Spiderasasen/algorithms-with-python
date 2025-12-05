from tkinter import simpledialog
from sorting.bubble import bubbleSort, bubble_sort_steps
from sorting.insert import insertionSort, insertion_sort_steps
from sorting.selection import selection_sort, selection_sort_steps
from sorting.merge import mergeSort, merge_sort_steps
from components.main_algoithm_layout import main_layout, quick_sort_layout
from sorting.qucik_sort import randomized_quicksort, randomized_quick_sort_steps

#checking how many elements are called
def how_many_elements(root) -> int:
    n = simpledialog.askinteger("Input", "How many numbers do you want to sort?", parent=root)
    #if no element found, just return
    if n is None:
        return
    #if an element is found, return the number
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
            #does the thing
            main_layout(root, canvas, name, n, insertionSort, insertion_sort_steps, COMPLEXITIES)
        case "Bubble Sort":
            n = how_many_elements(root)
            #does the thing
            main_layout(root, canvas, name, n, bubbleSort, bubble_sort_steps, COMPLEXITIES)
        case "Selection Sort":
            n = how_many_elements(root)
            #does a thing
            main_layout(root, canvas, name, n, selection_sort, selection_sort_steps, COMPLEXITIES)
        case 'Merge Sort':
            n = how_many_elements(root)
            #does a thing
            main_layout(root, canvas, name, n, mergeSort, merge_sort_steps, COMPLEXITIES)
        case "Quick Sort":
            n = how_many_elements(root)
            #does a thing
            quick_sort_layout(root, canvas, name, n, randomized_quicksort, randomized_quick_sort_steps, COMPLEXITIES)