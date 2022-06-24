class Vector:
    def __init__(self, list1):
        self.coordinates = list(list1)

    def __str__(self):
        return str(tuple(self.coordinates)).replace(' ', '')

    def add(self, other):
        if len(self.coordinates) != len(other.coordinates):
            raise ValueError("Vectors must be the same length")
        return Vector([x + y for x, y in zip(self.coordinates, other.coordinates)])

    def subtract(self, other):
        if len(self.coordinates) != len(other.coordinates):
            raise ValueError("Vectors must be the same length")
        return Vector([x - y for x, y in zip(self.coordinates, other.coordinates)])

    def dot(self, other):
        if len(self.coordinates) != len(other.coordinates):
            raise ValueError("Vectors must be the same length")
        return sum(x * y for x, y in zip(self.coordinates, other.coordinates))

    def norm(self):
        return sum(el ** 2 for el in self.coordinates) ** 0.5

    def equals(self, other):
        return self.coordinates == other.coordinates
