import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

a = input('Привет! Как тебя зовут? (напиши свое имя и нажми Enter): ')
if a == 'Odin' or a == 'Один':
    print(f'\nОго! Тот самый {a}?!\n\nВерховный бог в германо-скандинавской мифологии?\nХозяин Вальхаллы, чертога убитых!')
else:
    print(f'\nО! {a}! Приятно познакомиться))')

# считаем гласные в имени
count = 0
vowels = set("aeiouауоиэыяюеё")
for letter in a.lower():
    if letter in vowels:
        count += 1
print("\nКоличество гласных равно:")
print(count)
print("Количество согласных равно:")
s_count = len(a) - count
print(s_count)

# визуализация имени
x=[count, s_count]

fig = plt.figure(figsize =(9, 5)) # размер круга

plt.pie(x, labels=("гласные в имени", "согласные в имени"))
plt.title('Графическая Визуализация Имени')