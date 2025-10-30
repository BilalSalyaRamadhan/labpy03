# latihan2.py

# Inisialisasi
MODAL_AWAL = 100000000  # 100 juta
TOTAL_KEUNTUNGAN = 0
JUM_BULAN = 8

print(f"Modal awal: {MODAL_AWAL}")
print("---")

# Perulangan untuk menghitung laba dari bulan 1 sampai 8
for bulan in range(1, JUM_BULAN + 1):
    laba_bulanan = 0
    persen_laba = 0
    
    # 1. Bulan 1 dan 2: Belum mendapat laba (0)
    if bulan in (1, 2):
        laba_bulanan = 0
        
    # 2. Bulan 3 dan 4: Laba 1%
    elif bulan in (3, 4):
        persen_laba = 0.01  # 1%
        laba_bulanan = MODAL_AWAL * persen_laba
        
    # 3. Bulan 5: Peningkatan 5%
    elif bulan == 5:
        persen_laba = 0.05  # 5%
        laba_bulanan = MODAL_AWAL * persen_laba
        
    # 4. Bulan 6, 7, dan 8: Penurunan keuntungan 2% dari bulan sebelumnya (5%)
    # Asumsi: Laba menjadi 5% - 2% = 3%
    elif bulan in (6, 7, 8):
        persen_laba = 0.03  # 3% (5% - 2%)
        laba_bulanan = MODAL_AWAL * persen_laba
        
    # Tampilkan laba bulanan
    print(f"laba bulan ke- {bulan} sebesar: {laba_bulanan:.1f}")
    
    # Akumulasi total keuntungan
    TOTAL_KEUNTUNGAN += laba_bulanan

print("---")
# Tampilkan total laba selama 8 bulan
# Pastikan tipe datanya int jika totalnya tidak memiliki desimal
print(f"Total laba adalah: {int(TOTAL_KEUNTUNGAN)}")