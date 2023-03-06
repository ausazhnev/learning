# Константа для ставки налога с продаж
TAX_RATE = 0.05

# Класс ServiceQuote

class ServiceQuote:
    def __init__(self, pcharge, lchrge):
        self.__parts_charges = pcharge
        self.__lador_charges = lchrge

    def set_parts_charges(self, pcharge):
        self.__parts_charges = pcharge

    def set_lador_charges(self, lcharge):
        self.__lador_charges = lcharge

    def get_parts_charges(self):
        return self.__parts_charges

    def get_lador_charges(self):
        return self.__lador_charges

    def get_sales_tax(self):
        return self.__parts_charges * TAX_RATE

    def get_total_charges(self):
        return self.__lador_charges + self.__lador_charges + (self.__parts_charges * TAX_RATE)