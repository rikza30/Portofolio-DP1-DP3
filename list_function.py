def Desimal():
    string = input("Masukkan string : ")
    desimal = 0
    for i in range(len(string)):
        desimal += ord(string[i]) * (256 ** (len(string)-1-i))
    print("Hasil konversi ke Desimal adalah :", desimal)

def Biner():
    string = input("Masukkan string : ")
    biner = ""
    for i in range(len(string)):
        biner += format(ord(string[i]), '08b')
    print("Hasil konversi ke Biner adalah :", biner)

def Oktal():
    string = input("Masukkan string : ")
    oktal = ""
    for i in range(len(string)):
        oktal += format(ord(string[i]), '03o')
    print("Hasil konversi ke Oktal adalah :", oktal)

def Hexadesimal():
    string = input("Masukkan string : ")
    hexa = ""
    for i in range(len(string)):
        hexa += format(ord(string[i]), '02X')
    print("Hasil konversi ke Hexadesimal adalah :", hexa)

def ASCII():
    string = input("Masukkan string : ")
    print("Hasil konversi ke ASCII adalah :")
    for i in range(len(string)):
        print(string[i], ":", ord(string[i]))
