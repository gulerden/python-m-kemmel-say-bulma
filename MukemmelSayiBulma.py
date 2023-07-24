print("Mükemmel Sayi Bulma Programı")

sayi=int(input("Sayiyi giriniz"))
liste=list()
i=1
deger=0

while(i<sayi):
    if(sayi%i==0):
        liste.append(i)
    i+=1
print(liste)

for a in liste:
    deger=deger+a
print(deger)

if(deger==sayi):
    print(sayi,"sı mükemmel bir sayıdır.")
else:
    print(sayi," sı mükemmel bir sayı değildir")