import pandas as pd
import random
import matplotlib.pyplot as plt
import math as math


x = [i for i in range(-20, 20)]
x = list(map(lambda el: el / 10, x))
y = list(map(lambda el: 2 * math.sin(math.pi * 3 * el) ,x))
print(x)
plt.plot(x,y)
plt.scatter(x,y)
plt.show()



backpack = ['100','150','200','140', '20', '450']
l = ['Винегрет овощной', 'Суп', 'Котлеты', 'Гречка', 'Чай', 'Тортик']
plt.pie(backpack,labels = l)
plt.show()



x = ['янв', 'фев', 'март', 'апр', 'май', 'июнь', 'июль', 'авг', 'сен', 'окт', 'нояб', 'дек']
y = [39.4, 35.5, 40.1, 48.4, 79.8, 65.9, 74.1, 43.9, 49.2, 40.3, 39.4, 43.2]
plt.bar(x,y)
plt.show()
