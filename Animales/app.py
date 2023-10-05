#https://github.com/jphed/hierarchyGUI-LP2
#type in terminal: pip install pillow
#type in terminal: pip install pillow
#type in terminal: pip install pillow
#type in terminal: pip install pillow
#type in terminal: pip install pillow
#type in terminal: pip install pillow
#type in terminal: pip install pillow
#type in terminal: pip install pillow
#type in terminal: pip install pillow
#type in terminal: pip install pillow
#type in terminal: pip install pillow
#type in terminal: pip install pillow
#type in terminal: pip install pillow
#type in terminal: pip install pillow
#type in terminal: pip install pillow
#type in terminal: pip install pillow
#type in terminal: pip install pillow
#type in terminal: pip install pillow

import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog, messagebox, scrolledtext
import os
from animal import Animal
from PIL import Image, ImageTk

class App():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Animals')
        self.window.pack_propagate(False)  # Set to False to allow automatic resizing
        
        self.myListbox = tk.Listbox(self.window, font=('Arial', 10))
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

        self.delete_button = ttk.Button(self.window, text="Delete Element", command=self.delete_element)
        self.delete_button.grid(column=1, row=2, padx=15, pady=15)

        self.show_files_button = ttk.Button(self.window, text="Show Files", command=self.show_files)
        self.show_files_button.grid(column=0, row=3, padx=15, pady=15)
        
        # Bind ListboxSelect event to update_picture function
        self.myListbox.bind("<<ListboxSelect>>", self.update_picture)

        # Set initial picture and name to first animal in list
        self.current_animal = self.animalsList[0]
        self.picture_label = ttk.Label(self.window, image=self.current_animal.picture)
        self.picture_label.grid(column=1, row=0, padx=15, pady=15)
        self.name_label = ttk.Label(self.window, text=self.current_animal.name, font=('Arial', 18))
        self.name_label.grid(column=1, row=1, padx=15, pady=15)

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
            # Update picture and name
            self.picture_label.configure(image=self.current_animal.picture)
            self.name_label.configure(text=self.current_animal.name)

    def add_element(self):
        element = simpledialog.askstring("Add Element", "Enter the element to add:")
        if not element:
            element = "default"
        # Find corresponding image
        try:
            image = Image.open(f'hierarchyGUI-LP2/Animales/img/{element}.png')
        except FileNotFoundError:
            messagebox.showerror("Error", f"No image found for {element}")
            return
        resized_image = image.resize((200, 200))
        self.current_animal = Animal(self.window, element)  
        self.current_animal.picture = ImageTk.PhotoImage(resized_image)
        self.picture_label.configure(image=self.current_animal.picture)
        self.myListbox.insert(tk.END, element)

    def delete_element(self):
        selection = self.myListbox.curselection()
        if selection:
            index = selection[0]
            name = self.myListbox.get(index)
            # Find corresponding Animal object
            for animal in self.animalsList:
                if animal.name == name:
                    self.animalsList.remove(animal)
                    break
            # Delete item from Listbox
            self.myListbox.delete(index)
            # Update picture
            if self.animalsList:
                # Set current animal to first animal in list
                self.current_animal = self.animalsList[0]
                self.picture_label.configure(image=self.current_animal.picture)
            else:
                # Set current animal to None and clear picture
                self.current_animal = None
                self.picture_label.configure(image=None)

            self.animal_frame = None

    def show_files(self):
        # Create new window
        files_window = tk.Toplevel(self.window)
        files_window.title('Available Files')
        files_window.geometry('300x200')
        
        # Get list of files in img folder
        files = os.listdir('hierarchyGUI-LP2/Animales/img')
        # Create ScrolledText widget to display available files
        file_list = scrolledtext.ScrolledText(files_window, width=30, height=10)
        file_list.grid(column=0, row=0, padx=15, pady=15)
        # Insert file names into ScrolledText widget
        for file in files:
            file_list.insert(tk.END, file + '\n')

        file_list.config(state=tk.DISABLED)

if __name__ == '__main__':
    App()
    tk.mainloop()