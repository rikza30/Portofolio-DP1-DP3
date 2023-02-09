from prettytable import PrettyTable
string = input
def Desimal():
#    input_string = str(input('Masukan kata atau kalimat Anda : ')) 
#    decimal_list = [str(ord(x)) for x in input_string]
#    decimal_string = ''.join(decimal_list)
#    output_string = ' '.join([decimal_string[i:i+2] for i in range(0, len(decimal_string), 2)])
#    print("Hasil konversi anda adalah sebagai berikut " + input_string + " diubah menjadi " + output_string)

    # membuat table dan menambah kolom
    table = PrettyTable(['Kata', 'Nilai Desimal'])

    # input string
    input_string = str(input('Masukan kata atau kalimat Anda : '))

    # memisahkan setiap kata di string menggunakan fungsi split
    words = input_string.split()

    # mengkonversi setiap kata menjadi desimal dan membuat row baru di tabel untuk setiap kata
    for word in words:
        decimal_value = [str(ord(x)) for x in word]
        decimal_string = ''.join(decimal_value)
        table.add_row([word, decimal_string])

    # print table
    print(table)

def Biner():
    # input_string = str(input('Masukan kata atau kalimat Anda : ')) 
    # binary_string = ''.join(format(ord(x), 'b').zfill(8) for x in input_string)
    # output_string = '_'.join([binary_string[i:i+8] for i in range(0, len(binary_string), 8)])
    # print(output_string)

    # create table 
    table = PrettyTable(['Kata', 'Nilai Biner'])
    
    # input string
    input_string = str(input('Masukan kata atau kalimat Anda : '))

    # split word
    words = input_string.split()

    # looping
    for word in words:
        binary_value = [format(ord(x), 'b').zfill(8) for x in word]
        binary_string = ''.join(binary_value)
        table.add_row([word, binary_string])

    # print table
    print(table)

def Oktal():
    result = oct(int(string))
    print("Result in Octal:", result)

def Hexadesimal():
    result = hex(int(string))
    print("Result in Hexadecimal:", result)

def ASCII():
    result = ' '.join([str(ord(c)) for c in string])
    print("Result in ASCII:", result)