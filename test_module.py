"""PyTest Module"""
from unittest import main, TestCase

from arithmetic_arranger import arithmetic_arranger


class TestArithmeticFormatter(TestCase):
    def test_too_many_problems(self):
        current = arithmetic_arranger(
            ["66 + 145", "9 + 2", "85 - 12", "859 + 20", "74 - 32", "2147 - 785"])
        expected = "Error: Too many problems."
        self.assertEqual(
            current, expected, "Expected:\n {} \n Gets:\n {}".format(expected, current)
        )

    def test_incorrect_operator(self):
        current = arithmetic_arranger(["73 * 74", "7 - 2", "75 / 5", "47 + 1"])
        expected = "Error: Operator must be '+' or '-'."
        self.assertEqual(
            current, expected, "Expected:\n {} \n Gets:\n {}".format(expected, current)
        )

    def test_too_many_digits(self):
        current = arithmetic_arranger(["2 + 789545", "7777 - 9", "8788 + 54", "7892 + 654321"])
        expected = "Error: Numbers cannot be more than four digits."
        self.assertEqual(
            current, expected, "Expected:\n {} \n Gets:\n {}".format(expected, current)
        )

    def test_only_digits(self):
        current = arithmetic_arranger(["38 + 29", "120 - 20", "445 + 430", "107 - 6r9"])
        expected = "Error: Numbers must only contain digits."
        self.assertEqual(
            current, expected, "Expected:\n {} \n Gets:\n {}".format(expected, current)
        )

    def test_result_without_display_answers(self):
        current = arithmetic_arranger(["5 + 321", "1000 - 6", "64 + 13", "888 + 74"])
        expected = "    5      1000      64      888\n+ 321    -    6    + 13    +  74\n-----    ------    ----    -----"
        self.assertEqual(
            current, expected, "Expected:\n {} \n Gets:\n {}".format(expected, current)
        )

    def test_result_displaying_answers(self):
        current = arithmetic_arranger(["5 - 321", "9999 + 6", "64 + 13", "888 + 74"], True)
        expected = "    5      9999      64      888\n- 321    +    6    + 13    +  74\n-----    ------    ----    -----\n -316     10005      77      962"
        self.assertEqual(
            current, expected, "Expected:\n {} \n Gets:\n {}".format(expected, current)
        )


if __name__ == "__main__":
    main()
