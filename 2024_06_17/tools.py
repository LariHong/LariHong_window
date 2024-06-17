from tkinter.simpledialog import Dialog
from tkinter import ttk
from tkinter import Misc
import tkinter as tk
import tkintermapview as tkmap
from data import Info


class CustomMessagebox(Dialog):    
    def __init__(self, parent:Misc, title:str,site:Info):        
        self.site_data=site
        super().__init__(parent=parent, title=title)

    def body(self, master):
        contain_frame = ttk.Frame(master)         
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
        contain_frame.pack(expand=True,fill="both",pady=10,padx=30)

    def apply(self):
        pass

    def buttonbox(self):
        box = ttk.Frame(self)
        self.ok_button = tk.Button(box, text="確定", width=10, command=self.ok, default=tk.ACTIVE)
        self.ok_button.pack(side=tk.LEFT, padx=5, pady=5)
        box.pack()

    def ok(self):
        super().ok()