# TASK_7.3.1
"""
from math import pow  # Импорт функции возведения в степень

a, b = int(input()), int(input())  # Ввод данных
counter = 0  # Установка значения счетчика
for i in range(a, b + 1):  # Создания цикла с итерациями от a до b+1
    if pow(i, 3) % 10 == 4 or pow(i, 3) % 10 == 9:  # Проверка условия
        counter += 1  # Подсчет значений если условие True
print(counter)  # Вывод результатов

a = int(input())
b = int(input())
counter = 0
for i in range(a, b + 1):
    if i % 10 == 4 or i % 10 == 9:
        counter += 1
print(counter)
"""
# TASK_7.3.2
"""
n = int(input())
counter = 0
for i in range(n):
    counter += int(input())
print(counter)
V-2
# print(sum(int(input()) for _ in range(int(input()))))
"""

# TASK_7.3.3
"""
from math import log
n = int(input())
value = 0
for i in range(1, n + 1):
    value += 1 / i

sum_value = value - log(n)
print(sum_value)
"""
# TASK_7.3.4
"""
n = int(input())
total = 0
for i in range(1, n+1):
    if (i**2) % 10 == 2 or (i**2) % 10 == 5 or (i**2) % 10 == 8:
        total += i
    else:
        total == 0
print(total)

V-2
print(sum([i for i in range(1,int(input())+1) if i**2%10 in (2,5,8)]))
"""

# TASK_7.3.5 factorial (n! = 1 * 2 * 3...*n)
"""
from math import factorial
print(factorial(int(input())))

V-2
n = int(input())
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(factorial)
"""

# TASK_7.3.5
"""
Напишите программу, которая считывает 10 чисел и выводит произведение отличных от нуля чисел.

Формат входных данных
На вход программе подаются 10 целых чисел, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести произведение отличных от нуля чисел.

num = 1
for _ in range(10):
    num_input = int(input())
    num *= num_input + (num_input == 0)
print(num)

V-2
total = 1
for i in range(10):
    num = int(input())
    if num != 0:
        total *= num
print(total)
"""

# TASK_7.3.6
"""
n = int(input())
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        count += i
print(count)
"""

# TASK_7.3.7
"""
n = int(input())

if n % 2 == 0:
    print(-n // 2)
else:
    print(n // 2 + 1)
    
V-2
n, sum = int(input()), 0
for i in range(1, n + 1):
    sum += (-1)**(i+1) * i
print(sum)

V-3
n = int(input())
total = 0
flag = True
for i in range(1, n + 1):
    if flag == True:
        total += i
        flag = False
    else:
        total -= i
        flag = True 
print(total)

V-4
# На вход программе подается натуральное число n. Напишите программу вычисления знакочередующей суммы:
# 1 - 2 + 3 - 4 ... + (- 1) ** (n + 1) * n
# Данная знакочередующая сумма состоит из сложения нечетных и отрицания четных чисел
# поэтому создадим два сумматора, один сумматор четных чисел (отрицательных), второй - нечетных (положительных)
# сумма обоих и будет решением нашей задачи
n = int(input())  # ввод конечного числа
x = 0  # начальное значение сумматора отрицательных чисел
y = 0  # начальное значение сумматора положительных чисел
for i in range(1, n + 1):  # перебор чисел от 1 до n + 1
    if i % 2 == 0:  # нахождение отрицательных чисел (четные числа)
        x = x - i  # сумматор отрицательных чисел
    else:  # нахождение положительных чисел (нечетные числа)
        y = y + i  # сумматор положительных чисел
z = x + y  # сумма всех чисел
print(z)  # вывод суммы n-чисел

V-5
print(sum([i if i % 2 != 0 else -i for i in range(1, int(input()) + 1)]))
"""

# TASK_7.3.8
"""
n = int(input())   # вводится число членов дальнейшей последовательности 
largest = n   # n идёт в начале всей последовательности и до введения следующих является наибольшим
previous_largest = 0   # предыдущее не вводилось, примем за 0 до переприсвоения

for _ in range(n):   # начинаем цикл записи остальных чисел, их сравнивания и переприсвоения
    num = int(input())
    if num > largest:    # если введённое число больше largest (самое первое largest = n)
        previous_largest = largest    # прошлое самое большое становится предыдущим наибольшим
        largest = num   # а данное введённое становится наибольшим пока не введут следующие
    elif previous_largest < num < largest:   # если введ. числ. больше предыдущего наибольшего но меньше наибольшего
        previous_largest = num   # оно вытесняет пред наибольшее и само становится им.
    else:    # num < previous_largest: если введённое число меньше предыдущего наиб, ничего не изменится
        num = num
print(largest)
print(previous_largest)

V-2
n = int(input())
prev_largest = -1
largest = -1

for i in range(n):
    number = int(input())
    if number > prev_largest:
        largest = prev_largest
        prev_largest = number
    elif number > largest:
        largest = number

print(prev_largest)
print(largest)
"""

# TASK_7.3.9
"""
flag = 'YES'
for _ in range(10):
    a = int(input())
    if a % 2 != 0:
        flag = 'NO'
print(flag)

V-2
result = 'YES'
for _ in range(10):
    num = int(input())
    if num % 2 != 0:
        result = 'NO'
print(result)
"""

# TASK_7.3.10
n = int(input())
fib1 = 1
fib2 = 1

for i in range(n):
    print(fib1, end=' ')
    fib1, fib2 = fib2, fib1 + fib2




