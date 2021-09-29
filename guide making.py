rehber = [["baekhyun", "byun", "096282,72"], ["junmyeon", "kim", "0912345"],["lay", "zhang", "09657482"]]


def kayıt_ekle(rehber):
    while True:
        isim = input("isim giriniz: ")
        soyad = input("soyad giriniz: ")
        numara = input("numara giriniz: ")
        if emin_misin():
            rehber += [[isim, soyad, numara]]

        if devam_mı():
            continue
        else:
            break


def emin_misin():
    a = input("emin misin (evet,hayır): ")
    if a.lower().startswith("e"):
        return True
    else:
        False



def devam_mı():
    a = input("devam etmek istiyor musun (evet,hayır): ")
    if a.lower().startswith("e"):
        return True
    else:
        False



def kayıt_listele(rehber):
    for i, j, k in rehber:
        print("isim---> {} soyad---> {}    numara---> {}".format(i, j, k))



def kayıt_ara(rehber):
    while True:
        isim = input("bulmak istediğiniz kişinin adını veya soyadını giriniz: ")
        for i in rehber:
            if isim in i:
                print("isim--> {}  soyad--> {}    numara--> {}".format(i[0], i[1], i[2]))
        if devam_mı():
            continue
        else:
            break


def kayıt_sil(rehber):
    while True:
        for i in rehber:
            print(*i)
        isim = input("silmek istediğiniz kişinin ismini giriniz: ")
        if emin_misin():
            for i in rehber:
                if isim in i:
                    rehber.remove(i)
        if devam_mı():
            continue
        else:
            break


while True:
    a = int(input("""
    1) kayıt ekle
    2) kayıtları listele
    3) kayıt ara
    4) kayıt sil
    5) çıkış

    """))
    if a == 1:
        kayıt_ekle(rehber)
    elif a == 2:
        kayıt_listele(rehber)
    elif a == 3:
        kayıt_ara(rehber)
    elif a == 4:
        kayıt_sil(rehber)
    elif a == 5:
        print("Görüşmeleriniz Bitmiştir :) ")
        break