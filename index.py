# -*- coding: utf-8 -*-

class Building:
    """
    Возвращает новый экземпляр класса Building (класса здания) с юго-западным углом расположенным в точке с координатами [south, west],
    длиной стен, идущих по направлению "восток-запад" - width_WE, длиной стен, идущих по направлению "север-юг" - width_NS, и высотой height.
    Параметр height является положительным числом со значением по умолчанию равным 10.
    """
    def __init__(self, south, west, width_WE, width_NS, height=10):
        self.south = south
        self.west = west
        self.width_WE = width_WE
        self.width_NS = width_NS
        self.height = height

    def corners(self):
        """
        Возвращает словарь (dictionary) с координатами углов здания. Словарь имеет следующие ключи: "north-west", "north-east", "south-west", "south-east".
        Значениями являются списки (list) или кортежи (tuples) с двумя числовыми значениями.
        """
        return {"north-west": [self.south + self.width_NS, self.west], "north-east": [self.south + self.width_NS, self.west + self.width_WE], "south-west": [self.south, self.west], "south-east": [self.south, self.west + self.width_WE]}

    def area(self):
        """Возвращает площадь основания здания. """
        return self.width_NS * self.width_WE

    def volume(self):
        """ Возвращает объем здания."""
        return self.width_NS * self.width_WE * self.height

    def __repr__(self):
        """
        Это представление объекта Building в виде текстовой строки.
        Метод используется в функциях print или str (преобразование в строку). Возвращает строку следующего вида:
        "Building({south}, {west}, {width_we}, {width_ns}, {height})"
        """
        return 'Building({%(south)s}, {%(west)f}, {%(width_we)f}, {%(width_ns)f}, {%(height)f})' % {"south": self.south, "west": self.west, "width_we": self.width_WE, "width_ns": self.width_NS, "height": self.height}


# функция алгоритма последствий выполнения кода
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def json_dict(d):
        return dict((k, list(v)) for k, v in d.items())

    b = Building(1, 2, 2, 3)
    b2 = Building(1, 2, 2, 3, 5)
    assert json_dict(b.corners()) == {'north-east': [4, 4], 'south-east': [1, 4],
                                      'south-west': [1, 2], 'north-west': [4, 2]}, "Corners"
    assert b.area() == 6, "Area"
    assert b.volume() == 60, "Volume"
    assert b2.volume() == 30, "Volume2"
    assert str(b) == "Building(1, 2, 2, 3, 10)", "String"