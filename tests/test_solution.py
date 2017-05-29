from unittest import TestCase


class TestSolution(TestCase):
    def test_solution(self):
        from build import solution
        from random import randint

        num1 = randint(1, 1000)
        num2 = randint(1, 1000)
        num3 = randint(1, 1000)
        num4 = randint(1, 1000)

        array = [num4, num3, num2, num1]

        result = solution(array)

        self.assertNotEqual(result, None)

        self.assertTrue(result[0], float(num4))
        self.assertTrue(result[1], float(num3))
        self.assertTrue(result[2], float(num2))
        self.assertTrue(result[3], float(num1))
