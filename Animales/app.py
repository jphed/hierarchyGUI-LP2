import tkinter as tk
from tkinter import ttk
import animal as an

class App():
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.title('Animals')
        self.window.geometry('1000x700')
        
        self.myListbox = tk.Listbox(self.window)
        self.myListbox.grid(column=0, row=0, padx=15, pady=15)
        
        # Create Animal objects
        animal1 = an.Animal(self.window, 'Amogus')
        animal2 = an.Animal(self.window, 'smurfcat')
        
        # Store Animal objects in a list
        self.animalsList = [animal1, animal2]
        
        for animal in self.animalsList:
            self.myListbox.insert(tk.END, animal.name)
        
        self.myListbox.bind('<<ListboxSelect>>', self.show_details)
        
        self.animal_frame = None

    def show_details(self, event):
        selected_item_index = self.myListbox.curselection()
        
        if selected_item_index:
            selected_index = selected_item_index[0]
            selected_item = self.animalsList[selected_index]
            
            if self.animal_frame is not None:
                # Destroy the previous frame
                self.animal_frame.destroy()
            
            # Create a new frame for the selected animal
            self.animal_frame = an.Animal(self.window, selected_item.name)
            self.animal_frame.grid(column=1, row=0)


if __name__ == '__main__':
    App()
    tk.mainloop()