list_angka = [1,20,300,4400,5000,601,0.7,0.8,9,10]

angka_terbesar = list_angka[0]

a = 0

print(f"Angka terbesar sekarang = {angka_terbesar}\n")

print("For-Loop")
print("--------")
for i in range(len(list_angka)):
    if angka_terbesar < list_angka[i]:
        print(f"{angka_terbesar} < {list_angka[i]}")
        angka_terbesar = list_angka[i]
        print(f"Angka terbesar sekarang = {angka_terbesar}\n")
    else:
        # angka_terbesar = angka_terbesar
        print(f"{angka_terbesar} > {list_angka[i]}")
        print(f"Angka terbesar sekarang = {angka_terbesar}\n")
        
print("==============================\n")

print("While-Loop")
print("----------")
while a < len(list_angka):
    if angka_terbesar < list_angka[a]:
        print(f"{angka_terbesar} < {list_angka[a]}")
        angka_terbesar = list_angka[a]
        a += 1
        print(f"Angka terbesar sekarang = {angka_terbesar}\n")
    else:
        print(f"{angka_terbesar} > {list_angka[a]}")
        print(f"Angka terbesar sekarang = {angka_terbesar}\n")
        a += 1
        