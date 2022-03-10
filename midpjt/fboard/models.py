from datetime import datetime
from django.db import models


class Related_Info(models.Model) : # 연관 정보 db
    accident_no =  models.CharField(max_length = 8) # 사고 일련번호
    news_code_no =  models.CharField(max_length = 8) # 뉴스 일련번호 News_Info의 news_no 참조
    news_info = models.CharField(max_length = 50) # 뉴스 정보
    accident_info = models.CharField(max_length = 50) # 사고정보(키워드 등...)
    
    def __str__(self) :
        return self.news_info
    
class News_Info(models.Model) : # 뉴스정보 db
    news_no = models.CharField(max_length = 8, primary_key = True) # 뉴스 일련번호
    news_kind = models.CharField(max_length = 10) # 뉴스 구분
    news_date = models.DateTimeField(default = datetime.now(), blank = True) # 뉴스 일자
    news_content = models.TextField() # 뉴스 내용
    news_keyword = models.CharField(max_length = 50) # 뉴스 키워드
    weather_info = models.CharField(max_length = 20) # 날씨 정보
    gender = models.CharField(max_length = 2) # 성별 / int defualt=0/1해서 할지 상의 요망
    age = models.IntegerField() # 나이 / 해당 정보 member의 model 주민등록번호 참조할지 상의 요망
    
    def __str__(self) :
        return self.news_content
    
class Notice(models.Model) : # 공지사항 db 생성
    notice_title = models.CharField(max_length = 50) # 공지사항 타이틀
    notice_content = models.TextField() # 공지사항 내용
    notice_dt = models.DateTimeField(default = datetime.now(), blank = True) # 등록일자
    notice_cnt = models.IntegerField(default=1) # 조회수
    
    def __str__(self) :
        return self.notice_title