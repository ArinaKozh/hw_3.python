"""
Задача HARD необязательная Имеется список чисел. Создайте список, в который попадают числа, 
описывающие максимальную возрастающую последовательность. Порядок элементов менять нельзя.
Одно число - это не последовательность.
Пример:
[1, 5, 2, 3, 4, 6, 1, 7] => [1, 7]
[1, 5, 2, 3, 4, 1, 7, 8 , 15 , 1 ] => [1, 5]
[1, 5, 3, 4, 1, 7, 8 , 15 , 1 ] => [3, 5]
"""

a = [1, 5, 2, 3, 4, 6, 1, 7] 
mas = []
for k in range(2):
    for i in a:
        t = False
        for j in range(0, len(mas)):
            if (i-1) == mas[j][len(mas[j])-1]:
                mas[j].append(i)
                t = True
        if t == False:
            mas.append([i])
print(mas)

max = 0
res = []
for i in mas:
    if len(i)>max:
        max = len(i)
        res = [i[0],i[len(i)-1]]
print(res)
