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