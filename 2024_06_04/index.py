from pprint import pprint
import tkinter as tk
from tkinter import ttk,messagebox
from ttkthemes import ThemedTk
from tkinter.simpledialog import Dialog
import tools

class Window(ThemedTk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title("AQI顯示")
        #字體設定
        # self.option_add("*Font","微軟正黑體 40")

        #ttk 要先自訂出實體 再丟入去使用
        style =ttk.Style()
        style.configure("Top.TFrame")
        style.configure("Top.TLabel",font=("helvetica",25))

        #標題的frame
        title_frame=ttk.Frame(self,style="Top.TFrame",width="200",height="200",borderwidth=10,relief="groove")
        ttk.Label(title_frame,text="全台空氣品質指標(AQI)",style="Top.TLabel").pack(expand=True,fill="y")
        title_frame.pack(ipadx=100,ipady=30,padx=10,pady=10)

        #按鈕的frame
        fuc_frame=ttk.Frame(self,style="Top.TFrame",width="200",height="200",borderwidth=10,relief="groove")
        ttk.Button(fuc_frame,text="AQI品質最好的5個",command=self.click1).pack(side="left",expand=True)
        ttk.Button(fuc_frame,text="AQI品質最差的5個",command=self.click2).pack(side="left",expand=True)
        ttk.Button(fuc_frame,text="pm2.5品質最好的5個",command=self.click3).pack(side="left",expand=True)
        ttk.Button(fuc_frame,text="pm2.5品質最差的5個",command=self.click5).pack(side="left",expand=True)
        fuc_frame.pack(ipadx=100,ipady=30,padx=10,pady=10)

    def click1(self):
        messagebox.showinfo("information","XXXXXXXXXXXX")

    def click2(self):
        messagebox.showerror("error","YYYYYYYYYYYYYYY")

    def click3(self):
        messagebox.showwarning("警告","ZZZZZZZZZZZZZZZZZZZ")

    def click4(self):
        messagebox.askyesno("Y/N","WWWWWWWWWWWWWWW")

    def click5(self):
        ShowInfo(parent=self,title="這是Dialog")

class ShowInfo(Dialog):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
    #顯示內容文
    def body(self,master):
        #內容間距 和 不能打字
        text=tk.Text(self,height=8,padx=10,pady=10,font=("helvetica",25),width=40)
        text.pack()
        #先放字再關閉
        text.insert(tk.INSERT,"內容文")
        text.config(state='disabled')
        

        return None

def main():
    
    # try:
    #     all_data:dict[any]=tools.GetDownload_Json()
    # except Exception as error:
    #     print(error)
    # else:
    #     data:list[dict]=tools.get_date(all_data)
    #     pprint(data)

    #theme樣式
    window = Window(theme="itft1")
    window.mainloop()

if __name__ =="__main__":
    main()