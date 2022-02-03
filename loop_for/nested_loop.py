# for i in range(8):
#     for j in range(i + 1):
#         print('*', end='')
#     print()
#
# for i in range(1, 4):
#     for j in range(3, 6):
#         print(i, j)

# for i in range(1, 4):
#     for j in range(3, 5):
#         print(i + j, end='')

# counter = 0
# for i in range(99, 102):
#     temp = i
#     while temp > 0:
#         counter += 1
#         temp //= 10
# print(counter)

# TASK_7.8.1
"""
Дано натуральное число n (n≤ 9). Напишите программу, которая печатает таблицу размером n×3
состоящую из данного числа (числа отделены одним пробелом).

n = int(input())
for i in range(n):
    for j in range(3):
        print(n, end=' ')
    print()
"""

# TASK_7.8.2
"""
Дано натуральное число n (n≤ 9). Напишите программу, которая печатает таблицу размером n×5, 
где в i-ой строке указано число i (числа отделены одним пробелом).

num = int(input())

for i in range(1, num + 1):
    for _ in range(5):
        print(i, '', end='')
    print()
"""

# TASK_7.8.3

"""
Дано натуральное число n (n≤ 9). Напишите программу, которая печатает таблицу сложения для всех чисел от 1 до n.

num = int(input())

for i in range(1, num + 1):
    for j in range(1, 10):
        print(i, '+', j, '=', i + j)
    print()
"""

# TASK_7.8.4

"""
Дано нечетное натуральное число n. Напишите программу, которая печатает равнобедренный звездный треугольник с основанием, равным n.

num = int(input())

for i in range(1, num + 1):
    print('*' * min(i, num - i + 1))
"""

# TASK_7.8.5

"""
Дано натуральное число n. Напишите программу, которая печатает численный треугольник

n = int(input())
for i in range(1, n + 1):
    for _ in range(i):
        print(i, end='')
    print()
    
V-2_my

num = int(input())

for i in range(1, num + 1):
    print(str(i) * i)
"""
