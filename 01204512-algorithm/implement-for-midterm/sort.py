class SortTools(object):
    class algorithm:
        MERGE_SORT = 0
        QUICK_SORT = 1
        BUBBLE_SORT = 2,
        INSERTION_SORT = 3

    def __init__(self, method):
        avaliable_algorithm = [
            self.merge_sort,
            self.quick_sort,
            self.bubble_sort,
            self.insertion_sort
        ]
        self.sort = avaliable_algorithm[method]

    def merge_sort(self, data):
        if len(data) > 1:
            mid_idx = len(data)//2
            left_data, right_data = data[:mid_idx], data[mid_idx:]
            self.merge_sort(left_data)
            self.merge_sort(right_data)
            i = j = k = 0
            while i < len(left_data) and j < len(right_data):
                if left_data[i] < right_data[j]:
                    data[k] = left_data[i]
                    i += 1
                else:
                    data[k] = right_data[j]
                    j += 1
                k += 1
            while i < len(left_data):
                data[k] = left_data[i]
                i += 1
                k += 1
            while j < len(right_data):
                data[k] = right_data[j]
                j += 1
                k += 1

    def partition(self, data, low, high):
        i = (low-1)
        pivot = data[high]

        for j in range(low, high):
            if data[j] <= pivot:
                i = i+1
                data[i], data[j] = data[j], data[i]
        data[i+1], data[high] = data[high], data[i+1]
        return i+1

    def quick_sort(self, data, low=None, high=None):
        if low is None or high is None:
            low, high = 0, len(data)-1
        if len(data) == 1:
            return data
        if low < high:
            pi = self.partition(data, low, high)
            self.quick_sort(data, low, pi-1)
            self.quick_sort(data, pi+1, high)

    def bubble_sort(self, data):
        is_sorted = False
        while not is_sorted:
            is_sorted = True    # assume when finish this loop data is sorted
            for i in range(len(data)-1):
                if data[i] > data[i+1]:
                    is_sorted = False
                    data[i], data[i+1] = data[i+1], data[i]

    def insertion_sort(self, data):
        for i in range(1, len(data)):
            key = data[i]
            j = i-1
            while j >= 0 and key < data[j]:
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = key


if __name__ == "__main__":
    sort_tool = SortTools(method=SortTools.algorithm.INSERTION_SORT)
    data = [3, 1, 5, 2, 6, 9, 4, 7]
    sort_tool.sort(data)
    print(data)
