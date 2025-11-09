from tkinter import *
from tkinter.messagebox import showinfo

class Penjumlahan:
    #buat constructor
    def __init__(self, master):
        self.hasil = 0
        self.master = master
        master.title("Aplikasi Penjumlahan")
        master.geometry("500x200")
        #buat label "Masukkan bilangan pertama:” dengan tambahan grid
        label_bilangan1 = Label(master, text="Masukkan bilangan pertama: ")
        label_bilangan1.grid(row=1, column=1)
        #buat Entry untuk input bilangan pertama dengan tambahan grid dan jenis IntVar
        self.entry_bilangan1 = Entry(master)
        self.entry_bilangan1.grid(row=1, column=2)
        #buat label "Masukkan bilangan kedua:” dengan tambahan grid
        label_bilangan2 = Label(master, text="Masukkan bilangan kedua: ")
        label_bilangan2.grid(row=2, column=1)
        #buat Entry untuk input bilangan kedua dengan tambahan grid dan jenis IntVar
        self.entry_bilangan2 = Entry(master)
        self.entry_bilangan2.grid(row=2, column=2)
        #buat Button Hitung untuk menghitung penjumlahan dan menampilkan hasil penjumlahan
        self.button_hitung = Button(master, text="Hitung", width=10, height=2, bg="lightblue", command=self.tambah)
        self.button_hitung.grid(row=3, column=2)
        #buat Label Hasil untuk menampilkan label hasil dengan tambahan grid
        self.label_hasil = Label(master, text="Hasil: ")
        self.label_hasil.grid(row=4, column=2)
    #buat def function tambah untuk menghitung hasil penjumlahan
    def tambah(self):
        bilangan1 = self.entry_bilangan1.get()
        bilangan2 = self.entry_bilangan2.get()
        self.hasil = int(bilangan1) + int(bilangan2)
        self.label_hasil.config(text=f"Hasil: {self.hasil}")
#buat master Tkinter
master = Tk()
#buat object dari class HelloMhs_v2
penjumlahan = Penjumlahan(master)
#Jalankan TKinter
master.mainloop()