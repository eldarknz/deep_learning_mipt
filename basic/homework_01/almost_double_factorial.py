# https://stepik.org/lesson/316052/step/8?unit=301794

def almost_double_factorial(n):

    factorial = 1

    while n > 1:
        if n % 2 != 0:
            factorial *= n
        n -= 1

    return factorial


def almost_double_factorial2(n):
    k = 1

    if n == 0:
        return 1

    for i in range(1,n+1):
        if ((i >= 0) & (i % 2 != 0)):
            k = k*i
            
    return k

for i in range(0, 1001):
    print(i)
    res = almost_double_factorial(i) == almost_double_factorial2(i)
    if res == False:
        print (res)
    print("--------")
