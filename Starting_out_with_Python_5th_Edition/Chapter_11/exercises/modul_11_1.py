# Описание класса Employee (Сотрудник)
class Employee:
    # Если параметры не переданы, то устанавливаем значения None
    def __init__(self, name=None, id_num=None):
        self.__name = name
        self.__id_num = id_num

    def set_name(self, name):
        self.__name = name

    def get_name(self,):
        return self.__name

    def set_id_num(self, id_num):
        self.__id_num = id_num

    def get_id_num(self):
        return self.__id_num


# Описание класса ProductionWorker (Рабочий)
class ProductionWorker(Employee):
    def __init__(self, name=None, id_num=None, working_shift=None, hourly_rate=None):
        # Передаем атрибуты класса родителя в него
        super().__init__(name, id_num)
        self.__working_shift = working_shift
        self.__hourly_rate = hourly_rate

    def set_working_shift(self, working_shift):
        self.__working_shift = working_shift

    def set_hourly_rate(self, hourly_rate):
        self.__hourly_rate = hourly_rate

    def get_working_shift(self):
        return self.__working_shift

    def get_hourly_rate(self):
        return self.__hourly_rate

