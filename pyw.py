
# def hide_card(card_number):

#     return '*' * 12 + ''.join(card_number).replace(' ', '')[-4:]


# card = '9056781234561256'

# print(hide_card(card))


# def same_parity(numbers):

#     if numbers == []:
#         return []

#     if numbers[0] % 2 == 0:
#         return [i for i in numbers if i % 2 == 0]
#     else:
#         return [ i for i in numbers if i % 2 != 0]


# print(same_parity([]))


# def is_valid(string):

#     if not string:
#         return False

#     if len(string) in [4, 5, 6] and string.isdigit():
#         return True
#     return False


# print(is_valid(''))


# def print_given(*args, **kwargs):

#     for i in args:
#         print(i, type(i))

#     for key, value in sorted(kwargs.items()):
#         print(key, value, type(value))

# print_given(b=2, d=4, c=3, a=1)


# def convert(string):

#     low_txt = []
#     uper_txt = []


#     for i in string:
#         if i.isalpha() and i.islower():
#             low_txt.append(i)
#         elif i.isalpha() and i.isupper():
#             uper_txt.append(i)

#     if len(low_txt) >= len(uper_txt):
#         return string.lower()
#     else:
#         return string.upper()


# # TESTS - просто размести их под кодом
# assert (convert('BEEgeek')) == 'beegeek'
# assert (convert('pyTHON')) == 'PYTHON'
# assert (convert('pi31415!')) == 'pi31415!'
# assert (convert('ABCDEF')) == 'ABCDEF'
# assert (convert('abcdef')) == 'abcdef'
# assert (convert('12345!?')) == '12345!?'
# assert (convert('PI31415!')) == 'PI31415!'
# assert (convert('ABCdef')) == 'abcdef'
# assert (convert('ABCdef123')) == 'abcdef123'
# assert (convert('AbCdEf12345')) == 'abcdef12345'
# assert (convert('dEfAbC')) == 'defabc'
# print('TESTS_OK')  # если распечатался TESTS_OK, значит все ОК )


# def filter_anagrams(word, words):

#     sort_word = sorted(word)

#     return [ i for i in words if sorted(i) == sort_word]


# print(filter_anagrams('tommarvoloriddle', ['iamlordvoldemort', 'iamdevolremort', 'mortmortmortmort', 'remortvolremort']))


# def likes(names):

#     leng_name = len(names)


#     if leng_name == 0:
#         return 'Никто не оценил данную запись'
#     if leng_name == 1:
#         return f'{names[0]} оценил(а) данную запись'
#     if leng_name == 2:
#         return f'{names[0]} и {names[1]} оценили данную запись'

#     if leng_name == 3:
#         return f'{names[0]}, {names[1]} и {names[2]} оценили данную запись'
#     if leng_name >= 4:
#         return f'{names[0]}, {names[1]} и {str(leng_name -2)} других оценили данную запись'

# # TESTS - просто размести их под кодом

# assert (likes(['Дима', 'Алиса'])) == 'Дима и Алиса оценили данную запись'
# assert (likes(['Эндрю', 'Тоби', 'Том'])) == 'Эндрю, Тоби и Том оценили данную запись'
# assert (likes([])) == 'Никто не оценил данную запись'
# assert (likes(['Том'])) == 'Том оценил(а) данную запись'
# assert (likes(['Эндрю', 'Тоби', 'Том', 'Артур'])) == 'Эндрю, Тоби и 2 других оценили данную запись'
# assert (likes(['Эндрю', 'Тоби', 'Том', 'Артур', 'Тимур'])) == 'Эндрю, Тоби и 3 других оценили данную запись'
# assert (likes(['Артур', 'Тимур', 'Руслан', 'Анри', 'Дима', 'Алиса'])) == 'Артур, Тимур и 4 других оценили данную запись'
# names = [str(i) * 3 for i in range(100)]
# assert (likes(names)) == '000, 111 и 98 других оценили данную запись'

# print('TESTS_OK')  # если распечатался TESTS_OK, значит все ОК )


