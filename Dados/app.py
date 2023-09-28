import tkinter as tk
from tkinter import ttk
from dado import Dado

class App:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Dados")
        #self.window.geometry('1000x700')

        self.d1 = Dado(master=self.window, valor=6)
        self.d1.grid(row=0, column=0, padx=10)

        self.d2 = Dado(master=self.window, valor=6)
        self.d2.grid(row=0, column=1, padx=10)

        ttk.Button(text="Lanzar", command=self.lanzar_dado).grid(row=2, column=0, columnspan=2, pady=10, ipadx=5,ipady=5)

        self.window.mainloop()

    def lanzar_dado(self):
        self.d1.lanzar()
        self.d2.lanzar()

if __name__ == '__main__':
    App()
