print('-----------------------------')

#menerima input dari pengguna
name=input("nama saudara:")
print("hello" ,name, "apa kabarnya..!")
print('             ')
#konversi tipe data input
absen_str=input('berapa No.absen  ' +name+ ":")
absen=int(absen_str)#mengonversi string ke integer
print("No.absen saudara" , name , "adalah" ,absen, "betul..!")
print('------------------------------------')
#menggabungkan input dengan oprasi if
print(name,"mari belajar pernyataan dari kondisi multi if!")
print('                      ')
nilai=input("nilai ulangan harian "+name+" adalah:")
nilai=int(nilai)

#fungsi kondisi multi if
if nilai>=90:
    print('selamat',name,'dengan skor',nilai,'saudara sangat kompeten')
elif 70<=nilai<90:
    print('selamat',name,'dengan skor',nilai,',saudara kompeten')
elif 60<=nilai<70:
    print('selamat',name,'dengan skor',nilai,',saudara cukup kompeten')
else:
    print('mohon maaf',name,'dengan skor',nilai,',saudara tidak kompeten')
print('     ')
      
