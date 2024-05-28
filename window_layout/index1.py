import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title("pack1")
        #按鈕1
        btn1:ttk.Button=ttk.Button(self,text="Top")
        btn1.pack()
        #按鈕2
        btn2:ttk.Button=ttk.Button(self,text="Middle")
        btn2.pack()
        #按鈕3
        btn3:ttk.Button=ttk.Button(self,text="Bottom")
        btn3.pack()
        
        # #只產生一次 後續操控無法作用
        # ttk.Button(self,text="Top").pack()
        # ttk.Button(self,text="Middle").pack()
        # ttk.Button(self,text="Bottom").pack()
        
        #Liteal 代表只能用那幾個值
        ttk.Button(self,text="Left").pack(side="left")
        ttk.Button(self,text="Center").pack(side="bottom")
        ttk.Button(self,text="Right").pack(side="right")

        #創立300x200的方法
        self.geometry("500x200")
        
if __name__ == "__main__":
    window:Window=Window()
    window.mainloop()