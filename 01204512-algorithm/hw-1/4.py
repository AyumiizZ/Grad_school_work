"""
    File name: 4.py
    Author: AyumiizZ
    Date created: 2020/10/04
    Python Version: 3.8.5
    About: Find the key in array with O(log n) time complexity problem 
"""
from random import randint

# Defind for prevent memory usage and prevent buggy program
DATASET_SIZE_LIMIT = 1 << 20
DEBUG = False


def generate_data(n: int, min_data: int = 1, max_data: int = 100):
    ''' Generate sorted n elements array

    Parameters
    ----------
    n : integer
        Number of elements in array
    min_data, max_data: integer
        All element in the array be like min_data <= each elements <= max_data
    '''
    if n > DATASET_SIZE_LIMIT:
        print(f"n is limit at {DATASET_SIZE_LIMIT}")
        exit()
    if(2*n > max_data-min_data-1):
        print("Please change max min data")
        exit()
    dataset = []
    for i in range(n):
        random_number = None
        while random_number == None or random_number in dataset:
            random_number = randint(min_data, max_data)
        dataset.append(random_number)
    return sorted(dataset)


def binary_search(arr, key, lower, upper):
    '''Recursive finding key from dataset

    Parameters
    ----------
    arr : 1d array
            Sorted array
    key: int
           key for finding
    lower: int
           Lower range of interest (for first time value must be 0)
    upper: int
           Upper range of interest(for first time value must be len(arr))
    '''
    if (upper < lower):
        return -1
    mid = (upper + lower) // 2
    if(arr[mid] == key):
        return mid
    if(arr[mid] > key):
        return binary_search(arr, key,  lower, mid-1)
    if(arr[mid] < key):
        return binary_search(arr, key,  mid+1, upper)


def print_dataset(dataset):
    '''Print dataset pretty format'''
    print("Dataset")
    print("-------")
    print(dataset)


def find_in(dataset):
    '''Loop for finding number in dataset'''
    try:
        print_dataset(dataset)
        while True:
            key = int(input('Input the key (Ctrl-c to break): '))
            index = binary_search(dataset, key, 0, len(dataset)-1)
            if index == -1:
                print(f"Not found {key} in dataset")
            else:
                print(f"Found {key} at index {index}")
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    dataset_size = int(input("Input size of dataset: "))
    dataset = generate_data(n=dataset_size)
    find_in(dataset)
