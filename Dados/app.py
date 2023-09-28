import tkinter as tk
from tkinter import ttk
import random

class Dado(ttk.Frame):
    def __init__(self, master, valor=6):
        super().__init__(master, borderwidth=2, relief="solid")
        self.__valor = tk.IntVar(value=valor)  # Cambio en el nombre de la variable
        self.valor = valor
        self.image_path = f'hierarchyGUI-LP2/Dados/img/{self.valor}.png'
        self.photo = tk.PhotoImage(file=self.image_path)
        ttk.Label(self, image=self.photo).grid(column=0, row=1)

    @property
    def valor(self):
        return self.__valor.get()

    @valor.setter
    def valor(self, valor):
        if not isinstance(valor, int):
            raise TypeError("valor debe ser un número")
        if valor < 1 or valor > 6:
            raise ValueError("Valor debe estar entre 1 y 6")
        self.__valor.set(valor)

    def lanzar(self):
        new_value = random.randint(1, 6)
        self.valor = new_value
        self.update_image()

    def update_image(self):
        self.image_path = f'hierarchyGUI-LP2/Dados/img/{self.valor}.png'
        self.photo = tk.PhotoImage(file=self.image_path)
        label = self.winfo_children()[0]  # Obtener el primer widget (Label) dentro de este Frame
        label.configure(image=self.photo)

class App:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Dados")
        #self.window.geometry('1000x700')

        # PRIMER DADO
        self.d1 = Dado(master=self.window, valor=6)
        self.d1.grid(row=0, column=0, padx=10)

        # SEGUNDO DADO
        self.d2 = Dado(master=self.window, valor=6)
        self.d2.grid(row=0, column=1, padx=10)

        ttk.Button(text="Lanzar", command=self.lanzar_dado).grid(row=2, column=0, columnspan=2, pady=10, ipady=10)

        self.window.mainloop()

    def lanzar_dado(self):
        self.d1.lanzar()
        self.d2.lanzar()

if __name__ == '__main__':
    App()
