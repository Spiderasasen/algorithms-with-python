from tkinter import simpledialog
from sorting.bubble import bubbleSort, bubble_sort_steps
from sorting.insert import insertionSort, insertion_sort_steps
from sorting.selection import selection_sort, selection_sort_steps
from sorting.merge import mergeSort, merge_sort_steps
from components.main_algoithm_layout import main_layout, quick_sort_layout
from sorting.qucik_sort import randomized_quicksort, randomized_quick_sort_steps
from sorting.heaps import max_heap, max_heap_steps, min_heap, min_heap_steps
from sorting.counting import counting_sort, counting_sort_steps
from sorting.Radix import radix_sort, radix_sort_steps
from sorting.bucket import bucket_sort, bucket_sort_steps

#checking how many elements are called
def how_many_elements(root) -> int:
    n = simpledialog.askinteger("Input", "How many numbers do you want to sort?", parent=root)
    #if no element found, just return
    if n is None:
        return
    #if an element is found, return the number
    print(n)
    return n

def which_heap(root)-> str:
    n = simpledialog.askstring("Input", "Which heap do you want to sort?\nMin or Max", parent=root)
    #if no element found is found
    if n is None or n == "" or n.isdigit():
        print(n)
        return None
    print(n)
    return n

# Dictionary of complexities for each algorithm
COMPLEXITIES = {
    "Insertion Sort": "Best: O(n), \nAverage/Worst: O(n^2)",
    "Bubble Sort": "Best: O(n), \nAverage/Worst: O(n^2)",
    "Selection Sort": "Always: O(n^2)",
    "Merge Sort": "Best/Average/Worst: O(n log n)",
    "Quick Sort": "Best/Average: O(n log n), \nWorst: O(n^2)",
    "Heap Sort": "Best/Average/Worst: O(n log n)",
    "Counting Sort": "Best/Average/Worst: O(n + k)",
    "Radix Sort": "Best Case/Average/Worst: n + k",
    "Bucket Sort": "Best: n + k, \n Average: n, \n Worst: n^2"
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
        case "Heap Sort":
            n = how_many_elements(root)
            type_heap = which_heap(root)

            #if the user typed something other than min or max
            if type_heap is None:
                simpledialog.askstring("NO HEAP SELECTED", "going to do a merge sort instead", parent=root)
                main_layout(root, canvas, "Merge Sort", n, mergeSort, merge_sort_steps, COMPLEXITIES)

            heap = type_heap.lower()
            #calls the min heap function
            if "min" in heap:
                print("doing min")
                main_layout(root, canvas, name, n, min_heap, min_heap_steps, COMPLEXITIES)
            #calls the max heap function
            elif "max" in heap:
                print("doing max")
                main_layout(root, canvas, name, n, max_heap, max_heap_steps, COMPLEXITIES)
            else:
                simpledialog.askstring("NO HEAP SELECTED", "going to do a merge sort instead", parent=root)
                main_layout(root, canvas, "Merge Sort", n, mergeSort, merge_sort_steps, COMPLEXITIES)
        case "Counting Sort":
            n = how_many_elements(root)
            main_layout(root, canvas, name, n, counting_sort, counting_sort_steps, COMPLEXITIES)
        case "Radix Sort":
            n = how_many_elements(root)
            main_layout(root, canvas, name, n, radix_sort, radix_sort_steps, COMPLEXITIES)
        case "Bucket Sort":
            n = how_many_elements(root)
            main_layout(root, canvas, name, n, bucket_sort, bucket_sort_steps, COMPLEXITIES)