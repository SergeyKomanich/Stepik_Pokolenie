# TASK_1
# for i in range(10):
#     print('Python is awesome!')

# TASK_2
"""
strings = input()
num_str = int(input())

for i in range(num_str):
    print(strings)
"""
# TASK_3
"""
for _ in range(6):
    print('A' * 3)
for _ in range(5):
    print('B' * 4)
print('E')
for _ in range(9):
    print('T' * 5)
print('G')
"""

# TASK_4
# x = int(input())
# for _ in range(x):
#     print('*' * 19)

# TASK_5
# str_input = input()
# for i in range(10):
#     print(i, str_input)

# TASK_6
# num = int(input())
# for i in range(num + 1):
#     print(f'Квадрат числа {i} равен {i ** 2}')

# TASK_7
# n = int(input())
# for i in range(n, 0, -1):
#     print('*' * i)

# TASK_8
"""
a * (b / 100 + 1) ** i
где а - стартовое количество организмов
b -  среднесуточное увеличение в %
i - переменная цикла

m = m  + m * p / 100

m = float(input())
p = float(input())
n = int(input())

for i in range(n):
    print(i + 1, m * (1 + p / 100) ** i)
"""

# TASK_7.2.1
"""
m = int(input())
n = int(input())
for i in range(m, n + 1):
    print(i)
"""

# TASK_7.2.2
"""
m = int(input())
n = int(input())

if m < n:
    for i in range(m, n + 1):
        print(i)
else:
    for i in range(m, n - 1, -1):
        print(i)
"""
# TASK_7.2.3
"""
m = int(input())
n = int(input())

# start = ((m - 1) // 2) * 2 + 1
start = m % 2 + m - 1

for i in range(start, n - 1, -2):
    print(i)
"""

# TASK_7.2.4
"""
m = int(input())
n = int(input())
for i in range(m, n + 1):
    if i % 17 == 0 or i % 10 == 9 or i % 15 == 0:
        print(i)
        
m = int(input())
n = int(input())
[print(i) for i in range(m, n + 1) if i % 17 == 0 or i % 10 == 9 or i % 15 == 0]
"""

# TASK_7.2.5
n = int(input())
for i in range(1, 11):
    print(f'{n} x {i} = {n * i}')
