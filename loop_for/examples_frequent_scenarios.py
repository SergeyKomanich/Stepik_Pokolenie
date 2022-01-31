# Программа, которая считывает 10 чисел и определяет сколько из них больше 10.
counter = 0
for i in range(10):
    num = int(input())
    if num > 10:
        counter = counter + 1
print('Было введено', counter, 'чисел, больших 10.')

# Модифицируем программу: посчитаем еще и количество нулей среди введенных чисел.
counter1 = 0
counter2 = 0
for i in range(10):
    num = int(input())
    if num > 10:
        counter1 = counter1 + 1
    if num == 0:
        counter2 = counter2 + 1
print('Было введено', counter1, 'чисел, больших 10.')
print('Было введено', counter2, 'нулей.' )

# подсчитать количество чисел из диапазона [1; 100], квадрат которых оканчивается на 4.
counter = 0
for i in range(1, 101):
    if i**2 % 10 == 4:
        counter = counter + 1
print(counter)

# программа, которая считывает 10 чисел и определяет сумму тех из них, которые больше 10.
total = 0
for i in range(10):
    num = int(input())
    if num > 10:
        total = total + num
print('Сумма чисел больших 10 равна',  total)

# программа, которая считает сумму натуральных чисел от 1 до 100:
total = 0
for i in range(1, 101):
    total = total + i
print('Сумма равна', total)

# программа, которая запрашивает 10 целых чисел и находит их среднее значение:
total = 0
for i in range(10):
    num = int(input())
    total = total + num
average = total / 10
print('Среднее значение равно', average)

# программа, определяющую, что натуральное число является простым:
num = int(input())
flag = True

for i in range(2, num):
    if num % i == 0:        #  если исходное число делится на какое-либо отличное от 1 и самого себя
        flag = False

if num == 1:
    print('Это единица, она не простая и не составная')
elif flag == True:
    print('Число простое')
else:
    print('Число составное')

# программа, которая считывает 10 положительных чисел и находит среди них наибольшее число.
largest = -1
for i in range(10):
    num = int(input())
    if num > largest:
        largest = num
print('Наибольшее число равно', largest)

# программа, которая считывает 10 чисел (необязательно положительных) и находит среди них наибольшее:
largest = int(input())  # принимаем первое число за максимальное
for i in range(9):
    num = int(input())
    if num > largest:
        largest = num
print('Наибольшее число равно', largest)