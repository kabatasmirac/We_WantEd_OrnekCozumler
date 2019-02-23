toplam = 0

def tersiniYaz(sayi):

    if sayi==0:
        return sayi

    print(sayi%10,end="")
    sayi = sayi // 10
    return tersiniYaz(sayi)


sayi = int(input("bir sayi giriniz"))
tersiniYaz(sayi)