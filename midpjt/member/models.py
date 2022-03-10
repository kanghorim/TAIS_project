from datetime import datetime
from django.db import models

class User_Info(models.Model) : # 사용자 정보 db
    user_id = models.CharField(max_length = 20, primary_key = True) #아이디
    user_pw = models.CharField(max_length = 20) #패스워드
    user_email = models.CharField(max_length = 20) #이메일
    user_name = models.CharField(max_length = 20) #이름
    user_regno = models.IntegerField() # 주민번호 앞자리로 설정되어 있음 / 해당 model full fegno로 설정할지 상의 요망
    user_phoneno = models.IntegerField() # 핸드폰 번호
    user_zipcode = models.IntegerField() # 우편번호
    user_add1 = models.CharField(max_length = 50) # 상세주소 1
    user_add2 = models.CharField(max_length = 50) # 상세주소 2
    reg_dt = models.DateTimeField(default=datetime.now(), blank=True) # 가입일자
    # subscript = models.IntegerField(default = 0, primary_key = True) # 구독여부 - 0/1이냐에 따라 구독여부 판단 요망
    ## 주소 / 주민등록번호를 PK로 설정해야할 필요성 -- 사고정보, 뉴스정보가 포함된 연관정보를 가져올 PK
    
    def __str__(self) :
        return self.user_name
    
