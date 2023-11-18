# import sys

# # readline работает как input, только без подсказки
# # rstrip удаляет каретку в вводе
# name = sys.stdin.readline().rstrip()
# print(f'Здарова, {name}')


# jopa = [1, 2, 2, 2, 23, 3, 4, 5, 4, 6]

# for i in range(len(jopa)):
#     # print(i)
#     print(jopa[i])


# with open('input.txt', 'r') as file_in:
#     lines = file_in.readlines()

# summa = 0
# for i in lines:
#     summa += int(i)

# with open('output.txt', 'w') as file_out:
#     file_out.write(str(summa))


# def find_element(sorted_numbers, element):
#     """Находит индекс element в отсортированном списке sorted_numbers."""
#     # Левая граница (левый индекс) рассматриваемого набора элементов.
#     # В начале работы она равна индексу первого элемента в списке - нулю.
#     left = 0
#     # Правая граница (правый индекс) рассматриваемого набора элементов.
#     # В начале работы она равна индексу последнего элемента в списке.
#     right = len(sorted_numbers) - 1
#     # Пока левая граница меньше правой или равна ей:
#     while left <= right:
#         # Находим в наборе элементов индекс среднего элемента.
#         mid = (left + right) // 2
#         # Если элемент с этим индексом равен искомому, возвращаем его индекс.
#         if sorted_numbers[mid] == element:
#             return mid
#         # Если средний элемент меньше искомого...
#         if sorted_numbers[mid] < element:
#             # ...то изменяем левую границу поиска:
#             left = mid + 1
#         # Если средний элемент больше искомого...
#         else:
#             # ...то изменяем правую границу поиска:
#             right = mid - 1
#     # Если левая граница оказалась больше правой,
#     # значит, элемент не найден. Возвращаем None.
#     return None

# array = [6, 5, 3, 1, 8, 7, 2, 4]


# def bubble_sort(array):

#     for i in range(len(array) - 1, 0, -1):
#         swapped = False
 
#         for item_index in range(array[i]):
#             if array[item_index] > array[item_index + 1]:
#                 array[item_index], array[item_index + 1] = (
#                     array[item_index + 1], array[item_index])

#                 swapped = True

#         if not swapped:
#             break

#     return array


# print(bubble_sort(array))


# import random


# lenght_of_array = 10
# random_array = [random.randint(1, 100) for i in range(lenght_of_array)]

# print(random_array)


# def bubble_sort(random_array):
#     for last_index in range(len(random_array) - 1, 0, -1):
#         swapped = False

#         for item_index in range(last_index):
#             if random_array[item_index] > random_array[item_index + 1]:
#                 random_array[item_index], random_array[item_index + 1] = (
#                     random_array[item_index + 1], random_array[item_index])

#                 swapped = True

#         if not swapped:
#             break

#     return random_array


# binar_target = random.choice(random_array)


# def binar_search(random_array, binar_target):
#     left = 0
#     right = len(random_array) - 1

#     while left <= right:
#         mid = left + right // 2

#         if binar_target > random_array[mid]:
#             left = mid - 1
#         if binar_target == random_array[mid]:
#             return (f'Его позиция - {mid}')
#         else:
#             right = mid + 1

#     return None


# print(bubble_sort(random_array))
# print(f'Рандомный элемент - {binar_target}')
# print(binar_search(random_array, binar_target))

# import sys

# len_of_array = int(input())
# array = sys.stdin.readline().strip()

# array_clear = array.split()

# for i in range(len_of_array):
#     if i != '_':
#         count_of_num = array_clear.count(array_clear[i])
#         if count_of_num >= 2:
#             for j in range(count_of_num - 1):
#                 array_clear.remove(array_clear[i])
#                 array_clear.append('_')

# stroka = ' '.join(array_clear)
# print(stroka)


# def remove_duplicates(arr):
#     unique_elements = []
#     duplicates = []
    
#     for element in arr:
#         if element not in unique_elements:
#             unique_elements.append(element)
#         else:
#             duplicates.append('_')
     
