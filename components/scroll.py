import tkinter as tk
from typing import Union

parent = Union[tk.Tk, tk.Frame]

class ScrollableFrame(tk.Frame):
    def __init__(self, container: parent, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        #creats the scrollbar
        canvas = tk.Canvas(self)
        scrollbar = tk.Scrollbar(self, orient="vertical", command=canvas.yview)

        self.scrollable_frame = tk.Frame(canvas)

        #updateing the scroll region
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0,0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")