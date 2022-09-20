class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def adition(self):
        print(self.a + self.b)

    def multiplication(self):
        print(self.a * self.b)

    def division(self):
        print(self.a / self.b)

    def subtraction(self):
        print(self.a - self.b)

# Тут я слюлил, но оставил прошлое решение. Оно ведь тоже правильно?
def math(a, b):
    yield a + b
    yield a - b
    yield a * b
    yield a / b


math1 = math(99, 11)

for i in math1:
    print(i)
