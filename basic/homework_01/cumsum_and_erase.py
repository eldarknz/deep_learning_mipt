# https://stepik.org/lesson/316052/step/11?unit=301794

def cumsum_and_erase(A, erase=1):
    B, cumsum = [], 0

    for i in range(len(A)):
        cumsum += A[i]
        if cumsum != erase:
            B.append(cumsum)

    return B

A = [5, 1, 4, 5, 14]

print(cumsum_and_erase(A, erase=10))
