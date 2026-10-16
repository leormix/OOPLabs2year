import tkinter as tk
from tkinter import messagebox
from shapes import PointShape


class PaintApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Main window")
        self.geometry("500x400")

        self.current_tool = tk.StringVar(value="Dot")
        self.shapes = []

        self.init_menu()

        self.canvas = tk.Canvas(self, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.canvas.bind("<ButtonPress-1>", self.on_canvas_click)

    def init_menu(self):
        menubar = tk.Menu(self)

        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label='Exit', command=self.quit)
        menubar.add_cascade(label='File', menu=file_menu)

        objects_menu = tk.Menu(menubar, tearoff=0)

        tools = ["Dot", "Line", "Rectangle", "Ellipse"]

        for tool in tools:
            objects_menu.add_radiobutton(
                label=tool,
                variable=self.current_tool,
                value=tool,
                command=self.on_tool_changed
            )
        menubar.add_cascade(label='Objects', menu=objects_menu)

        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)

        menubar.add_cascade(label="Help", menu=help_menu)

        self.config(menu=menubar)

    def on_tool_changed(self):
        print(f"Chosen instrument: {self.current_tool.get()}")

    def show_about(self):
        messagebox.showinfo("Help", 'Some info')

    def on_canvas_click(self, event):
        if self.current_tool.get() == "Dot":
            if len(self.shapes) < 102:
                shape = PointShape(event.x, event.y)
                self.shapes.append(shape)
                shape.show(self.canvas)


if __name__ == "__main__":
    app = PaintApp()
    app.mainloop()
