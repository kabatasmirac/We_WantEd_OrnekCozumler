def buyuk_bul(sayilar,boyut):
    max,max2=0,0

    for i in range(0,boyut):
        if liste[i] > max:
            max = liste[i]

        elif ((liste[i] != max) & (liste[i] > max2)):
            max2 = liste[i]

    print("\nEn buyuk = {} , En buyuk ikinci = {}".format(max,max2))


liste = []
boyut = int(input("Kac eleman gireceksin : "))

for i in range(0,boyut):
    liste.append(int(input("Sayi gir : ")))

buyuk_bul(liste,boyut)