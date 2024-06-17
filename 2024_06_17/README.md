[參考網址](https://github.com/roberthsu2003/PythonForDataAnalysis)

[參考網址](https://matplotlib.org/stable/api/index)

> ## 自訂類別自訂類別 使用ttk.Frame
```
import tkinter as tk
from tkinter import ttk
from tkinter import Misc


class Example(ttk.Frame):
    def __init__(self,master:Misc,**kwargs):
        super().__init__(master=master,**kwargs)
        master.title('Lines')   


def main():
    window = tk.Tk()
    Example(window)
    window.geometry("400x250")
    window.mainloop()

if __name__ == "__main__":
    main()
```

> ## 圖形說明
```
    def __create_line(self):
        # 給一個canvas
        canvas = tk.Canvas(self)
        # 從左上為基準往左+ 往下+
        #兩點畫一線
        canvas.create_line(15, 30, 200,30)
        #dash線 實線長度 空白長度
        canvas.create_line(300,35, 300, 200,dash=(8,2))
        #畫三角形 但給他終點
        canvas.create_line(55,85,155,85,105,180,55,85)
        canvas.pack(expand=True,fill='both')

    
    def create_graph(self):
        canvas = tk.Canvas(self)
        #創矩形 outline邊框線顏色
        canvas.create_rectangle(30,10,120,80,outline='#000',fill='#fb0')
        #創中文
        canvas.create_text(40, 40, text='中文測試', anchor='nw', fill='#0a0', font=('Arial', 18, 'bold','italic'))
        #創橢圓形 outline邊框線顏色 width 邊框寬度
        canvas.create_oval(150,10,200,60,outline='#000',fill='#1f1',width=2)
            
        canvas.pack(expand=True,fill='both')   

    #from PIL import Image,ImageTk
    def create_photo(self):
        canvas = tk.Canvas(self)
        # 插入圖片 但是要存入attribute 要不然資料會消失
        self.img=Image.open('tvdi.png')   
        self.tvdi =ImageTk.PhotoImage(self.img)
        canvas.create_image(210,10,anchor="nw",image=self.tvdi)
        canvas.pack(expand=True,fill='both')

    

    #pip install Pillow 如果沒有 PIL
    #requirements.txt 新增 matplotlib numpy pandas 

    
```
