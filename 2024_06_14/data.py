import requests 
from requests import Response,JSONDecodeError
from pydantic import RootModel,BaseModel,field_serializer,Field,ConfigDict
from datetime import datetime

# 加底線代表對內function
def __GetDownloadJson():
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
    rent_bikes:int=Field(alias="available_rent_bikes")
    latitude:float
    longitude:float
    retuen_bikes:int=Field(alias="available_return_bikes")
    #加這行 就能夠左邊名  右邊名都能使用
    model_config =ConfigDict(
        populate_by_name=True
    )

    #暫時無快速解決之方案 先放著
    # @field_serializer("mday","updateTime")
    # def serialize_str(self,value:datetime) -> str:
    #     return value.strftime('%Y-%m-%d %p%I:%M:%S')
    
    # @field_serializer("sna")
    # def serialize_split(self,value:str) -> str:
    #     return value.split("_")[-1]
    
    # @field_serializer("act")
    # def serialize_act(self,value:bool) -> str:
    #     if bool:
    #         return "營業中"
    #     else:
    #         return "維護中"

class Ubike_Data(RootModel):
    root:list[Info]


def load_data()->list[dict]:

    alldata=__GetDownloadJson()
    youbike_data=Ubike_Data.model_validate(alldata)
    data = youbike_data.model_dump()

    return data



class FilterData():
    @staticmethod
    def get_selected_site(sna:str,data:list[dict])->Info:
        
        #內建的filter 如果給function 那就會將data 每一個元素依序 丟入去過濾
        right_list:list[dict]=list(filter(lambda item:True if item["sna"] == sna else False,data))
        data:dict=right_list[0]
        return Info.model_validate(data)