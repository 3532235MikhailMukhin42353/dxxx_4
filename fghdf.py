# ЗАДАЧА 22
import random

number_one = int(input('Введите первое кличество цифр: '))
number_two = int(input('Введите второе кличество цифр: '))

my_list_one = [random.randint(0,20) for _ in range(number_one)]
my_list_two = [random.randint(0,20) for _ in range(number_two)]
print(f'Первый список чисел = {my_list_one}')
print(f'Второй список чисел = {my_list_two}')
my_list_one.sort()
print(f'Первый отсортированный список: {my_list_one}')
my_list_two.sort()
print(f'Второй отсортированный список: {my_list_two}')

itog = list(set(my_list_one) & set(my_list_two))
print(itog)