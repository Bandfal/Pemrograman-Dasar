from math import *

a = int(input("Masukkan titik x1 = "))
b = int(input("Masukkan titik y1 = "))
c = int(input("Masukkan titik x2 = "))
d = int(input("Masukkan titik y2 = "))

print(f"""Titik pertama = {a, b}
Titik kedua   = {c, d}""")

def pythagoras(panjang, tinggi):
  return sqrt(panjang ** 2 + tinggi ** 2)

def jarak_titik(x1,y1,x2,y2):
  panjang = x2 - x1
  tinggi = y2 - y1
  jarak = pythagoras(panjang, tinggi)
  print(f"Hasil Pythagoras titik {a, b} dan titik {c, d} adalah = {jarak}")


jarak_titik(a,b,c,d)