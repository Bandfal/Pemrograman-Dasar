try:
    with open("database_mahasiswa.txt", "r", encoding="utf-8") as file:
        isi_file = file.read()
        data = eval(isi_file)  # ubah teks ke dictionary

    nama_cari = input("Masukkan nama mahasiswa: ").capitalize()
    ditemukan = False

    # Loop untuk mencari di dictionary
    for prodi, info in data.items():
        nama_pendek = info["nama_pendek"]
        nama_lengkap = info["nama_lengkap"]
        daftar_nim = info["nim"]
        alamat = info["alamat"]
        matakuliah = info["matakuliah"]

        if nama_cari in nama_pendek:
            index = nama_pendek.index(nama_cari)
            print(f"\nNama Lengkap : {nama_lengkap[index]}")
            print(f"NIM          : {daftar_nim[index]}")
            print(f"Prodi        : {prodi}")
            print(f"Alamat Kampus: {alamat}")
            print(f"Matakuliah   : {', '.join(matakuliah)}")
            ditemukan = True
            break

    if not ditemukan:
        print("⚠️ Data mahasiswa tidak ditemukan.")

except FileNotFoundError:
    print("❌ File database tidak ditemukan. Jalankan dulu file 'simpan_data.py'.")
except Exception as e:
    print("Terjadi kesalahan:", e)