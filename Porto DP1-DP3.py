from list_function import *

def fungsiInput():

    print('<--Selamat Datang-->')
    print('Silahkan Pilih Menu Dibawah Ini')
    print('1. Desimal')
    print('2. Biner')
    print('3. Oktal')
    print('4. Hexadesimal')
    print('5. ASCII')

    inputan = int(input("Pilihan anda : "))

    if inputan == 1 :
        Desimal()

    elif inputan == 2 : 
        Biner()

    elif inputan == 3 :
        Oktal()

    elif inputan == 4 :
        Hexadesimal()

    else :
        print('Mohon masukkan angka sesuai dalam menu!!')
        print('')

    inputLg = input('Apakah anda ingin melakukan operasi lagi ? (y/n) : ')

    if inputLg == 'y' : 
        fungsiInput()
    else : 
        print('Terimakasih')
        exit
fungsiInput()