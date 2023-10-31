jumlah_data = 0
nilai_rata_rata = 0

while True:
    print()
    print('MENGHITUNG JUMLAH & RATA-RATA SEJUMLAH DATA NILAI')
    print('CACAH DATA TIDAK DIKETAHUI DENGAN PASTI')
    print('PEMBACAAN DATA DIHENTIKAN DENGAN DATA SENTINEL')
    print('DATA SENTINEL BERUPA SEMBARANG BILANGAN NEGATIF')
    print()
    print("ISIKAN BILANGAN NEGATIF UNTUK SELESAI")

    while True:
        data = float(input("MASUKKAN DATA NILAINYA = "))
        if data < 0:
            break
        jumlah_data += data
        nilai_rata_rata += 1

    if nilai_rata_rata > 0:
        rata_rata = jumlah_data/nilai_rata_rata
    else:
        rata_rata = 0

    print("\nJUMLAH DATA = ", jumlah_data)
    print("\nNILAI RATA RATA = ", rata_rata)    

    exit()