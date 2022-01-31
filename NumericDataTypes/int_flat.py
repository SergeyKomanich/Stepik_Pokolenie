# TASK_1
"""
num1 = float(input())
num2 = float(input())

triangle_area = 1 / 2 * num1 * num2
print(triangle_area)
"""

# TASK_2
"""
distance = float(input())
speed1 = float(input())
speed2 = float(input())

time = distance / (speed1 + speed2)

print(time)
"""

# TASK_3
"""
num = float(input())
if num == 0:
    print('Обратного числа не существует')
else:
    print(1 / num)
"""

# TASK_4
"""
f = float(input())
c = 5 / 9 * (f - 32)
print(c)
"""

# TASK_5
"""
dog_age = int(input())
if dog_age <= 2:
    print(dog_age * 10.5)
else:
    print(round((10.5 * 2) + (dog_age - 2) * 4))

t = int(input())
print(min(2, t) * 10.5 + max(t - 2, 0) * 4)
"""

# TASK_6
"""
num_float = float(input())
print(int(num_float * 10) % 10)
"""

# TASK_7
"""
number = float(input())
print((number - int(number)))
"""

# TASK_8
"""
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())

print('Наименьшее число =', min(num1, num2, num3, num4, num5))
print('Наибольшее число =', max(num1, num2, num3, num4, num5))
"""

# TASK_9
"""
num1 = int(input())
num2 = int(input())
num3 = int(input())
num_max = max(num1, num2, num3)
num_min = min(num1, num2, num3)
num_med = num1 + num2 + num3 - num_min - num_max
print(num_max)
print(num_med)
print(num_min)
"""

# TASK_10
"""
num = int(input())
num3 = num % 10
num2 = num // 10 % 10
num1 = num // 100
if num3 + num2 + num1 == 2 * max(num3, num2, num1):
    print('Число интересное')
else:
    print('Число неинтересное')
"""

# TASK_11
"""
print(sum((abs(float(input())) for i in range(5))))
"""

# TASK_12
p1 = int(input())
p2 = int(input())
q1 = int(input())
q2 = int(input())
print(abs(p1 - q1) + abs(p2 - q2))



























































