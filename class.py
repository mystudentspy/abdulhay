# class Mashina():
#     def __init__(self,nomi,rangi,narxi):
#         self.nomi = nomi
#         self.rangi = rangi
#         self.narxi = narxi
#     def get_nomi(self):
#         return self.nomi
#     def get_rangi(self):
#         return self.rangi
#     def get_narxi(self):
#         return self.narxi
# name1 = Mashina("Spark","Oq","7000$")
# name2 = Mashina("Cobalt","Qora","12000$")
# print(name1.get_rangi())
# print(name2.get_narxi())
# class Kitob():
#     def __init__(self,nomi,rangi,narxi):
#         self.nomi = nomi
#         self.rangi = rangi
#         self.narxi = narxi
#     def get_nomi(self):
#         return self.nomi
#     def get_rangi(self):
#         return self.rangi
#     def get_narxi(self):
#         return self.narxi
# foydalanuvchi1 = Kitob("O'tkan kunlar","Oq","100 000 so'm")
# foydalanuvchi2 = Kitob("Kecha va kunduz","Qora","80 000 so'm")
# foydalanuvchi3 = Kitob("Mol hona", "Qizil", "50 000 so'm")
# print(foydalanuvchi1.get_nomi())
# print(foydalanuvchi2.get_narxi())
# print(foydalanuvchi3.get_rangi())









class Kitob():
    def __init__(self, name, narxi, rangi):
        self.name = name
        self.narxi = narxi
        self.rangi = rangi
    def get_full_name(self):
        return self.name

user1 = Kitob("molxona", "45 000 so'm", "Qora")
print(user1.get_full_name())




