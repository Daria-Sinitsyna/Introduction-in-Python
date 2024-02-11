"""
Напишите функцию print_operation_table(operation, num_rows, num_columns), 
которая принимает в качестве аргумента функцию, вычисляющую элемент по 
номеру строки и столбца. По умолчанию номер столбца и строки = 9.
Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, 
которые должны быть распечатаны.
Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
Если строк меньше двух, выдайте текст
ОШИБКА! Размерности таблицы должны быть больше 2!.
Примечание: бинарной операцией называется любая операция, у которой 
ровно два аргумента, как, например, у операции умножения.

Между элементами должен быть 1 пробел, в конце строки пробел не нужен.

На входе:
print_operation_table(lambda x, y: x * y, 3, 3)

На выходе:
1 2 3
2 4 6 
3 6 9
"""


def print_operation_table(operation, num_rows=9, num_columns=9):
    if num_rows < 2:
        return print('ОШИБКА! Размерности таблицы должны быть больше 2!')

    res = [[operation(i, j) for j in range(1, num_columns + 1)]
           for i in range(1, num_rows + 1)]
    for item in res:
        print(*[f'{x}' for x in item])


print_operation_table(lambda x, y: x * y)

# def print_operation_table(operation, num_rows=9, num_columns=9):
#     result = []
#     if num_rows < 2 or num_columns < 2:
#         print('ОШИБКА! Размерности таблицы должны быть больше 2!')
#     else:
#         for i in range(1, num_rows + 1):
#             for j in range(1, num_columns + 1):
#                 if j != num_columns :
#                     result.append(f'{operation(i, j)} ')
#                 else:
#                     result.append(operation(i, j))
#             result.append('\n')
#         print(''.join([str(i) for i in result[:len(result) - 1]]))


"""
Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
Поскольку разобраться в его кричалках не настолько просто, 
насколько легко он их придумывает, Вам стоит написать программу.

Винни-Пух считает, что ритм есть, если число слогов 
(т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
Фраза может состоять из одного слова, если во фразе несколько слов, 
то они разделяются дефисами.
Фразы отделяются друг от друга пробелами.

Стихотворение  Винни-Пух передаст вам автоматически в переменную 
stroka в виде строки. В ответе напишите Парам пам-пам, если с 
ритмом все в порядке и Пам парам, если с ритмом все не в порядке.
Если фраза только одна, то ритм определить не получится 
и необходимо вывести: Количество фраз должно быть больше одной!.

На входе:
stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'

На выходе:
Парам пам-пам
"""


def ritm(song: str):
    phrase = list(song.split())

    if len(phrase) < 2:
        print('Количество фраз должно быть больше одной!')
        return

    vowels_in_phrase = []

    for word in phrase:
        vowels = 0
        for item in word:
            if item in 'аоуыэеёиюя':
                vowels += 1

        vowels_in_phrase.append(vowels)

    if len(vowels_in_phrase) == vowels_in_phrase.count(vowels_in_phrase[0]):
        print('Парам пам-пам')
    else:
        print('Пам парам')
    return


stroka = 'пара'
# worlds = stroka.split()
# print(len(worlds))

ritm(stroka)
