# https://stepik.org/lesson/316052/step/8?unit=301794

def almost_double_factorial(n):
    k = 1

    if n == 0:
        return 1

    for i in range(1,n+1):
        if ((i >= 0) & (i % 2 != 0)):
            k = k*i
            
    return k

print(almost_double_factorial(int(input())))
