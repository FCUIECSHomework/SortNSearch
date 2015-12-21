from random import *


class BubbleSort:
    def __init__(self, data):
        self.sort(data)

    def sort(self, data):
        if len(data) <= 1:
            return
        else:
            for i in range(0, len(data)-1):
                for j in range(0, len(data)-1-i):
                    if data[j] > data[j+1]:
                        data[j], data[j+1] = data[j+1], data[j]


class QuickSort:
    def __init__(self, data):
        self.sort(data, 0, len(data)-1)

    def sort(self, data, left, right, stringSort=False):
        if len(data) <= 1:
            return
        elif right <= left:
            return
        else:
            pivotIndex = int((left+right)/2)
            pivot = data[pivotIndex]
            data[pivotIndex], data[right] = data[right], data[pivotIndex]
            swapIndex = left
            for i in range(left, right):
                if data[i] <= pivot:
                    data[i], data[swapIndex] = data[swapIndex], data[i]
                    swapIndex += 1
            data[swapIndex], data[right] = data[right], data[swapIndex]
            self.sort(data, left, swapIndex-1)
            self.sort(data, swapIndex+1, right)