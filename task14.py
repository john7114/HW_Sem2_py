# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k),
# не превосходящие числа N.

N = int(input("Введите число: "))

i = 0
num = 2
exponentiation = 0
while exponentiation < N:
    exponentiation = num**i
    if exponentiation < N:
        print(exponentiation, end='; ')
    i += 1
