class TwoDvector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j")


class ThreeDvector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k")


a = TwoDvector(1, 2)
a.show()

b = ThreeDvector(5, 2, 3)
b.show()
