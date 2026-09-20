import tkinter as tk
from tkinter import messagebox
import module1
import module2
import module3


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Головне вікно")
        self.geometry("400x400")
        self.resizable(False, False)

        self.selected_group = 'Grupa ne vibrana'
        self.lbl_title = tk.Label(self, text='Result of choice')
        self.lbl_title.pack(pady=45)

        self.lbl_result = tk.Label(
            self, text=self.selected_group, font=("Arial", 11))
        self.lbl_result.pack(pady=5)

        menubar = tk.Menu(self)
        menubar.add_command(label="Робота1", command=self.popa1)
        menubar.add_command(label="Робота2", command=self.popa2)
        self.config(menu=menubar)

    def popa1(self):
        step = 1
        while step > 0:
            if step == 1:
                res = module1.run_step1(self)
                if res == 1:
                    step = 2
                else:
                    break
            elif step == 2:
                res = module2.run_step2(self)
                if res == 1:
                    messagebox.showinfo(
                        "Інформація", "Діалог завершено успішно!")
                    break
                elif res == -1:
                    step = 1
                else:
                    break

    def popa2(self):
        group = module3.run_step3(self)
        if group:
            self.selected_group = group
            self.lbl_result.config(text=self.selected_group)


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
