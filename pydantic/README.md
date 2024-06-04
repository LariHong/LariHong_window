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
    """XXXXXXXXXXXX""" #說明文字 or 多行字串格式

    #在dataclass內這叫 field 但實際上是attribute
    name: str
    unit_price: float
    quantity_on_hand: int = 0

item =InventoryItem(name="AAA",unit_price=150.5)
print(item)
```

# pydantic 作法
>pydantic 好處是 如果格是錯誤 or 資料不足 可以靠它補齊
>pydantic 會自動轉換格式

>### pydantic 的基礎宣告
```
from pydantic import BaseModel

class InventoryItem(BaseModel):
    """Class for keeping track of an item in inventory.""" #說明文字

    #在dataclass內這叫 field 但實際上是attribute
    name: str
    unit_price: float
    quantity_on_hand: int = 0

#pydantic 中設定了 unit_price 為float  你設定了字串15.5 但會自動轉型
item1 = InventoryItem(name="XXX",unit_price="15.5")

#python 如果 "10.5"  要轉成int 就要 int(float("10.5"))
```
>### pydantic的ValidationError
```
# 這裡的quantity_on_hand="10.5" 會raise ValidationError
# quantity_on_hand="10" 則會正常
from pydantic import ValidationError
try:
    item2 = InventoryItem(name="XXX",unit_price="15.5",quantity_on_hand="10.5")
    print(item2)
except ValidationError as e:
    print(e)
```
>### model_valdate(dict) model_valdate_json(json格式的字串) 用法
```
#使用class method 建立實體
#model_valdate(dict)
#model_valdate_json(json格式的字串)

#dict的 key 要用字串
data:dict={
    "name":"手機套1",
    "unit_price":"140.3",
    "quantity_on_hand":"13"
}

try:
    item3=InventoryItem.model_validate(data)
except ValidationError as e:
    print(e)
else:
    print(item3)


data_json:str='''{
    "name":"手機套2",
    "unit_price":"144.3",
    "quantity_on_hand":"17"
}'''

try:
    item4=InventoryItem.model_validate_json(data_json)
except ValidationError as e:
    print(e)
else:
    print(item4)
```
>### optional的解釋
```
class InventoryItem2(BaseModel):
    name: str
    unit_price: float
    #設定 如果沒有接收東西時  給他 None型別 值None
    quantity_on_hand: int |None= None #optional (資料可有可無)

data_json2:str='''{
    "name":"手機套3",
    "unit_price":"144.3"
}'''

item6=InventoryItem2.model_validate_json(data_json2)
print(item6)
```

>### Field 的用法
```
from pydantic import BaseModel,Field

data= '''{
    "id":100,
    "First Name":"John",
    "LASTNAME":"Smith",
    "age in years":42
}
'''

data2 = '''{
    "id":101,
    "First Name":"Aohn",
    "LASTNAME":"Bmith"
}
'''

class Person(BaseModel):
    # 使用Field(alias) 將一些系統不符合規矩的給合理化
    id_:int=Field(alias="id")
    first_name:str=Field(alias="First Name")
    last_name:str=Field(alias="LASTNAME")
    age:int|None=Field(alias="age in years",default=None)


p1=Person.model_validate_json(data)
print(p1)

p2 = Person.model_validate_json(data2)
print(p2)
```
>### 如何建立多層架構
```
data3:dict ={
    "firstName": "Arthur",
    "lastName": "Clarke",
    "born":{
        "place":{
            "country":"Lunar Colony",
            "city": "Central City"
        },
        "date":"2001-01-01"
    }
}

class Place(BaseModel):
    country:str
    city:str

class Born(BaseModel):
    place:Place
    date:str

class Site(BaseModel):
    first_name:str=Field(alias="firstName")
    last_name:str=Field(alias="lastName")
    born:Born

s1:Site=Site.model_validate(data3)
print(s1)
print(s1.born.place.country)
print(s1.born.place.city)
```

>### 多層資料結構 只獲取部分資料
```
from pydantic import BaseModel,Field

#可以只獲取 我要的資料就好
class Site(BaseModel):
    sitename:str
    county:str
    aqi:int
    status:str

class AQI(BaseModel):
    records:list[Site]

aqi1_data:AQI=AQI.model_validate_json(res.text)
records:list[Site]=aqi1_data.records
print(aqi1_data)

for record in records:
    print(record)
```
># **主體是這邊 轉成python的格式**
```
#轉成 python 的資料結構
all_data:dict=aqi1_data.model_dump()
```
>#
```
#使用field_validator
from pydantic import BaseModel,Field,ValidationError,field_validator

#可以只獲取 我要的資料就好
class Site(BaseModel):
    sitename:str
    county:str
    aqi:int
    status:str
    # 不管要不要驗證都會錯 因為它會自動驗證
    # pm25:float =Field(alias="pm2.5",validate_default=None)

    /*
    field_validator 就是要綁定 
    @field_validator()
    @classmethod
    */
    -----------------------------------------
    pm25:float =Field(alias="pm2.5")
    co:float
    #先做這邊的驗證  再去pm25:float驗證
    @field_validator('pm25','co',mode='before')
    @classmethod
    def to_zero(cls,value:str)->float:
        if value == "":
            return 0.0
        else:
            return float(value)
    ----------------------------------------

class AQI(BaseModel):
    records:list[Site]
try:
    aqi1_data:AQI=AQI.model_validate_json(res.text)
except ValidationError as e:
    print(e)
except Exception as e:
    print(f"不知名的錯誤{e}")
else:
    records:list[Site]=aqi1_data.records
    print(aqi1_data)

    for record in records:
        print(record)
```
### [線上看json參考網址](https://jsonviewer.stack.hu/)
### module.requests
>[參考網址](https://pypi.org/project/requests/)
>[參考網址](https://github.com/roberthsu2003/python/tree/master/pydantic)