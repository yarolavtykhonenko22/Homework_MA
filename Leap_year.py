def check_leap_year(year):
    if year % 100 == 0 and year % 400 == 0:
        return "YES"
    elif year % 4 == 0 and year % 100 == 0:
        return "NO"
    elif year % 4 == 0:
        return "YES"
    else:
        return "NO"
year = int(input())
if __name__ == "__main__":
    check_leap_year(year)
def test():
    test_cases = [(2000, "YES"), (1800, "NO"), (1600, "YES"), (40, "YES")]
    for test_years, test_returnes in test_cases:
        assert check_leap_year(test_years) == test_returnes, f"test year:{test_years} doesn't work, expected {test_returnes} got {check_leap_year(test_years)}"
if __name__ == "__main__":
    test()

