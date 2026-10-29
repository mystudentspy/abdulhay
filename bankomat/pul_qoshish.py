def pul_qoshish(balans):
    user = input("qancha pul qoshmoqchisiz:")
    if user.isdigit():
        user = int(user)
        balans += user
        print(f"pul muvaffaqqiyatli qoshildi,sizning balansingiz{balans} som")
    else:
        print("Faqat pul kiriting")
    return balans
