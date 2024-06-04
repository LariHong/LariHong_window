>## [參考網址](https://data.gov.tw/dataset/151824)
>## [參考網址](https://pypi.org/project/requests/)
>## [參考網址](https://github.com/roberthsu2003/python/tree/master/pydantic)

### requests

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
