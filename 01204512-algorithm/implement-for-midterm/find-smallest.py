"""
    File name: find-smallest.py
    Author: AyumiizZ
    Date created: 2020/10/24
    Python Version: 3.8.5
    About: find smallest number in decreasing and increasing sequence
"""


def find_smallest(arr):
    n = len(arr)
    if (n == 1):
        return arr[0]
    if (arr[1] > arr[0]):  # increase only
        return arr[0]
    if arr[n-1] < arr[n-2]:  # decrese only
        return arr[n-1]
    lower = 1
    upper = n-2
    while (lower <= upper):
        mid = (lower+upper)//2
        if ((arr[mid] < arr[mid-1]) and (arr[mid] < arr[mid+1])):
            ans = arr[mid]
            break
        elif((arr[mid - 1] < arr[mid]) and (arr[mid] < arr[mid + 1])):
            upper = mid - 1
        else:
            lower = mid + 1
    return ans
