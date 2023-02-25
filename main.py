class Vector:
    """Класс в котором производятся действия с векторами"""

    def __init__(self, massive):
        """Инициализация вектора"""
        self.massive = massive

    def __str__(self):
        """Возвращение строкой векторов"""
        string = '('
        for i in range(len(self.massive)):
            string = string + str(self.massive[i]) + ','
        return string[:-1] + ')'

    def push(self, val):
        """Добавление значения в массив"""
        self.massive.append(val)

    def equals(self, other):
        """Проверка на одинаковость векторов"""
        if len(self.massive) != len(other.massive):
            return False
        for i in range(0, len(self.massive)):
            if self.massive[i] != other.massive[i]:
                return False
        return True

    def add(self, n):
        """Функция для сложения векторов"""
        if len(self.massive) != len(n.massive):
            return False
        add_vec = Vector([])
        for i in range(len(self.massive)):
            add_vec.push(self.massive[i] + n.massive[i])
        return add_vec

    def subtract(self, n):
        """Фунцкия для вычитания векторов"""
        if len(self.massive) != len(n.massive):
            return 'exception'
        subtract_vec = Vector([])
        for i in range(len(self.massive)):
            subtract_vec.push(self.massive[i] - n.massive[i])
        return subtract_vec

    def dot(self, n):
        """Умножение векторов"""
        if len(self.massive) != len(n.massive):
            return 'exception'
        dot_vec = 0
        for i in range(len(self.massive)):
            dot_vec += self.massive[i] * n.massive[i]
        return dot_vec

    def norm(self):
        """Нахождение длины вектора"""
        nor = 0
        for i in self.massive:
            nor += i ** 2
        return nor ** 0.5


