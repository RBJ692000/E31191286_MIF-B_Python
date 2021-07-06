print("Pilih Opsi")
print("Penjumlahan")
print("Pengurangan")
print("Perkalian")
print("Pembagian")

opsi = input("Opsi :")
a = int(input("Masukan nilai bilangan a: "))
b = int(input("Masukan nilai bilangan b: "))

if opsi=="Penjumlahan":
    jumlah = a+b
    print("a", "+", "b", "=", jumlah)
elif opsi=="Pengurangan":
    jumlah = a-b
    print("a", "-", "b", "=", jumlah)
elif opsi=="Perkalian":
    jumlah = a * b
    print("a", "x", "b", "=", jumlah)
elif opsi=="Pembagian":
    jumlah = a / b
    print("a", "/", "b", "=", jumlah)    