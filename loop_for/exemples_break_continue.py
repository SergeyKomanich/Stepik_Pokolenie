# Оператор break прерывает ближайший цикл for или while.
# Напишем программу, определяющую, что число является простым:

num = int(input())
flag = True

for i in range(2, num):
    if num % i == 0:        #  если исходное число делится на какое-либо отличное от 1 и самого себя
        flag = False
        break               # останавливаем цикл если встретили делитель числа

if flag == True:
    print('Число простое')
else:
    print('Число составное')

# Как только мы встречаем делитель отличный от 1 и num, мы меняем значение сигнальной метки и прерываем цикл,
# поскольку дальнейшее его выполнение лишено смысла: число гарантированно не является простым.

# программа, использующает цикл for, которая считывает 10 чисел и суммирует их до тех пор,
# пока не обнаружит отрицательное число. В этом случае выполнение цикла прерывается командой break:
result = 0
for i in range(10):
    num = int(input())
    if num < 0:
        break
    result += num
print(result)

# программа, которая определяет, содержит ли введенное пользователем число, цифру 7.
num = int(input())
number = num
flag = False
while num != 0:
    last_digit = num % 10
    if last_digit == 7:
        flag = True
        break        # прерываем цикл, так как число гарантированно содержит цифру 7
    num //= 10

if flag == True:
    print('Число', number, 'содержит цифру 7')
else:
    print('Число', number, 'не содержит цифру 7')

# V-2
"""
n = int(input())
flag = False
while n != 0:
    last = n % 10
    if last == 7:
        flag = True
        break        # прерываем цикл, так как число гарантированно содержит цифру 7
    n //= 10

if flag is True:
    print('Число', n, 'содержит цифру 7')
else:
    print('Число', n, 'не содержит цифру 7')
    
v-3

n = int(input())
while n != 0:
    last = n % 10
    if last == 7:
        print('Число', n, 'содержит цифру 7')
        break
    n //= 10
else:
    print('Число', n, 'не содержит цифру 7')
"""

# CONTINUE -- Оператор continue позволяет перейти к следующей итерации цикла for или while до завершения всех команд в теле цикла.

#  программа, которая выводит все числа от 1 до 100, кроме чисел 7, 17, 29 и 78.

for i in range(1, 101):
    if i == 7 or i == 17 or i == 29 or i == 78:
        continue  # переходим на следующую итерацию
    print(i)

for i in range(10):
    print(i, end='*')
    if i > 6:
        break

i = 100
while i > 0:
    if i == 40:
        break
    print(i, end='*')
    i -= 20

n = 10
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n, end='*')

result = 0
for i in range(10):
    if i % 2 == 0:
        continue
    result += i
print(result)

mult = 1
for i in range(1, 11):
   if i % 2 == 0:
      continue
   if i % 9 == 0:
      break
   mult *= i
print(mult)
































