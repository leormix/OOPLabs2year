import tkinter as tk


class Module3Dialog(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Step 3")
        self.geometry("300x220")
        self.resizable(False, False)
        self.transient(parent)
        self.grab_set()

        self.selected_group = None
        self.listbox = tk.Listbox(self, height=6)
        self.listbox.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)

        groups = ["IM-51", "IM-52", "IM-52", "IM-53", "IM-54"]

        for g in groups:
            self.listbox.insert(tk.END, g)

        self.listbox.selection_set(0)
        self.listbox.bind("<Double-Button-1>", lambda event: self.on_ok())
        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=10)

        btn_ok = tk.Button(btn_frame, text="OK", width=8, command=self.on_ok)
        btn_ok.pack(side=tk.LEFT, padx=5)

        btn_cancel = tk.Button(btn_frame, text="Cancel",
                               width=8, command=self.on_cancel)
        btn_cancel.pack(side=tk.LEFT, padx=5)

    def on_ok(self):
        cur_sel = self.listbox.curselection()
        if cur_sel:
            self.selected_group = self.listbox.get(cur_sel[0])
        self.destroy()

    def on_cancel(self):
        self.selected_group = None
        self.destroy()


def run_step3(parent):
    dlg = Module3Dialog(parent)
    parent.wait_window(dlg)
    return dlg.selected_group
