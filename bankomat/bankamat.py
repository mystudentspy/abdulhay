from balans_korish import balanse_korish
from pin_tekshirish import pin_tekshir
from pin_ozgartirish import pin_ozgartirish
from pin_qoyish import pin_qoyish
from pul_qoshish import pul_qoshish
from pul_yechish import pul_yechish

def bankamat():
    with open("check.txt", "w"):
        pass
    balans = 0
    pin = pin_qoyish()
    if not pin_tekshir(pin):
        return "Tizimga kirish rad etildi."
    with open("check.txt", "w"):
        pass
    while True:
        print("bankamatga xush kelibsiz\n"
        "1. Balans korish\n"
        "2. pul qoshish\n"
        "3. pul yechish\n"
        "4. pin ozgartirish\n"
        "5. chiqish")
        amal = input("amal tanlang: ")
        if amal == "1":
            balans = balanse_korish(balans)
            with open("check.txt", "a") as f:
                f.write(f"sizning balansingiz: {balans} so'm\n")
        elif amal == "2":
            balans = pul_qoshish(balans)
            with open("check.txt", "a") as f:
                f.write(f"pul muvaffaqqiyatli qoshildi,sizning balansingiz{balans} som\n")
        elif amal == "3":
            balans = pul_yechish(balans)
            with open("check.txt", "a") as f:
                f.write(f"pul muvaffaqiyatli yechildi, sizning balansingiz {balans} so'm\n")
        elif amal == "4":
            pin = pin_ozgartirish(pin)
            with open("check.txt", "a") as f:
                f.write(f"parol {pin} ga muvaffaqqiyatli ozgartirildi.\n")
        elif amal == "5":
            with open("check.txt", "a") as f:
                f.write(f"Tizimdan chiqdingiz hayr!")
            return "Tizimdan chiqdingiz hayr!"
        else:
            print("xato amal, 1-5 orasidan tanlang!")



