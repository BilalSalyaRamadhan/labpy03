# latihan3.py

# Inisialisasi saldo awal
saldo = 1000000

# Loop utama ATM. Loop akan berjalan terus sampai pengguna memilih menu '2' (Keluar) 
# atau saldo habis (menjadi 0).
while True:
    print("\n--------------------------------")
    # Tampilkan saldo saat ini
    print(f"Saldo saat ini: Rp {saldo:,}".replace(",", ".")) # Format angka dengan titik
    print("--------------------------------")
    
    # Cek kondisi saldo habis
    if saldo <= 0:
        print("Saldo Anda telah habis. Transaksi tidak dapat dilanjutkan.")
        break
        
    # Tampilkan menu
    print("1. Tarik Uang")
    print("2. Keluar")
    
    # Ambil input pilihan menu
    pilihan = input("Pilih menu (1/2): ")
    
    # --- Pilihan 1: Tarik Uang ---
    if pilihan == '1':
        # Minta jumlah penarikan
        try:
            jumlah_tarik = int(input("Masukkan jumlah penarikan: "))
            
            # Cek validitas penarikan
            if jumlah_tarik <= 0:
                print("Penarikan harus lebih dari Rp 0.")
            elif jumlah_tarik > saldo:
                print(f"Penarikan gagal! Saldo Anda (Rp {saldo:,}.00) tidak mencukupi.")
            else:
                # Lakukan penarikan
                saldo -= jumlah_tarik
                print("Penarikan berhasil!")
                
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")
            
    # --- Pilihan 2: Keluar ---
    elif pilihan == '2':
        print("\nTerima kasih telah menggunakan ATM!")
        break # Keluar dari loop while
        
    # --- Pilihan Tidak Valid ---
    else:
        print("Pilihan menu tidak valid. Silakan pilih 1 atau 2.")

# Program berakhir