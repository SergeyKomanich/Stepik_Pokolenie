# TASK_8.1.5
"""
for i in range(10, 25):
    print('Python awesome!')

15 раз Python awesome! на каждой строке
"""


# TASK_8.1.6
"""
n = int(input())
counter = 0

for i in range(1, n + 1):
    if i % 3 == 0 and i % 7 != 0:
        counter += 1
print(counter)

выводит количество чисел от 1 до n кратных 3, но не кратных 7
"""
# TASK_8.1.7
"""
n = int(input())
total = 0
for i in range(1, n + 1):
     total += i
print(total)
"""

# TASK_8.1.8
"""
i = 4
while i <= 10:
    print('Python!')
    i += 1

n = int(input())
i = 2
while n % i != 0:
    i += 1
print(i)

OUTPUT --> 4
"""

# TASK_8.1.9
"""
n = int(input())
res = 1
i = 2
while i <= n:
    res *= i
    i += 1
print(res)

выводит факториал числа n
"""

# TASK_8.1.10

"""
n = int(input())
i = 2
while n % i != 0:
    i += 1
print(i)

выводит минимальный делитель числа, отличный от единицы
"""

# TASK_8.1.11

"""
n = int(input())
total = 0

while n != 0:
    last_digit = n % 10
    total += last_digit
    n //= 10
print(total)
"""

# TASK_8.1.12

"""
n = int(input())
counter = 0

while n > 0:
    counter += 1
    n //= 10
print(counter)
"""

# TASK_8.2.1
"""
На обработку поступает натуральное число. Нужно написать программу, которая выводит на экран сумму чётных цифр 
этого числа или 0, если чётных цифр в записи нет.

n = int(input())
s = 0
while n > 0:
    if n % 2 == 0:
        s += n % 10
    n //= 10
print(s)
"""

# TASK_8.2.2
"""
На обработку поступает последовательность из 8 целых чисел. Известно, что вводимые числа по абсолютной величине не 
превышают 10^12. Нужно написать программу, которая выводит на экран количество делящихся нацело на 4 чисел в исходной 
последовательности и максимальное делящееся нацело на 4 число. Если делящихся нацело на 4 чисел нет, 
требуется на экран вывести «NO». 

n = 8
count = 0
maximum = -10**6
for i in range(1, n + 1):
    x = int(input())
    if x % 4 == 0:
        count += 1
        if x > maximum:
            maximum = x
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')
"""

# TASK_8.2.3
"""
На обработку поступает последовательность из 4 целых чисел. Известно, что вводимые числа по абсолютной величине не 
превышают 10^8. Нужно написать программу, которая выводит на экран количество нечётных чисел в исходной 
последовательности и максимальное нечётное число. Если нечётных чисел нет, требуется на экран вывести «NO».

count = 0
maximum = -1
for i in range(4):
    x = int(input())
    if x % 2 != 0:
        count += 1
        if x > maximum:
            maximum = x
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')
"""

# TASK_8.2.4

"""
На вход программе подается натуральное число nn. Напишите программу, которая печатает звездную рамку размерами n×19.

row_count = int(input())

for i in range(1, row_count + 1):
    if i == 1 or i == row_count:
        print('*' * 19)
    else:
        print('*' + ' ' * 17 + '*')
        
# V-2
n = int(input())
for i in range(1, n + 1):
  if i == 1: # по условию первый ряд весь заполнен звездочка
    print('*' * 19)
  elif i == n: # по условию весь последний ряд заполнен звездочками
    print('*' * 19)
  else: # середина имеет звездочку в начале и в конце, середина заполнена пробелами, 19 - 2 = 17 пробелов. 
    print('*', ' ' * 17, '*', sep='')
"""

# TASK_8.2.5
"""
Дано натуральное число (n>99). Напишите программу, которая определяет его третью (с начала) цифру.

V-1
num = int(input())
num3 = 0
while num >= 100:
    num3 = num % 10
    num //= 10
print(num3)

V-2
num = int(input())

while num > 999:
    num //= 10   
print(num % 10)
"""

# TASK_8.2.6

"""
Дано натуральное число. Напишите программу, которая вычисляет:

количество цифр 3 в нем;
сколько раз в нем встречается последняя цифра;
количество четных цифр;
сумму его цифр, больших пяти;
произведение цифр, больших семи (если цифр больших семи нет, то вывести 1, если такая цифра одна, то вывести ее);
сколько раз в нем встречается цифры 0 и 5 (всего суммарно).

num = int(input())

num_of_digits_3 = 0
last_digit = 0
even_digits = 0
sum_greater_five = 0
product_greater_seven = 1
how_num_0_5 = 0
last_num = num % 10

while num > 0:
    x = num % 10
    if x == 3:
        num_of_digits_3 += 1
    if x == last_num:
        last_digit += 1
    if x % 2 == 0:
        even_digits += 1
    if x > 5:
        sum_greater_five += x
    if x > 7:
        product_greater_seven *= x
    if x == 0 or x == 5:
        how_num_0_5 += 1
    num //= 10

print(num_of_digits_3)
print(last_digit)
print(even_digits)
print(sum_greater_five)
print(product_greater_seven)
print(how_num_0_5)
"""

"""
# TASK_8.2.7

Напишите программу, которая находит аналогичные интересные числа. 
В ответе запишите первые 5 чисел в порядке возрастания, включая число 1729.
# От 1729 до 40000 просчитало за 11 секунд! В этом промежутке получилось 6 "интересных чисел"

total = 0
for i in range(1729, 40000):            # верхнюю границу увеличивал, чтобы выдало минимум 5 чисел
    x = int(i ** (1 / 3))               # верхняя граница (т.к. число не больше корня 3й ст. из i)
    for j in range(1, x + 1):
        for k in range(1, x + 1):
            if j ** 3 + k ** 3 == i:
                total += 1
    if total >= 3:                      # чтобы напечатать числа в которых есть разные j и k
        print(i)
    total = 0
    
# V-2

num = 0
for i in range(1, 50):
    for j in range(1, 50):
        for k in range(1, 50):
            for l in range(1, 50):
                if (i != k and i != l and j != k and j != l and i ** 3 + j ** 3 == k ** 3 + l ** 3):
                    if i ** 3 + j ** 3 != num:
                        num = i ** 3 + j ** 3
                        print(num)
"""































