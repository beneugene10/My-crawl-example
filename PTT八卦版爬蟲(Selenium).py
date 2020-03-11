from bs4 import BeautifulSoup
from selenium import webdriver
import requests

driver=webdriver.Chrome("/Users/beneu/Downloads/chromedriver" )
driver.get("https://www.ptt.cc/bbs/Gossiping/index1.html")
driver.find_element_by_xpath("//body/div[2]/form[@action='/ask/over18']//button[@name='yes']").click()
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
#選擇想爬取頁數,爬n頁點n-1次下頁
pages=int(input("請輸入想收集幾頁PTT八卦版的資料:"))
page=0
nextpage =0
for i in range(pages):
    html = driver.current_url
    geturl()
    nextpage+=1
    page+=1
    print("第{0}頁\n".format(page))
    if pages>1 and nextpage!=pages:
        driver.find_element_by_css_selector(".wide:nth-child(3)").click()
