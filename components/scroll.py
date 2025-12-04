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

        #adding this to the gird system
        self.scrollable_frame.grid_columnconfigure(0, weight=1)

        #updateing the scroll region
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        window_id = canvas.create_window((0,0), window=self.scrollable_frame, anchor="n")

        def _resize(event):
            canvas.itemconfig(window_id, width=event.width)

        canvas.bind("<Configure>", _resize)

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")