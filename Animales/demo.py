import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import simpledialog

class Animal(ttk.Frame):
    def __init__(self, master, name):
        super().__init__(master)
        self._name = name
        image = Image.open(f'hierarchyGUI-LP2/Animales/img/{self.name}.png')
        resized_image = image.resize((200, 200))  # Cambiar la resolución a 200x200
        self.picture = ImageTk.PhotoImage(resized_image)
        self.picture_label = ttk.Label(self, image=self.picture)
        self.picture_label.grid(column=0, row=1)
        self.name_label = ttk.Label(self, text=self.name)
        self.name_label.grid(column=0, row=0)

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

class App():
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.title('Animals')
        self.window.geometry('1000x700')
        
        self.myListbox = tk.Listbox(self.window)
        self.myListbox.grid(column=0, row=0, padx=15, pady=15)
        
        # Create Animal objects
        animal1 = Animal(self.window, 'Amogus')
        animal2 = Animal(self.window, 'smurfcat')
        
        # Store Animal objects in a list
        self.animalsList = [animal1, animal2]

        self.add_button = ttk.Button(self.window, text="Add Element", command=self.add_element)
        self.add_button.grid(column=0, row=2, padx=15, pady=15)
        
        for animal in self.animalsList:
            self.myListbox.insert(tk.END, animal.name)
        
        self.myListbox.bind('<<ListboxSelect>>', self.show_details)
        
        self.animal_frame = None

    def add_element(self):
        element = simpledialog.askstring("Add Element", "Enter the element to add:")
        if not element:
            element = "default"
        self.myListbox.insert(tk.END, element)

    def show_details(self, event):
        selected_item_index = self.myListbox.curselection()
        
        if selected_item_index:
            selected_index = selected_item_index[0]
            selected_item = self.animalsList[selected_index]
            
            if self.animal_frame is not None:
                # Destroy the previous frame
                self.animal_frame.destroy()
            
            # Create a new frame for the selected animal
            self.animal_frame = Animal(self.window, selected_item.name)
            self.animal_frame.grid(column=1, row=0)


if __name__ == '__main__':
    App()
    tk.mainloop()
