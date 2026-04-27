def kalkulator_bunga_sederhana(principal, rate, time):
    """
    Menghitung bunga sederhana.
    :param principal: jumlah awal uang (prinsipal)
    :param rate: tingkat bunga per periode (dalam desimal, misal 5% = 0.05)
    :param time: waktu (periode)
    :return: jumlah bunga
    """
    bunga = principal * rate * time
    return bunga

def kalkulator_bunga_majemuk(principal, rate, time, n):
    """
    Menghitung bunga majemuk.
    :param principal: jumlah awal uang (prinsipal)
    :param rate: tingkat bunga per periode (dalam desimal, misal 5% = 0.05)
    :param time: waktu (tahun)
    :param n: jumlah periode per tahun (misal, n=12 untuk bulanan)
    :return: nilai akhir setelah bunga majemuk
    """
    nilai_akhir = principal * (1 + rate / n) ** (n * time)
    return nilai_akhir

# Contoh penggunaan
principal = 1000  # Prinsipal
rate = 0.05      # Tingkat bunga 5%
time = 3         # Waktu 3 tahun
n = 12           # Periode per tahun (bulanan)

bunga_sederhana = kalkulator_bunga_sederhana(principal, rate, time)
nilai_akhir_majemuk = kalkulator_bunga_majemuk(principal, rate, time, n)

print(f"Bunga Sederhana: {bunga_sederhana}")
print(f"Nilai Akhir dengan Bunga Majemuk: {nilai_akhir_majemuk}")
