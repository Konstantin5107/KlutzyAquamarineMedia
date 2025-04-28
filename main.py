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
from turtle import width
from PIL import Image,ImageDraw,ImageFont
from PIL.ImageFont import truetype
from PIL._imaging import fill

print("Генератор мемов запущен!")
text1 = input("Введите верхний текст:")
text2 = input("Введите нижний текст:")
print(text1,text2)
print("Список картинок:")
print("1.Кот в ресторане")
print("2. Кот в очках")
Unumber = int(input("Введите номер картинки:"))
if Unumber == 1:
    file = "Кот в ресторане.png"
if Unumber == 2:
    file = "Кот в очках.png"
image = Image.open(file)
draw = ImageDraw.Draw(image)
font = truetype("arial ttf", size=70)
draw.text((0,0), text1 , font = font, fill = "black")
text = draw.textbbox((0,0),text1 , font)
textw = text[2]
draw.text(((width - textw)/2 , 10 , text1 , font == font ,fill == "black"))
draw.text((0,0), text2 , font = font, fill = "black")
text = draw.textbbox((0,0),text2 , font)
textw = text[2]
draw.text(((width - textw)/2 , 10 , text2 , font == font ,fill == "black"))
image.save("new_meme.jpg")