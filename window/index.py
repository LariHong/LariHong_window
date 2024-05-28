import tkinter as tk
# tkinter 內有一個ttk
from tkinter import ttk

def get_names()->list[str]:
    with open('names.txt',encoding="utf-8") as file3:
        content2:str=file3.read()
    names:list[str]=content2.split()

    return names

names = get_names()

class Window(tk.Tk):

    def __init__(self,title:str=None,**kwargs):
        super().__init__(**kwargs)
        self.title(title)

class Window2(tk.Tk):

    def __init__(self,title:str=None,**kwargs):
        super().__init__(**kwargs)
        self.title(title)
        laber:ttk.Label=ttk.Label(self,
                                  text="我是ttk",
                                  font=("Arial",20,"bold"),
                                  foreground="#f00")                         
        laber.pack(padx=100,pady=100)

#目前檔案為 index.py 如果是執行這個檔案 __name__ == __main__  為這個index.py
if __name__ =="__main__":

    names:list[str]=get_names()
    window:tk.Tk=tk.Tk()
    window.title("我是視窗")
    window.mainloop()

    window2:tk.Tk=Window("我是視窗2",screenName="789")
    window2.mainloop()

    window3:tk.Tk=Window2()
    window3.mainloop()