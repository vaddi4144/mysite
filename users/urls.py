from django.urls import path
from .views import register, login_user, dashboard,assign_task,home_page,logout_user

app_name = 'users'
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('assign_task/', assign_task, name='assign_task'),
    path('', home_page, name='home')
]