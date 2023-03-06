# Задание #3 к главе 10
# Текст задания находится в файле tasks_ru.txt
# Описание класса Pet находится в файле 'm_information_10_3.py':
#
# Task #3 to chapter 10
# The text of the task is in the file tasks_en.txt
# Описание класса Pet находится в файле 'm_information_10_3.py':

# Импортируем модуль и даем ему псевдоним 'car'
import m_information_10_3 as information


def main():
    my_info = information.information('WarFish', 'Russia, Astrakhan', 39, 79997249999)
    friend1 = information.information('VeVeshnik', 'Russia, Mosсow', 45, 79997240001)
    friend2 = information.information('Karlson', 'Russia, Astrakhan', 54, 79997240002)


if __name__ == '__main__':
    main()
