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


































