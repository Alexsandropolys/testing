import unittest

class Kek:

    def __init__(self, name, rofl):
        self.name = name
        self.rofk = rofl

    def get_rofl_of_old_kek(self):
        return self.rofl / 2

    def is_equal_name(self, name):
        return self.name == name


class KekGenerator:
    iter = 0
    def generate(self):

        self.iter += 1
        return Kek('Kek' + str(self.iter), self.iter * 2) 


if __name__ == "__main__":
    unittest.main();
    N = 10
    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaawwwwwwwwwwwwwwwwwwwwwwwwww")
    generator = KekGenerator()
    for i in range(0, N):
        kek = generator.generate()
        print(product.name)
        print(product.rofl)
        print(product.get_rofl_of_old_kek())
        print("-----iteration-----")
