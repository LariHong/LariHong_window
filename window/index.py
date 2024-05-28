import tkinter as tk

def get_names()->list[str]:
    with open('names.txt',encoding="utf-8") as file3:
        content2:str=file3.read()

    names:list[str]=content2.split()
    return names

names = get_names()

for name in names:
    print(name)

#目前檔案為 index.py 如果是執行這個檔案 __name__ == __main__  為這個index.py
if __name__ =="__main__":
    names:list[str]=get_names()
    window:tk.Tk=tk.Tk()
    window.title("我是視窗")
    window.mainloop()