import random
Welcome_message = "halo fikri"
angka_boom = random.randint(1,10)
print(f"{Welcome_message} selamat datang  di program pyhton")

nama_saya = input("siapa kamu: ")

if nama_saya == "fikri":
    print("halo fikri")

password = int(input("masukan password:"))

if password == 15:
    print("benar")
else:
    print("salah")
    
    
    
    
    
print(f''' halo {nama_saya} coba tebak angka boom
1,2,3,4,5,6,7,8,9,10''')

while True:
    pilihan_user = int(input("menurtumu mana angka boomnya?"))
    if pilihan_user == (angka_boom):
     print("benar")
     break
else:
    print(f"salah angka boomnya adalah {angka_boom}")
