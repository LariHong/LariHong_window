import requests
from requests import Response,JSONDecodeError
from pydantic import BaseModel,Field,RootModel,field_validator

class Site(BaseModel):
    site_name:str=Field(alias="sitename")
    county:str
    aqi:int
    status:str
    date:str=Field(alias="datacreationdate")
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