# TASK 4.3.1
"""
speed_zuma = int(input())
speed_flash = int(input())
if speed_zuma > speed_flash:
    print('NO')
elif speed_flash > speed_zuma:
    print('YES')
elif speed_flash == speed_zuma:
    print("Don't know")
"""


# TASK 4.3.2
"""
a, b, c = int(input()), int(input()), int(input())

if a == b == c:
    print('Равносторонний')
elif (a == b or a == c or b == c) and (a != c or a != b or b != c):
    print('Равнобедренный')
elif a != b and a != c and c != b:
    print('Разносторонний')
"""

# TASK 4.3.3
"""
num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 < num2 < num3 or num1 > num2 > num3:
    print(num2)
elif num2 < num3 < num1 or num2 > num3 > num1:
    print(num3)
else:
    print(num1)
"""

# TASK 4.3.3
"""
num_month = int(input())

if num_month == 2:
    print('28')
elif num_month <= 7:
    print(30 + num_month % 2)
else:
    print(31 - num_month % 2)
"""

# TASK 4.3.4
"""
weigth = int(input())

if weigth < 60:
    print('Легкий вес')
elif weigth < 64:
    print('Первый полусредний вес')
elif weigth < 69:
    print('Полусредний вес')
"""

# TASK 4.3.5
"""
num1 = int(input())
num2 = int(input())
math_operation = input()

if math_operation == '+':
    print(num1 + num2)
elif math_operation == '-':
    print(num1 - num2)
elif math_operation == '*':
    print(num1 * num2)
elif math_operation == '/':
    if num2 == 0:
        print('На ноль делить нельзя!')
    else:
        print(num1 / num2)
else:
    print('Неверная операция')
"""

# TASK 4.3.6
"""
color1 = input()
color2 = input()

if color1 == 'красный' and color2 == 'синий' or (color1 == 'синий' and color2 == 'красный'):
    print('фиолетовый')
elif color1 == 'желтый' and color2 == 'синий' or (color1 == 'синий' and color2 == 'желтый'):
    print('зеленый')
elif color1 == 'красный' and color2 == 'желтый' or (color1 == 'желтый' and color2 == 'красный'):
    print('оранжевый')
elif color1 == 'красный' and color2 == 'красный' or color1 == 'желтый' and color2 == 'желтый' or \
        color1 == 'синий' and color2 == 'синий':
    print(color1)
else:
    print('ошибка цвета')
"""

# TASK 4.3.7
"""
a = int(input())
if a == 0:
    print("зеленый")
elif a < 0 or a > 36:
    print("ошибка ввода")
elif (1 <= a <= 10 or 19 <= a <= 28) + (not a % 2) == 1:
    print("красный")
else:
    print("черный")
    
*************************************
pocket_num = int(input())
if pocket_num < 0 or pocket_num > 36:
    print('ошибка ввода')
elif pocket_num == 0:
    print('зеленый')
elif 1 <= pocket_num <= 10:
    if pocket_num % 2 == 0:
        print('черный')
    else:
        print('красный')
elif 11 <= pocket_num <= 18:
    if pocket_num % 2 == 0:
        print('красный')
    else:
        print('черный')
elif 19 <= pocket_num <= 28:
    if pocket_num % 2 == 0:
        print('черный')
    else:
        print('красный')
elif 29 <= pocket_num <= 36:
    if pocket_num % 2 == 0:
        print('красный')
    else:
        print('черный')
"""

# TASK 4.3.8
a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
if a2 < a1:
    if b2 < a1:
        print('пустое множество')
    elif b2 == a1:
        print(b2)
    elif a1 < b2 <= b1:
        print(a1, b2)
    elif b2 > b1:
        print(a1, b1)
elif a2 == a1:
    if b2 <= b1:
        print(a2, b2)
    else:
        print(a2, b1)
elif a2 < b1:
    if b2 <= b1:
        print(a2, b2)
    else:
        print(a2, b1)
elif a2 == b1:
    print(a2)
else:
    print('пустое множество')




























