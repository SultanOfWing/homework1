# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import math
import random


def hello_there(str_input: str):
    print("Hello, " + str_input + "!")


def sum_triple(term_1: int, term_2: int, term_3: int):
    print(term_1 + term_2 + term_3)


def find_prev_and_next(string_input: str):
    try:
        int_input = int(string_input)
        print("The next number for the number " + string_input + " is " + str(int_input + 1))
        print("The previous number for the number " + string_input + " is " + str(int_input - 1))
    except ValueError:
        pass


def find_square_edge_by_area(area: int):
    try:
        print(math.sqrt(area))
    except ValueError:
        pass


def find_triangle_perimeter_and_area_by_edges(edge_1: int, edge_2: int, edge_3: int):
    try:
        perimeter = edge_1 + edge_2 + edge_3
        p = perimeter / 2
        area = math.sqrt(p * (p - edge_1) * (p - edge_2) * (p - edge_3))
        print("Perimeter of triangle is " + str(perimeter) + " and the area is " + str(area))
    except ValueError:
        pass


def calculate_loan_payments(credit: int, percent: int):
    overpayment = credit * percent * 0.01
    print("Total amount: " + str(overpayment + credit) + " overpayment " + str(overpayment))


def simple_operations(param_1: int, param_2: int):
    sum = param_1 + param_2
    difference = param_1 - param_2
    multiplication = param_1 * param_2
    division = param_1 / param_2
    remainder = param_1 % param_2
    print("sum: " + str(sum) + ", difference: " + str(difference) + ", multiplication: " + str(
        multiplication) + ", division: " + str(division) + ", remainder: " + str(remainder))


def int_float_in_interval(min: int, max: int):
    random_int = random.randint(min, max)
    random_float = random.uniform(min, max)
    print("Random integer in range: " + str(random_int) + ", random rational " + str(random_float))


def min_in_two_numbers(param_1: int, param_2: int):
    print(min(param_1, param_2))


def sign(number: int):
    if number > 0:
        return 1
    elif number < 0:
        return -1
    else:
        return 0


def calculate(param_1: int, param_2: int, _operator: str):
    try:
        print(eval(str(param_1) + _operator + str(param_2)))
    except ValueError:
        pass


def resolve_quadratic(a: int, b: int, c: int):
    d = (b * b) - (4 * a * c)
    x_1 = (-b + math.sqrt(d)) / (2 * a)
    x_2 = (-b - math.sqrt(d)) / (2 * a)
    print("x1 is " + str(x_1) + " and x2 is " + str(x_2))


def calculate_tariff(minutes: int, sms_count: int):
    additional_minutes = minutes - 100
    additional_sms = sms_count - 30
    additional_minutes_cost = 0
    additional_sms_cost = 0
    if additional_minutes > 0:
        additional_minutes_cost = additional_minutes * 0.3
    if additional_sms > 0:
        additional_sms_cost = additional_sms * 0.25

    print(30 + additional_minutes_cost + additional_sms_cost)


def check_if_vowel_or_consonant(input_char: str):
    vowels = ["a", "e", "i", "o", "u", "y"]

    char = input_char.lower().strip()
    if len(char) > 1:
        char = char[0]
    elif len(char) < 1:
        return

    if char in vowels:
        print("This is vowel")
    elif char not in vowels:
        print("This is consonant")


def define_triangle_type(a: int, b: int, c: int):
    if a == b == c:
        print("Triangle is equilateral")
    elif a == b or b == c or a == c:
        print("Triangle is isosceles")
    else:
        print("Triangle neither equilateral, neither isosceles")


class WordType:
    left_hand_set = ["q", "w", "e", "r", "t", "a", "s", "d", "f", "g", "z", "x", "c", "v", "b"]
    right_hand_set = ["y", "u", "i", "o", "p", "h", "j", "k", "l", "n", "m"]
    left_hand_set.sort()
    right_hand_set.sort()

    @staticmethod
    def check_if_word_comfortable(word: str):
        output = True
        for x in range(len(word) - 1):
            if WordType.binary_search(WordType.left_hand_set, word[x]):
                if WordType.binary_search(WordType.right_hand_set, word[x + 1]):
                    continue
                else:
                    output = False
                    break

            elif WordType.binary_search(WordType.right_hand_set, word[x]):
                if WordType.binary_search(WordType.left_hand_set, word[x + 1]):
                    continue
                else:
                    output = False
                    break

        return output

    # binary search for more efficient sorting
    @staticmethod
    def binary_search(arr, x: str):
        left = 0
        right = len(arr)
        while left <= right:
            middle = left + ((right - left) // 2)
            if x == arr[middle]:
                return True
            elif x > arr[middle]:
                left = middle + 1
            else:
                right = middle - 1

        return False


hello_there(input())
sum_triple(7, 21, 14)
find_prev_and_next(input())
find_square_edge_by_area(12)
find_triangle_perimeter_and_area_by_edges(3, 4, 5)
calculate_loan_payments(1000, 10)
simple_operations(6, 10)
int_float_in_interval(2, 11)
min_in_two_numbers(9, 2)
print(sign(-9))
calculate(1, 4, "/")
resolve_quadratic(1, 5, 6)
calculate_tariff(120, 35)
check_if_vowel_or_consonant("a")
define_triangle_type(6, 5, 6)
wordType = WordType()
print(wordType.check_if_word_comfortable('test'))
