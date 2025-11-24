# --- TUGAS: Pembuatan kasus menggunakan notasi Big(O)

# ---Kelompok [Semangat]---
# 1. Christoford N. Gumerung (250211060020)
# 2. Gerald I. Manulang (250211060004)
# 3. Marvel E. Kumaat (250211060066)

# Program: Sistem Pencarian dan Pengurutan Produk
# Tujuan: Mensimulasikan dua jenis kompleksitas (O(n) dan O(n²))
# Prinsip readability diterapkan: nama variabel jelas, fungsi terpisah, komentar informatif

# Fungsi 1: Mencari produk berdasarkan nama (kompleksitas O(n))
def cari_produk(daftar_produk, nama_dicari):
    """
    Melakukan pencarian produk berdasarkan nama.
    Menggunakan pencarian linear (linear search).
    Kompleksitas waktu: O(n)
    """
    for produk in daftar_produk:
        if produk["nama"].lower() == nama_dicari.lower():
            return produk  # ditemukan → langsung kembalikan hasil
    return None  # tidak ditemukan


# Fungsi 2: Mengurutkan produk berdasarkan harga (kompleksitas O(n²))
def urutkan_produk_berdasarkan_harga(daftar_produk):
    """
    Mengurutkan daftar produk dari harga terendah ke tertinggi.
    Menggunakan algoritma bubble sort.
    Kompleksitas waktu: O(n²)
    """
    n = len(daftar_produk)
    for i in range(n):
        for j in range(0, n - i - 1):
            if daftar_produk[j]["harga"] > daftar_produk[j + 1]["harga"]:
                # Tukar posisi jika harga tidak sesuai urutan
                daftar_produk[j], daftar_produk[j + 1] = daftar_produk[j + 1], daftar_produk[j]


def main():
    # Daftar produk dalam toko online
    produk_list = [
        {"nama": "Laptop", "harga": 8500000},
        {"nama": "Mouse", "harga": 150000},
        {"nama": "Keyboard", "harga": 300000},
        {"nama": "Monitor", "harga": 1200000},
        {"nama": "Headset", "harga": 250000}
    ]

    print("=== Sistem Pencarian dan Pengurutan Produk ===\n")

    # O(n): Cari produk
    nama_dicari = "Mouse"
    hasil = cari_produk(produk_list, nama_dicari)
    if hasil:
        print(f"Produk '{nama_dicari}' ditemukan dengan harga Rp{hasil['harga']:,}")
    else:
        print(f"Produk '{nama_dicari}' tidak ditemukan.")

    # O(n²): Urutkan produk
    print("\nDaftar produk sebelum diurutkan:")
    for p in produk_list:
        print(f"- {p['nama']:10} : Rp{p['harga']:,}")

    urutkan_produk_berdasarkan_harga(produk_list)

    print("\nDaftar produk setelah diurutkan berdasarkan harga:")
    for p in produk_list:
        print(f"- {p['nama']:10} : Rp{p['harga']:,}")


if __name__ == "__main__":
    main()
