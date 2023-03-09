# Класс Player
# содержит информацию об игроках участвующих в викторине

class Player:

    def __init__(self, name):
        self.__name = name
        self.__score = 0

    def add_point(self):
        self.__score += 1

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score
