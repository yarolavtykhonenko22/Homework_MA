def same_numbers(a, b, c):
    if a / b != 1 and a / c != 1 :
        print(0)
    elif a / b == 1 and a / c == 1 :
        print(3)
    else:
        print(2)
first_integer=int(input())
second_integer=int(input())
third_integer=int(input())
same_numbers(first_integer, second_integer, third_integer)