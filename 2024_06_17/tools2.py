from ttkthemes import ThemedTk
import tkinter as tk
from tkinter import ttk, messagebox,Misc
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageTk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class PieChaetFrame(ttk.Frame):
    def __init__(self,master:Misc=None,**kwargs):
        super().__init__(master=master,**kwargs)
        self.__create_window()
        style=ttk.Style()
        style.configure("abc.TFrame",background="#ffffff")
        self.config(style="abc.TFrame")

    def __create_window(self):
        self.configure({'borderwidth':2,'relief':'groove'})
        self.pack()
        self.canvas =tk.Canvas(self)
        self.canvas.pack(expand=True,fill="both")

    def __cleanInfoList(self):
        #清除 infos的list
        for w in self.winfo_children():
            w.destroy()
    #清除 canvas記憶體的問題
    def __cleanCanvas(self,canvas:FigureCanvasTkAgg):
        for item in canvas.get_tk_widget().find_all():
            canvas.get_tk_widget().delete(item)
        #把figure給完整消滅
        plt.close()

    @property
    def infos(self)->None:
         return None
    
    @infos.setter
    def infos(self,datas:list[list])->None:
        self.__cleanInfoList()

        for data in datas:
            sitename:str =data[0]
            area:str=data[1]
            infotime:str =data[2]
            address:str=data[3]
            total:int=data[4]
            rents:int=data[5]
            returns:int=data[6]
            oneFrame=ttk.Frame(self,style="abc.TFrame")
            ttk.Label(oneFrame,text="站點名稱:").grid(row=0,column=0,sticky="e")
            ttk.Label(oneFrame,text=sitename).grid(row=0,column=1,sticky="w")

            ttk.Label(oneFrame,text="行政區:").grid(row=1,column=0,sticky="e")
            ttk.Label(oneFrame,text=area).grid(row=1,column=1,sticky="w")

            ttk.Label(oneFrame,text="時間:").grid(row=2,column=0,sticky="e")
            ttk.Label(oneFrame,text=infotime).grid(row=2,column=1,sticky="w")

            ttk.Label(oneFrame,text="地址:").grid(row=3,column=0,sticky="e")
            ttk.Label(oneFrame,text=address).grid(row=3,column=1,sticky="w")

            ttk.Label(oneFrame,text="總車輛數:").grid(row=4,column=0,sticky="e")
            ttk.Label(oneFrame,text=str(total)).grid(row=4,column=1,sticky="w")

            ttk.Label(oneFrame,text="可借:").grid(row=5,column=0,sticky="e")
            ttk.Label(oneFrame,text=str(rents)).grid(row=5,column=1,sticky="w")

            ttk.Label(oneFrame,text="可還:").grid(row=6,column=0,sticky="e")
            ttk.Label(oneFrame,text=str(returns)).grid(row=6,column=1,sticky="w")

            figure=draw_piechart(rents,returns)
            
            canvas =FigureCanvasTkAgg(figure,oneFrame)
            canvas.draw()
            canvas.get_tk_widget().grid(row=7,column=0,columnspan=2)
            
            self.__cleanCanvas(canvas)

            oneFrame.pack(side='left',expand=True,fill="both")
        

def draw_piechart(value1,value2:list):

        def func(pct, allvals):
            absolute = int(np.round(pct/100.*np.sum(allvals)))
            return f"{absolute:d}pcs - {pct:.1f}%"

        values=[value1,value2]
        labels=["Rend","Return"]
        colors=["green","red"]

        figure=plt.figure(figsize=(5,5),dpi=72)
        axes =figure.add_subplot()
        axes.pie(values,colors=colors,labels=labels
            ,textprops=dict(color="w"),labeldistance=1.2,shadow=True
            ,autopct=lambda pct: func(pct, values))

        axes.legend(title="rate:",
                        loc="center left",
                        bbox_to_anchor=(0, 0, 0, 2))  

        return figure
