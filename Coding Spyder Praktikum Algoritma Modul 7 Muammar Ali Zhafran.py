def cek_prima(angka):
    if angka < 2:
        return False

    for i in range(2, int(angka ** 0.5) + 1):
        if angka % i == 0:
            return False

    return True


def bilangan_prima(angka):
    if cek_prima(angka):
        print(angka, "adalah bilangan Prima")
    else:
        print(angka, "bukanlah bilangan Prima")


while True:
    angka = int(input("Masukkan angka: "))

    if angka == 0:
        break

    bilangan_prima(angka)
    
def ordinal(angka):
    if 10 <= angka % 100 <= 13:
        akhiran = "th"
    elif angka % 10 == 1:
        akhiran = "st"
    elif angka % 10 == 2:
        akhiran = "nd"
    elif angka % 10 == 3:
        akhiran = "rd"
    else:
        akhiran = "th"

    return (angka, akhiran)


def tampilkan_ordinal(angka):
    print(ordinal(angka))


print("Ordinal Number")
print("ketik 0 untuk menghentikan program")

while True:
    angka = int(input("masukkan angka: "))
    tampilkan_ordinal(angka)

    if angka == 0:
        print("terima kasih telah menggunakan program saya")
        break