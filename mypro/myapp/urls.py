from . import views
from django.urls import path

urlpatterns = [
   
    path('', views.signup, name='signup'),
    path('signin.html', views.signin, name='signin'), 
    path('main.html',views.home ,name='main.html')
]
