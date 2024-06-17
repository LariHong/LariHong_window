import tkinter as tk
from tkinter import Misc, ttk
from PIL import Image,ImageTk

class Graph(ttk.Frame):
    def __init__(self,master:Misc=None,**kwargs):
        super().__init__(master=master,**kwargs)
        self.__create_window()
        

    def __create_window(self):
        self.master.title("line")
        #下面兩種擇一  
        self.configure({'borderwidth':2,'relief':'groove'})
        # self.config({'borderwidth':2,'relief':'groove'})        
        # self['borderwidth'] = 2
        # self['relief'] = 'groove' 
        self.pack(expand=True,fill='both')
        #一開始就創立一個canvas
        self.canvas =tk.Canvas(self)
        self.canvas.pack(expand=True,fill="both")


    def create_line(self):
        # 從左上為基準往左+ 往下+
        #兩點畫一線
        self.canvas.create_line(15, 30, 200,30)
        #dash線 實線長度 空白長度
        self.canvas.create_line(300,35, 300, 200,dash=(8,2))
        #畫三角形 但給他終點
        self.canvas.create_line(55,85,155,85,105,180,55,85)

#多個 canvas 會以後面的為準 
class Graph2(ttk.Frame):
    def __init__(self,master:Misc=None,**kwargs):
        super().__init__(master=master,**kwargs)
        self.__create_window()
    
    def __create_window(self):
        self.master.title("graph") 
        self.configure({'borderwidth':2,'relief':'groove'})
        self.pack(expand=True,fill='both')
        #一開始就創立一個canvas
        self.canvas =tk.Canvas(self)
        self.canvas.pack(expand=True,fill="both")

    def create_graph(self):
        #創矩形 outline邊框線顏色
        self.canvas.create_rectangle(30,10,120,80,outline='#000',fill='#fb0')
        #創中文
        self.canvas.create_text(40, 40, text='中文測試', anchor='nw', fill='#0a0', font=('Arial', 18, 'bold','italic'))
        #創橢圓形 outline邊框線顏色 width 邊框寬度
        self.canvas.create_oval(150,10,200,60,outline='#000',fill='#1f1',width=2)
        
    def create_photo(self):
        
        # 插入圖片 但是要存入attribute 要不然資料會消失
        self.img=Image.open(r"D:\LariHong_window\2024_06_17\tvdi.png")   
        self.tvdi = ImageTk.PhotoImage(self.img)
        self.canvas.create_image(210,10,anchor='nw', image=self.tvdi) 

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
class Graph3(ttk.Frame):
    
    def __init__(self,master:Misc=None,**kwargs):
        super().__init__(master=master,**kwargs)
        
        self.__create_window()
        
    
    def __create_window(self):
        
        self.master.title("color")
        self.configure({'borderwidth':2,'relief':'groove'})
        self.pack(expand=True,fill='both')
        self.canvas =tk.Canvas(self)
        self.canvas.pack(expand=True,fill="both")

        self.draw_matplot()
    
    def draw_matplot(self):
        #figsize 指定图形的尺寸，单位为英寸 宽度为 5 英寸，高度为 4 英寸
        figure=plt.figure(figsize=(5,4),dpi=100)
        axes=figure.add_subplot()
        axes.plot([1,2,3,4,5],[2,3,5,7,11])
        axes.set_title("XXX")
        axes.set_xlabel("X")
        axes.set_ylabel("Y")
        #(要話的對象資料,父級畫面)
        canvas=FigureCanvasTkAgg(figure,self)
        canvas.draw()
        canvas.get_tk_widget().pack()

def main():
    # window:tk.Tk = tk.Tk()
    # garph=Graph(window)
    # garph.create_line()
    # window.geometry("400x250")
    # window.mainloop()

    # window2:tk.Tk = tk.Tk()
    # garph2=Graph2(window2)
    # garph2.create_graph()
    # garph2.create_photo()
    # window2.geometry("400x250")
    # window2.mainloop()

    window3:tk.Tk = tk.Tk()
    garph3=Graph3(window3)
    
    window3.geometry("600x500")
    window3.mainloop()
    


if __name__ ==  "__main__":
    main()