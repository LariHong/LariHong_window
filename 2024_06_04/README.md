>## [參考網址](https://data.gov.tw/dataset/151824)
>## [參考網址](https://pypi.org/project/requests/)
>## [參考網址](https://github.com/roberthsu2003/python/tree/master/pydantic)
>## [參考網址](https://ttkthemes.readthedocs.io/en/latest/themes.html)
>## [參考網址](https://github.com/roberthsu2003/pythonWindow/tree/master/tkinter%E5%B8%B8%E7%94%A8%E4%BB%8B%E9%9D%A2%E9%A1%9E%E5%88%A5)
>## [參考網址](https://github.com/roberthsu2003/pythonWindow/tree/master/%E5%B0%8D%E8%A9%B1%E6%A1%86%E5%92%8C%E8%A1%A8%E5%96%AE)

>### requests
    requests.Response.text 這個會是純文字

>### pprint套件  Response().json()轉換 JSONDecodeError判斷

```
import requests
from requests import Response,JSONDecodeError
from pprint import pprint
aqi_url='https://data.moenv.gov.tw/api/v2/aqx_p_488?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=datacreationdate desc&format=JSON'

try:
    res:Response=requests.get(aqi_url)
except Exception as error:
    print(error)
else:
    if res.status_code ==200:
        #任何的資料結構
        #Response有一個method json 直接轉
        try:
            all_data:dict[any]= res.json()
            #這是dict python資料結構
            pprint(all_data)
        except JSONDecodeError:
            print("api_key為測試用,連線已至上限,請稍後再試,josn格式錯誤")
    else:
        print("下載狀態不是200")
```

> ### 將上述轉為 自訂function
    function 失敗就會跳出 raise Exception
```
import requests
from requests import Response,JSONDecodeError
from pprint import pprint

def GetDownload_Json()->dict[any]:

    aqi_url='https://data.moenv.gov.tw/api/v2/aqx_p_488?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=datacreationdate desc&format=JSON'

    try:
        res:Response=requests.get(aqi_url)
    except Exception:
        #GetDownload_Json 失敗會執行raise
        raise Exception("連線失敗")
    else:
        if res.status_code ==200:
            try:
                all_data:dict[any]= res.json()
                return all_data
            except JSONDecodeError:
                raise Exception("api_key為測試用,連線已至上限,請稍後再試,josn格式錯誤")
        else:
            raise Exception("下載狀態不是200")

try:
    all_data=GetDownload_Json()
    pprint(all_data)
except Exception as error:
    print(error)
```

> ### RootModel 的說明
```
from pydantic import BaseModel,Field,RootModel

#BaseModel 用於根是dict
class Site(BaseModel):
    site_name:str=Field(alias="sitename")
    county:str
    aqi:int
    status:str
#RootModel 用於根是list
class Records(RootModel):
    root:list[Site]

#model_validate這是讀python 的資料結構
records:Records=Records.model_validate(all_data['records'])

data=records.model_dump()
```

> ### field_validator 這次將 pm25轉成str 
```
from pydantic import BaseModel,Field,RootModel,field_validator

#BaseModel 用於根是dict
class Site(BaseModel):
    site_name:str=Field(alias="sitename")
    county:str
    aqi:int
    status:str
    
    #pydantic str 可以轉成float
    pm25:float=Field(alias="pm2.5")
    @field_validator("pm25",mode="before")
    @classmethod
    def ToZero(cls,value:str)->str:
        if value=="":
            return "0.0"
        else:
            return value
        
#RootModel 用於根是list
class Records(RootModel):
    root:list[Site]

#model_validate這是讀python 的資料結構
records:Records=Records.model_validate(all_data['records'])

data=records.model_dump()

pprint(data)
```

> ### module內 可以放 class function
    建立 tools.py 當作module

