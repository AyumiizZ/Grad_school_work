"""
    File name: train.py
    Author: AyumiizZ
    Date created: 2020/10/24
    Python Version: 3.8.5
    About: Calulate n Platform for list of arrival and departure
"""

from sort import SortTools
arr = [2.00, 2.10, 3.00, 3.20, 3.50, 5.00]
dep = [2.30, 3.40, 3.20, 4.30, 4.00, 5.20]
arr = [2.0, 2.3]
dep = [2.3, 2.4]


def minPlatforms(arrival, departure):
    sort_tool = SortTools(method=SortTools.algorithm.MERGE_SORT)
    sort_tool.sort(arr)
    sort_tool.sort(dep)
    count = 0
    platforms = 0
    i = j = 0
    while i < len(arrival):
        if arrival[i] < departure[j]:
            count = count + 1
            platforms = max(platforms, count)
            i = i + 1
        else:
            count = count - 1
            j = j + 1

    return platforms


print(minPlatforms(arr, dep))
