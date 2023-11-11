#   Bu yerda har bir mehmonning ismi yangi qatordan chiqdi

# mehmonlar = ['Jonibek', 'Temurbek', 'Javlonbek', 'O\'tkirbek']
# for mehmon in mehmonlar:
#     print(mehmon)


# Yana bitta shunga o'xshash misol ⬆️

# mehmonlar = ['Jonibek', 'Temurbek', 'Javlonbek', 'O\'tkirbek']
# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon}, sizni 20-Mart kuni oshga taklif qilamiz")
#     print("Hurmat bilan, Palonchiyevlar oilasi")


# Huddi shu kabi agar takrorlanishi kerak bo'magan kodni tsikldan so'ng o'ngga surib qo'ysak Python bu qatorni

# tsiklning tarkibida deb hisoblab, qayta-qayta bajaradi:
# mehmonlar = ['Jonibek', 'Temurbek', 'Javlonbek', 'O\'tkirbek']
# for mehmon in mehmonlar:
# print(mehmon)

# print(mehmonlar) # bu qator tsikl tashqarisida bo'lishi kerak edi


# Bu yerda biz belgilangan sondan boshlab ohirgi belgilangan songacha sonlarning kv hisoblayabmiz

# sonlar = list(range(1,11))
# for son in sonlar:
#     print(f"{son} ning kvadrati {son**2} ga teng")


# bu yerda sonlarni bosh o'zgaruvchiga yuklab uni kv sini hisoblayabmiz

# sonlar = list(range(11)) # 1 dan 10 gacha sonlar ro'yxatini yaratamiz
# sonlar_kvadrati = [] # bo'sh ro'yxat yaratamiz
# for son in sonlar:  # sonlar dagi har bir son uchun
#     sonlar_kvadrati.append(son**2) # uning kv.ni hisoblab, sonlar_kvadrati ga yuklaymiz
#
# print(sonlar)
# print(sonlar_kvadrati)

# for operatori va input() funktsiyasini jamlab, ro'yxatni foydalanuvchidan olingan qiymatlar bilan to'ldirish mumkin:

# dostlar = [] # bo'sh ro'yxat
# print("5 ta eng yaqin do'stingiz kim?")
# for n in range(5): # n bu yerda 0 dan 4 gacha qiymatlar oladi
#     dostlar.append(input(f"{n+1}-do'stingizning ismini kiriting: "))
# print(dostlar)


# car0 = {
#     'model': 'lacetti',
#     'rang': 'oq',
#     'yil': 2018,
#     'narh': 13000,
#     'km': 50000,
#     'korobka': 'avtomat'
# }
#
# car1 = {
#     'model': 'nexia3',
#     'rang': 'qora',
#     'yil': 2015,
#     'narh': 9000,
#     'km': 50000,
#     'korobka': 'mexanika'
# }
#
# car2 = {
#     'model': 'gentra',
#     'rang': 'qizil',
#     'yil': 2019,
#     'narh': 15000,
#     'km': 20000,
#     'korobka': 'mexanika'
# }

# car = car0
# print(f"{car['model'].title()},\
#   {car['rang']} rang,\
#   {car['yil']}-yil, {car['narh']}$")
#
# car = car1
# print(f"{car['model'].title()},\
#   {car['rang']} rang,\
#   {car['yil']}-yil, {car['narh']}$")
#
# car = car2
# print(f"{car['model'].title()},\
#   {car['rang']} rang,\
#   {car['yil']}-yil, {car['narh']}$")


# cars = [car0, car1, car2]
# for car in cars:
#     print(f"{car['model'].title()}, "
#           f"{car['rang']} rang, "
#           f"{car['yil']}-yil, {car['narh']}$")
# print(cars[0])
# print(cars[0]['model'])
# print(f"{cars[2]['rang'].title()} "
#       f"{cars[2]['model']}")

# malibus = []
# for n in range(10):
#     yangi_mashina = {
#         'model': 'gentra',
#         'rang': 'qizil',
#         'yil': 2019,
#         'narh': 15000,
#         'km': 20000,
#         'korobka': 'mexanika'
#     }
#     malibus.append(yangi_mashina)
# print(malibus)
# for malibu in malibus[:3]:
#     malibu['rang'] = 'qizil'
#
# for malibu in malibus[3:6]:
#     malibu['rang'] = 'qora'
# # print(malibus)
#
# for malibu in malibus:
#     if malibu['korobka'] == 'avto':
#         malibu['narh'] = 40000
#     else:
#         malibu['narh'] = 35000
# print(malibus)
# hamkasblar = {
#     'ali': {'familiya': 'valiyev',
#             'tyil': 1995,
#             'malumot': 'oliy',
#             'tillar': ['python', 'c++']
#             },
#     'vali': {'familiya': 'aliyev',
#              'tyil': 2001,
#              'malumot': 'orta-maxsus',
#              'tillar': ['html', 'css', 'js']
#              },
#     'hasan': {'familiya': 'husanov',
#               'tyil': 1999,
#               'malumot': 'maxsus',
#               'tillar': ['python', 'php']
#               }
# }
# for ism, info in hamkasblar.items():
#     print(f"\n{ism.title()} {info['familiya'].title()}, "
#           f"{info['tyil']}-yilda tug'ilgan. "
#           f"Ma'lumoti: {info['malumot']}. \n"
#           "Quyidagi dasturlash tillarini biladi:")
#     for til in info['tillar']:
#         print(til.upper())


