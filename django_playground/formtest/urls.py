from django.urls import path
from formtest import views
from django.contrib import admin

app_name = 'formtest'
urlpatterns = [
    path('',views.index,name='index'),
    #path('admin/', admin.site.urls,name='adim'),
    path('Registration/',views.Registration,name='Registration'),
    path('logout/',views.user_log_out,name='log_out'),
    path('login/',views.user_log_in,name='log_in'),
]

