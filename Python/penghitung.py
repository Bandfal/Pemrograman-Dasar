from tkinter import *

class Penghitung:
    def __init__(self, master):
        self.master = master
        master.title("Penghitung Sederhana")
        master.geometry("600x200")
        
        self.hitungan = 0

        self.label = Label(master, text=self.hitungan, font=("Arial", 24))
        self.label.pack(pady=20)
        
        self.button_tambah = Button(master, text="Tambah", command=self.tambah, bg="lightgreen")
        self.button_tambah.pack()
        
        self.button_kurang = Button(master, text="Kurang", command=self.kurang, bg="red")
        self.button_kurang.pack()

    def tambah(self):
        self.hitungan += 1
        self.label.config(text=self.hitungan)

    def kurang(self):
        self.hitungan -= 1
        self.label.config(text=self.hitungan)
master = Tk()
penghitung = Penghitung(master)
master.mainloop()