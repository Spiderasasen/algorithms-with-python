import tkinter as tk
from components.on_event import on_clicked
from components.scroll import ScrollableFrame

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

    #Insertion Sort
    insort_button = tk.Button(content, text="Insertion Sort", command=lambda: on_clicked('Insertion Sort', root, canvas), width=20)
    insort_button.grid(row=2, column=0 ,pady=15)

    #bubble sort
    bubble_button = tk.Button(content, text="Bubble Sort", command=lambda: on_clicked('Bubble Sort', root, canvas), width=20)
    bubble_button.grid(row=3, column=0 ,pady=15)

    #selection sort
    selection_button = tk.Button(content, text="Selection Sort", command=lambda: on_clicked('Selection Sort', root, canvas), width=20)
    selection_button.grid(row=4, column=0, pady=15)

    #merge sort
    merge_button = tk.Button(content, text="Merge Sort", command=lambda: on_clicked('Merge Sort', root, canvas), width=20)
    merge_button.grid(row=5, column=0, pady=15)

    #quick sort
    quick_sort_button = tk.Button(content, text="Randomized Quick Sort", command=lambda: on_clicked('Quick Sort', root, canvas), width=20)
    quick_sort_button.grid(row=6, column=0, pady=15)

    #heap sort
    heap_button = tk.Button(content, text="Heap Sort", command=lambda: on_clicked('Heap Sort', root, canvas), width=20)
    heap_button.grid(row=7, column=0, pady=15)

    #counting sort
    count_button = tk.Button(content, text="Counting Sort", command=lambda: on_clicked('Counting Sort', root, canvas), width=20)
    count_button.grid(row=8, column=0, pady=15)

    #radix sort
    radix_button = tk.Button(content, text="Radix Sort", command=lambda: on_clicked('Radix Sort', root, canvas), width=20)
    radix_button.grid(row=9, column=0, pady=15)

    #bucket sort
    bucket_button = tk.Button(content, text="Bucket Sort", command=lambda: on_clicked('Bucket Sort', root, canvas), width=20)
    bucket_button.grid(row=10, column=0, pady=15)

    # exit button
    exit_button = tk.Button(content, text="Exit", command=on_exit, width=20)
    exit_button.grid(row=11, column=0, pady=15)

    root.mainloop()

if __name__ == '__main__':
    main()