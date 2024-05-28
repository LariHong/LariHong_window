### 檔案讀取
>檔案開啟後 一定要關閉
```
#此為實體
file = open('檔案名', 'w', encoding="utf-8")

#檔案是否開啟
file.closed
```

>with ... as ...
```
#這段會自己關閉檔案
with open('names.txt',encoding="utf-8") as file2:
    pass
```
>function的hint
```
# -> 為function 的hint
def get_names()->list[str]:
    with open('names.txt',encoding="utf-8") as file3:

        content2:str=file3.read()

    names:list[str]=content2.split()

    return names
```
>定義出主程式的進入點
```
#目前檔案為 index.py 如果是執行這個檔案 __name__ == __main__  為這個index.py
if __name__ =="__main__":
    names:list[str]=get_names()
    print("__main__")
```
## Tkinter 
[Tkinter說明書](https://docs.python.org/zh-tw/3/library/tk.html)

[徐老師的步驟](https://github.com/roberthsu2003/pythonWindow/tree/master/%E5%88%9D%E8%A6%8Btkinter)

```
import tkinter as tk

#內建的有一個 class Tk  在 tkinter內
window:tk.Tk=tk.Tk()
#會讓視窗一直執行
window.title("視窗名")
window.mainloop()
```
## 使用繼承Tkinter
```
class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("我是視窗2")


window2:tk.Tk=Window()
window2.mainloop()
```

## **kwargs的多參數用法
```
class Window(tk.Tk):
    #**xxxx   可以放入父類別的所有參數 也可以不放入
    def __init__(self,title:str=None,**kwargs):
        super().__init__(**kwargs)
        self.title(title)
# __init__ 內沒有screenName 因為加入**kwargs 
window2:tk.Tk=Window("123",screenName="789")
window2.mainloop()
```

## Tkinter 有一個 ttk 其中ttk.Label.pack() 會有個新視窗
```
class Window2(tk.Tk):

    def __init__(self,title:str=None,**kwargs):
        super().__init__(**kwargs)
        self.title(title)
        laber:ttk.Label=ttk.Label(self,text="我是ttk")
        laber.pack()

window3:tk.Tk=Window2()
window3.mainloop()
```