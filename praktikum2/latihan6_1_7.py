hasil = 0

while True:
    print()
    print('MENGHITUNG JUMLAH & RATA-RATA SEJUMLAH DATA NILAI')
    print('CACAH DATA TIDAK DIKETAHUI DENGAN PASTI')
    print('PEMBACAAN DATA DIHENTIKAN DENGAN DATA SENTINEL')
    print('DATA SENTINEL BERUPA SEMBARANG BILANGAN NEGATIF')
    print()
    bil1 = int(input('Ketik Bilangan Pertama = '))
    bil2 = int(input('Ketik Bilangan Kedua = '))

    if bil1 >= bil2:
        hasil = hasil + 5
        print(bil1, "-", bil2, "-", bil2, "-", bil2, "-", bil2, "-", bil2 , "=", hasil ," Kali Perulangannya")
        print()

    ulang = input("Mau ulang Program Tekan [Y] / Keluar [T] =")

    if ulang == 'T':
        break