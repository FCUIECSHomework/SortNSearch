from sort import *
import tkinter.messagebox as messageBox


class LinearSearch:
    def __init__(self, data, target):
        newData = list(data)
        index = self.search(newData, target)
        if not index:
            messageBox.showinfo("Target: " + str(target) + " Not Found!")
        else:
            messageBox.showinfo("Target: " + str(target) + " Found at " + str(index) + " in data!")

    def search(self, data, target):
        if len(data) < 1:
            return False
        else:
            data.append(target)
            for i in range(0, len(data)-1):
                if data[i] == target:
                    data.pop()
                    return i
            else:
                data.pop()
                return False


class BinarySearch:
    def __init__(self, data, target):
        newData = list(data)
        index = self.search(newData, target)
        if not index:
            messageBox.showinfo("Target: " + str(target) + " Not Found!")
        else:
            messageBox.showinfo("Target: " + str(target) + " Found at " + str(index) + " in data! (After sort)")

    def search(self, data, target):
        if len(data) < 1:
            return False
        else:
            QuickSort(data)
            low = 0
            high = len(data) - 1
            while low <= high:
                index = int((low + high) / 2)
                if data[index] == target:
                    return index
                elif data[index] > target:
                    high = index - 1
                else:
                    low = index + 1
            else:
                return False
