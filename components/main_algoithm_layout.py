from components.creat_list import creatingTheList
from components.visulaize import visualizer
from components.algoirthm_results import show_algorithm
from typing import List

def main_layout(root, canvas, name: str,num_elements: int, sortingAlgorithmConsole, sortingAlgorithmVisualizer, complexity):
    #for the console log
    num:List[int] = creatingTheList(num_elements)
    num2: List[int] = sortingAlgorithmConsole(num.copy())
    print(f"{num2}\ndid the algorithm in the background")
    #for the visualizer
    print("starting the visual effects")
    steps = sortingAlgorithmVisualizer(num.copy())
    time = complexity.get(name, "")
    visualizer(canvas, steps, complexity=time, name=name)
    print("finished the visualization")
    #shows the results
    show_algorithm(root, name, num, num2)
    #showed the list

def quick_sort_layout(root, canvas, name: str, num_elements: int, sortingAlgorithmConsole, sortingAlgorithmVisualizer, complexity):
    # for the console log
    num: List[int] = creatingTheList(num_elements)
    num2: List[int] = sortingAlgorithmConsole(num.copy(), 0, len(num)-1)
    print(f"{num2}\ndid the algorithm in the background")
    # for the visualizer
    print("starting the visual effects")
    steps = sortingAlgorithmVisualizer(num.copy(), 0, len(num)-1)
    time = complexity.get(name, "")
    visualizer(canvas, steps, complexity=time, name=name)
    print("finished the visualization")
    # shows the results
    show_algorithm(root, name, num, num2)
    # showed the list