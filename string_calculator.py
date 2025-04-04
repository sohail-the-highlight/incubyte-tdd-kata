import re

class NegativeNumberException(Exception):
    def __init__(self, negatives):
        message = "negative numbers not allowed " + ",".join(map(str, negatives))
        super().__init__(message)

def add(numbers: str) -> int:
    if not numbers:
        return 0

    delimiter = ",|\n"
    if numbers.startswith("//"):
        parts = numbers.split("\n", 1)
        custom_delim = parts[0][2:]
        numbers = parts[1]
        delimiter = re.escape(custom_delim)

    tokens = re.split(delimiter, numbers)
    integers = []

    for token in tokens:
        if token.strip():
            num = int(token)
            integers.append(num)

    negatives = [num for num in integers if num < 0]
    if negatives:
        raise NegativeNumberException(negatives)

    return sum(integers)
