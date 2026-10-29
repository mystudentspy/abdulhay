def pin_ozgartirish(pin):
    user = input("eski parolni kiriting:")
    if user == pin:
        new_user = input("yangi parolni kiriting:")
        if new_user.isdigit() and len(new_user) == 4:
            new_user2 = input("yangi parolni tasdiqlang: ")
            if new_user == new_user2:
                print(f"parol {new_user} ga muvaffaqqiyatli ozgartirildi.")
                return new_user
            print("parollar mos kelmadi")
            return pin
        print("parollar 4 xonali bolishi kerak")
        return pin
    print("eski parol xato")
    return pin
