print("Nomor1")
#"Dengan menggunakan pustaka pandas di Python,
# # buatlah sebuah DataFrame dari data jumlah produksi sampah berdasarkan Kabupaten/Kota di Jawa Barat. 
# # Pastikan kolom-kolomnya menyertakan nama Kabupaten/Kota, jumlah produksi sampah (dalam ton), dan tahun penc

import pandas as pd

# Membuat DataFrame sesuai dengan data yang diberikan
data_smph_jbr = {
    'nama_provinsi': ['JAWA BARAT'] * 40,
    'nama_kabupaten': [
        'KABUPATEN BOGOR', 'KABUPATEN SUKABUMI', 'KABUPATEN CIANJUR', 'KABUPATEN BANDUNG', 'KABUPATEN GARUT', 
        'KABUPATEN TASIKMALAYA', 'KABUPATEN CIAMIS', 'KABUPATEN KUNINGAN', 'KABUPATEN CIREBON', 'KABUPATEN MAJALENGKA',
        'KABUPATEN BOGOR', 'KABUPATEN SUKABUMI', 'KABUPATEN CIANJUR', 'KABUPATEN BANDUNG', 'KABUPATEN GARUT', 
        'KABUPATEN TASIKMALAYA', 'KABUPATEN CIAMIS', 'KABUPATEN KUNINGAN', 'KABUPATEN CIREBON', 'KABUPATEN MAJALENGKA',
        'KABUPATEN BOGOR', 'KABUPATEN SUKABUMI', 'KABUPATEN CIANJUR', 'KABUPATEN BANDUNG', 'KABUPATEN GARUT', 
        'KABUPATEN TASIKMALAYA', 'KABUPATEN CIAMIS', 'KABUPATEN KUNINGAN', 'KABUPATEN CIREBON', 'KABUPATEN MAJALENGKA',
        'KABUPATEN BOGOR', 'KABUPATEN SUKABUMI', 'KABUPATEN CIANJUR', 'KABUPATEN BANDUNG', 'KABUPATEN GARUT', 
        'KABUPATEN TASIKMALAYA', 'KABUPATEN CIAMIS', 'KABUPATEN KUNINGAN', 'KABUPATEN CIREBON', 'KABUPATEN MAJALENGKA'
    ],
    'jumlah_sampah': [
        1511.15, 419.01, 981.41, 1895.94, 464.74, 464.52, 260.91, 251.7, 465.75, 254.63,
        1716.80, 415.50, 965.19, 2068.06, 473.89, 458.45, 263.01, 248.52, 466.25, 249.26,
        2914.65, 1003.64, 1115.81, 1334.12, 1144.01, 753.06, 560.57, 537.25, 3.15, 515.70,
        2977.00, 1006.00, 1117.00, 1355.00, 1151.00, 754.00, 564.00, 540.00, 1096.00, 518.00
    ],
    'satuan': ['TON PER HARI'] * 40,
    'tahun': [2017] * 10 + [2018] * 10 + [2019] * 10 + [2020] * 10
}

df = pd.DataFrame(data_smph_jbr)
print(df)

print("\n")

print("Nomor2") #menjumlahkan data sampah tahun tahun tertentu
total_sampah_2018 = 0
for index, row in df.iterrows():
    if row['tahun'] == 2018:
        total_sampah_2018 += row['jumlah_sampah']

print(f"\nTotal produksi sampah di Jawa Barat untuk tahun 2018 adalah: {total_sampah_2018:.2f} ton sampah")
print("\n")

print("Nomor3")   #menjumlahkan data pertahun
total_per_tahun = {}

for i, row in df.iterrows():
    tahun = row['tahun']
    jumlah_sampah = row['jumlah_sampah']
    if tahun not in total_per_tahun:
        total_per_tahun[tahun] = 0
    total_per_tahun[tahun] += jumlah_sampah  

print("Total produksi sampah per tahun:")
for tahun, total in total_per_tahun.items():
    print(f"Tahun {tahun}: {total:.2f} ton sampah pertahun") 

    
print("\n")
print("Nomor4")
total_per_kabupaten_tahun = {}

for index, row in df.iterrows():
    kabupaten = row['nama_kabupaten']
    tahun = row['tahun']
    jumlah_sampah = row['jumlah_sampah']
    
    if kabupaten not in total_per_kabupaten_tahun:
        total_per_kabupaten_tahun[kabupaten] = {}

    if tahun not in total_per_kabupaten_tahun[kabupaten]:
        total_per_kabupaten_tahun[kabupaten][tahun] = 0
        
    total_per_kabupaten_tahun[kabupaten][tahun] += jumlah_sampah

print("Total produksi sampah per Kota/Kabupaten per tahun:")
for kabupaten, tahun_data in total_per_kabupaten_tahun.items():
    print(f"\n{kabupaten}:")
    for tahun, total in tahun_data.items():
        print(f"  Tahun {tahun}: {total:.2f} ton sampah pertaun")
        
# Export ke CSV
csv_nama_file = "dataCSV.csv"
df.to_csv(csv_nama_file, index=False)

# Export ke Excel
excel_file_name = "dataEXCEL.xlsx"
df.to_excel(excel_file_name, index=False)

        
