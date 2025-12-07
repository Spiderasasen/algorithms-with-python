import tkinter as tk
import time

def draw_bars(canvas, array, active_index=None, compare_index=None, complexity="", name=""):
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
    canvas.create_text(10, 10, text=f"{name}:", anchor="nw", font=("Arial", 20, "bold"), fill="black")
    canvas.create_text(40,40, text=f"Time Complexity:\n{complexity}",
                       anchor="nw", font=("Arial", 12, "bold"), fill="black")
    canvas.update_idletasks()

def visualizer(canvas, steps, delay=0.1, complexity="", name=""):
    for state, active_index, compare_index in steps:
        draw_bars(canvas, state, active_index=active_index, compare_index=compare_index, complexity=complexity, name=name)
        time.sleep(delay)