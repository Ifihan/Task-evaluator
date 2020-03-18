from django.urls import path
from . import views

urlpatterns = [
    path('', views.InputView.as_view(), name='input'),
    path('info/', views.InfoView.as_view(), name='info'),
    path('result/', views.ResultView.as_view(), name='result'),
]