def leap_year(b):
    if b % 4 == 0 and b % 100 != 0 and b % 400 == 0:
        print('YES')
    else:
        print('NO')
year = int(input())
leap_year(year)
