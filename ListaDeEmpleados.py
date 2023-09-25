import tkinter as tk
from tkinter import ttk

class EmpleadoCmp(ttk.Frame):
    def __init__(self, master, name, photo, major) -> None:
        super().__init__(master, borderwidth=2, relief="solid")
        self.name = name
        ttk.Label(self, text=self.name).grid(column=0, row=0)
        self.pht = tk.PhotoImage(file=photo) 
        ttk.Label(self, image=self.pht).grid(column=0,row=1)
        ttk.Label(self, text=major).grid(column=0, row=2)

class App():
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.title("List of employees")
        self.window.geometry("1000x700")

        EmpleadoCmp(master=self.window, name="Rodolfo", photo="hierarchyGUI-LP2/img/catSmurf.png",
                     major='ITIT').grid(column=0,row=0)



        self.window.mainloop()


if __name__ == '__main__':
    App()