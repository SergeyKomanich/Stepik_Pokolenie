# TASK_7.6.1
# n = int(input())
#
# for i in range(2, n + 1):
#     if n % i == 0:
#         break
# print(i)

# TASK_7.6.2
# num = int(input())
# for i in range(1, num + 1):
#     if 5 <= i <= 9 or 17 <= i <= 37 or 78 <= i <= 87:
#         continue
#     print(i)

# ЧИСЛО В ОБРАТНОМ ПОРЯДКЕ
# n = 5
# while n > 0:
#     n -= 1
#     print(n)
# else:
#     print('Цикл завершен.')

# n = 0
# while n < 10:
#     n += 2
#     print(n)
# else:
#     print('Цикл завершен.')

# РЕВЬЮ КОДА

# НЕПРАВИЛЬНО
"""
count = 0
p = 0                     # 1
for i in range(1, 10):    # 11
    x = int(input())
    if x > 0:              # >=
        p = p * x
        count = count + 1
if count > 0:
    print(x)                # count
    print(p)
else:
    print('NO')
"""

"""
На обработку поступает последовательность из 1010 целых чисел. Известно, что вводимые числа по абсолютной величине не превышают 10^6
Нужно написать программу, которая выводит на экран сумму всех отрицательных чисел последовательности и максимальное отрицательное число 
в последовательности. Если отрицательных чисел нет, требуется вывести на экран «NO». Программист торопился и написал программу неправильно.

mx = -10**6 # неверно задана переменная (сравнивать будет с минимальным)
s = 0
for _ in range(10):  # неверно задан диапозон (было 11), замена "i" на "_"
    x = int(input())
    if x < 0:
        s += x  # неверно задана формула (было равенство "=")
        if x > mx:  # смещен блок кода, чтобы условие работало только для x < 0
            mx = x
if s == 0:  # не был задано условие для вывода при отсутствии отрицательных чисел
    print('NO')
else:
    print(s)
    print(mx)
"""

"""
На обработку поступает натуральное число. Нужно написать программу, которая выводит на экран максимальную цифру числа, кратную 33. 
Если в числе нет цифр, кратных 33, требуется на экран вывести «NO». Программист торопился и написал программу неправильно.

n = int(input())
max_digit = -1 # берем максимальное число '-1' что б пройти проверку если среди введеных цифр будет '0'
while n > 0:
    digit = n % 10
    if digit % 3 == 0:
        if digit > max_digit: # проверка или цифра числа максимальная
            max_digit = digit
    n = n // 10 # уменьшаем число на один знак
if max_digit < 0: # если условие не истина, значит чисел чисел кратных "3" не было
    print('NO')
else:
    print(max_digit)
"""

"""
На обработку поступает натуральное число. Нужно написать программу, которая выводит на экран его первую (старшую) цифру. 
Программист торопился и написал программу неправильно.

n = int(input())
while n > 9:  # Ошибка - цикл имеет смысл только в случае если данное натурально число дву- и  более -значное.
    n //= 10  # Ошибка - нам необходимо постепенно отбрасывать числа до первого, а не выяснять последние из них.
print(n)
"""

"""
На обработку поступает натуральное число. Нужно написать программу, которая выводит на экран произведение цифр введенного числа

n = int(input())
product = 1
while n > 0:
    digit = n % 10
    product *= digit
    n //= 10
print(product)
"""
