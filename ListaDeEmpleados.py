import tkinter as tk
from tkinter import ttk

class App():
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.title("List of employee")
        self.window.geometry("1000x700")

        #Label employees
        ttk.Label(self.window, text="Employees").grid(column=0,row=0, ipadx=5, ipady=5)

# ------------------------------------------------------------------------------------------------------------------ #
        #Nombre1
        ttk.Label(self.window, text="Pedro").grid(column=0,row=1, ipadx=5, ipady=5)

        #Imagen1
        catsmurf = tk.PhotoImage(file='hierarchyGUI-LP2/img/catSmurf.png') 
        ttk.Label(self.window, image=catsmurf).grid(column=0,row=2)

        #Nombre1
        ttk.Label(self.window, text="Ing. Sistemas").grid(column=0,row=3, ipadx=5, ipady=5)

# ------------------------------------------------------------------------------------------------------------------ #

# ------------------------------------------------------------------------------------------------------------------ #
        #Nombre2
        ttk.Label(self.window, text="Manuel").grid(column=1,row=1, ipadx=5, ipady=5)

        #Imagen2
        catsmurf2 = tk.PhotoImage(file='hierarchyGUI-LP2/img/catSmurf.png') 
        ttk.Label(self.window, image=catsmurf2).grid(column=1,row=2)

        #Nombre2
        ttk.Label(self.window, text="Lic. Administracion").grid(column=1,row=3, ipadx=5, ipady=5)

# ------------------------------------------------------------------------------------------------------------------ #

# ------------------------------------------------------------------------------------------------------------------ #
        #Nombre3
        ttk.Label(self.window, text="Maria").grid(column=2,row=1, ipadx=5, ipady=5)

        #Imagen3
        catsmurf3 = tk.PhotoImage(file='hierarchyGUI-LP2/img/catSmurf.png') 
        ttk.Label(self.window, image=catsmurf3).grid(column=2,row=2)

        #Nombre3
        ttk.Label(self.window, text="Arquitecto").grid(column=2,row=3, ipadx=5, ipady=5)

# ------------------------------------------------------------------------------------------------------------------ #

        self.window.mainloop()
if __name__ == '__main__':
    App()