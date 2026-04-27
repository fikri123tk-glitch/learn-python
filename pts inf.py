'''
Nama : KHOIRUL FIKRI
No.Absen :21
Kelas : X TJKT2
Mapel : Agoritma dan Pemrogaman
Aplikasi : Python 3.12
Nama Program : Kasir Sederhana.py
tanggal : Kamis, 29 Februari 2024
'''
def fungsimakanan():
    global totalmkn, porsi, mkn
    print("\n----------------- Menu Makanan -----------------")
    print("1. Nasi Goreng - Rp 15000")
    print("2. Soto - Rp 9000")
    print("3. Mie Ayam - Rp 11000")
    print(' ')
    nomor = int(input("Masukan Pilihan : "))
    porsi = int(input("Berapa Porsi    : "))

    if nomor == 1:
        totalmkn = porsi * 15000
        mkn = "Nasi Goreng"
    elif nomor == 2:
        totalmkn = porsi * 9000
        mkn = "Soto"
    elif nomor == 3:
        totalmkn = porsi * 11000
        mkn = "Mie Ayam"
    else:
        print("Pilihan Tidak Ada, Silahkan Masukan Lagi!!")
        fungsimakanan()

def fungsiminuman():
    global totalmnm, gelas, mnm
    print("\n----------------- Menu Minuman -----------------")
    print("1. Es Teh - Rp 2000")
    print("2. Es Jeruk - Rp 3500")
    print("3. Es Kopi - Rp 4000")
    print(' ')
    nomor = int(input("Masukan Pilihan : "))
    gelas = int(input("Berapa Gelas    : "))

    if nomor == 1:
        totalmnm = gelas * 2000
        mnm = "Es Teh"
    elif nomor == 2:
        totalmnm = gelas * 3500
        mnm = "Es Jeruk"
    elif nomor == 3:
        totalmnm = gelas * 4000
        mnm = "Es Kopi"
    else:
        print("Pilihan Tidak Ada, Silahkan Masukan Lagi!!")
        fungsiminuman()

pembeli = input("Masukkan Nama Konsumen : ")
print(f"Nama Konsumen : {pembeli}")

fungsimakanan()
fungsiminuman()

total_semua = totalmkn + totalmnm
print(f"\nTOTAL HARUS DIBAYAR : Rp {total_semua}")
uang_tunai = int(input("UANG TUNAI KONSUMEN : Rp "))
kembalian = uang_tunai - total_semua
print(f"UANG KEMBALIAN    : Rp {kembalian}")

print("\n=================================")
print("======= S T R U K   B E L I ========")
print("===================================")
print(f"Nama Konsumen\t: {pembeli}")
print(f"Jenis Pesanan\t: {porsi} {mkn} ( Rp {totalmkn})")
print(f"\t\t {gelas} {mnm} ( Rp {totalmnm})")
print(f"Tagihan\t\t: Rp {total_semua}")
print(f"Dibayar\t\t: Rp {uang_tunai}")
print(f"Kembalian\t: Rp {kembalian}")
print("==================================")
print("==================================")   
