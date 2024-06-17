[參考網址](https://www.pythontutorial.net/tkinter/)

> ## grid pack 只能在frame 使用其中一個
```
#mainFrame=======================================start
mainFrame = ttk.Frame(self,borderwidth=1,relief='groove')
#在mainFrame已使用pack() 不可以再用grid
ttk.Label(mainFrame,text="台北市YouBike2.0及時資料",font=('arial',25)).pack()



        #tableFrame======================================start
        tableFrame = ttk.Frame(mainFrame)

        columns = ('sna', 'sarea', 'mday','ar','total','rent_bikes','retuen_bikes')
        #selectmode="browse" 只能單選
        tree = ttk.Treeview(tableFrame, columns=columns, show='headings',selectmode="browse")
        # define headings
        tree.heading('sna', text='站點')
        tree.heading('sarea', text='行政區')
        tree.heading('mday', text='時間')
        tree.heading('ar', text='地址')
        tree.heading('total', text='總數')
        tree.heading('rent_bikes', text='可借')
        tree.heading('retuen_bikes', text='可還')


        # add data to the treeview
        for site in self.data:

            tree.insert('', tk.END,values=(site['sna'],site['sarea'],site['mday'],site['ar'],site['total'],site['rent_bikes'],site['retuen_bikes']))

        #此處為tableFrame所以可以用grid
        tree.grid(row=0, column=0, sticky='nsew')

        scrollbar = ttk.Scrollbar(tableFrame, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')

        #tableFrame======================================end
        tableFrame.pack(expand=True,fill=tk.BOTH)



#mainFrame=======================================end
mainFrame.pack(expand=True,fill=tk.BOTH,padx=10,pady=10)
```

> ## Command Binding
```
# 使用者事件
    tree.bind('<<TreeviewSelect>>',self.item_selected)

    def item_selected(self,event):
        #會抓到呼叫event的
        tree=event.widget
        #確認tree是否 為ttk.Treeview實例出來的
        print(isinstance(tree,ttk.Treeview))

        #tree.selection() 是一個tuple
        for selected_item in tree.selection():
            #獲得一的dict資料
            item=tree.item(selected_item)
            record:list =item["values"]
            a,b=FilterData.get_selected_site(sna=record[0],data=self.data)

```

> ## python filter

```
class FilterData():
    @staticmethod
    def get_selected_site(sna:str,data:list[dict])->tuple[float]:
        
        def functionA(item:dict)->bool:
            if item["sna"] == sna:
                return True
            else:
                return False 
        #內建的filter 如果給function 那就會將data 每一個元素依序 丟入去過濾
        right_list:list[dict]=list(filter(functionA,data))

        return (right_list[0]["latitude"],right_list[0]["longitude"])
```

> ## lambda

```
true_value if bool condition else false_value


class FilterData():
    @staticmethod
    def get_selected_site(sna:str,data:list[dict])->tuple[float]:
        
        right_list:list[dict]=list(
            filter(
                lambda item:True if item["san"] == sna else False,data
                )
            )

        return (right_list[0]["latitude"],right_list[0]["longitude"])
```

```
from pydantic import RootModel,BaseModel,field_serializer,Field,ConfigDict

#加這行 就能夠左邊名  右邊名都能使用
model_config =ConfigDict(
    populate_by_name=True
)

```

> ## 加入 地圖套件
requirements.txt  插入tkintermapview

$ pip install tkintermapview

import tkinter as tk
import tkintermapview as tkmap

```
map_frame=ttk.Frame(contain_frame)
#建立地圖
map_widget=tkmap.TkinterMapView(map_frame,width=800,height=600,corner_radius=0)
map_widget.pack()
#標定座標
marker=map_widget.set_position(self.site_data.latitude,self.site_data.longitude,marker=True)
marker.set_text(f"行政區 {self.site_data.sarea}\n站點: {self.site_data.sna}\n總車輛: {self.site_data.total}\n可借: {self.site_data.rent_bikes}\n可還: {self.site_data.retuen_bikes}")
#兩點 畫線
start_point =self.site_data.latitude,self.site_data.longitude
end_point =start_point[0],start_point[1]-0.002
path=map_widget.set_path([start_point,end_point])

map_widget.set_zoom(30)
map_frame.pack(expand=True,fill="both")
```
> ## [updata參考網址](https://github.com/roberthsu2003/pythonWindow/blob/master/%E5%AF%A6%E9%9A%9B%E6%A1%88%E4%BE%8B/%E5%8F%B0%E5%8C%97%E5%B8%82youbike1/youbike.py)
