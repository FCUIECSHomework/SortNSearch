from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import *
import os
import json
import csv
import time
from search import *


class MainGUI(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        master.wm_title("Sort & Search")
        self.grid()
        self.originalText = []
        self.sortText = []
        self.createWidgets(master)
        self.current_milli_time = lambda: int(round(time.time() * 1000))

    def createWidgets(self, master):
        self.searchBox = Entry(self, width=90)
        self.searchBox.grid(row=0, column=0, columnspan=4)
        self.searchBox.config(font="Consolas")
        self.searchButton = Button(self, text="搜尋", command=lambda: self.searchItem(self.searchBox.get()))
        self.searchButton.grid(row=0, column=4)

        self.originalTextList = Listbox(self, height=40, width=40)
        self.originalTextList.grid(row=1, column=0, columnspan=2, rowspan=7)
        self.originalTextList.config(font="Consolas")
        self.sortTextList = Listbox(self, height=40, width=40)
        self.sortTextList.grid(row=1, column=3, columnspan=2, rowspan=7)
        self.sortTextList.config(font="Consolas")

        self.loadDataButton = Button(self, text="讀取資料", command=lambda: self.loadData(askopenfilename(title="開啟檔案",
                                                                                                      filetypes=[(
                                                                                                                 'Json檔案',
                                                                                                                 ".json"),
                                                                                                                 (
                                                                                                                 'Csv檔案',
                                                                                                                 ".csv"),
                                                                                                                 (
                                                                                                                 '純文字檔案',
                                                                                                                 ".txt"),
                                                                                                                 (
                                                                                                                 '所有檔案',
                                                                                                                 '.*')])))
        self.loadDataButton.grid(row=1, column=2, sticky=NSEW)
        self.saveDataButton = Button(self, text="儲存資料", command=lambda: self.saveData(
            asksaveasfilename(title="另存新檔", filetypes=[('Json檔案', ".json"), ('所有檔案', '.*')])))
        self.saveDataButton.grid(row=2, column=2, sticky=NSEW)
        self.sortData = Button(self, text="排序資料", command=lambda: self.sortItem())
        self.sortData.grid(row=3, column=2, sticky=NSEW)
        self.addData = Button(self, text="新增資料", command=lambda: self.addDataView())
        self.addData.grid(row=4, column=2, sticky=NSEW)
        self.editData = Button(self, text="修改資料",
                               command=lambda: self.editDataView(self.originalTextList.curselection()[0]))
        self.editData.grid(row=5, column=2, sticky=NSEW)
        self.removeData = Button(self, text="刪除資料",
                                 command=lambda: self.removeDataView(self.originalTextList.curselection()[0]))
        self.removeData.grid(row=6, column=2, sticky=NSEW)
        self.exitButton = Button(self, text="離開程式", command=lambda: master.destroy())
        self.exitButton.grid(row=7, column=2, sticky=NSEW)

    def loadData(self, filename=None):
        if filename is None:
            pass
        else:
            ext = os.path.splitext(filename)[-1]
            if ext == '.json':
                with open(filename) as jsonFile:
                    self.originalText = json.load(jsonFile)['data']
                    jsonFile.close()
            elif ext == '.csv':
                with open(filename) as csvFile:
                    self.originalText = csv.reader(csvFile)
                    csvFile.close()
            else:
                with open(filename) as File:
                    self.originalText = File.readlines()
                    File.close()
            self.listReload()

    def saveData(self, filename=None):
        mode = False
        result = messageBox.askquestion("儲存檔案", "你要存哪一邊到檔案呢？\n（Yes=左欄、No=右欄）")
        if result == "yes":
            mode = True

        if filename is None or mode is None:
            pass
        else:
            with open(filename, 'w') as file:
                if mode:
                    json.dump({"data": self.originalText}, file, sort_keys=False, indent=4)
                else:
                    json.dump({"data": self.sortText}, file, sort_keys=False, indent=4)
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
        window.ok = Button(window, text="確定", command=lambda: window.enter.get() is not None if MainGUI.addData(self,window,
                                                                                                               window.enter.get()) else window.destroy)
        window.ok.grid(row=2, column=0)
        window.cancel = Button(window, text="取消", command=lambda: window.destroy())
        window.cancel.grid(row=2, column=1)

    def addData(self, window, Data):
        self.originalText.append(Data)
        self.sortText = []
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
        window.ok = Button(window, text="確定", command=lambda: MainGUI.editData(self, window=window , index=index, newData=window.enter.get()))
        window.ok.grid(row=2, column=0)
        window.cancel = Button(window, text="取消", command=lambda: window.destroy())
        window.cancel.grid(row=2, column=1)

    def editData(self, window, index, newData):
        self.originalText[index] = newData
        self.sortText = []
        self.listReload()
        window.destroy()

    def removeDataView(self, index):
        window = Toplevel()
        window.focus_force()
        window.grid()
        window.wm_title("刪除資料")
        window.info = Label(window, text="確定刪除以下資料？")
        window.info.grid(row=0, column=0, columnspan=2)
        window.data = Label(window, text=self.originalText[index])
        window.data.grid(row=1, column=0, columnspan=2)
        window.ok = Button(window, text="確定", command=lambda: MainGUI.removeData(self, window=window, index=index))
        window.ok.grid(row=2, column=0)
        window.cancel = Button(window, text="取消", command=lambda: window.destroy())
        window.cancel.grid(row=2, column=1)

    def removeData(self, window, index):
        self.originalText.pop(index)
        self.sortText = []
        self.listReload()
        window.destroy()

    def listReload(self):
        self.originalTextList.delete(0, END)
        self.sortTextList.delete(0, END)
        for i in self.originalText:
            self.originalTextList.insert(END, i)
        if len(self.sortText) > 0:
            for i in self.sortText:
                self.sortTextList.insert(END, i)

    def searchItem(self, data):
        result = messageBox.askquestion("選擇搜尋法？", "要用線性搜尋法搜尋嗎？\n(Yes=線性搜尋法、No=排序後二分搜尋法)")
        runtime = 0
        if result == "yes":
            runtime = self.current_milli_time()
            LinearSearch(self.originalText, data)
            runtime = self.current_milli_time() - runtime
        else:
            runtime = self.current_milli_time()
            BinarySearch(self.originalText, data)
            runtime = self.current_milli_time() - runtime
        messageBox.showinfo("花費時間", "本次搜尋花費"+str(runtime)+"ms.")

    def sortItem(self):
        result = messageBox.askquestion("選擇排序法", "要用泡沫搜尋法搜尋嗎？\n(Yes=泡沫搜尋法、No=快速排序法)")
        runtime = 0
        if result == "yes":
            runtime = self.current_milli_time()
            self.sortText = BubbleSort.sort(self, list(self.originalText))
            runtime = self.current_milli_time() - runtime
        else:
            runtime = self.current_milli_time()
            self.sortText = QuickSort.sort(self, list(self.originalText), 0, len(self.originalText)-1)
            runtime = self.current_milli_time() - runtime
        self.listReload()
        messageBox.showinfo("花費時間", "本次排序花費"+str(runtime)+"ms.")