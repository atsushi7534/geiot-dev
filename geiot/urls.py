from django.urls import path
from django.conf import settings
from . import views


# アプリ名を記述
app_name = 'geiot'

# ここの配列の中にルーティングを書いていきます。
urlpatterns = [
  path('', views.index, name="index"),
  path('result', views.result, name="result"),
  path('select', views.select, name="select"),
  path('test', views.test, name="test"),
]