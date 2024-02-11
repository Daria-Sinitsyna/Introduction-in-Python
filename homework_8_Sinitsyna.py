"""
Программа должна выводить данные
Программа должна сохранять данные в текстовом файле
Пользователь может ввести одну из характеристик для поиска опред.записи


Дополнить телефонный справочник возможностью изменения и удаления данных.
Пользовательн также может ввести имя и фамилию, и Вы должны реализовать
функционал для изменения и удаления данных.
"""
from typing import List
import os


def read_file(file):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            return lines
    except FileNotFoundError:
        print('Файла не существует. Сначала введите данные.\n')
        return []


def show_data(data: list):
    # data = read_file(file)
    for line in data:
        print(line)

    # try:
    #     with open('phone_book.txt', 'r', encoding='utf-8') as f:
    #         lines = f.readlines()
    #         for line in lines:
    #             print(line)
    # except FileNotFoundError:
    #     print('Файла не существует. Сначала введите данные.\n')


def input_data(file):
    print('Введите данные контакта: ')

    first_name = input('Введите имя: ')
    last_name = input('Введите фамилию: ')
    patronymic = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')

    with open(file, 'a', encoding='utf-8') as f:
        f.write(f'{first_name}, {last_name}, {patronymic}, {phone_number} \n')


def search_data(contacts: List[str]):  # list[str]
    print('Введите по какому параметру вы ходите искать контакт:')
    print('0 - имя')
    print('1 - фамилия')
    print('2 - отчество')
    print('3 - номер телефона\n')

    search_index = int(input())

    search_str = input('Введите параметр для поиска: ')
    founded = []

    for contact in contacts:
        if search_str.lower() in contact.split(', ')[search_index].lower():
            founded.append(contact)

    return founded


def change_data(file):
    print('Введите что вы хотите изменить:')
    print('0 - имя')
    print('1 - фамилия')
    print('2 - отчество')
    print('3 - номер телефона\n')

    change_index = int(input())
    search_str = input('Введите что хотите изменить: ')
    new_str = input('Введите на что хотите поменять: ')

    with open(file, 'r', encoding='utf-8') as f:
        old_data = f.read()

    new_data = old_data.replace(search_str, new_str)
    # print(new_data)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(new_data)

    return file


def delete_data(contacts, file):
    print('Введите параметр контакта, по которому будете искать контакт: ')
    print('0 - имя')
    print('1 - фамилия')
    print('2 - отчество')
    print('3 - номер телефона\n')

    delete_index = int(input())
    search_str = input('Введите значение параметра: ')

    new_data = []

    for contact in contacts:
        if search_str.lower() not in contact.split(', ')[delete_index].lower():
            new_data.append(contact)

    # print(new_data)

    with open(file, 'w', encoding='utf-8') as f:
        f.writelines(new_data)

    return file


def delete_data_more_param(contacts, file):
    print('Введите сочетания парметров поиска: ИФ\n ФИО \n ФИО и номер телефона \n можно поставить прочерк, если информация отсутствует')
    print('0 - имя')
    print('1 - фамилия')
    print('2 - отчество')
    print('3 - номер телефона\n')

    delete_index1 = 1
    delete_index2 = 2
    delete_index3 = 3
    delete_index4 = 4

    search_str1 = input('Введите имя: ')
    search_str2 = input('Введите фамилию: ')
    search_str3 = input('Введите отчество: ')
    search_str4 = input('Введите номер телефона: ')

    new_data = []

    for contact in contacts:
        if (search_str1.lower() not in contact.split(', ')[delete_index1].lower()) and (search_str2.lower() not in contact.split(', ')[delete_index2].lower()):
            # print('++++')
            new_data.append(contact)
        # elif (search_str1.lower() not in contact.split(', ')[delete_index1].lower()) and (search_str2.lower() not in contact.split(', ')[delete_index2].lower()) and (search_str3.lower() not in contact.split(', ')[delete_index3].lower()):
        #     new_data.append(contact)
        # elif (search_str1.lower() not in contact.split(', ')[delete_index1].lower()) and (search_str2.lower() not in contact.split(', ')[delete_index2].lower()) and (search_str3.lower() not in contact.split(', ')[delete_index3].lower()) and (search_str4.lower() not in contact.split(', ')[delete_index4].lower()):
        #     new_data.append(contact)

    # print(new_data)

    with open(file, 'w', encoding='utf-8') as f:
        f.writelines(new_data)

    return file


def main():
    file_name = 'phone_book.txt'
    flag = True

    while flag:
        print('0 - выход')
        print('1 - запись в файл')
        print('2 - показать записи')
        print('3 - поиск данных')
        print('4 - изменение данных')
        print('5 - удаление контакта')
        print('6 - удаление по нескольким параметрам\n')

        answer = input('Выберите действие: \n ')
        if answer == '0':
            flag = False
        elif answer == '1':
            input_data(file_name)
        elif answer == '2':
            data = read_file(file_name)
            show_data(data)
        elif answer == '3':
            data = read_file(file_name)
            founded_data = search_data(data)
            show_data(founded_data)
        elif answer == '4':
            change_data(file_name)
        elif answer == '5':
            data = read_file(file_name)
            delete_data(data, file_name)
        elif answer == '6':
            data = read_file(file_name)
            delete_data_more_param(data, file_name)


if __name__ == '__main__':
    main()
