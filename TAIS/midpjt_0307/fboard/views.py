from django.shortcuts import render
import urllib.request
import requests
from bs4 import BeautifulSoup
from PIL import Image
from fboard.models import News_Info

# Create your views here.
def notification(request):
    return render(request, 'fboard/notification.html')

def notification_view(request):
    return render(request, 'fboard/notification_view.html')

def news(request):
    qs = News_Info.objects.all()
    qs.delete()
    
    firms = ["교통"]
    for firm in firms:
        url = f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={firms}"
        res = requests.get(url)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "lxml")
        soup_tit = soup.find_all("a", attrs={"class": "news_tit"})
        soup_info = soup.find_all("span", attrs={"class": "info"})
        soup_img =  soup.find_all("img",attrs = {"class":"thumb api_get"})
    #     dates = [ date.get_text() for date in soup.find_all('span', attrs={'class':'info'})] # 기사 작성일
        indx =0
        for tit, time,img in zip(soup_tit, soup_info,soup_img):
            if firm in tit.get_text():
                tit_box = []
                url_box = []
                img_box = []
    #             print(f"{tit.get_text()} {info.get_text()} {tit['href']}")
                print(tit.get_text())
                print(time.get_text())
                print(tit['href'])
                print(img['src'])
                indx +=1
                urllib.request.urlretrieve(img['src'], "이미지{}.jpg".format(indx))
                news_img = "이미지{}.jpg".format(indx)
                print(news_img)
                tit_box.append(tit.get_text())
                url_box.append(tit['href'])
                news_keyword = tit_box[0]
                news_content = url_box[0]
                qs = News_Info(news_keyword=news_keyword, news_img=news_img, news_content=news_content)
                qs.save()
    # news_img = img_box[0]
    
    # qs = News_Info(news_keyword=news_keyword, news_img=news_img, news_no='1',news_kind='1',news_content='1', weather_info='1' )
    
    return render(request, 'fboard/news.html')

# def community(request):
#     return render(request, 'community.html')

def news_page(request):
    return render(request, 'fboard/news_page.html')