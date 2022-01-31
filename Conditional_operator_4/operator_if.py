"""
Задача 2.

num = int(input())
last_digit = num % 10    # последняя цифра числа
first_digit = num // 10  # первая цифра числа

if last_digit == first_digit:
    print('ДА')
else:
    print('НЕТ')
"""

"""
# TASK 3
num1, num2, num3 = int(input()), int(input()), int(input())
counter = 0  # переменная счётчик
if num1 % 2 == 0:
    counter = counter + 1  # увеличиваем счётчик на 1
if num2 % 2 == 0:
    counter = counter + 1  # увеличиваем счётчик на 1
if num3 % 2 == 0:
    counter = counter + 1  # увеличиваем счётчик на 1
print(counter)
"""

"""
# TASK 4.1
if i % 2 == 0:
    print(i, 'чётное')
else:
    print(i, 'нечётное')
 ###########################   
if i % 2 != 0:
    print(i, 'нечётное')
else:
    print(i, 'чётное')
"""

"""
# ЗАДАЧА 4.1_3
password1 = input()
password2 = input()

if password1 == password2:
    print('Пароль принят')
else:
    print('Пароль не принят')
"""
"""
# ЗАДАЧА 4.1_4

num = int(input())

if num % 2 == 0:
    print('Четное')
else:
    print('Нечетное')
"""

# ЗАДАЧА 4.1_5
"""
num = int(input())

first_num = num // 1000
second_num = num // 100 - (num // 1000 * 10)
third_num = (num % 100 - num % 10) / 10
last_num = num % 10
if first_num + last_num == second_num - third_num:
    print('ДА')
else:
    print('НЕТ')
"""
# ЗАДАЧА 4.1_6
"""
age = int(input())

if age >= 18:
    print('Доступ разрешен')
else:
    print('Доступ запрещен')
"""

# ЗАДАЧА 4.1_7
"""
num1 = int(input())
num2 = int(input())
num3 = int(input())

if num2 - num1 == num3 - num2:
    print('YES')
else:
    print('NO')
"""

# ЗАДАЧА 4.1_8
"""
num1 = int(input())
num2 = int(input())

if num1 < num2:
    print(num1)
else:
    print(num2)
"""

# ЗАДАЧА 4.1_9
"""
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num_min = min(num1, num2, num3, num4)

print(num_min)
#####################################
a, b, c, d = int(input()), int(input()), int(input()), int(input())
if a < b < c < d:
    print (a)
else:
    if b < c < d:
        print (b)
    else:
        if c < d:
            print (c)
        else:
            print (d)
"""

# ЗАДАЧА 4.1_10
"""
a = int(input())
if a <= 13:
    print('детство')
elif a >= 14 and a <= 24:
    print('молодость')
elif a >= 25 and a <= 59:
    print('зрелость')
elif a >= 60:
    print('старость')
    *******************************
    
user_age = int(input())

if user_age <= 13:
    print('детство')
else:
    if user_age == 14 or user_age <= 24:
        print('молодость')
    else:
        if user_age == 25 or user_age <= 59:
            print('зрелость')
        else:
            print('старость')
********************************************
a = int(input())
if a <= 13:
    print("детство")
elif a <= 24:
    print("молодость")
elif a <= 59:
    print("зрелость")
elif a > 60:
    print("старость")
"""

# ЗАДАЧА 4.1_11

num1 = int(input())
num2 = int(input())
num3 = int(input())

sum_num = 0
if num1 > 0:
    sum_num += num1
if num2 > 0:
    sum_num += num2
if num3 > 0:
    sum_num += num3
    print(sum_num)
else:
    print(sum_num)





























