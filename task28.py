#  Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
a = int(input('Введите число 1: '))
b = int(input('Введите число 2: '))

def summa(a, b):
    if a == 0:
        return b
    return summa(a-1, b+1)

print(summa(a,b))