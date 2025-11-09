from tkinter import *
from tkinter.messagebox import showinfo

class HelloMhs:
    #buat constructor
    def __init__(self, master):
        self.master = master
        master.title("Hello Mahasiswa")
        master.geometry("500x300")
        #buat label "Masukkan nama kamu:"
        label_nama = Label(master, text="Masukkan nama kamu: ")
        label_nama.pack()
        #buat Entry untuk input nama user
        self.entry_nama = Entry(master)
        self.entry_nama.pack(pady=10)
        #buat label "Masukkan kelas:"
        label_kelas = Label(master, text="Kelas: ")
        label_kelas.pack()
        #buat Entry untuk input kelas user
        self.entry_kelas = Entry(master)
        self.entry_kelas.pack(pady=10)
        #buat Button Input untuk menampilkan showinfo hello mahasiswa
        self.button_input = Button(master, text="Input", width=10, height=2, bg="lightblue", command=self.input)
        self.button_input.pack(pady=20)
    #buat def function input untuk menampilkan showinfo
    def input(self): 
        nama = self.entry_nama.get()
        kelas = self.entry_kelas.get()
        showinfo("Hello Mahasiswa", f"Hello {nama} dari kelas {kelas}!")
#buat master Tkinter
master = Tk()
#buat object dari class HelloMhs
hello_mhs = HelloMhs(master)
#Jalankan TKinter
master.mainloop()