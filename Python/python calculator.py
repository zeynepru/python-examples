def Topla(x, y):
    return x + y

def Cikar(x, y):
    return x - y

def Carp(x, y):
    return x * y

def Bol(x, y):
    return x / y

print("Yapılacak İşlemi Seçin.")
print("=======================")
print("+")
print("-")
print("*")
print("/")


secim = input("Seçiminiz (+/-/*//):")
sayi1 = int(input("1. Sayı: "))
sayi2 = int(input("2. Sayı: "))

if secim == '+':
    print(sayi1, "+", sayi2, "=", Topla(sayi1, sayi2))

elif secim == '-':
    print(sayi1, "-", sayi2, "=", Cikar(sayi1, sayi2))

elif secim == '*':
    print(sayi1, "*", sayi2, "=", Carp(sayi1, sayi2))

elif secim == '/':
    print(sayi1, "/", sayi2, "=", Bol(sayi1, sayi2))
else:
    print("Geçersiz Giriş")