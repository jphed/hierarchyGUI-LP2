import tkinter as tk
from tkinter import ttk

class Animal(ttk.Frame):
    def __init__(self, master, name):
        super().__init__(master)
        self._name = name  # Use a private variable for name
        self.picture = tk.PhotoImage(file=f'hierarchyGUI-LP2/Animales/img/{self.name}.png')
        
        # Create a Label widget to display the picture
        ttk.Label(master, textvariable=self.name).grid(column=0, row=0)
        self.picture_label = ttk.Label(self, image=self.picture).grid(column=0, row=1)

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
        return f"Animal: {self.name}"
