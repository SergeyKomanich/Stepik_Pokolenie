# TASK_9.3.1
"""
На вход программе подается строка состоящая из имени и фамилии человека, разделенных одним пробелом.
Напишите программу, которая проверяет, что имя и фамилия начинаются с заглавной буквы.

str_in = input()
if str_in == str_in.title():
    print('YES')
else:
    print('NO')
"""

# TASK_9.3.2
"""
На вход программе подается строка. Напишите программу, которая меняет регистр символов, 
другими словами замените все строчные символы заглавными и наоборот.

str_in = input()
str_changes = str_in.swapcase()

print(str_changes)
"""

# TASK_9.3.3
"""
На вход программе подается строка текста. Напишите программу, которая определяет является ли оттенок текста 
хорошим или нет. Текст имеет хороший оттенок, если содержит подстроку «хорош» во всевозможных регистрах.

Программа должна вывести «YES» если текст имеет хороший оттенок и «NO» в противном случае.

str_in = input()
if 'хорош' in str_in.lower():
    print('YES')
else:
    print('NO')
"""

# TASK_9.3.4
"""
На вход программе подается строка. Напишите программу, которая подсчитывает 
количество буквенных символов в нижнем регистре.
"""
str_in = input()
lower_let = 0
for i in range(len(str_in)):
    if str_in[i].islower():
        lower_let += 1
print(lower_let)
