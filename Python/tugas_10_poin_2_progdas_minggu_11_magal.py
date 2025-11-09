from tkinter import *
from tkinter.messagebox import showinfo

class HelloMhs:
    #buat constructor
    def __init__(self, master):
        self.master = master
        master.title("Hello Mahasiswa")
        master.geometry("500x300")
        #buat label "Masukkan nama panjang:" dengan tambahan grid
        label_nama = Label(master, text="Masukkan nama panjang: ")
        label_nama.grid(row=1, column=1)
        #buat Entry untuk input nama user dengan tambahan grid
        self.entry_nama = Entry(master, width=55)
        self.entry_nama.grid(row=1, column=2)
        #buat label "Masukkan NIM:" dengan tambahan grid
        label_nim = Label(master, text="Masukkan NIM: ")
        label_nim.grid(row=2, column=1, sticky=W)
        #buat Entry untuk input NIM user dengan tambahan grid
        self.entry_nim = Entry(master, width=55)
        self.entry_nim.grid(row=2, column=2)
        #buat Button Input untuk menampilkan showinfo hello mahasiswa
        self.button_input = Button(master, text="Input", width=10, height=2, bg="lightblue", command=self.input)
        self.button_input.grid(row=3, column=2)
    #buat def function input untuk menampilkan showinfo
    def input(self): 
        nama = self.entry_nama.get()
        nim = self.entry_nim.get()
        showinfo("Hello Mahasiswa", f"Hello {nama} dengan NIM {nim}, kamu pasti dari kelas 2025F ya?")
#buat master Tkinter
master = Tk()
#buat object dari class HelloMhs
hello_mhs = HelloMhs(master)
#Jalankan TKinter
master.mainloop()