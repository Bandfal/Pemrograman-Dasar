# =====================================
# Soal Take Home Test - Database Mahasiswa
# File 1: Membuat file data mentah + dictionary
# =====================================

# --- 1. Data Mahasiswa ---
nama_mahasiswa = ["Naufal", "Adit", "Ripan"]
nama_lengkap_mahasiswa = ["Muhammad Naufal Akif Magal", "Aditya Hendra Paramuda", "Taqrifan Wicaksono"]
nim = ["25031554183", "25031554275", "25031554165"]
nama_prodi = ("Sains Data",)
alamat_kampus = ("Jl. A.Yani No.25, Surabaya",)
matakuliah = {"Kalkulus", "Pemrograman", "Statistika"}

# --- 2. Simpan file database polosan (belum bentuk dictionary) ---
with open("database_mahasiswa_polosan.txt", "w", encoding="utf-8") as file_raw:
    file_raw.write("=== DATA MAHASISWA ===\n")
    for i in range(len(nama_mahasiswa)):
        file_raw.write(f"{i+1}. {nama_lengkap_mahasiswa[i]} ({nama_mahasiswa[i]})\n")
        file_raw.write(f"   NIM   : {nim[i]}\n")
        file_raw.write(f"   Prodi : {nama_prodi[0]}\n")
        file_raw.write(f"   Alamat: {alamat_kampus[0]}\n")
        file_raw.write(f"   Mata Kuliah: {', '.join(matakuliah)}\n\n")

print("✅ File 'database_mahasiswa_polosan.txt' berhasil dibuat.")

# --- 3. Buat dictionary sesuai permintaan soal ---
data_mahasiswa = {
    nama_prodi[0]: {
        "nama_pendek": nama_mahasiswa,
        "nama_lengkap": nama_lengkap_mahasiswa,
        "nim": nim,
        "alamat": alamat_kampus[0],
        "matakuliah": list(matakuliah)
    }
}

# --- 4. Simpan dictionary ke file ---
with open("database_mahasiswa.txt", "w", encoding="utf-8") as file_dict:
    file_dict.write(repr(data_mahasiswa))

print("✅ File 'database_mahasiswa.txt' (dictionary) berhasil dibuat.")