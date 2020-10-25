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


# print(arr)
# print(dep)
# n = len(arr)
# plat_needed = 1
# result = 1
# i = 1
# j = 0

# while (i < n and j < n):
#     if (arr[i] < dep[j]):
#         plat_needed += 1
#         i += 1
#     elif(arr[i] > dep[j]):
#         plat_needed -= 1
#         j += 1

#     if (plat_needed > result):
#         result = plat_needed

# print(result)
