import random
from random import choice

print("Добро пожаловать в игру про приключения рыцаря!")
health = 100
level = 0
bogatstvo = 0
print("Ваше здоровье равно 100 , уровень и богатство равны 0")
vibor = input("перед вами развилка , вы можете пойти направо или налево . Куда вы пойдёте?")
if vibor == "налево":
    print("Вы встретили дракона охраняющего сокровища!Вы можете напасть на него или вернуться к развилке.")
    choise2 = input("Что же вы выберете?Напасть или вернуться к развилке?:")
    if choise2 == "напасть":
      chans = random.randint(1,100)
      if chans <= 34:
        print("вы невероятный счастливчик , вы не только убили дракона и повысили свой уровень , но и забрали с собой сокровища которые он охранял!!!Вам также удалось подобрать сердце дракона , которое пригодиться вам в будующем .")
        level += 1
        bogatstvo += 10000
        print("Вы попали на городской рынок. Так как вам удалось до этого заработать денег , вы можете заняться перепродажей предметов или улучшить свое снаряжение.Также вы можете поработать на какого - либо купца.")
        if bogatstvo >= 10000:
            soglasie = input("Ваш баланс достаточен дла того чтобы заняться перекупкой. Хотите заняться ей , купить броню или подрабатывать у купцов.(перекупка/подработка/покупка):")
            if soglasie == "перекупка":
                print("Поздравляю!!! вы смогли разбогатеть и стать вельможей.Теперь вас не интересуют такие вещи как рыцарство. Вы разблокировали пятизвёздочную концовку. Вам рекомендуеться начать игру с начала .")
            if soglasie == "подработка":
                print("Вам удалось заработать еще немного денег и прикупить хорошее снаряжение.Продолжение этой концовки в след. версии игры.5-ти звездочная концовка.")
            if soglasie == "покупка":
                print("Вам удалось закупиться хорошей броней на следующие приключения .5-ти звездочная концовка.Продолжение в след. частях игры.")
      if chans >=35:
        print("Вы не смогли убить дракона , и он отнял у вас 50 здоровья , но к вашему счастью вы смогли скрыться с поля битвы жаждя мести.")
        health -= 50
        print("вы снова на развилке!вы можете снова вернуться к дракону , ведь ваша ярость придала вам сил , или можете отправиться в неизведанность - направо.")
        vibor2 = input("Что же ты выберешь?:")
        if vibor2 == "напасть":
            chans2 = random.randint(1,100)
            if chans2 <= 60:
                print("Вам удалось наконец победить этого дракона!!!Вы смогли востановить свое здовье до 100 а также повысили уровень на 2 и богатство на 16000 золотых!!!5-ти звездочная концовка разблокирована")
                health += 50
                level += 2
                bogatstvo += 16000
                print("Вы попали на городской рынок. Так как вам удалось до этого заработать денег , вы можете заняться перепродажей предметов или улучшить свое снаряжение.Также вы можете поработать на какого - либо купца.")
                if bogatstvo >= 10000:
                    soglasie = input("Ваш баланс достаточен дла того чтобы заняться перекупкой. Хотите заняться ей , купить броню или подрабатывать у купцов.(перекупка/подработка/покупка):")
                    if soglasie == "перекупка":
                        print("Поздравляю!!! вы смогли разбогатеть и стать вельможей.Теперь вас не интересуют такие вещи как рыцарство. Вы разблокировали пятизвёздочную концовку. Вам рекомендуеться начать игру с начала .")
                    if soglasie == "подработка":
                        print("Вам удалось заработать еще немного денег и прикупить хорошее снаряжение.Продолжение этой концовки в след. версии игры.5-ти звездочная концовка.")
                    if soglasie == "покупка":
                        print("Вам удалось закупиться хорошей броней на следующие приключения .5-ти звездочная концовка.Продолжение в след. частях игры.")
            if chans2 > 60:
                print("Кажеться рыцарство - это не твое . На этот раз дракон убил тебя :(")
                health -= 50
        if vibor2 == "направо":
            print("Вы попали на городской рынок. Так как вам не удалось до этого заработать денег , вы занялись подработкой на купцов. 2-х звездочная концовка.")
    if choise2 == "вернуться":
         print("У вас нету денег , вам следует поработать на какого - либо купца.")
         if bogatstvo >= 10000:
            soglasie = input("Ваш баланс достаточен дла того чтобы заняться перекупкой. Хотите заняться ей , купить броню или подрабатывать у купцов.(перекупка/подработка/покупка):")
            if soglasie == "перекупка":
                print("Поздравляю!!! вы смогли разбогатеть и стать вельможей.Теперь вас не интересуют такие вещи как рыцарство. Вы разблокировали трехзвёздочную концовку. Вам рекомендуеться начать игру с начала .")
            if soglasie == "подработка":
                print("Вам удалось заработать еще немного денег и прикупить хорошее снаряжение.Продолжение этой концовки в след. версии игры.3-х звездочная концовка.")
            if soglasie == "покупка":
                print("Вам удалось закупиться хорошей броней на следующие приключения .2-х звездочная концовка.Продолжение в след. частях игры.")
         if bogatstvo < 10000:
             print ("так как у вас нету денег вы устроились на подработку.Вы сможете потратить накопленные деньги и узнать продолжение в след. главе.1 звезлочная концовка")
if vibor  == "направо":
    print("так как у вас неne денег вы устроились на подработку.Вы сможете потратить накопленные деньги и узнать продолжение в след. главе.1 звезлочная концовка")