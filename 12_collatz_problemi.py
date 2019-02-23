def collatz_problemi(sayi):
    print(sayi, end="   ")
    sayac = 0
    while 1:

        sayac += 1

        if(sayi == 1):
            break

        elif sayi % 2 == 0:
            sayi /= 2
            print(sayi,end="   ")

        elif sayi % 2 == 1:
            sayi = (3*sayi)+1
            print(sayi,end="   ")

    print("\n\n\nCollatz islemi sonucu {} kadar sayiyla etkilesmistir".format(sayac))

sayi = input("bir sayi giriniz....")
sayi = int(sayi)

collatz_problemi(sayi)