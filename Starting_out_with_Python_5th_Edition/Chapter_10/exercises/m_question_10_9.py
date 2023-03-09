# Класс Question

class Question:
    def __init__(self, discription, answer1, answer2, answer3, answer4, correct):
        self.__discription = discription
        self.__answer1 = answer1
        self.__answer2 = answer2
        self.__answer3 = answer3
        self.__answer4 = answer4
        self.__correct = correct

    def get_discription(self):
        return self.__discription

    def get_answer1(self):
        return self.__answer1

    def get_answer2(self):
        return self.__answer2

    def get_answer3(self):
        return self.__answer3

    def get_answer4(self):
        return self.__answer4

    def get_correct(self):
        return self.__correct

    # Добавлены, что бы были, но в работе они не используются
    def set_discription(self, discription):
        self.__discription = discription

    def set_answer1(self, answer1):
        self.__answer1 = answer1

    def set_answer2(self, answer2):
        self.__answer2 = answer2

    def set_answer3(self, answer3):
        self.__answer3 = answer3

    def set_answer4(self, answer4):
        self.__answer4 = answer4

    def set_correct(self, correct):
        self.__correct = correct
