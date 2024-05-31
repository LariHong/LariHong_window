### @classmethod
```
class Student(Person):

    #cls代表這個class
    @classmethod 
    def get_student(cls,name:str,age:int,score:int):
        return Student(name=name,age=age,score=score)
    
    def __init__(self,name,age,score:int,**kwargs):
        super().__init__(name,age,**kwargs)
        self.score=score
    def get_level(self):
        if  self.score>=60:
            return "及格"
        else:
            return "不及格"
        
s1= Student("XXX",50,80)
print(s1.get_level())

s2=Student.get_student("SSS",30,59)
print(s2.get_level())
```

### dataclasses 作法
```
from dataclasses import dataclass

#python 內建的class 會自動產生 __init__ __repr__  
@dataclass
class InventoryItem:
    """XXXXXXXXXXXX""" #說明文字

    #在dataclass內這叫 field 但實際上是attribute
    name: str
    unit_price: float
    quantity_on_hand: int = 0

item =InventoryItem(name="AAA",unit_price=150.5)
print(item)
```

### pydantic 作法
>pydantic 好處是 如果格是錯誤 or 資料不足 可以靠它補齊
```
from pydantic import BaseModel

class InventoryItem(BaseModel):
    """Class for keeping track of an item in inventory.""" #說明文字

    #在dataclass內這叫 field 但實際上是attribute
    name: str
    unit_price: float
    quantity_on_hand: int = 0

item1 = InventoryItem(name="XXX",unit_price=15.5)
```
### [參考網址](https://jsonviewer.stack.hu/)
### module.requests
>[參考網址](https://pypi.org/project/requests/)