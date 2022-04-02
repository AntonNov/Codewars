class Vector:
    def __init__(self, list1):
        self.list1 = list1

    def __str__(self):
        return "({})".format(",".join(str(el) for el in self.list1))

    def add(self, other):
        if len(self.list1) != len(other.list1):
            raise ValueError("Vectors must be the same length")
        return Vector([el[0] + el[1] for el in zip(self.list1, other.list1)])

    def subtract(self, other):
        if len(self.list1) != len(other.list1):
            raise ValueError("Vectors must be the same length")
        return Vector([el[0] - el[1] for el in zip(self.list1, other.list1)])

    def dot(self, other):
        if len(self.list1) != len(other.list1):
            raise ValueError("Vectors must be the same length")
        return sum(el[0] * el[1] for el in zip(self.list1, other.list1))

    def norm(self):
        return sum(el ** 2 for el in self.list1) ** 0.5

    def equals(self, other):
        if len(self.list1) != len(other.list1):
            return False
        for el in zip(self.list1, other.list1):
            if el[0] != el[1]:
                return False
        return True
