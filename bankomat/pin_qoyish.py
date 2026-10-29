def pin_qoyish():
    while True:
        parol = input("parol qoying:")
        if parol.isdigit() and len(parol) == 4:
            return parol
        else:
            print("bunday parol qoyish mumkin emas")

