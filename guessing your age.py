import datetime
now = datetime.datetime.now()
now = int(now.year)
def yas (t):
    if (t <= 0) :
     z = "0 veya negatif sayı girilemez"
    elif (t >= now) :

     z = "bu yıl girilemez"

    elif (t < now) :
      z=now - t
      return z
print(yas(t = int(input("doğum tarihinizi giriniz :"))))

