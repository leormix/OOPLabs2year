import tkinter as tk

class Module1Dialog(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Window 1')
        self.geometry("260x120")
        self.resizable(0,0)
        self.transient(parent)
        self.grab_set()

        self.result = 0

        label = tk.Label(self, text='SWAG')
        label.pack(pady=10)

        btn_frame = tk.Frame(self)
        btn_frame.pack(pady= 5)

        btn_next = tk.Button(btn_frame, text='Next', width=10, command=self.on_next)
        btn_next.pack(side=tk.LEFT, padx=10)

        btn_next = tk.Button(btn_frame, text='Cancel', width=10, command=self.on_cancel)
        btn_next.pack(side=tk.LEFT, padx=5)

    def on_next(self):
        self.result = 1
        self.destroy()
        
    def on_cancel(self):
        self.result = 0
        self.destroy()


def run_step1(parent):
    dlg = Module1Dialog(parent)
    parent.wait_window(dlg)
    return dlg.result