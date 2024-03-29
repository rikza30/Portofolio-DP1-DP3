import tkinter as tk

def Desimal():
    string = entry.get()
    hasil_konversi = ""
    for i in range(len(string)):
        desimal = ord(string[i])
        hasil_konversi += "{} : {}\n".format(string[i], desimal)
    result_label.config(text="Hasil konversi ke Desimal:\n" + hasil_konversi)

def Biner():
    string = entry.get()
    biner = ""
    for i in range(len(string)):
        biner += format(ord(string[i]), '08b')
    result_label.config(text="Hasil konversi ke Biner adalah : " + biner)

def Oktal():
    string = entry.get()
    oktal = ""
    for i in range(len(string)):
        oktal += format(ord(string[i]), '03o')
    result_label.config(text="Hasil konversi ke Oktal adalah : " + oktal)

def Hexadesimal():
    string = entry.get()
    hexa = ""
    for i in range(len(string)):
        hexa += format(ord(string[i]), '02X')
    result_label.config(text="Hasil konversi ke Hexadesimal adalah : " + hexa)

def ASCII():
    string = entry.get()
    ascii_str = "Hasil konversi ke ASCII adalah :\n"
    for i in range(len(string)):
        ascii_str += string[i] + " : " + str(ord(string[i])) + "\n"
    result_label.config(text=ascii_str)

def convert():
    inputan = option_var.get()
    string = entry.get()
    if inputan == 1 and string.isdigit():
        Desimal()
    elif inputan == 2 and string.isalnum():
        Biner()
    elif inputan == 3 and string.isalnum():
        Oktal()
    elif inputan == 4 and string.isalnum():
        Hexadesimal()
    elif inputan == 5:
        ASCII()


window = tk.Tk()
window.title("Konversi String")
window.geometry("1000x450")


welcome_label = tk.Label(window, text="Selamat Datang", font=("Montserrat", 14))
welcome_label.pack(pady=10)

option_label = tk.Label(window, text="Silahkan Pilih Menu Dibawah Ini", font=("Arial", 12))
option_label.pack()

option_var = tk.IntVar()
option_var.set(1)
desimal_radiobutton = tk.Radiobutton(window, text="Desimal", variable=option_var, value=1)
desimal_radiobutton.pack()
biner_radiobutton = tk.Radiobutton(window, text="Biner", variable=option_var, value=2)
biner_radiobutton.pack()
oktal_radiobutton = tk.Radiobutton(window, text="Oktal", variable=option_var, value=3)
oktal_radiobutton.pack()
hexa_radiobutton = tk.Radiobutton(window, text="Hexadesimal", variable=option_var, value=4)
hexa_radiobutton.pack()
ascii_radiobutton = tk.Radiobutton(window, text="ASCII", variable=option_var, value=5)
ascii_radiobutton.pack()

entry_label = tk.Label(window, text="Masukkan Angka atau String :")
entry_label.pack(pady=10)
entry = tk.Entry(window)
entry.pack()

convert_button = tk.Button(window, text="Konversi", command=convert)
convert_button.pack(pady=10)

result_label = tk.Label(window, font=("Montserrat", 12))
result_label.pack()

window.mainloop()
