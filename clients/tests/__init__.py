class Mult:
    def __init__(self, number):
        self.number = number

    def __call__(self, op):
        def wrapper(a, b):
            return op(a * self.number, b * self.number)
        return wrapper


@Mult(5)
def soma(a, b):
    return a + b


if __name__ == '__main__':
    assert soma(2, 3) == 25
