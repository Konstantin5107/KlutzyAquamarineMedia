import random
number = random.randint(0, 5)
print("Попробуй угадать число от 0 до 5!")
user_number = int(input("Введи число: "))
attempts = 1
while user_number != number and attempts <3:
    print("Не угадал")
    user_number -= user_number
    user_number = int(input())
    attempts += 1
if user_number == number:
    print("Это верно, я загадал число", number)
    print("Ты выиграл")
elif attempts == 3 and user_number != number:
    print("Ты проиграл")
