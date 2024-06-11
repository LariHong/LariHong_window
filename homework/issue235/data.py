import requests 
from requests import Response,JSONDecodeError
from pydantic import RootModel,BaseModel,field_serializer
from datetime import datetime

def GetDownloadJson():
    ubike_url="https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json"
    try:
        res=requests.get(ubike_url)
    except Exception :
        raise("連線失敗")
    else:
        if res.status_code == 200:
            try:
                #此已經是普通字串 雖然是json格式
                all_data:dict[any]= res.json()
                return all_data
            except JSONDecodeError:
                raise Exception("api_key為測試用,連線已至上限,請稍後再試,josn格式錯誤")
        else:
            raise Exception("下載狀態不是200")

class Info(BaseModel):
    sna:str
    sarea:str
    mday:datetime
    ar:str
    act:bool
    updateTime:datetime
    total:int
    available_rent_bikes:int
    latitude:float
    longitude:float
    available_return_bikes:int

    @field_serializer("mday","updateTime")
    def serialize_str(self,value:datetime) -> str:
        return value.strftime('%Y-%m-%d %p%I:%M:%S')
    
    @field_serializer("sna")
    def serialize_split(self,value:str) -> str:
        return value.split("_")[-1]
    
    @field_serializer("act")
    def serialize_act(self,value:bool) -> str:
        if bool:
            return "營業中"
        else:
            return "維護中"

class Youbike_Data(RootModel):
    root:list[Info]


def load_data()->list[dict]:

    alldata=GetDownloadJson()
    youbike_data=Youbike_Data.model_validate(alldata)
    data = youbike_data.model_dump()

    return data