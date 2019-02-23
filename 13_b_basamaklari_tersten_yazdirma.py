
def tersiniYaz(sayi,toplam):
    if sayi == 0:
        return toplam

    gecici = sayi%10
    toplam = (toplam*10) + gecici
    return tersiniYaz(sayi//10 ,toplam)


toplam = 0
sayi = int(input("Bir sayi giriniz"))
print(tersiniYaz(sayi,toplam))