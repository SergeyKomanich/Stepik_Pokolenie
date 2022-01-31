"""
a = "1.2"

print(a.isdigit())


a = "spam".title()

print(a)


a = "spam"

print(len(a) * 2)


st = "1"
a = "1,2"

print(a.startswith(st))
"""


# print(int(input()) + int(input()) + int(input()))
"""
fin_length = int(input())

cube_volume = fin_length ** 3
total_surface_area = 6 * fin_length ** 2

print('Объем =', cube_volume)
print('Площадь полной поверхности =', total_surface_area)
"""

"""
# вычисления значения функции f(a, b) = 3(a + b)^3 + 275b^2 - 127a - 41
a = int(input())
b = int(input())

function_values = 3 * (a + b) ** 3 + 275 * b ** 2 - 127 * a - 41

print(function_values)
"""


"""
num = int(input('Введите число'))

next_number = num + 1
previous_number = num - 1

print(f'Следующее за числом {num} число: {next_number}')
print(f'Для числа {num} предыдущее число: {previous_number}')
"""

"""
monitor_price = int(input())
system_price = int(input())
keyboard_price = int(input())
mouse_price = int(input())

computer_price = monitor_price + system_price + keyboard_price + mouse_price
total_price = computer_price * 3

print(total_price)
"""

"""
a = int(input())
b = int(input())

x = a + b
y = a - b
c = a * b

print(a, '+', b, '=', x)
print(a, '-', b, '=', y)
print(a, '*', b, '=', c)
"""

"""
a1 = int(input())
d = int(input())
n = int(input())
n_th_progres = a1 + d * (n - 1)

print(n_th_progres)
"""

#x = int(input())

#print(x, x * 2, x * 3, x * 4, x * 5, sep='---')

"""
a = 15 // (16 % 7)
b = 34 % a * 5 - 29 % 5 * 2

print(a + b)
"""

#a = 82 // 3 ** 2 % 7
#print(a)

"""
b1 = int(input())
q = int(input())
n = int(input())

n_th_progres = b1 * q ** (n  - 1)

print(n_th_progres)
"""

#metre = int(input())
#print(metre // 100)

"""
students = int(input())
mandarins = int(input())

stud_mand = mandarins // students
basket = mandarins % students
print(stud_mand)
print(basket)

print(*(lambda x,y: (y//x,y%x))(int(input()),int(input())),sep='\n')
"""

"""
people = int(input())
dead_people = people // 2
survivors = people % 2
total_people = dead_people + survivors
print(total_people)
###################
n = int(input())

print((n + 1) // 2)
"""

# ВАГОН
#seat = int(input())
#print((seat-1) // 4 + 1)

"""
min = int(input())
hours = min // 60
minutes = min % 60

print(f'{min} мин - это {hours} час {minutes} минут.')
##############
min = int(input())
print(min, f'мин - это {min // 60} час {min % 60} минут.')
"""


"""
number = int(input())
a = number % 10           # Третья цифра
b = (number % 100) // 10  # Вторая цифра
c = number // 100         # Первая цифра
multiplication = a * b * c
sum_of_numbers = a + b + c
print('Сумма цифр =', sum_of_numbers)
print('Произведение цифр =', multiplication)
"""

"""
number = int(input())
a = number // 100         # Первая цифра
b = (number % 100) // 10  # Вторая цифра
c = number % 10           # Третья цифра

print(a, b, c, sep='')
print(a, c, b, sep='')
print(b, a, c, sep='')
print(b, c, a, sep='')
print(c, a, b, sep='')
print(c, b, a, sep='')
"""


"""
number = int(input())

num1 = number // 1000
num2 = (number // 100) % 10
num3 = (number // 10) % 10
num4 = number % 10

print('Цифра в позиции тысяч равна', num1)
print('Цифра в позиции сотен равна', num2)
print('Цифра в позиции десятков равна', num3)
print('Цифра в позиции едениц равна', num4)
"""




"""
Дано пятизначное число, которое хранится в переменной n. В переменных a, b, c, d, e хранятся:

a – число десятков тысяч (первая цифра),
b – число тысяч (вторая цифра),
c – число сотен (третья цифра),
d – число десятков (четвертая цифра),
e – число единиц (пятая цифра).

n = input()
a = n // 10000
b = n % 10000 // 1000
c = n % 1000 // 100
d = n % 100 // 10
e = n % 10
"""
"""
a = 17 // (23 % 7)
b = 34 % a * 5 - 29 % 4 * 3
print(a * b)

print('*****************')
print('*               *')
print('*               *')
print('*****************')


a = int(input())
b = int(input())
print(f'Квадрат суммы {a} и {b} равен {(a + b) ** 2}')
print(f'Сумма квадратов {a} и {b} равна {a ** 2 + b ** 2}')
"""

"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = a ** b + c ** d
print(e)
"""


n = int(input())
nn = n * 10 + n
nnn = n * 100 + n * 10 + n
print(n + nn + nnn)















































