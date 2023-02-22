# Задание #4 к главе 9
# Текст задания находится в файле tasks_ru.txt
# Исходный файл для анализа 'dop\text_9_4.txt'
#
# Task #4 to chapter 9
# The text of the task is in the file tasks_en.txt
# Source file for analysis 'dop\text_9_4.txt'

def show(unique_word):
    cout = 0
    for word in unique_word:
        print(f'[#] > {word}')
        cout += 1
    print(f'[#] > Всего найдено: {cout} уникальных слов')


def main():
    with open('dop\\text_9_4.txt', 'r', encoding='utf=8') as file:
        unique_word = set()
        data = file.readlines()
        for line in data:
            # убираем все '.'  из строки
            line = line.replace('.', '')
            # убираем все ','  из строки
            line = line.replace(',', '')
            # убираем все '!'  из строки
            line = line.replace('!', '')
            # убираем все '?'  из строки
            line = line.replace('?', '')
            line = line.strip('\n')
            # объединяем что позволяет исключить повторы слов
            unique_word = unique_word.union(line.split(' '))
        show(unique_word)


if __name__ == '__main__':
    main()
