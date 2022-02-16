# Метод count()
# s = 'foo goo moo'
# print(s.count('oo'))
# print(s.count('oo', 0, 8))  # подсчет с 0 по 7 символ
#
# # Метод startswith()
# s = 'foobar'
# print(s.startswith('foo'))
# print(s.startswith('baz'))
#
# # Метод endswith()
# s = 'foobar'
# print(s.endswith('bar'))
# print(s.endswith('baz'))
#
# # Методы find(), rfind()
# s = 'foo bar foo baz foo qux'
# print(s.find('foo'))
# print(s.find('bar'))
# print(s.find('qu'))
# print(s.find('python'))

# Метод strip()
# s = '    foo bar foo baz foo qux      '
# print(s.strip())

# # Метод lstrip()
# s = '     foo bar foo baz foo qux      '
# print(s.lstrip())
#
# # Метод rstrip()
# s = '      foo bar foo baz foo qux      '
# print(s.rstrip())

# Метод replace()
s = 'foo bar foo baz foo qux'
print(s.replace('foo', 'grault'))

# Метод replace() может принимать опциональный третий аргумент <count>,  который определяет количество замен.
s = 'foo bar foo baz foo qux'
print(s.replace('foo', 'grault', 2))


