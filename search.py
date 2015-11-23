from sort import *


class BinarySearch:
    def __init__(self, data, target):
        index = self.search(data, target)
        if not index:
            print("Target: " + str(target) + " Not Found!")
        else:
            print("Target: " + str(target) + " Found at " + str(index) + " in data!")

    def search(self, data, target):
        if len(data) < 1:
            return False
        else:
            newData = list(data)
            QuickSort(newData)
            low = 0
            high = len(data) - 1
            while low <= high:
                index = int((low + high) / 2)
                if newData[index] == target:
                    return index
                elif newData[index] > target:
                    high = index - 1
                else:
                    low = index + 1
            else:
                return False
