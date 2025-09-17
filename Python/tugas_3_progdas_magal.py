kata = input("Masukkan kata: ")
cek_vokal = kata.lower()
vokal = 0
for i in range(len(cek_vokal)):
    if cek_vokal[i] == 'a':
        print(cek_vokal[i])
        vokal += 1
    elif cek_vokal[i] == 'i':
        print(cek_vokal[i])
        vokal += 1
    elif cek_vokal[i] == 'u':
        print(cek_vokal[i])
        vokal += 1
    elif cek_vokal[i] == 'e':
        print(cek_vokal[i])
        vokal += 1
    elif cek_vokal[i] == 'o':
        print(cek_vokal[i])
        vokal += 1
    else:
        vokal = vokal
print(f"Jumlah huruf vokal dalam {kata} adalah {vokal}")