```
import requests
from requests import Response,JSONDecodeError
from pydantic import BaseModel,Field,RootModel,field_validator

class Site(BaseModel):
    site_name:str=Field(alias="sitename")
    county:str
    aqi:int
    status:str
    data:str=Field(alias="datacreationdate")
    pm25:float=Field(alias="pm2.5")
    @field_validator("pm25",mode="before")
    @classmethod
    def ToZero(cls,value:str)->str:
        if value=="":
            return "0.0"
        else:
            return value
        
class Records(RootModel):
    root:list[Site]

def GetDownload_Json()->dict[any]:

    aqi_url='https://data.moenv.gov.tw/api/v2/aqx_p_488?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=datacreationdate desc&format=JSON'

    try:
        res:Response=requests.get(aqi_url)
    except Exception:
        #GetDownload_Json 失敗會執行raise
        raise Exception("連線失敗")
    else:
        if res.status_code ==200:
            try:
                all_data:dict[any]= res.json()
                return all_data
            except JSONDecodeError:
                raise Exception("api_key為測試用,連線已至上限,請稍後再試,josn格式錯誤")
        else:
            raise Exception("下載狀態不是200")

def get_date(all_data)->list[dict]:
    records:Records=Records.model_validate(all_data['records'])
    data:list[dict]=records.model_dump()

    return data
```

> ### ttkthemes

```
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk

class Window(ThemedTk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title("AQI顯示")
        self.geometry("500x300")
        ttk.Button(self,text="Quit",command=self.destroy).pack()

def main():
    #theme樣式
    window = Window(theme="arc")
    window.mainloop()
```

> ### tkinter frame
```
#ttk 要先自訂出實體 再丟入去使用
style =ttk.Style()
style.configure("Top.TFrame",background="#F00")
style.configure("Top.TLabel",font=("helvetica",25))


/*
#標題架構
title_frame

label(title_frame).pack

title_frame.pack
*/

#標題的frame
title_frame=ttk.Frame(self,style="Top.TFrame",width="200",height="200")
#會依據這個pack 為基準 
#全部擴展 + 上下填滿(讓文字置中)
ttk.Label(title_frame,text="全台空氣品質指標(AQI)",style="Top.TLabel").pack(expand=True,fill="y")
#ipadx 是對frame 就是padding  padx是margin
title_frame.pack(ipadx=100,ipady=30,padx=10,pady=10)


/*
#標題架構
fuc_frame

Button(fuc_frame).pack
Button(fuc_frame).pack
Button(fuc_frame).pack
Button(fuc_frame).pack

fuc_frame.pack
*/
#按鈕的frame
fuc_frame=ttk.Frame(self,style="Top.TFrame",width="200",height="200",borderwidth=10,relief="groove")
ttk.Button(fuc_frame,text="AQI品質最好的5個").pack(side="left",expand=True)
ttk.Button(fuc_frame,text="AQI品質最差的5個").pack(side="left",expand=True)
ttk.Button(fuc_frame,text="pm2.5品質最好的5個").pack(side="left",expand=True)
ttk.Button(fuc_frame,text="pm2.5品質最差的5個").pack(side="left",expand=True)
fuc_frame.pack(ipadx=100,ipady=30,padx=10,pady=10)

#一些 messagebox
from tkinter import ttk,messagebox
def click1(self):
        messagebox.showinfo("information","XXXXXXXXXXXX")

def click2(self):
    messagebox.showerror("error","YYYYYYYYYYYYYYY")

def click3(self):
    messagebox.showwarning("警告","ZZZZZZZZZZZZZZZZZZZ")

def click4(self):
    messagebox.askyesno("Y/N","WWWWWWWWWWWWWWW")
```

>### Dialog
```
import tkinter as tk
from tkinter import ttk
from tkinter.simpledialog import Dialog


def click5(self):
    ShowInfo(parent=self,title="這是Dialog")

class ShowInfo(Dialog):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
    #顯示內容文
    def body(self,master):
        #內容間距 和 不能打字
        text=tk.Text(self,height=8,state='disable',padx=10,pady=10)
        text.pack()
        

        return None
```
