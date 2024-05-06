repeat = 0
sisa = 2
saldo = 20000



while repeat < 3 :
    user = input('username :')
    password = input('password :')
    if(user == 'admin' and password == '12345'):
        lanjut = "Y"
        while lanjut == 'Y':
            print('ATM FTI UNISKA')
            print('====================')
            print('Menu :')
            print('1. Cek Saldo')
            print('2. Setor Tunai')
            print('3. Tarik Tunai')
            print('4. Keluar')
            menuYangDipilih = input('Pilih Menu : ')
            if(menuYangDipilih == '1'):
                
                print('Anda memilih cek saldo')
                print('saldo anda saat ini : ', saldo)
                break
            elif(menuYangDipilih == '2'):
                print('Anda memilih setor tunai')
                inputSetor = int(input('Masukkan nominal setor tunai : '))
                saldo = saldo + inputSetor
                print('Saldo anda setelah setor : ' , saldo)
                break
            elif(menuYangDipilih == '3'):
                print('Anda memilih tarik tunai')
                nominalTarik = int(input('Masukkan Nominal Tarik Tunai : '))
                if(nominalTarik < saldo):
                    saldo = saldo - nominalTarik
                    print('Saldo anda setelah tarik tunai tersisa : ', saldo)
                    break
                else:
                    print('saldo anda tidak mencukupi untuk melakukan penarikan.')
                    print('saldo anda saat ini tersisa : ', saldo)
                    break
                
        else:
            print('Terima Kasih!!')
            break
        lanjut = input('Lanjut transaksi? (Y/T)')
        if(lanjut == 'T' ):
            print('Terimakasih telah menggunakan layanan kami')
            break
        
    else:
        print('username atau password yang anda masukkan salah.')
        print('sisa kesempatan login : ' , sisa)
        repeat += 1
        sisa -= 1
