from tkinter import *
from tkinter.scrolledtext import ScrolledText
import tkinter.messagebox as messageBox
from tkinter.filedialog import *
import os
import json
import csv


class MainGUI(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.originalText = []
        self.sortText = []
        self.createWidgets()

    def createWidgets(self):
        self.searchBox = Entry(self, width=100)
        self.searchBox.grid(row=0, column=0, columnspan=4)
        self.searchButton = Button(self, text="搜尋")
        self.searchButton.grid(row=0, column=4)

        self.originalTextList = Listbox(self, height=40, width=50)
        self.originalTextList.grid(row=1, column=0, columnspan=2, rowspan=5)
        self.sortTextList = Listbox(self, height=40, width=50)
        self.sortTextList.grid(row=1, column=3, columnspan=2, rowspan=5)

        self.loadDataButton = Button(self, text="讀取資料")
        self.loadDataButton.grid(row=1, column=2)
        self.saveDataButton = Button(self, text="儲存資料")
        self.saveDataButton.grid(row=2, column=2)
        self.addData = Button(self, text="新增資料")
        self.addData.grid(row=3, column=2)
        self.editData = Button(self, text="修改資料")
        self.editData.grid(row=4, column=2)
        self.removeData = Button(self, text="刪除資料")
        self.removeData.grid(row=5, column=2)

    def loadData(self, filename=None):
        if filename is None:
            pass
        else:
            ext = os.path.splitext(filename)[-1]
            if ext == '.json':
                with open(filename) as jsonFile:
                    self.originalText = json.load(jsonFile)
                    jsonFile.close()
            elif ext == '.csv':
                with open(filename) as csvFile:
                    self.originalText = csv.reader(csvFile)
                    csvFile.close()
            else:
                with open(filename) as File:
                    self.originalText = File.readlines()
                    File.close()

    def saveData(self, filename=None, mode=None):
        if filename is None or mode is None:
            pass
        else:
            with open(filename, 'w') as file:
                if mode:
                    json.dump(self.originalText, file, sort_keys=False, indent=4)
                else:
                    json.dump(self.sortText, file, sort_keys=False, indent=4)
                file.close()

    def addDataView(self):
        window = Toplevel()
        window.focus_force()
        window.grid()
        window.wm_title("新增資料")
        window.info = Label(window, text="請輸入要新增的資料：")
        window.info.grid(row=0, column=0, columnspan=2)
        window.enter = Entry(window, width=40)
        window.enter.grid(row=1, column=0, columnspan=2)
        window.ok = Button(window, text="確定", command=lambda x: window.enter.get() is not None if self.addData(window, window.enter.get()) else window.destroy)
        window.ok.grid(row=2, column=0)
        window.cancel = Button(window, text="取消", command=window.destroy())
        window.cancel.grid(row=2, column=1)

    def addData(self, window, Data):
        self.originalText.append(Data)
        self.listReload()
        window.destroy()

    def editDataView(self, index):
        window = Toplevel()
        window.focus_force()
        window.grid()
        window.wm_title("修改資料")
        window.info = Label(window, text="請輸入要修改的資料：")
        window.info.grid(row=0, column=0, columnspan=2)
        window.enter = Entry(window, width=40, text=self.originalText[index])
        window.enter.grid(row=1, column=0, columnspan=2)
        window.ok = Button(window, text="確定", command=lambda:self.editData(window, index, window.enter.get()))
        window.ok.grid(row=2, column=0)
        window.cancel = Button(window, text="取消", command=window.destroy())
        window.cancel.grid(row=2, column=1)

    def editData(self, window, index, newData):
        self.originalText[index] = newData
        window.destory()

    def removeDataView(self, index):
        window = Toplevel()
        window.focus_force()
        window.grid()
        window.wm_title("刪除資料")
        window.info = Label(window, text="確定刪除以下資料？")
        window.info.grid(row=0, column=0, columnspan=2)
        window.data = Label(window, text=self.originalText[index])
        window.data.grid(row=1, column=0, columnspan=2)
        window.ok = Button(window, text="確定", command=lambda:self.removeData(window, index))
        window.ok.grid(row=2, column=0)
        window.cancel = Button(window, text="取消", command=window.destroy())
        window.cancel.grid(row=2, column=1)

    def removeData(self, window, index):
        self.originalText.pop(index)
        window.destroy()
        pass

    def listReload(self):
        self.originalTextList.delete(0, END)
        self.sortTextList.delete(0, END)
        for i in self.originalText:
            self.originalTextList.insert(i)

    def searchBox(self):
        pass