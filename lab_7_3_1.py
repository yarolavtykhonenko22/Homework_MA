class Date:
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @staticmethod
    def is_date_valid(string_date, splitter):
        day, month, year = map(int, string_date.split(splitter))
        return day <= 31 and 12 >= month and 9999 >= year

    @staticmethod
    def from_string_static(string_date, splitter):
        day, month, year = map(int, string_date.split(splitter))
        return [day, month, year]

    @classmethod
    def from_string(cls, string_date, splitter):
        day, month, year = map(int, string_date.split(splitter))
        return cls(day, month, year)
def test1():
    test_cases = ["15-2-200", True], ["32-12-6534", False], ["1-13-1234", False], ["12-4-98777", False]
    for test_values, test_returns in test_cases:
        test = Date.is_date_valid(test_values, "-")
        assert test == test_returns, f"case: {test_values} doesn't work, expected {test_returns}, got {test}"

def test2():            # 1 test for function from_string_static and from_string because they are same
    test_cases = [("15-2-200", 15, 2, 200), ("32-12-6534", 32, 12, 6534), ("1-13-1234", 1, 13, 1234),("12-4-98777", 12, 4, 98777)]
    for test_values, *test_returns in test_cases:
        test = Date.from_string_static(test_values, "-")
        assert test == test_returns, f"case:{test_values} doesn't work, expected{test_returns}, got {test}"
if __name__ == "__main__":
    test1()
    test2()