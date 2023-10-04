import tkinter as tk
from tkinter import ttk
import random


class Dado(ttk.Frame):
    def __init__(self, master, valor=6):
        super().__init__(master, borderwidth=2, relief="solid")
        self.__valor = tk.IntVar(value=valor)
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
        self.image_path = f'hierarchyGUI-LP2/Dados/img/{self.valor}.png'
        self.photo = tk.PhotoImage(file=self.image_path)
        label = self.winfo_children()[0]
        label.configure(image=self.photo)