# def index_of_nearest(numbers, number):
#     if not numbers:
#         return -1

#     min_diff = float('inf')
#     nearest_index = -1

#     for i, num in enumerate(numbers):
#         diff = abs(num - number)
#         if diff == 0:
#             return i
#         elif diff < min_diff:
#             min_diff = diff
#             nearest_index = i

#     return nearest_index


# print(index_of_nearest([], 17)) #-1
# print(index_of_nearest([7, 13, 3, 5, 18], 0)) #2
# print(index_of_nearest([9, 5, 3, 2, 11], 4)) #1
# print(index_of_nearest([7, 5, 4, 4, 3], 4)) #2
# print(index_of_nearest([6, 100, 101, 2], 4)) #0
# print(index_of_nearest([734234423423423, 5343423423546463423, 934234423423423423, -1], 0)) #3
# print(index_of_nearest([1, 14, 100, 65, 6], 5)) #4
# print(index_of_nearest([10, 164, 100, 265, 16], 8)) #0
# print(index_of_nearest([10, 99, 0, -12, 16], -9)) #3
# print(index_of_nearest([1, 1, 1, 1, 1], 1)) #0


# def spell(*args):
#     res = {}

#     words = [ arg .lower() for arg in args]

#     for work in words:
#         first_leter = work[0]
#         max_leng = max(len(work), res.get(first_leter, 0))
#         res[first_leter] = max_leng
#     return res


# words = ['Россия', 'Австрия', 'Австралия', 'РумыниЯ', 'Украина', 'КИТай', 'УЗБЕКИСТАН']

# print(spell(*words))

# def choose_plural(amount, declensions):
#     # Проверяем последние две цифры
#     last_two_digits = amount % 100
#     # Проверяем последние цифры числа
#     last_digit = amount % 10

#     # Если последние две цифры числа от 11 до 14, используем третью форму
#     if 11 <= last_two_digits <= 14:
#         return f"{amount} {declensions[2]}"
#     # Если последняя цифра 1, используем первую форму
#     elif last_digit == 1:
#         return f"{amount} {declensions[0]}"
#     # Если последняя цифра 2, 3 или 4, используем вторую форму
#     elif 2 <= last_digit <= 4:
#         return f"{amount} {declensions[1]}"
#     # Во всех остальных случаях используем третью форму
#     else:
#         return f"{amount} {declensions[2]}"


# assert choose_plural(21, ('пример', 'примера', 'примеров')) == '21 пример'
# assert choose_plural(92, ('гвоздь', 'гвоздя', 'гвоздей')) == '92 гвоздя'
# assert choose_plural(8, ('яблоко', 'яблока', 'яблок')) == '8 яблок'
# assert choose_plural(111223, ('копейка', 'копейки', 'копеек')) == '111223 копейки'
# assert choose_plural(763434, ('рубль', 'рубля', 'рублей')) == '763434 рубля'
# assert choose_plural(512312, ('цент', 'цента', 'центов')) == '512312 центов'
# assert choose_plural(59, ('помидор', 'помидора', 'помидоров')) == '59 помидоров'
# assert choose_plural(23424157, ('огурец', 'огурца', 'огурцов')) == '23424157 огурцов'
# assert choose_plural(240, ('курица', 'курицы', 'куриц')) == '240 куриц'
# assert choose_plural(49324, ('плюмбус', 'плюмбуса', 'плюмбусов')) == '49324 плюмбуса'
# assert choose_plural(505, ('утка', 'утки', 'уток')) == '505 уток'
# assert choose_plural(666, ('шкаф', 'шкафа', 'шкафов')) == '666 шкафов'
# assert choose_plural(11, ('стул', 'стула', 'стульев')) == '11 стульев'
# assert choose_plural(3458438435812, ('доллар', 'доллара', 'долларов')) == '3458438435812 долларов'
# assert choose_plural(2, ('пример', 'примера', 'примеров')) == '2 примера'
# assert choose_plural(111, ('пример', 'примера', 'примеров')) == '111 примеров'
# assert choose_plural(1223123111, ('пример', 'примера', 'примеров')) == '1223123111 примеров'

