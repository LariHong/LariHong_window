>### class 基本三元素
* class
    * attribute

    * property

    * method(實體方法)

### 範例
```
class Person():
    #如果我要有無參建構子就可以設定=None
    def __init__(self,name:str=None):
        # attribute(屬性)
        self.name =name
    def __repr__(self):
        return f"我是Person實體,我的名字= {self.name}"

    #繼承 Person
class Student(Person):
    #設定預設值要放在最後面
    def __init__(self,chinese:int=None,math:int=None,english:int=None, name: str = None):
        super().__init__(name=name)
        #attri可以被修改
        self.__chinese=chinese
        self.__math=math
        self.__english=english
        
    #property可以設定 不能改 
    @property
    def chinese(self):
        return self.__chinese
    
    @property
    def math(self):
        return self.__math
    
    @property
    def english(self):
        return self.__english
    
    @property
    def scores(self):
        return self.chinese+self.english+self.math
    
    def __repr__(self):
        message =f"我是Student實體,我的名字 {self.name}\n"
        message+=f"我的國文分數: {self.chinese}\n"
        message+=f"我的數學分數: {self.math}\n"
        message+=f"我的英文分數: {self.english}"

        return message

    #自訂實體方法(method)
    def average(self):
        return self.scores / 3   
```


>### 這是raise錯誤 的其中一個錯誤

```
IndexError                                Traceback (most recent call last)
Cell In[12], line 1
----> 1 l1[5]

IndexError: list index out of range
```

>### 解決錯誤的方法(但還是有錯要修正)
```
try:
    #檢查有沒有 raise Error
except 明確的錯誤1:
    #解決 try中丟出的 Error
except 明確的錯誤2:
    #解決 try中丟出的 Error
    .
    .
    .
except Exception:
    #解決 try中丟出的 Error
```

### list 補充
是一種 **sequence資料架構**
>list[index] => 叫 subscript

### dict 補充
是一種 **mapping資料架構**

python中 value=dict['key'] **要用' '**   

### in 的補充
in sequence_value
list1=[1,2,3,4]
if 2 in list1  #2為**value**

in mapping[key]
dic={"one":1, "two":2,"three":3,}
if one in dic  #2為**value**

### 上述的實體方法
>抓出裡面的元素  dict內的是一組tuple 所以有key value
```
for key,value in dic.items():
    print(f"key= {key} ,value= {value}" )
```