# Задание 1

def q():
    print("Don't let the noise of others' opinions")
    print("drown out your own inner voice.")
    print("                            Steve Jobs")
q()

# Задание 2

def o(a, b):
    for i in range(min(a, b), max(a, b)+1):
        if i % 2 == 1:
            print(i, end=" ")
    print()  # перенос строки после вывода чисел
o(3, 15)

# Задание 3

def l(length, d, c):
    if d == "h":
        print(c * length)
    else:
        for _ in range(length):
            print(c)
l(5, "h", "*")

# Задание 4

def m(a, b, c, d):
    x = a
    if b > x: x = b
    if c > x: x = c
    if d > x: x = d
    return x
print(m(7, 2, 9, 4))

# Задание 5

def s(a, b):
    sum_ = 0
    for i in range(min(a, b), max(a, b)+1):
        sum_ += i
    return sum_
print(s(1, 5))

# Задание 6

def p(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print(p(13))

# Задание 7

def f(n):
    s = str(n)
    if len(s) != 6:
        return False
    return int(s[0])+int(s[1])+int(s[2]) == int(s[3])+int(s[4])+int(s[5])
print(f(123420))