import random
Welcome_message = "halo fikri"
musang = random.randint(1,5)
print(f"{Welcome_message} selamat datang  di program pyhton")

nama_saya = input("siapa kamu: ")
while nama_saya == "":
    nama_saya = input("nama tidak boleh kosong, tolong masukkan namamu: ")

print(f"halo {nama_saya}")
    
bentuk_lubang = "|_|"
lubang_kosong = [bentuk_lubang]* 5
lubang = lubang_kosong.copy()
lubang[musang -1] = "|0_0|"
lubang_kosong = ' '.join(lubang_kosong)
lubang = ' '.join(lubang)
print(f'''coba tebak musang ada di lobang nomor berapa?
      {lubang_kosong}''')
    
while True:
    pilihan_user = int(input("menurtumu di luang mana musang itu berada? (1-5): "))
    while pilihan_user < 1 or pilihan_user >5:
        pilihan_user = int(input("input tidak valid, tolong masukkan angka antara 1-5: "))
    confirm_user = input(f"apakah kamu yakin kalo {pilihan_user} jawabannya? (y/n):")
    if confirm_user == 'n':
        print("oke coba tebak lagi yaa")
        exit()
    elif confirm_user == 'y':
        if pilihan_user == (musang):
            print(f"benar sekali {nama_saya}, musang ada di lubang nomor {musang} \n {lubang}")
            break
        else:
            print(f"salah yaa {nama_saya}, musang ada di lubang nomor {musang} \n {lubang}")
    else:
        print("input tidak valid, program dihentikan")
        exit()
