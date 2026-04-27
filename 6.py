#lat coding 5

'''
latihan membuat menu calculator
berdasarkan nilai yang di masukan
'''

print(' ')
print('selamat mencoba program calculator sederhana')
print('===================================================')
nama=input('silahkan tuliskan nama saudara:')
print('                                     ')
print('SELAMATMENCOBA SAUDARA',nama,'!')
print('------------------------------------')
print('                                     ')
def tambah(x,y):
    return x+y
def kurang(x,y):
    return x-y
def kali(x,y):
    return x*y
def bagi(x,y):
    if y !=0:
       return x/y
    else:
       return"Error:Pembagian oleh NOL"

#tampilan menu
print ('pilih oprasi:')
print ("=================")
print ('1.penjumlahan')
print ('2.pengurangan')
print ('3.perkalian')
print ('4.pembagian')

print('                                  ')
#minta pengguna memasukan pilihan
pilihan=input('masukan nomor oprasi(1/2/3/4):')
print('                                        ')
# minta pengguna memasukan angka
angka1=int(input('masukan angka pertama:'))
angka2=int(input('masukan angka ke dua:'))

#lakukan oprasi sesuai pilihan
if pilihan=='1':
   hasil=tambah(angka1,angka2)
elif pilihan=='2':
   hasil=kurang(angka1,angka2)
elif pilihan=='3':
     hasil=kali(angka1,angka2)
elif pilihan=='4':
     hasil=bagi(angka1,angka2)
else:
    hasil=('invalid input.pilihan tidak dikenali.')

#tampil hasil
print('        --------')
print('hasil oprasinya adalah:',hasil)

print(' ')
print('-------------------------------------')
print(' ')



