class Figure:
    NAME = None

    @property
    def area(self) -> float:
        return False

    def perimeter(self) -> float:
        return False

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise AttributeError('Неверная фигура')
        return self.area + figure.area
