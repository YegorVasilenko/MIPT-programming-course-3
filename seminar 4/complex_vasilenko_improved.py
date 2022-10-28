import math


# краткая справка по классу (будет дополняться)
# параметры
# _Re | вещественная часть алгебраической формы
# _Im | мнимая часть алгебраической формы
# _r  | модуль тригонометрической формы
# _phi| аргумент тригонометрической формы
# методы
# sum |
# substract |
# product |
# divide |
# get_exponential_form |
# get_algebraic_form |


class ComplexNumber:


    """
    организация класса
    """


    # инициализация проводится в алгебраической форме
    def __init__(self, Re, Im):
        self._Re = Re
        self._Im = Im
        self._r, self._phi = self.get_exponential_form()


    # простая доморощенная функция для отладки
    def error(self, msg):
        print(msg)
        exit(-1)


    """
    простые геттеры
    """


    def get_Re(self):
        return self._Re


    def get_Im(self):
        return self._Im

    def get_r(self):
        return self._r


    def get_phi(self):
        return self._phi


    """
    сеттеры, учитывающие все обновления
    """


    def set_Re(self, Re):
        self._Re = Re
        self._r, self._phi = self.get_exponential_form()


    def set_Im(self, Im):
        self._Im = Im
        self._r, self._phi = self.get_exponential_form()


    def set_r(self, r):
        self._r = r
        self._Re, self._Im = self.get_algebraic_form()


    def set_phi(self, phi):
        self._phi = phi
        self._Re, self._Im = self.get_algebraic_form()


    """
    переводы между алгебраической и тригонометрической формами
    """


    # из алгебраической формы вычисляет и возвращает
    # модуль и аргумент
    def get_exponential_form(self):
        r = math.sqrt(self._Re**2 + self._Im**2)
        x = self._Re
        y = self._Im

        if x > 0 and y == 0:
            phi = 0
        elif x > 0 and y > 0:
            phi = math.atan(abs(y/x))
        elif x == 0 and y > 0:
            phi = math.pi / 2
        elif x < 0 and y > 0:
            phi = math.pi - math.atan(abs(y/x))
        elif x < 0 and y == 0:
            phi = math.pi
        elif x < 0 and y < 0:
            phi = -math.pi + math.atan(abs(y/x))
        elif x == 0 and y < 0:
            phi = - math.pi / 2
        elif x > 0 and y < 0:
            phi = -math.atan(abs(y/x))

        return r, phi


    # из экспоненциальной формы вычисляет и возвращает
    # Re и Im части
    def get_algebraic_form(self):
        Re = self._r * math.cos(self._phi)
        Im = self._r * math.sin(self._phi)
        return Re, Im


    """
    методы-реализации арифметических операций
    """


    # возвращает новое комплексное число -- сумму данного числа и аргумента
    def sum(self, z):
        return ComplexNumber(self.get_Re() + z.get_Re(), self.get_Im() + z.get_Im())


    # возвращает новое комплексное число -- разность данного числа и аргумента,
    # аргумент вычитается из данного числа
    def substract(self, z):
        return ComplexNumber(self.get_Re() - z.get_Re(), self.get_Im() - z.get_Im())


    # возвращает новое комплексное число -- произведение данного числа и аргумента
    def product(self, z):
        return ComplexNumber(self.get_Re() * z.get_Re() - self.get_Im() * z.get_Im(),
                             self.get_Re() * z.get_Im() + self.get_Im() * z.get_Re())


    # возвращает новое комплексное число -- частное данного числа и аргумента,
    # аргумент вычитается из данного числа
    def divide(self, z):
        if z.get_Re() == 0 and z.get_Im() == 0:
            error("division by zero is impossible")
        a = self.get_Re()
        b = self.get_Im()
        c = z.get_Re()
        d = z.get_Im()
        return ComplexNumber((a*c+b*d)/(c**2+d**2), (b*c-a*d)/(c**2+d**2))


    """
    перегрузка операторов
    """


    def __add__(self, z):
        return self.sum(z)


    def __sub__(self, z):
        return self.substract(z)


    def __truediv__(self, z):
        return self.divide(z)


    def __mul__(self, z):
        return self.product(z)


    def __eq__(self, z):
        return self.get_Re() == z.get_Re() and self.get_Im() == z.get_Im()
