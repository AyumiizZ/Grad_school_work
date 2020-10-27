"""
    File name: 6.py
    Author: AyumiizZ
    Date created: 2020/10/04
    Python Version: 3.8.5
    About: Merge k sorted arrays, each with n elements problem 
"""
from random import randint
import numpy as np
import pprint

DEBUG = False


def generate_data(k: int, n: int, min_data: int = 1, max_data: int = 100):
    '''Generate k sorted arrays, each with n elements

    Parameters
    ----------
    k : integer
        Number of sorted arrays 
    n : integer
        Number of elements in each arrays 
    min_data, max_data: integer
        All element in the array be like min_data <= each elements <= max_data
    '''
    if(k*n > max_data-min_data-1):
        print("Please change max min data")
        exit()
    used = []
    dataset = []
    for i in range(k):
        temp = []
        for j in range(n):
            random_number = None
            while random_number == None or random_number in used:
                random_number = randint(min_data, max_data)
            used.append(random_number)
            temp.append(random_number)
        dataset.append(sorted(temp))
    return dataset


def merge_2(arr1: list, arr2: list):
    '''Merge two 1d arrays to one array

    Parameters
    ----------
    arr1 : 1d array
           Elements to merge 
    arr2 : 1d array
           Elements to merge 
    '''
    merged = list(np.zeros((len(arr1)+len(arr2))))
    i = j = k = 0
    while(i < len(arr1) and j < len(arr2)):
        if(arr1[i] < arr2[j]):
            merged[k] = arr1[i]
            i += 1
        else:
            merged[k] = arr2[j]
            j += 1
        k += 1
    while(i < len(arr1)):
        merged[k] = arr1[i]
        i += 1
        k += 1
    while(j < len(arr2)):
        merged[k] = arr2[j]
        j += 1
        k += 1
    return merged


def merge_k(arr_k: list):
    '''Recursive merge all k sorted arrays

    Parameters
    ----------
    arr_k : k dimension array
            Elements to merge
    '''
    if len(arr_k) == 1:
        return arr_k[0]
    mid = len(arr_k) // 2
    arr1 = arr_k[:mid]
    arr2 = arr_k[mid:]

    arr1 = merge_k(arr1)
    arr2 = merge_k(arr2)
    merged = merge_2(arr1, arr2)
    if (DEBUG):
        print(f"arr1: {arr1}")
        print(f"arr2: {arr2}")
        print(f"merged: {merged}")
    return merged


def print_result(dataset: list, merged: list):
    '''Print result pretty format'''
    pp = pprint.PrettyPrinter(indent=4)
    print("Dataset")
    print("-------")
    pp.pprint(dataset)
    print("Result")
    print("-------")
    print(merged)


if __name__ == "__main__":
    k = int(input("K: "))
    n = int(input("N: "))
    dataset = generate_data(k=k, n=n)
    merged = merge_k(dataset)
    print_result(dataset, merged)
