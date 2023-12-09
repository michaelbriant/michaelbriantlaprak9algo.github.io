# ELKOM 1
print('@@@@@@@ @ @@@@@ @    @ @@@@@ @@@@@ @')
print('@  @  @ @ @     @    @ @   @ @     @')
print('@  @  @ @ @     @@@@@@ @@@@@ @@@@@ @')
print('@  @  @ @ @     @    @ @   @ @     @')
print('@  @  @ @ @@@@@ @    @ @   @ @@@@@ @@@@@')

print("========== ELKOM 1 ==========")

def list_to_tuple(input_list):
    return tuple(input_list)

# Contoh list
listnya = [0, 6, 4, 0, 0, 2, 3, 0, 0, 0, 0, 4]

# Konversi list menjadi tuple
tuplenya = list_to_tuple(listnya)

print(listnya)
print("hasil reverse ke tuple")
print(tuplenya)


# ELKOM 2
print('@@@@@@@ @ @@@@@ @    @ @@@@@ @@@@@ @')
print('@  @  @ @ @     @    @ @   @ @     @')
print('@  @  @ @ @     @@@@@@ @@@@@ @@@@@ @')
print('@  @  @ @ @     @    @ @   @ @     @')
print('@  @  @ @ @@@@@ @    @ @   @ @@@@@ @@@@@')

def calculate_averages(nested_tuple):
    averages = []

    for tup in nested_tuple:
        total = sum(tup)
        count = len(tup)
        if count != 0:
            average = total / count
            averages.append(average)

    return averages

# tuple yang berisi tuple
tuplenya = ((10, 20, 30), (40, 50, 60), (70, 80, 90))

# Menghitung rata-rata
rata_ratanya = calculate_averages(tuplenya)

print(tuplenya)
print("rata rata dari tuple adalah: ")
print(rata_ratanya)

print("===== MICHAEL BRIANT =====")
print("===== 064002300004 =====")


# ELKOM 3
print('@@@@@@@ @ @@@@@ @    @ @@@@@ @@@@@ @')
print('@  @  @ @ @     @    @ @   @ @     @')
print('@  @  @ @ @     @@@@@@ @@@@@ @@@@@ @')
print('@  @  @ @ @     @    @ @   @ @     @')
print('@  @  @ @ @@@@@ @    @ @   @ @@@@@ @@@@@')

def hitung_hasil_kali(input_list):
    # Memastikan list tidak kosong
    if not input_list:
        return None

    # Menggunakan fungsi untuk mengalikan semua nilai dalam list
    hasil_kali = 1
    for nilai in input_list:
        hasil_kali *= nilai

    return hasil_kali

# list nilai
contoh_list = [5, 6, 4, 2]

# Memanggil fungsi
hasil_kali = hitung_hasil_kali(contoh_list)

print("ELKOM 3")

# Menampilkan hasil perhitungan hasil kali
print(contoh_list)
print(hasil_kali)


# ELKOM 4
print('@@@@@@@ @ @@@@@ @    @ @@@@@ @@@@@ @')
print('@  @  @ @ @     @    @ @   @ @     @')
print('@  @  @ @ @     @@@@@@ @@@@@ @@@@@ @')
print('@  @  @ @ @     @    @ @   @ @     @')
print('@  @  @ @ @@@@@ @    @ @   @ @@@@@ @@@@@')

def hitung_jumlah_string_sama(lst):
    jumlah = 0
    for elemen in lst:
        if isinstance(elemen, str) and len(elemen) >= 2 and elemen[0] == elemen[-1]:
            jumlah += 2
    return jumlah

# penggunaan:
list_elemen = ['x', 'def', 'cac', '244']
hasil = hitung_jumlah_string_sama(list_elemen)
print("['z', 'xvc', 'cac', 244]")
print("- cac")
print("- 244")
print("Terdapat", hasil, "string yang memenuhi syarat")