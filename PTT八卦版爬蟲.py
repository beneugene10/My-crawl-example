from bs4 import BeautifulSoup
import requests

#把標題,作者,日期顯示出來,並回傳下一頁連結
def geturl():
    headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
             "cookie":"over18=1" }
    res=requests.get(html,headers=headers)
    soup=BeautifulSoup(res.text,"html.parser")
    title=soup.select(".title a")
    author=soup.select(".author")
    date=soup.select(".date")
    for i,j,k in zip(title,author,date):
        print(i.text,j.text,k.text)
    nextpage=soup.select(".wide:nth-child(3)")
    url=nextpage[0]["href"]
    return url
#選擇想爬取頁數
page=0
html="https://www.ptt.cc/bbs/Gossiping/index1.html"
for i in range(int(input("請輸入想收集幾頁PTT八卦版的資料:"))):
    html="https://www.ptt.cc"+geturl()
    page+=1
    print("第{0}頁\n".format(page))