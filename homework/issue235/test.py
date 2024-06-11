import tkinter as tk
from tkinter import ttk

# 創建主窗口
root = tk.Tk()
root.title("Treeview 範例")

# 創建 Treeview 控制項
tree = ttk.Treeview(root, columns=("size", "modified", "owner"))

# 定義列
tree.column("#0", width=200, minwidth=150, stretch=tk.NO)
tree.column("size", width=100, minwidth=100, stretch=tk.NO)
tree.column("modified", width=150, minwidth=150, stretch=tk.NO)
tree.column("owner", width=100, minwidth=100, stretch=tk.NO)

# 定義列標題
tree.heading("#0", text="Name", anchor=tk.W)
tree.heading("size", text="Size", anchor=tk.W)
tree.heading("modified", text="Modified", anchor=tk.W)
tree.heading("owner", text="Owner", anchor=tk.W)

# 插入數據
tree.insert("", "end", text="example1.txt", values=("1 KB", "2023-01-01 10:00", "User1"))
tree.insert("", "end", text="example2.txt", values=("2 KB", "2023-01-02 11:00", "User2"))
tree.insert("", "end", text="example3.txt", values=("3 KB", "2023-01-03 12:00", "User3"))

# 將 Treeview 放置在主窗口中
tree.pack(pady=20, padx=20)

# 運行主循環
root.mainloop()