def pul_yechish(balans):
    user = input("Qancha pul yechmoqchisiz: ")

    if user.isdigit():
        user = int(user) * 1.01

        if user < balans:
            balans -= user
            print(f"pul muvaffaqiyatli yechildi sizning balansingiz {balans} so'm")
            return True
        else:
            print("Hisobingizda pul yetarli emas!")
    else:
        print("Faqat raqam kiriting!")
    return balans


