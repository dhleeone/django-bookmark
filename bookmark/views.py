from django.shortcuts import render

# Create your views here.
# CRUD: Create, Read, Update, Delete
# List

# 클래스형 뷰, 함수형 뷰
# 클래스형 뷰는 장고에서 기본적으로 제공하는 Generic 뷰를 사용할 때
# 함수형 뷰는 직접 만드는 뷰
# url을 입력 -> 웹 서버가 뷰를 찾아서 동작시킨다. -> 응답 / 뷰에서 어떤 url을 넣어야 view가 동작할지 정해줘야함

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

from django.urls import reverse_lazy
from .models import Bookmark

class BookmarkListView(ListView): # listview를 상속받아 만든다.
    model = Bookmark

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list')
    template_name_suffix = '_create'

class BookmarkDetailView(DetailView):
    model = Bookmark
