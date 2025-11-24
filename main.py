#Halaman Utama 
import operations
import input_handler

def main():
    while True:
        print("\n=== Kalkulator Sederhana ===")
        print("1. Tambah")
        print("2. Kurang")
        print("3. Kali")
        print("4. Bagi")
        print("5. Keluar")

        pilihan = input("Pilih operasi (1-5): ").strip()

        if pilihan == '5':
            print("Terima kasih!")
            break

        a, b = input_handler.get_numbers()

        if pilihan == '1':
            print("Hasil:", operations.tambah(a, b))
        elif pilihan == '2':
            print("Hasil:", operations.kurang(a, b))
        elif pilihan == '3':
            print("Hasil:", operations.kali(a, b))
        elif pilihan == '4':
            print("Hasil:", operations.bagi(a, b))
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
