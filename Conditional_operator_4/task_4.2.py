# ЗАДАЧА 4.2.1
"""
num = int(input())
if num > -1 and num < 17:
    print('Принадлежит')
else:
    print('Не принадлежит')
"""

# ЗАДАЧА 4.2.2
"""
num = int(input())
if num <= -3 or num >= 7:
    print('Принадлежит')
else:
    print('Не принадлежит')
"""

# ЗАДАЧА 4.2.3
"""
num = int(input())
if (-30 < num <= -2) or (7 < num <= 25):
    print('Принадлежит')
else:
    print('Не принадлежит')
"""

# ЗАДАЧА 4.2.4
"""
n = int(input())
if (n % 7 == 0 or n % 17 == 0) and (n >= 1000 and n <= 9999):
    print('YES')
else:
    print('NO')
"""

# ЗАДАЧА 4.2.5
"""
a, b, c = int(input()), int(input()), int(input())
print("YES" if (a < b + c) and (b < c + a) and (c < a + b) else "NO")

a = int(input())
b = int(input())
c = int(input())

if a + b > c and a + c > b and b + c > a:
    print('YES')
else:
    print('NO')
"""

# ЗАДАЧА 4.2.6
"""
import calendar
print("YES" if calendar.isleap(int(input())) else "NO")

year = int(input())
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print('YES')
else:
    print('NO')
"""

# ЗАДАЧА 4.2.7
"""
a, b, c, d = int(input()), int(input()), int(input()), int(input())

if a == c or b == d:
    print('YES')
else:
    print('NO')
"""


# ЗАДАЧА 4.2.8
a, b, c, d = int(input()), int(input()), int(input()), int(input())
if (-1 <= a - c <= 1) and (-1 <= b - d <= 1):
    print('YES')
else:
    print('NO')





















