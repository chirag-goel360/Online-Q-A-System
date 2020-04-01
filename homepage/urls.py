from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name = 'homepage'),
    path('registration/',views.regist,name = 'register'),
    path('registration/accountcreated/',views.profile,name = 'profile'),
    path('login/mainpage/profile/',views.profile,name = 'profile'),
    path('login/mainpage/1881/profile/',views.profile,name = 'profile'),
    path('login/mainpage/8118/profile/',views.profile,name = 'profile'),
    path('login/profile/',views.profile,name = 'profile'),
    path('login/',views.login,name="login"),
    path('login/forgotpsw/',views.forgot,name = 'forgotpsw' ),
    path('login/mainpage/',views.mainpage,name = 'mainpage'),
    path('login/mainpage/women/',views.women,name = 'women'),
    path('login/mainpage/1881/women/',views.women,name = 'women'),
    path('login/mainpage/8118/women/',views.women,name = 'women'),
    path('login/mainpage/signout/',views.signout,name = 'signout'),
    path('login/mainpage/1881/signout/',views.signout,name = 'signout'),
    path('login/mainpage/8118/signout/',views.signout,name = 'signout'),
    path('login/mainpage/question/',views.question,name = 'question'),
    path('login/mainpage/report/',views.report,name = 'report'),
    path('login/mainpage/1881/report/',views.report,name = 'report'),
    path('login/mainpage/8118/report/',views.report,name = 'report'),
    path('login/mainpage/about/', views.about, name='about'),
    path('login/mainpage/1881/about/', views.about, name='about'),
    path('login/mainpage/8118/about/', views.about, name='about'),
    path('login/mainpage/options/', views.options, name='options'),
    path('login/mainpage/1881/options/', views.options, name='options'),
    path('login/mainpage/8118/options/', views.options, name='options'),
    path('login/mainpage/options/delete/', views.delete, name='delete'),
    path('login/mainpage/answer/', views.answer, name='answer'),
    path('login/mainpage/answer/<int:question_id>/', views.answer, name='answer'),
    path('login/mainpage/seeanswers/<int:question_id>/', views.seeanswers, name='seeanswer'),
    path('login/mainpage/seeanswers/<int:question_id>/<int:ans_id>/', views.upvotes, name='upvotes'),
    path('login/mainpage/<int:your>/',views.your,name = 'your'),








]