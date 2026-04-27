#lat3 coding menginput dua bilangan
'''
nama: Khoirul Fikri
kelas: Xtjkt2
pembahasan fungsi = input, print, float, interger

'''

name=input("siapa namamu:")
print("hello " +name+ "!")
print("               ")
print("--------------------------------------------------")
print('perhitungan dua bilangan')
x=input('masukan bilangan pertama : ') #Model input
y=input('masukan bilangan kedua   : ')
print('                         ------ +')
x=int(x)
y=int(y)
print('jumlahnya adalah          ',(x+y))
print(" ========================================================================================================")
print("1. berapa nilai pemjumlahan bilangan dari " ,(x),"+",(y),"adalah",(x+y)) #ini fungsi operator penambahan
print("2. berapa nilai perkalian bilangan dari " ,(x),"x",(y),"adalah ",(x*y)) #ini funsi operator perkalian
print("                                                                     ") #ini fungsi garis
print("3. berapa nilai pengkurangan bilangan dari " ,(x),"-",(y),"adalah ",(x-y)) #ini fungsi operator pengkurangan
print("                                                                    ") #ini fungsi garis
print("4. berapa nilai pembagian bilangan dari " ,(x),"/",(y),"adalah ",(x/y))#ini fungsi operator pembagian
print("                                                                     ")#ini fungsi garis
print("5. berapa nilai perpangkatan bilangan dari " ,(x),"%",(y),"adalah ",(x%y)) #ini fungsi operator perpangkatan
print("                                                                     ") # ini fungsi garis
print("6. berapa nilai quaadrat bilangan dari " ,(x),"**",(y),"adalah ",(x**y)) # ini fungsi operator quaadrat
print("                                                                     ") #ini fungsi garis
print("=============================================================================================================")
