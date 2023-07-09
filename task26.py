# Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

a = int(input('Введите число: '))
b = int(input('Введите степень: '))

def exponent(a,b):
    if b == 0:
        return 1
    return a*exponent(a,b-1)

print(exponent(a,b))