# shaxslar = {
#     'abu abdulloh ali muhammad ibn ismoil': {
#         'tyil': 810,
#         't_topgan': 'buxoro',
#         "umr-ko'rgan": 60,
#     }
# }
#
# for nomlar, yillar in shaxslar.items():
#     print(f"\n{nomlar.title()}. ", end='')
#     for yil in yillar:
#         print(f'{yil}', end="")


#     "abu abdulloh ali muhammad ibn ismoil 810-yilda buxoroda tavallud topgan": "60 yil umr ko'rgan",
#     "abdulla qodiriy 1894-yilda toshkentda tavallud topgan": "44 yil umr ko'rgan",
#     "erkin vohidov 1936-yilda farg'onada tavallud topgan": "80 yil umr ko'rgan",
#     "alisher navoiy 1441-yilda xirotda tavallud topgan": "60 yil umr ko'rgan"

# buxoriy = {'ism': 'Abu Abdulloh Muhammad ibn Ismoil',
#            'tyil': 810,
#            'vyil': 870,
#            'tjoy': 'Buxoro'
#            }
#
# qodiriy = {'ism': 'Abdulla Qodiriy',
#            'tyil': 1894,
#            'vyil': 1938,
#            'tjoy': 'Toshkent'
#            }
#
# vohidov = {'ism': 'Erkin Vohidov',
#            'tyil': 1936,
#            'vyil': 2016,
#            'tjoy': "Farg'ona"
#            }
#
# navoiy = {'ism': 'Alisher Navoiy',
#           'tyil': 1441,
#           'vyil': 1501,
#           'tjoy': "Xirot"
#           }
#
# shaxslar = [buxoriy, qodiriy, vohidov, navoiy]
#
# for shaxs in shaxslar:
#     ism = shaxs['ism']
#     tyil = shaxs['tyil']
#     vyil = shaxs['vyil']
#     tjoy = shaxs['tjoy']
#     print(f"{ism} {tyil}-yilda {tjoy}da tavallud topgan. "
#           f"{vyil - tyil} yil umr ko'rgan.")


# Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing.
# Mahsulotlar nomini birma-bir qabul qilib, yangi ro'yxatga joylang.


# savatcha = []
#
# while True:
#     mahsulot = input("Mahsulotingizni savatchaga qo'shing: ")
#     savatcha.append(mahsulot)
#     javob = input("Yana mahsulot kiritasizmi? (ha/yo'q)")
#     if javob != 'ha':
#         break

# ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting
# Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring:

# ismlar = ["anvar", "jasur", 'javohir']
# print("Salom " + ismlar[0].title() + " bugun choyxona bormi?")
# print(ismlar[1].title() + " ertaga kinoga tushmaymizmi?")
# print("Bugun basseynga boraylik " + ismlar[2] + ".")

# sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik).
# Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring.
# Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring.

# sonlar = [21, -43, 321.0, 123_221_323, 32323, 7883]
# sonlar[0] = sonlar[2]
# sonlar[4] = sonlar[4] + 12
# del sonlar[5]
# print(sonlar)

# t_shaxslar va z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning,
# ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting.
# Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop()), quyidagi ko'rinishda chiqaring:

# t_shaxslar = ["Imom Buxoriy", "Bobur", "Amir Temur"]
# z_shaxslar = ["Bill Geyts", "Jek Ma", "Ilon Mask", "Mark Zuckerberg"]
# print(f"\nMen tarixiy shaxslardan {t_shaxslar.pop(2)} bilan,\n\
# zamonaviy shaxslardan esa {z_shaxslar.pop(3)} bilan\n\
# suhbat qilishni istar edim\n")

# friends nomli bo'sh ro'yxat tuzing va unga
# .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting.
# Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang.
#
# friends = []
# friends.append("Javohir")
# friends.append("Rasul")
# friends.append("Mansur")
# print(friends)
# print('friends')
# friends.remove("Masur")
