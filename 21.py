koloda = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4

import random

random.shuffle(koloda)
print("Поиграем в 21")
count = 0
aifpk = 0
x = 1
otvet = ""
otv1 = "Извини у тебя перебор и ты продул!"
otv2 = "Поздравляю у тебя 21 и ты победил!"


def pechat1(ottv):
    print("ваш счет %d" % count)
    print(ottv)


while x == 1:
    otvet = input("Берем карту? y/n ")
    match otvet:
        case "y":
            current = koloda.pop()
            print("Вам попалась карта достоинством %d" % current)
            count += current
            if count > 21:
                pechat1(otv1)
                break
            elif count == 21:
                print(otv2)
                break
            else:
                print("У вас %d очков" % count)
        case "n":
            fpk = koloda.pop()
            aifpk += fpk
            print("У крупье выпало %d " % fpk)
            x = 2
while x == 2:

    if fpk <= count and fpk <= 21:
        print("Крупье решает брать ему карту или нет")
        ai = random.randint(1, 2)
        print("Искуственный интелект выбор говорит= " + str(ai))

        if ai == 1:

            fpk = koloda.pop()
            aifpk += fpk
            if aifpk == 21:
                if aifpk > count:
                    print("Крупье выпало %d" % aifpk)
                    print("У вас %d" % count)
                    print("Крупье выигрывает с 21")
                    break
                elif aifpk == count:
                    print("Крупье выпало %d" % aifpk)
                    print("У вас %d" % count)
                    print("У вас ничья!")
                    break
                elif aifpk < count:
                    print("Крупье выпало %d" % aifpk)
                    print("У вас %d" % count)
                    print("Крупье продул!")
                    break
                if aifpk > 21:
                    print("Крупье выпало %d" % aifpk)
                    print("У вас %d" % count)
                    print("Крупье проиграл у него больше 21")
                    x = 3
                    break
            print("Крупье выпало %d" % aifpk)
            print("У вас %d" % count)
        elif ai == 2:
            if aifpk > count and fpk < 21:

                print("Крупье останавливает игру и просит сравнение")
                if aifpk > count:
                    if aifpk < 21:
                        print("Крупье выпало %d" % aifpk)
                        print("У вас %d" % count)
                        print("У крупье больше счет  чем у вас и он выигрывает!")
                        break
                    elif aifpk > 21:
                        print("Крупье выпало %d" % aifpk)
                        print("У вас %d" % count)
                        print("У крупье больше 21 и он проигрывает!")
                        x = 3
                        break

                elif aifpk == count:
                    print("Крупье выпало %d" % aifpk)
                    print("У вас %d" % count)
                    print("У вас ничья!")
                    break
                elif aifpk < count:
                    print("У вас болше чем у крупье и вы победили!")
                    print("Крупье выпало %d" % aifpk)
                    print("У вас %d" % count)
                    break
            elif aifpk < 10:
                fpk = koloda.pop()
                aifpk += fpk
                print("Крупье выпало %d" % aifpk)
                if aifpk > count:
                    if aifpk < 21:
                        print("Крупье выпало %d" % aifpk)
                        print("У вас %d" % count)
                        print("У крупье больше счет  чем у вас и он выигрывает!")
                        break
                    elif aifpk > 21:
                        print("Крупье выпало %d" % aifpk)
                        print("У вас %d" % count)
                        print("У крупье больше 21 и он проигрывает!")
                        x = 3
                        break

                    elif aifpk == count:
                        print("Крупье выпало %d" % aifpk)
                        print("У вас %d" % count)
                        print("У вас ничья!")
                        x = 3
                        break
                    elif aifpk < count:
                        print("У вас болше чем у крупье и вы победили!")
                        print("Крупье выпало %d" % aifpk)
                        print("У вас %d" % count)
                        break
        else:
            print("Крупье скинул карты и проиграл!")
            x = 3
            break
print("До новых встреч!")
