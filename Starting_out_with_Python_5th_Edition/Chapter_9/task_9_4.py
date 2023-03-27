# Задание #4 к главе 9
# Текст задания находится в файле tasks_ru.txt
# Исходный файл для анализа 'dop\text_9_4.txt'
#
# Task #4 to chapter 9
# The text of the task is in the file tasks_en.txt
# Source file for analysis 'dop\text_9_4.txt'

# список спецсимволов которые будут удаляться из текста
MARKS = ':;!@#$%^&*()_-=+<>.,`*?—\\/"\n'


# Показать результат на экране
def show(unique_word):
    for word in unique_word:
        print(f'[#] > {word}')
    print(f'[#] > Всего найдено: {len(unique_word)} уникальных слов')


# Убираем все спец символы из строки и формируем множество для вывода на экран
def del_marks(unique_word, lines_in_file):
    for line in lines_in_file:
        for word in line.split():
            word = word.strip(MARKS)
            unique_word.add(word.lower())


# Читаем данные из файла
def get_data():
    with open('dop/text_9_4.txt', 'r', encoding='utf=8') as file:
        lines_in_file = file.readlines()
        return lines_in_file


def main():
    unique_word = set()
    lines_in_file = get_data()
    del_marks(unique_word, lines_in_file)
    show(unique_word)


if __name__ == '__main__':
    main()
