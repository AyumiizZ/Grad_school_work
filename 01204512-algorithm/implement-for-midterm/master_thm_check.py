from math import log, copysign


def f(n):
    return 1
    # return n**2*log(n, 2)


def master_brute_force(f, a, b, base=10):
    deg = log(a, b)
    # print('deg', deg)
    n = [i*100000 for i in range(1, 101)]
    case2 = [(i ** deg) * log(i, base) for i in n]
    res_f = [f(i) for i in n]
    error = 0
    for i in zip(case2, res_f):
        ea_err = i[0]-i[1]
        error += copysign(1, ea_err) * (ea_err**2)
        # print(error)
    error = error/sum(case2)
    # print('error', error)
    if error < 1e5 and error > -1e5:
        print('case2')
    elif error > 0:
        print('case1')
    else:
        print('case3')
    # print('----')


# Slide
master_brute_force(lambda n: n, 4, 2)
master_brute_force(lambda n: n*log(n, 10), 2, 2)
master_brute_force(lambda n: n*log(n, 10), 1, 3)
master_brute_force(lambda n: n**2, 8, 2)
master_brute_force(lambda n: n**3, 9, 3)
master_brute_force(lambda n: 1, 1, 2)
master_brute_force(lambda n: log(n, 10), 2, 2)
print()
# HW
master_brute_force(lambda n: n**2, 5, 2)
master_brute_force(lambda n: n**1.5, 5, 2)
master_brute_force(lambda n: (n**2)*log(n, 2), 10, 10, base=2)
