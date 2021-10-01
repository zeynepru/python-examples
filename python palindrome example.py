metin = input('Metni Girin : \n')
ters=metin[::-1]

print('Girilen metin =' ,metin)
print('Girilen metnin tersi =',ters)
if ters == metin:
    print('Girilen metin palindrome')
else:
    print('Girilen metin palindrome değil.')

