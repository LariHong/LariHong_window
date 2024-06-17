from ttkthemes import ThemedTk
import tkinter as tk
from tkinter import ttk, messagebox,Misc
import data
from data import FilterData,Info
from tools import CustomMessagebox
import tools2

class Window(ThemedTk):
    @property
    def data(self) -> list[dict]:
        return self.__data
    
    def __init__(self,theme:str='arc',**kwargs):
        super().__init__(theme=theme,**kwargs)
        self.title('台北市YouBike2.0及時資料')
        try:
            self.__data = data.load_data()
            
        except Exception as e:
            messagebox.showwarning(title='警告',message=str(e))
        
        self._display_interface()
        
    def _display_interface(self):
        
        mainFrame = ttk.Frame(self,borderwidth=1,relief='groove')

        ttk.Label(mainFrame,text="台北市YouBike2.0及時資料",font=('arial',25)).pack()
        #=================================
        tableFrame = ttk.Frame(mainFrame)

        columns = ('sna', 'sarea', 'mday','ar','total','rent_bikes','retuen_bikes')
        tree = ttk.Treeview(tableFrame, columns=columns, show='headings')
        # define headings
        tree.heading('sna', text='站點')
        tree.heading('sarea', text='行政區')
        tree.heading('mday', text='時間')
        tree.heading('ar', text='地址')
        tree.heading('total', text='總數')
        tree.heading('rent_bikes', text='可借')
        tree.heading('retuen_bikes', text='可還')

        # 定義欄位寬度
        tree.column('sarea',width=70,anchor=tk.CENTER)
        tree.column('mday',width=120,anchor=tk.CENTER)
        tree.column('ar',minwidth=100)
        tree.column('total',width=50,anchor=tk.CENTER)
        tree.column('rent_bikes',width=50,anchor=tk.CENTER)
        tree.column('retuen_bikes',width=50,anchor=tk.CENTER)
        
        # 使用者事件
        tree.bind('<<TreeviewSelect>>',self.item_selected)
        # add data to the treeview
        for site in self.data:
            tree.insert('', tk.END,
                        values=(site['sna'],site['sarea'],site['mday'],site['ar'],site['total'],site['rent_bikes'],site['retuen_bikes']))
        
        tree.grid(row=0, column=0, sticky='nsew')

        scrollbar = ttk.Scrollbar(tableFrame, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')

        tableFrame.pack()
        #======================================
        self.pieChartFrame = tools2.PieChaetFrame(mainFrame)
        self.pieChartFrame.pack()
        mainFrame.pack(padx=10,pady=10)

    def item_selected(self,event):
        #會抓到呼叫event的
        tree=event.widget
        #tree.selection() 是一個tuple
        self.bikeValues=[]
        records:list[list]=[]
        #[:3]代表只可以選取3個，超過也是3個
        for selected_item in tree.selection()[:3]: 
            #獲得一的dict資料
            item=tree.item(selected_item)
            record:list =item["values"]
            records.append(record)
            self.pieChartFrame.infos=records


def main():
    #讓終端機不會蹦潰
    def on_closing():
        print("手動關閉視窗")
        window.destroy()
        window.quit()

    window = Window(theme='breeze')
    window.protocol("WM_DELETE_WINDOW",on_closing)
    window.mainloop()

if __name__ == '__main__':
    main()