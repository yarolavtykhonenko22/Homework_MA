def shest(h, a, b):
    day = 1
    p = a
    while a < h:
        a -= b
        a += p
        day += 1
    else:
        print(day)
height = int(input())
lift = int(input())
descent = int(input())
shest(height, lift, descent)