#     result = sorted(unique_elements) + duplicates
#     return ' '.join(map(str, result))

# n = int(input())
# arr = list(map(int, input().split()))
# print(remove_duplicates(arr))

# import sys
# array = sys.stdin.readline().strip()
# target = int(input())
# array = array.split()
# array_clear = []

# for i in array:
#     array_clear.append(int(i))


# def index_define(array_clear, target):
#     if target in array_clear:
#         return array_clear.index(target)
#     else:
#         for i in array_clear:
#             if target > i:
#                 continue
#             else:
#                 return array_clear.index(i)
#         return len(array_clear)


# print(index_define(array_clear, target))

# def list_superset(list_set_1, list_set_2):
#     superset = []
#     for _ in list_set_1:
#         if _ in list_set_2:
#             superset.append(_)
#     if len(list_set_1) > len(list_set_2):
#         len_list = list_set_1
#     elif len(list_set_1) < len(list_set_2):
#         len_list = list_set_2
#     elif list_set_1 == superset:
#         return 'Наборы равны'
#     if len(superset) > 1 and len(list_set_1) > len(list_set_2):
#         return f'Набор {list_set_1} - супермножество.'
#     elif len(superset) > 1 and len(list_set_1) < len(list_set_2):
#         return f'Набор {list_set_2} - супермножество.'
#     else:
#         return 'Супермножество не обнаружено.'


# def list_superset(list1, list2):
#     set1 = set(list1)
#     set2 = set(list2)
    
#     if set1.issuperset(set2):
#         return f"Набор {set1} - супермножество."
#     elif set2.issuperset(set1):
#         return f"Набор {set2} - супермножество."
#     elif set1 == set2:
#         return "Наборы равны."
#     else:
#         return "Супермножество не обнаружено."


# list_set_1 = [1, 3, 5, 7]
# list_set_2 = [3, 5]
# list_set_3 = [5, 3, 7, 1]
# list_set_4 = [5, 6]

# print(list_superset(list_set_1, list_set_2))
# print(list_superset(list_set_2, list_set_3))
# print(list_superset(list_set_1, list_set_3))
# print(list_superset(list_set_2, list_set_4))

# import time

# # Количество элементов в массивах.
# elements_count = 100000000

# # Эксперимент 1
# # Засекаем время начала.
# start_time = time.time()
# # Резервируем место в памяти на 10 млн элементов.
# # При этом ОС забронирует чуть больший размер.
# data1 = [None] * elements_count
# for data_index in range(elements_count):
#     # Заполняем элементы списка по индексу.
#     data1[data_index] = f'Some new value {data_index}'
# # Печатаем время выполнения.
# print(
#     'Создание списка с 10 млн пустых элементов и его заполнение:', 
#     time.time() - start_time
# )

# # Эксперимент 2
# # Засекаем новое время.
# start_time = time.time()
# # Объявляем пустой список; ОС не знает его ожидаемый размер.
# data2 = []
# for data_index in range(elements_count):
#     # Добавляем новые элементы в конец списка.
#     data2.append(f'some new value {data_index}')
# # Печатаем время выполнения.
# print(
#     'Создание пустого списка и добавление в него 10 млн элементов:', 
#     time.time() - start_time
# ) 


# def valid_mountain_array(array) -> bool:
#     if len(array) < 3:
#         return False

#     index_of_max = array.index(max(array))

#     for i in range(index_of_max):
#         if array[i] >= array[i + 1]:
#             return False

#     for i in range(index_of_max, len(array) - 1):
#         if array[i] <= array[i + 1]:
#             return False

#     if max(array) == array[0] or max(array) == array[-1]:
#         return False

#     return True


# array = list(map(int, input().split()))
# print(valid_mountain_array(array))


# import hashlib


# class MarsURLEncoder:

#     def __init__(self, url_dict: dict):
#         self.url_dict = {}
#         self.url = 'https://ma.rs/'

