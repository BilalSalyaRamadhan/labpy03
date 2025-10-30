# latihan1.py

# Import fungsi random
from random import random

# Meminta input nilai N (jumlah data yang akan ditampilkan)
# Gunakan loop while untuk memastikan input adalah bilangan bulat positif,
# meskipun untuk tugas ini input() sederhana sudah cukup.
# Sesuai contoh output:
while True:
    try:
        # Masukkan nilai N: 5
        n_input = input("Masukkan nilai N: ")
        N = int(n_input)
        if N > 0:
            break
        else:
            print("N harus bilangan bulat positif.")
    except ValueError:
        print("Input tidak valid. Harap masukkan bilangan bulat.")

# Tampilkan N bilangan acak yang lebih kecil dari 0.5
print(f"data ke:")

for i in range(1, N + 1):
    # random() menghasilkan float antara 0.0 (inklusif) dan 1.0 (eksklusif)
    bilangan_acak = random()

    # Pastikan bilangan acak < 0.5
    # Karena random() sudah menghasilkan nilai antara [0.0, 1.0),
    # kita hanya perlu menampilkannya dan memeriksa kondisi di soal.
    # Jika soal menghendaki HANYA bilangan acak < 0.5 yang ditampilkan,
    # maka logic perlu diubah menggunakan loop while untuk menghasilkan 
    # bilangan acak sampai terpenuhi N kali.

    # Berdasarkan contoh output (semua nilainya < 0.5)
    # diasumsikan kita harus menghasilkan N buah bilangan acak < 0.5

    # Jika bilangan_acak < 0.5, tampilkan.
    # Ulangi sampai N bilangan yang ditampilkan.
    
    # --- INTERPRETASI SOAL: "Tampilkan N bilangan acak yang lebih kecil dari 0.5" ---
    # Jika ini berarti kita harus membuat/memastikan N bilangan acak yang 
    # dihasilkan *adalah* < 0.5, kita bisa menggunakan `random()` / 2, atau `random() * 0.5`.
    # Paling sederhana dan memenuhi syarat:
    bilangan_acak_kurang_dari_05 = random() * 0.5 
    
    # atau menggunakan loop:
    # while True:
    #     bilangan_acak_kurang_dari_05 = random()
    #     if bilangan_acak_kurang_dari_05 < 0.5:
    #         break
            
    # Saya gunakan cara yang paling ringkas: random() * 0.5
    
    # Format output seperti pada contoh: data ke: 1 => 0.1729492204357856
    print(f"data ke: {i} => {bilangan_acak_kurang_dari_05}")
    
# Tampilkan pesan selesai
print("Selesai")