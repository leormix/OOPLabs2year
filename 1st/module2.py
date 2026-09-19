import tkinter as tk

class Module2Dialog(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Step 2")
        self.geometry("300x120")
        self.resizable(False, False)
        self.transient(parent)
        self.grab_set()

        self.result = 0

        label = tk.Label(self, text="SWAG 2.")
        label.pack(pady=10)

        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=5)

        btn_back = tk.Button(btn_frame, text="Back", width=8, command=self.on_back)
        btn_back.pack(side=tk.LEFT, padx=3)

        btn_finish = tk.Button(btn_frame, text="OK", width=8, command=self.on_finish)
        btn_finish.pack(side=tk.LEFT, padx=3)

        btn_cancel = tk.Button(btn_frame, text="Cancel", width=8, command=self.on_cancel)
        btn_cancel.pack(side=tk.LEFT, padx=3)

    def on_back(self):
        self.result = -1
        self.destroy()

    def on_finish(self):
        self.result = 1
        self.destroy()

    def on_cancel(self):
        self.result = 0
        self.destroy()

def run_step2(parent):
    dlg = Module2Dialog(parent)
    parent.wait_window(dlg)
    return dlg.result