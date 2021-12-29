# 2차 url을 만들어줌

from django.urls import path
#from .views import BookmarkListView, BookmarkCreateView
from .views import *

urlpatterns = [
    # http://127.0.0.1/bookmark/???
    # ???
    path("", BookmarkListView.as_view(), name='list'), #클래스형 뷰 일때는 .as_view()를 붙여야하고, 함수형 뷰일 때는 그냥 사용/ name은 urlpatterns의 이름
    path("add/", BookmarkCreateView.as_view(), name='add'),
    path("detail/<int:pk>/", BookmarkDetailView.as_view(), name="detail"),
    # 디테일 뒤에 해당 북마크의 글번호를 쓰면 찾아서 보여줌 pk는 primary key/migration 에서 자동으로 만든 id 값/int:는 int형식에 맞는 것들만 가능함을 지정
    #그냥 <pk>는 기본적으로 문자열

]