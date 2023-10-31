suka_pedas = input("Suka pedas (Y/T)?")
tanggal_tua = input("Tanggal tua (Y/T)?")

if suka_pedas == "Y":
    if tanggal_tua == "Y":
        print("Rekomendasi menu: Nasi sambal")
    else:
        print("Rekomendasi menu: Nasi rica-rica iga sapi")
else:
    if tanggal_tua == "Y":
        print("Rekomendasi menu: Nasi kecap")
    else:
        print("Rekomendasi menu : Nasi ayam kecap")