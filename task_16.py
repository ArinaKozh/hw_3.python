"""
: Требуется вычислить, сколько раз встречается некоторое
число X в массиве A[1..N]. Пользователь в первой строке вводит
натуральное число N – количество элементов в массиве. В последующих
строках записаны N целых чисел Ai
. Последняя строка содержит число X
""" 
N = int(input("Введите количество элементов "))
a = []
for i in range(N):
    a.append(int(input("Введите элемент ")))
x = int(input("Введите x "))
count = 0
for i in a:
    if i == x:
        count+=1
print(count)
