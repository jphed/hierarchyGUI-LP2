import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class AnimalCmp(ttk.Frame):
    animalsList = []

    def __init__(self, master, name):
        super().__init__(master)
        self._name = name
        image = Image.open(f'hierarchyGUI-LP2/Animales/img/{self.name}.png')
        resized_image = image.resize((200, 200))
        self.picture = ImageTk.PhotoImage(resized_image)
        self.picture_label = ttk.Label(self, image=self.picture)
        self.picture_label.grid(column=0, row=1)
        self.name_label = ttk.Label(self, text=self.name)
        self.name_label.grid(column=0, row=0)
        
        AnimalCmp.animalsList.append(self)  # Agregar objeto AnimalCmp a la lista

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            self._name = new_name
        else:
            raise ValueError("Name must be a string")

    def __str__(self):
        return f"AnimalCmp: {self.name}"

class Animal:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            self._name = new_name
        else:
            raise ValueError("Name must be a string")