"""
    File name: 5.py
    Author: AyumiizZ
    Date created: 2020/10/04
    Python Version: 3.8.5
    About: Find kth smallest element in union set of two sorted arrays problem
"""

from random import randint
from time import sleep

DEBUG = False


def generate_data(n: int, min_data: int = 1, max_data: int = 100):
    ''' Generate sorted n elements array

    Parameters
    ----------
    n : integer
        Number of elements in each array
    min_data, max_data: integer
        All element in the array be like min_data <= each elements <= max_data
    '''
    if(2*n > max_data-min_data-1):
        print("Please change max min data")
        exit()
    A = []
    B = []
    for i in [A, B]:
        for j in range(n):
            random_number = None
            while random_number == None or random_number in (A+B):
                random_number = randint(min_data, max_data)
            i.append(random_number)
    return sorted(A), sorted(B)


def find_kth_element(A: list, B: list, k: int):
    '''Recursive finding kth smallest element from A UNION B

    Parameters
    ----------
    A,B : 1d array
          Sorted array
    k: int
       kth smallest element
    '''
    if(DEBUG):
        print(f"Finding {k}{get_ordinal(k)} smallest element")
        print_dataset(A, B)
    if(len(A) > len(B)):
        A, B = B, A
    if(len(A) == 0):
        return B[k-1]
    if(k == 1):
        return min(A[0], B[0])
    i = min(len(A), k//2)
    j = min(len(B), k//2)
    if(A[i-1] > B[i-1]):
        B = B[j:]
        return find_kth_element(A, B, k-j)
    else:
        A = A[i:]
        return find_kth_element(A, B, k-i)


def get_ordinal(k: int):
    '''Return ordinal number prefix'''
    if(k in [11, 12, 13] or k % 10 == 0 or k % 10 >= 4):
        return 'th'
    else:
        return ['st', 'nd', 'rd'][(k % 10)-1]


def print_dataset(A, B):
    '''Print dataset pretty format'''
    print(f"A: {A}")
    print(f"B: {B}")


def find_in(A, B):
    '''Loop for finding number in dataset'''
    try:
        print_dataset(A, B)
        while True:
            k = int(input('K (Ctrl-c to break): '))
            if(k > (len(A)*2)):
                print("ERROR")
                continue
            value = find_kth_element(A, B, k)
            print(f"Index {k}{get_ordinal(k)} is {value}")
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    dataset_size = int(input("Input size of dataset: "))
    A, B = generate_data(n=dataset_size)
    find_in(A, B)
