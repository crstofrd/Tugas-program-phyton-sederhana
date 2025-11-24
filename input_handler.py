#inputhandler.py 
def get_numbers():
    while True:
        try:
            a = float(input("Masukkan angka pertama: "))
            b = float(input("Masukkan angka kedua : "))
            return a, b
        except ValueError:
            print("Input tidak valid! Harus angka.\n")