#     def encode(self, long_url):
#         """Кодирует длинную ссылку в короткую вида https://ma.rs/X7NYIol."""
#         self.key = hashlib.md5(long_url.encode('utf-8')).hexdigest()[:7]
#         self.url_dict[self.key] = long_url
#         return self.url + self.key

#     def decode(self, short_url):
#         """Декодирует короткую ссылку вида https://ma.rs/X7NYIol в исходную."""
#         key = short_url.replace(self.url, '')
#         return self.url_dict[key]


# def find_two_indexes(data, expected_sum):
#     index_tuple = ()
#     for i in range(len(data)):
#         for j in range(i + 1):
#             if data[i] + data[j] == expected_sum and i != j:
#                 index_tuple = (j, i)
#                 return index_tuple
#     return None


# if __name__ == '__main__':
#     data = [1, 2, 3, 4, 5, 6, 7, 11]
#     expected_sum = 10
#     print(find_two_indexes(data, expected_sum))


# def minimal(array):
#     result_str = ''
#     for i in array:
#         count = 0
#         for j in array:
#             if i > j and i != j:
#                 count += 1
#         result_str += str(count)
#     return ' '.join(result_str)


# array = list(map(int, input().split()))
# print(minimal(array))

# import sys


# def is_correct_bracket_seq(brackets):
#     left_pointer = 0
#     right_pointer = len(brackets) - 1
#     brac_dict = {
#         '(': ')',
#         '{': '}',
#         '[': ']'
#     }

#     if len(brackets) % 2 != 0:
#         return False

#     while left_pointer < right_pointer:
#         if (brackets[left_pointer] in brac_dict.keys() and
#                 brackets[right_pointer] == brac_dict[brackets[left_pointer]]):
#             left_pointer += 1
#             right_pointer -= 1
#         else:
#             return False
#     return True


# brackets = sys.stdin.readline().strip()
# print(is_correct_bracket_seq(brackets))


# def is_correct_bracket_seq(brackets):
#     open_brackets = ['(', '[', '{']
#     close_brackets = [')', ']', '}']
#     stack = []

#     if len(brackets) % 2 != 0:
#         return False

#     for bracket in brackets:
#         if bracket in open_brackets:
#             stack.append(bracket)
#         elif bracket in close_brackets:
#             if not stack:
#                 return False
#             open_bracket = stack.pop()
#             if open_brackets.index(open_bracket) != close_brackets.index(bracket):
#                 return False

#     if stack:
#         return False

#     return True


# brackets = sys.stdin.readline().strip()
# print(is_correct_bracket_seq(brackets))

# import sys


# def delivery_service(input_array: list, limit) -> int:
#     if len(input_array) < 1:
#         raise ValueError('Incorrect data')

#     if min(input_array) >= limit:
#         return len(input_array)

#     sorted_array: list[int] = sorted(input_array)
#     left_index = 0
#     right_index = len(sorted_array) - 1
#     count: int = 0
#     while left_index <= right_index:
#         if input_array[left_index] + input_array[right_index] <= limit:
#             left_index += 1
#             right_index -= 1
#         else:
#             right_index -= 1
#             count += 1
#     return count


# input_array = list(map(int, input().split()))
# limit = int(input())
# print(delivery_service(input_array, limit))


# def delivery_service(input_array, limit):
#     if len(input_array) < 1:
#         raise ValueError('Incorrect data')

#     if min(input_array) >= limit:
#         return len(input_array)

#     count_of_platforms = sum(input_array) // limit



# input_array = list(map(int, input().split()))
# limit = int(input())
# print(delivery_service(input_array, limit))

#

from typing import List


def delivery_service(weights: List[int], limit: int) -> int:
    if len(weights) < 1:
        raise ValueError('Incorrect data')

    if min(weights) >= limit:
        return len(weights)

    weights.sort()
    count: int = 0
    left: int = 0
    right: int = len(weights) - 1

    while left <= right:
        if weights[left] + weights[right] <= limit:
            left += 1
            right -= 1
        else:
            right -= 1
        count += 1

    return count


weights = list(map(int, input().split()))
limit = int(input())

print(delivery_service(weights, limit))








































































































