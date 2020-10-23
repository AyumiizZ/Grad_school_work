# O(log n) Fast doubling fibonacci algorithm

def Fibonacci(n):
    '''return F(n), F(n+1)'''
    if n < 0:
        return None
    if n == 0:
        return (0, 1)
    a, b = Fibonacci(n // 2)
    c = a * ((2 * b) - a)
    d = (a ** 2) + (b ** 2)
    if n % 2 == 0:
        return (c, d)
    else:
        return (d, c + d)


if __name__ == "__main__":
    n = int(input('N: '))
    res = Fibonacci(n)
    if res:
        print(f'F({n}): {res[0]}')
    else:
        print('Error')
