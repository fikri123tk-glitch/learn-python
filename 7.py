'''
Latihan membuat menu calculator
berdasarkan nilai yang dimasukan
'''

print("")
print("Selamat Mencoba Program Calculator Sederhana")
print("===========================================================")
name=input("Silahkan Tuliskan nama saudara :")
print("")
print("Selamat Mencoba Saudara" ,name,)
print("-----------------------------------------------------------")
print
def tambah(x,y):
    return x+y
def kurang (x,y):
    return x-y
def kali(x,y):
    return x*y
def bagi (x,y):
    if y !=0:
        return x/y
    else:
        return"Error:Pembagian oleh NOL"

#Tampilan menu
print('pilih operasi:')
print("===================")
print("1.Penjumlahan")
print("2.Pengurangan")
print("3.Perkalian")
print("4.Pembagian")

print
#Minta Pengguna memasukan pilihan
pilihan=input("Masukan nomor operasi(1/2/3/4): ")
print
#Minta pengguna memasukkan angka
angka1=int(input("Masukkan angka pertama: "))
angka2=int(input("Masukkan angka kedua  : "))
           

#Lakukan operasi sesuai pilihan
if pilihan=='1':
    hasil=tambah(angka1,angka2)
elif pilihan=='2':
      hasil=kurang(angka1,angka2)
elif pilihan=='3':
      hasil=kali(angka1,angka2)
elif pilihan=='4':
      hasil=bagi(angka1,angka2)
else:
    hasil="Invalid input. Pilihan tidak dikenali."

#Tampilkan hasil
print('           -----------')
print("Hasil Operasinya adalah : ",hasil)
print('')
print('------------------------------------')
print('')

