__author__ = 'anonymousblack'
fib1 = 1#Инициализация переменной fib1 единицей
fib2 = 1#Инициализация переменной fib2 единицей
n = input("Последовательность значения какого числа Фибоначи вы хотите узнать?  ")#Ввод числа с клавиатуры
n = int(n) #Преобразование в целое число.
i = 2
while i<n and n > 0:
    fib_sum = fib2 + fib1
    fib1 = fib2
    fib2 = fib_sum
    i += 1
    print(fib_sum)
