# TASK_11.3.1
"""
Вывел длину списка;
Вывел последний элемент списка;
Вывел список в обратном порядке (вспоминаем срезы);
Вывел YES если список содержит числа 5 и 17, и NO в противном случае;
Вывел список с удаленным первым и последним элементами.
Примечание. Каждый вывод осуществлять с новой строки.

numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2,
           12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]

print(len(numbers))
print(numbers[-1])
print(numbers[::-1])
if 5 in numbers and 17 in numbers:
    print('YES')
else:
    print('NO')

del numbers[0]
del numbers[-1]
print(numbers)
"""

# TASK_11.3.2
"""
На вход программе подается натуральное число nn, а затем nn строк. 
Напишите программу, которая создает из указанных строк список и выводит его.

V0-1

n = int(input())
lst = [input() for _ in range(n)]
print(lst)

V-2

num_str = int(input())
in_lst = []

for _ in range(num_str):
    in_lst.append(input())
print(in_lst)
"""

# TASK_11.3.3
"""
Напишите программу, выводящую следующий список:

['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', ...]
Формат выходных данных
Программа должна вывести указанный список.

Примечание. Последний элемент списка состоит из 26 символов z.

V-1
print([chr(97 + i) * (i + 1) for i in range(26)])

V-2
n=[]
x=96
for i in range(1, 27):
    n.append(chr(x+i)*i)
print(n)

V-3
s = []
for i in range(1, 27):
    s.append(chr(96+i)*i)
print(s)

V-4
alphabet = []

for i in range(ord('z') - ord('a') + 1):
    alphabet.append(chr(ord('a') + i) * (i+1))
print(alphabet)
"""

# TASK_11.3.4
"""
На вход программе подается натуральное число nn, а затем nn целых чисел. Напишите программу, 
которая создает из указанных чисел список их кубов.

num_str = int(input())
cub_num = []
for _ in range(num_str):
    cub_num.append(int(input()) ** 3)
print(cub_num)
"""

# TASK_11.3.5
"""
На вход программе подается натуральное число nn. Напишите программу, которая создает список 
состоящий из делителей введенного числа.

V-1
n = int(input())
print([i for i in range(1, n + 1) if n % i == 0])

V-2
num = int(input())
devisor = []
for i in range(1, num + 1):
    if num % i == 0:
        devisor.append(i)
print(devisor)
"""

# TASK_11.3.6
"""
На вход программе подается натуральное число n  2n≥2, а затем nn целых чисел. Напишите программу, 
которая создает из указанных чисел список, состоящий из сумм соседних чисел (00 и 11, 11 и 22, 22 и 33 и т.д.).

row_count = int(input())
nums = int(input())
sum_num = []

for _ in range(row_count-1):
    num = int(input())
    sum_num.append(nums+num)
    nums = num
print(sum_num)
"""

# TASK_11.3.7
"""
На вход программе подается натуральное число nn, а затем nn целых чисел. Напишите программу, которая создает 
из указанных чисел список, затем удаляет все элементы стоящие по нечетным индексам, а затем выводит полученный список.

V-1
lst = [int(input()) for i in range(int(input()))]
print(lst[::2])

V-2
row_count = int(input())
lst = []

for i in range(row_count):
    lst.append(int(input()))
del lst[1::2]
print(lst)
"""

# TASK_11.3.8
"""
На вход программе подается натуральное число n и n строк, а затем число k. 
Напишите программу, которая выводит k-ую букву из введенных строк на одной строке без пробелов.

Формат входных данных
На вход программе подается натуральное число n,  далее n строк, каждая на отдельной строке.
В конце вводится натуральное число k – номер буквы (нумерация начинается с единицы).

row_count = int(input())
str = []

for _ in range(row_count):
    str.append(input())
k_let = int(input())
result = ''
for i in str:
    if len(i) >= k_let:
        result += i[k_let-1]

print(result)
"""

# TASK_11.3.9
"""
На вход программе подается натуральное число nn, а затем nn строк. Напишите программу, 
которая создает список из символов всех строк, а затем выводит его.

row_count = int(input())
tot_list = []

for _ in range(row_count):
    tot_list.extend(input())
print(tot_list)
"""

