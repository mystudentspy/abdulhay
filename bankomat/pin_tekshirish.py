def pin_tekshir(pin):
    urinish = 3
    while urinish > 0:
        user = input("PIN kodni kiriting: ")
        if user == pin:
            print("pin to'g'ri")
            return True
        else:
            urinish -= 1
            print("PIN noto'g'ri")
    print("karta bloklandi")
    return False



