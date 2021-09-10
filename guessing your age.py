import datetime

ad = input("Adınızı Girin: ")
dogum_yili = int(input("Doğum Yılınızı Girin :"))

guncel_tarih = datetime.datetime.now()
guncel_yil = guncel_tarih.year
yas = guncel_yil - dogum_yili

print("Merhaba {}, yaşınız {}'dır".format(ad, yas))