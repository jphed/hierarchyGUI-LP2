import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import simpledialog

class Animal(ttk.Frame):
    animalsList = []  # Lista de objetos Animal

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
        
        Animal.animalsList.append(self)  # Agregar objeto Animal a la lista

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
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Animals')
        self.window.geometry('1000x700')
        
        self.myListbox = tk.Listbox(self.window)
        self.myListbox.grid(column=0, row=0, padx=15, pady=15)
        
        # Create Animal objects
        animal1 = Animal(self.window, 'Amogus')
        animal2 = Animal(self.window, 'smurfcat')
        
        # Store Animal objects in a list
        self.animalsList = Animal.animalsList

        # Add animals to Listbox
        for animal in self.animalsList:
            self.myListbox.insert(tk.END, animal.name)

        self.add_button = ttk.Button(self.window, text="Add Element", command=self.add_element)
        self.add_button.grid(column=0, row=2, padx=15, pady=15)
        
        # Bind ListboxSelect event to update_picture function
        self.myListbox.bind("<<ListboxSelect>>", self.update_picture)

        # Set initial picture to first animal in list
        self.current_animal = self.animalsList[0]
        self.picture_label = ttk.Label(self.window, image=self.current_animal.picture)
        self.picture_label.grid(column=1, row=0, padx=15, pady=15)

    def add_element(self):
        element = simpledialog.askstring("Add Element", "Enter the element to add:")
        if not element:
            element = "default"
        # Find corresponding image
        try:
            image = Image.open(f'hierarchyGUI-LP2/Animales/img/{element}.png')
        except FileNotFoundError:
            image = Image.open(f'hierarchyGUI-LP2/Animales/img/default.png')
        resized_image = image.resize((200, 200))
        self.current_animal = Animal(self.window, element)
        self.current_animal.picture = ImageTk.PhotoImage(resized_image)
        self.picture_label.configure(image=self.current_animal.picture)
        self.myListbox.insert(tk.END, element)

    def update_picture(self, event):
        # Get selected item from Listbox
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            name = event.widget.get(index)
            # Find corresponding Animal object
            for animal in self.animalsList:
                if animal.name == name:
                    self.current_animal = animal
                    break
            # Update picture
            self.picture_label.configure(image=self.current_animal.picture)

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
