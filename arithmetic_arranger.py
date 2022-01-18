"""Arithmetic Formatter"""
from typing import List


def arithmetic_arranger(problems: List[str] = list, display_answers: bool = False) -> str:
    """
    :type problems: List[str]
    :type display_answers: bool
    :param display_answers: False
    :param problems: []
    """
    if len(problems) > 5:
        return "Error: Too many problems."

    operators = list(map(lambda op: op.split()[1], problems))
    if set(operators) != {"+", "-"}:
        return "Error: Operator must be '+' or '-'."

    numbers = []
    for p in problems:
        operation = p.split()
        numbers.extend([operation[0], operation[-1]])

    if not all(map(lambda n: n.isdigit(), numbers)):
        return "Error: Numbers must only contain digits."

    if not all(map(lambda n: len(n) < 5, numbers)):
        return "Error: Numbers cannot be more than four digits."

    results = list(map(lambda x: eval(x), problems))

    for i in range(0, len(numbers), 2):
        space = max(len(numbers[i]), len(numbers[i + 1]))
        numbers[i] = numbers[i].rjust(space + 2)
        numbers[i + 1] = operators[i // 2] + numbers[i + 1].rjust(space + 1)
        results[i // 2] = str(results[i // 2]).rjust(space+2)

    first_line = "    ".join(numbers[::2])
    second_line = "    ".join(numbers[1::2])
    third_line = "    ".join(["-" * len(n) for n in numbers[1::2]])
    fourth_line = "    ".join(results)

    return "\n".join([first_line, second_line, third_line]) if not display_answers else "\n".join(
        [first_line, second_line, third_line, fourth_line])
