from math import *
# TASK_1
"""
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

p = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
print(p)
"""

# TASK_2
"""
r = float(input())
s = pi * pow(r, 2)
c = 2 * pi * r
print(s)
print(c)
"""

# TASK_3
"""
a = float(input())
b = float(input())
arithmetic_average = (a + b) / 2
geometric_mean = sqrt(a * b)
harmonic_mean = 2 * a * b / (a + b)
root_mean_square = sqrt((a ** 2 + b ** 2) / 2)
print(arithmetic_average)
print(geometric_mean)
print(harmonic_mean)
print(root_mean_square)
"""

# TASK_4
"""
x = radians(float(input()))
trigonom_expression = sin(x) + cos(x) + tan(x)**2
print(trigonom_expression)
"""

# TASK_5
"""
x = float(input())
value_num_x = ceil(x) + floor(x)
print(value_num_x)
"""

# TASK_6
"""
a = float(input())
b = float(input())
c = float(input())

d = b ** 2 - 4 * a * c

if d < 0:
    print('Нет корней')
elif d == 0:
    print(-b / (2 * a))
elif d > 0:
    x1 = (-b - sqrt(d)) / (2 * a)
    x2 = (-b + sqrt(d)) / (2 * a)
    print(min(x1, x2))
    print(max(x1, x2))
"""

# TASK_7
"""
n = int(input())
a = float(input())

s = (n * a ** 2) / (4 * tan(pi / n))

print(s)
"""
