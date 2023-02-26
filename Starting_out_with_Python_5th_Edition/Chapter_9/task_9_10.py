# Задание #10 к главе 9
# Текст задания находится в файле tasks_ru.txt
# исходный файл для анализа 'dop/Kennedy.txt'
# файл в который записывается результат 'dop/index.txt'
#
# Task #10 to chapter 9
# The text of the task is in the file tasks_en.txt
# source file to analyze 'dop/Kennedy.txt'
# file where the result is written 'dop/index.txt'

F_NAME = 'Kennedy.txt'
F_INDEX = 'index.txt'


# Создаем требуемый словарь
def create_dict(all_data, dict_index):
    list_line = []
    set_word = set()
    # Создаем множество из слов файла (только уникальные значения)
    for line in all_data:
        for word in line.split():
            set_word.add(word)
    # Для всех элементов множества поверяем есть ли значение
    # в строке и обновляем значение ключа в словарь
    cout = 0
    for word in set_word:
        for line in all_data:
            cout += 1
            if word in line.split():
                list_line.append(cout)
        cout = 0
        dict_index[word] = list_line.copy()
        list_line.clear()


# Читаем содержимое исходного файла. dict_index - передается
# параметром и уйдет транзитом в функцию создания словаря
def read_file(dict_index):
    with open(f'dop//{F_NAME}', 'r', encoding='utf8') as r_file:
        all_data = r_file.readlines()
        create_dict(all_data, dict_index)


# Записываем содержимое полученного словаря в файл
def create_index_file(dict_index):
    with open(f'dop//{F_INDEX}', 'w', encoding='utf8') as w_file:
        # Для сортировки используем sorted, методы к словарю не применяем,
        # это позволяет в item получить только ключи
        for item in sorted(dict_index):
            # Убираем скобки при выводе, преобразовав список в строку
            # и убрав первый и последний символы
            w_file.write(f'{item} : {str(dict_index.get(item))[1:-1]}\n')


def main():
    dict_index = {}
    read_file(dict_index)
    create_index_file(dict_index)


if __name__ == '__main__':
    main()
