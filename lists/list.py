# TASK_11.1
"""
На вход программе подается одно число nn. Напишите программу, которая выводит список, состоящий из nn букв английского
алфавита ['a', 'b', 'c', ...] в нижнем регистре.

lst = int(input())

let = []
for i in range(97, lst + 97):
    ascii_char = chr(i)
    let += ascii_char
print(let)lst = int(input())

let = []
for i in range(97, lst + 97):
    ascii_char = chr(i)
    let += ascii_char
print(let)

V-2

lst2 = int(input())
alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(alph[0: lst2])
"""

# TASK_11.2.1

numbers = [12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324]
print(max(numbers) + min(numbers))

# TASK_11.2.5

evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
average = sum(evens) / len(evens)

print(average)

# TASK_11.2.6

rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
rainbow[-1] = 'Фиолетовый'
rainbow[3] = 'Зеленый'
print(rainbow)

# TASK_11.2.7

languages = ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic', 'Bengali', 'Portuguese', 'Russian', 'Japanese', 'Lahnda']
print(languages[::-1])

# TASK_11.2.8

numbers1 = [1, 2, 3] * 2
numbers2 = [6] * 9
numbers3 = [7, 8, 9, 10, 11, 12, 13]

print(numbers1 + numbers2 + numbers3)
