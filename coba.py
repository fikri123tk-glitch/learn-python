def welcome():
    print("----------------- Program Kasir Sederhana -----------------")
    print("1. Nasi Goreng - Rp 15000")
    print("2. Soto - Rp 9000")
    print("3. Mie Ayam - Rp 11000")
    print("4. Es Teh - Rp 2000")
    print("5. Es Jeruk - Rp 3500")
    print("6. Es Kopi - Rp 4000")
    print("7. Checkout")
    print("8. Keluar")

def order_food(pembeli):
    global total_makanan
    global jenis_makanan
    global jumlah_porsi

    nomor = int(input("Masukan Pilihan : "))

    if nomor == 1:
        total_makanan = jumlah_porsi * 15000
        jenis_makanan = "Nasi Goreng"
        print(f"Jumlah Pesanan {jumlah_porsi} Porsi Nasi Goreng = Rp{total_makanan}")
    elif nomor == 2:
        total_makanan = jumlah_porsi * 9000
        jenis_makanan = "Soto"
        print(f"Jumlah Pesanan {jumlah_porsi} Porsi Soto = Rp{total_makanan}")
    elif nomor == 3:
        total_makanan = jumlah_porsi * 11000
        jenis_makanan = "Mie Ayam"
        print(f"Jumlah Pesanan {jumlah_porsi} Porsi Mie Ayam = Rp{total_makanan}")
    else:
        print("Pilihan Tidak Ada, Silahkan Masukan Lagi!!")
        order_food(pembeli)

def order_drink(pembeli):
    global total_minuman
    global jenis_minuman
    global jumlah_gelas

    nomor = int(input("Masukan Pilihan : "))

    if nomor == 1:
        total_minuman = jumlah_gelas * 2000
        jenis_minuman = "Es Teh"
        print(f"Jumlah Pesanan {jumlah_gelas} Gelas Es Teh = Rp{total_minuman}")
    elif nomor == 2:
        total_minuman = jumlah_gelas * 3500
        jenis_minuman = "Es Jeruk"
        print(f"Jumlah Pesanan {jumlah_gelas} Gelas Es Jeruk = Rp{total_minuman}")
    elif nomor == 3:
        total_minuman = jumlah_gelas * 4000
        jenis_minuman = "Es Kopi"
        print(f"Jumlah Pesanan {jumlah_gelas} Gelas Es Kopi = Rp{total_minuman}")
    else:
        print("Pilihan Tidak Ada, Silahkan Masukan Lagi!!")
        order_drink(pembeli)

def checkout(pembeli):
    print("\n----------------- Checkout -----------------")
    print(f"Total Harga Makanan : Rp{total_makanan}")
    print(f"Total Harga Minuman : Rp{total_minuman}")
    print(f"Total Harga Pesanan : Rp{total_makanan + total_minuman}")

def main():
    global total_makanan
    global total_minuman
    global jenis_makanan
    global jenis_minuman
    global jumlah_porsi
    global jumlah_gelas

    total_makanan = 0
    total_minuman = 0
    jenis_m
