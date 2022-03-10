from datetime import datetime
from django.db import models
from member.models import User_Info

class Board(models.Model) : # 게시판 db 생성 / 자유게시판, 공지, 1대1 문의
    user_id = models.ForeignKey(User_Info, on_delete = models.DO_NOTHING, null = True) # member models에서 참조하는 외래키 사용자 아이디
    b_kind = models.CharField(max_length = 10) # 게시글 분류
    board_no = models.IntegerField(default = 1, primary_key = True) # 게시판 일련번호
    b_title = models.CharField(max_length = 1000) # 게시글 제목
    b_content = models.TextField() # 게시글
    b_date = models.DateTimeField(default = datetime.now(), blank = True) # 일자
    b_count = models.IntegerField(default = 1) # 조회수
    b_group = models.IntegerField(default=0) # 답글
    b_step = models.IntegerField(default=0) # 답글
    b_indent = models.IntegerField(default=0) # 답글
    b_img = models.ImageField(blank=True) # 보드 이미지
    
    def __str__(self) :
        return self.b_title
    
class Comment(models.Model) : # 댓글 db 생성
    user_id = models.ForeignKey(User_Info, on_delete = models.CASCADE, null = True) # member models에서 참조하는 외래키 사용자 아이디
    comment_no = models.ForeignKey(Board, on_delete = models.CASCADE, null = True, default = 0) # 게시판 일련번호 Board의 board_no 참조
    comment_content = models.TextField() # 댓글 내용
    comment_dt = models.DateTimeField(default = datetime.now(), null = True, blank = True) #  댓글 작성 일자
    
    def __str__(self) :
        return self.comment_content
    
    