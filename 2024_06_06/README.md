> ##
```
import tkinter as tk
from tkinter import ttk,simpledialog
from ttkthemes import ThemedTk

class App(ThemedTk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        
        self.window_design()
        self.title_design()
        self.input_design()

    def window_design(self):
        self.title("BMI計算器")
        # self.configure(bg="#00FFFF")
        #定義500x300的視窗，會依據離左100 離上50
        # self.geometry("500x300+100+50")
        #此功能預設可以調整視窗大小，底下就是不能改
        self.resizable(False,False)
        
    def title_design(self):
        style = ttk.Style()
        #title frame內 有標題label
        main_frame=ttk.Frame(self)
        title_label=ttk.Label(self,text="BMI計算器", font=("Arial", 20))
        title_label.pack(pady=10)
        main_frame.pack(padx=100,pady=50)

    def input_design(self):
        #style設定傳入 ttk.Frame
        style=ttk.Style()
        style.configure("input.TFrame",background="white")
        input_frame =ttk.Frame(self,width=100,height=100,style="input.TFrame")

        input_frame.pack(padx=100,pady=50)
```