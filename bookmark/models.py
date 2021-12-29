from django.db import models

# Create your models here.
# 모델 : 데이터 베이스를 sql 없이 다루기 위해 model을 사용
# 우리가 데이터를 객체화해서 다루기 위해
# 모델 = 테이블
# 모델의 필드(변수) = 테이블의 컬럼
# 인스턴스 = 테이블의 레코드
# 필드의 값 = 데이터 값

class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')
    def __str__(self):   # 매직 매소드 클래스의 인스턴스가 출력되도록
        return f"이름: {self.site_name}, 주소: {self.url}"



    # 필드의 종류가 결정하는 것
    # 1.데이터베이스의 컬럼 종류
    # 2.제약 사함(몇글자까지 쓸 수 있는지)
    # 3.Form의 종류
    # 4.Form에서 제약 사항

# 모델을 만들었다 -> 데이터베이스에 어떤 데이터들을 어떤 형태로 넣을지 결정했다
# migrate -> 데이터 베이스에 모델의 내용을 반영(테이블 실제로 생성)
# 모델을 수정하면 migrate 항상 해줘야함
# makemigrations -> 모델의 변경사함 추적해서 기록(정보), migrate 하기 전에 해야함 (migrations폴더 생성됨)

