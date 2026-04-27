#lat 4
'''
print("===================================")
pernyatan Kontrol meliputi if,while, dan for
pertemuan ke 4
perintah dasar :if,variable,int()

'''

print('--------------------------------')

#menerima input dari pengguna
name = input("nama saudara:") #perintah variabel input
print("hello",name+ "apa kabarnya..!")# tampilan dari variabel input
print('                 ')#memberikan jarak baris

#konversi tipe data input
age_str=input("berapa usia sekarang:")#perintah veriabel input
age=int(age_str)#mengonversi string ke integer
print("usia saudara",name,"sekarang",age,"tahun.")#tampilan dari variabel input
print('------------------------------------')#memberikan pembatas garis satu

# menggabungkan input dengan operasi if
print(name,'mari belajar pernyataan dari kondusi if!')
print('                                 ')
nilai=input("nilai ulangan harian "+name+" adalah:")#perintah variabel imput
nilai=int(nilai)

#fungsi kondisi if
if nilai>=60:
    print('selamat',name+',saudara kompeten')
else:
    print('mohon maaf,name,','saudara belum kompeten')
print('            ')
