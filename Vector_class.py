class Vector:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        return "(" + ",".join(str(i) for i in self.my_list) + ")"

    def add(self, other):
        if len(self.my_list) != len(other.my_list):
            raise ValueError("Vectors must be the same length")
        return Vector([el[0] + el[1] for el in zip(self.my_list, other.my_list)])

    def subtract(self, other):
        if len(self.my_list) != len(other.my_list):
            raise ValueError("Vectors must be the same length")
        return Vector([el[0] - el[1] for el in zip(self.my_list, other.my_list)])

    def dot(self, other):
        if len(self.my_list) != len(other.my_list):
            raise ValueError("Vectors must be the same length")
        return sum(el[0] * el[1] for el in zip(self.my_list, other.my_list))

    def norm(self):
        return sum([el ** 2 for el in self.my_list]) ** 0.5

    def equals(self, other):
        if len(self.my_list) != len(other.my_list):
            return False
        for el in zip(self.my_list, other.my_list):
            if el[0] != el[1]:
                return False
        return True
