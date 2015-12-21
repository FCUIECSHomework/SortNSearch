from sort import *
from search import *
from GUI import *

root = Tk()
root.resizable(width=False, height=False)
app = MainGUI(master=root)
app.mainloop()
app.focus_force()

