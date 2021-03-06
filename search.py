from sort import *
import tkinter.messagebox as messageBox


class LinearSearch:
    def __init__(self, data, target):
        newData = list(data)
        index = self.search(newData, target)
        if index is None:
            messageBox.showinfo("查無資料", "Target: " + str(target) + " Not Found!")
        else:
            messageBox.showinfo("找到資料", "Target: " + str(target) + " Found at " + str(index) + " in data!")

    def search(self, data, target):
        if len(data) < 1:
            return None
        else:
            data.append(target)
            for i in range(0, len(data) - 1):
                if data[i] == target:
                    data.pop()
                    return i
            else:
                data.pop()
                return None


class BinarySearch:
    def __init__(self, data, target):
        newData = list(data)
        index = self.search(newData, target)
        if index is None:
            messageBox.showinfo("查無資料", "Target: " + str(target) + " Not Found!")
        else:
            messageBox.showinfo("找到資料", "Target: " + str(target) + " Found at " + str(index) + " in data! (After sort)")

    def search(self, data, target):
        if len(data) < 1:
            return None
        else:
            newData = QuickSort.sort(self, list(data), 0, len(data)-1)
            low = 0
            high = len(newData) - 1
            while low <= high:
                index = int((low + high) / 2)
                if newData[index] == target:
                    return index
                elif newData[index] > target:
                    high = index - 1
                else:
                    low = index + 1
            else:
                return None
