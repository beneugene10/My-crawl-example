import requests
import pandas as pd
import json
#開始爬取資料,並且轉換成dic型態
air=requests.get("http://opendata.epa.gov.tw/webapi/Data/REWIQA/?$orderby=SiteName&$skip=0&$top=1000&format=json")
Air=air.json()
sitename =[i["SiteName"] for i in Air]
county =[i["County"]for i in Air]
aqi =[i["AQI"]for i in Air]
Air1={"Sitename":sitename,
      "County":county,
      "AQI":aqi}
db=pd.DataFrame(Air1)
#先經過編碼,以免輸出亂碼
db.to_csv("C:/Users/beneu\Desktop/空氣品質指標(AQI).csv",encoding="utf_8_sig")