# print('TESTS_OK')  # если распечатался TESTS_OK, значит все ОК


# def get_biggest(numbers):
#     if not numbers:
#         return -1

#     # Преобразуем числа в строки для удобства сортировки
#     numbers = list(map(str, numbers))

#     # Сортируем числа по правилам: сравниваем по (x+y) и (y+x)
#     numbers.sort(key=lambda x: x*10, reverse=True)

#     # Соединяем отсортированные строки и преобразуем обратно в число
#     result = ''.join(numbers)

#     # Преобразуем в целое число и возвращаем
#     # Проверка, чтобы избежать случаев с ведущими нулями
#     return int(result)

# # TESTS
# assert get_biggest([1, 2, 3]) == 321
# assert get_biggest([61, 228, 9, 3, 11]) == 961322811
# assert get_biggest([7, 71, 72]) == 77271
# assert get_biggest([]) == -1
# assert get_biggest([0, 0, 0, 0, 0, 0]) == 0
# assert get_biggest([13, 221, 423, 53, 1, 2, 33, 58, 78554, 34, 65, 65, 2, 1]) == 78554656558534233433222211311
# assert get_biggest([7, 7, 7, 7, 7, 7, 7, 7, 7]) == 777777777
# assert get_biggest([62, 626]) == 62662
# assert get_biggest([9, 6, 3, 0, 3, 6, 9]) == 9966330
# assert get_biggest([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 9876543210
# assert get_biggest([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 987654321100
# assert get_biggest([1, 2, 3, 5, 4, 6, 7, 8, 9, 10]) == 98765432110
# assert get_biggest([3]) == 3

# print('TESTS_OK')  # если распечатался TESTS_OK, значит все ОК


# def home(d1, d2, d3):

#     res1 = d1 + d2 + d3

#     route2 = d2 + d3 + d1

#     route3 = 2 * (d1 + d2)

#     res = min(res1, route2, route3)

#     print(res)


# a, b, c = input().lower(), input().lower(), input().lower()

# text_rus = "АаВСсЕеНКМОоРрТХху"
# text_iup_en = 'AaBCcEeHKMOoPpTXxy'





# a, b, c = input(), input(), input()

# text_rus = "АаВСсЕеНКМОоРрТХху"
# ru = [ord(i) for i in text_rus]

# text_en = "AaBCcEeHKMOoPpTXxy"
# en = [ord(i) for i in text_en]



# if ord(a) in en and ord(b) in en and ord(c) in en:
#     print("en")
# elif ord(a) in ru and ord(b) in ru and ord(c) in ru:
#     print("ru")
# else:
#     print("mix")






# number = int(input())

# group = {}

# for i in range(1, number+1):
#     digit_gr = sum(int(value) for value in str(i))
#     if digit_gr not in group:
#         group[digit_gr] = []
#     else:
#         group[digit_gr].append(i)


# max_groups_size = max(len(groups) for groups in group.values())
# print(max_groups_size)






# # импортируем тип date из модуля datetime
# from datetime import date

# # создаем объект, соответсвующий дате урагана
# hurricane_andrew = date(1998, 3, 13)

# # выводим день недели
# print(hurricane_andrew.weekday())


# florida_hurricane_dates = []



# from collections import Counter


# number = 10, 20, 10, 20, 30, 20, 10, 20

# res = []
# count = Counter(number)
# for k, v in count.items():
#     if v > 1:
#         res.append(int(k))
#     else:
#         continue

# print(max(*(res)))



# // Дан массив чисел [1, 2, 3, 4, 2, 1, 3, 5, 0]
# // Дано искомое число, например 5. Нужно найти все возможные пары чисел, которые при сложении дадут искомое число. 
# // Эти пары чисел записать и сохранить в массив.


# num = [1, 2, 3, 4, 2, 1, 3, 5, 0]

# stok = 5
# res = {}

# for i in range(len(num)):
#     for j in range(i+1, len(num)):
#         if num[i] + num[j] == stok:
#             res[num[i]] = num[j]
            
# print(res)




