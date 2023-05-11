def get_smallest_number(first_number, second_number, third_number):
    if second_number >= first_number <= third_number:
        return first_number
    elif first_number >= second_number <= third_number:
        return second_number
    else:
        return third_number

first_number = int(input())
second_number = int(input())
third_number = int(input())
if __name__ == "__main__":
    get_smallest_number(first_number, second_number, third_number)
def test():
    test_cases = [(23, 3, 5, 3), (10, 10, 10, 10), (23, 4, 23, 4), (-1, -3, -4, -4)]
    for *values, returns in test_cases:
        assert get_smallest_number(*values) == returns, f"case: {values} doesn't work, expected {returns} got {get_smallest_number(*values)}"
if __name__ == "__main__":
    test()
