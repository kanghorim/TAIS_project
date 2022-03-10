from django.db import models

class Event(models.Model) : # 이벤트 db 생성
    event_title = models.CharField(max_length = 50) # 이벤트 타이틀
    event_content = models.TextField() # 이벤트 내용
    event_dt = models.DateTimeField() # 등록일자
    event_st_dt = models.DateTimeField() # 이벤트 시작날짜
    event_en_dt = models.DateTimeField() # 이벤트 종료날짜
    event_cnt = models.IntegerField(default=1) # 조회수
    event_img = models.ImageField(blank=True) # 이벤트 페이지 이미지
    
    def __str__(self) :
        return self.event_title