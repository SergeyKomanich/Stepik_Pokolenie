# EXAMPLE while(пока)
"""
программа, которая считывает числа и находит их сумму, до тех пор пока пользователь не введет слово stop:

text = input()
total = 0
while text != 'stop':
    num = int(text)
    total += num
    text = input()
print('Сумма чисел равна', total)

i = 5
while i <= 11:
    print('Python awesome!')
    i += 1

i = 7
a = 5
while i < 11:
    a += i
    i += 2
print(a)
"""
# count = 1
# while count < 10:
#     print('Python awesome!')         # infinitely(бесконечно)
#     # count += 1                     # 9 once

# TASK_7.4.1
"""
words = input()
while words != 'КОНЕЦ':
    print(words)
    words = input()
"""

# TASK_7.4.2
"""
words = input()
while words != 'КОНЕЦ' and words != 'конец':
    print(words)
    words = input()
"""

# TASK_7.4.3
"""
words = input()
sum_words = 0
while words not in ('стоп', 'хватит', 'достаточно'):
    sum_words += 1
    words = input()
print(sum_words)
"""

# TASK_7.4.4
"""
num = int(input())
while not num % 7:
    print(num)
    num = int(input())
"""

# TASK_7.4.5
"""
num = int(input())
sum_num = 0
while num >= 0:
    sum_num += num
    num = int(input())

print(sum_num)
"""

# TASK_7.4.6
"""
grades = int(input())
grade_fives = 0
while 0 < grades < 6:
    if grades == 5:
        grade_fives += 1
    grades = int(input())
print(grade_fives)
"""

# TASK_7.4.7
"""
n = int(input())
k = 0
for i in (25, 10, 5, 1):
    while n // i > 0:
        k += 1
        n -= i
print(k)

V-2
sum_pay = int(input())
coins = 0
while sum_pay >= 25:
    coins += 1
    sum_pay -= 25
while sum_pay >= 10:
    coins += 1
    sum_pay -= 10
while sum_pay >= 5:
    coins += 1
    sum_pay -= 5
while  sum_pay >= 1:
    coins += 1
    sum_pay -= 1
print(coins)

V-3
counter = 0
num = int(input())
for i in (25, 10, 5, 1):
    while num >= i:
        counter += 1
        num -= i
print(counter)
"""
# TASK_7.5.1
"""
num = int(input())
while num != 0:  # пока в числе есть цифры
    reverse_num = num % 10  # Находим последнюю цифру
    print(reverse_num)   # Выводим ее
    num = num // 10  #  Удаляем последнюю цифру
"""
# TASK_7.5.2
"""
num = int(input())
while num != 0:  # пока в числе есть цифры
    reverse_num = num % 10  # Находим последнюю цифру
    print(reverse_num, end='')   # Выводим ее
    num = num // 10  #  Удаляем последнюю цифру
"""

# TASK_7.5.3
"""
num = input()
print('Максимальная цифра равна', max(num))
print('Минимальная цифра равна', min(num))

V-2
num = int(input())
min_mum = 9
max_mum = 0
while num > 0:
    x = num % 10
    if x < min_mum:
        min_mum = x
    if x > max_mum:
        max_mum = x
    num = num // 10
print(f'Максимальная цифра равна {max_mum}')
print(f'Минимальная цифра равна {min_mum}')
"""

# TASK_7.5.4
"""
from numpy import prod
m = [int(i) for i in input()]
print(sum(m), len(m), prod(m), sum(m)/len(m), m[0], m[0]+m[-1], sep = '\n')

V-2
n = int(input())                  # препарируемое число)))
num = n                           # уменьшаемый остаток для получения "стоп" в цикле
total = 0                         # сумма чисел
product = 1                       # произведение чисел
quantity = 0                      # количество чисел
 
# делаем цикл
while num:
    total += num % 10             # считаем суму чисел
    product *= num % 10           # считаем произведение чисел
    quantity += 1                 # считаем количество чисел
    num //= 10                    # откидывает последнее число
    
# выводим ответы    
print(total)                      # сумма чисел
print(quantity)                   # количество чисел
print(product)                    # произведение чисел
print(total / quantity)           # среднее арифмитическое всех чисел
print(n // 10 ** (quantity - 1))  # первое число
print(n // 10 ** (quantity - 1) + n % 10)  # произведение первого и последнего чисел

V-3
num = int(input())
sum_num = 0
amount_of_num = 0
product_of_num = 1
average = 0
first_num = 0
sum_last_first = 0
digit_last = num % 10

while num != 0:
    last_digit = num % 10
    sum_num += last_digit
    amount_of_num += 1
    product_of_num *= last_digit
    average = sum_num / amount_of_num
    first_num = last_digit
    sum_last_first = last_digit + digit_last
    num = num // 10
print(sum_num, amount_of_num, product_of_num, average, first_num, sum_last_first, sep='\n')
"""

# TASK_7.5.5
"""
num = int(input())

while num > 100:
    num //= 10

print(num % 10)
"""

# TASK_7.5.6
"""
num = str(input())
max, min = max(num), min(num)
if max == min:
    print('YES')
else:
    print('NO')
    
V-2
num = int(input())
digit = num % 10
result = 'YES'
while num != 0:
    if digit != num % 10:
        result = 'NO'
    num = num // 10
print(result)
"""

# TASK_7.5.7
"""
l = list(input()); print('YES' if l == sorted(l)[::-1] else 'NO')

V-2
num = int(input())
answer = 'YES'

while num // 10 != 0:
    i = num % 10
    num = num // 10
    if i > num % 10:
        answer = 'NO'

print(answer)
"""



















































