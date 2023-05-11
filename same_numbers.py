def check_quantity_of_same_numbers(first_integer, second_integer, third_integer):
    if first_integer / second_integer != 1 and first_integer / third_integer != 1:
        return 0
    elif first_integer / second_integer == 1 and first_integer / third_integer == 1:
        return 3
    else:
        return 2
first_integer = int(input())
second_integer = int(input())
third_integer = int(input())

if __name__ == "__main__":
    check_quantity_of_same_numbers(first_integer, second_integer, third_integer)
def test():
    test_cases = [(23, 3, 5, 0), (10, 10, 10, 3), (23, 4, 23, 2), (-1, -3, -4, 0)]
    for *test_values, test_returns in test_cases:
        assert check_quantity_of_same_numbers(*test_values) == test_returns, f"case: {test_values} doesn't work, expected {test_returns} got {check_quantity_of_same_numbers(*test_values)}"
if __name__ == "__main__":
    test()

