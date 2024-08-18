from django.urls import path
from . import views

app_name='users'

urlpatterns = [
    path('register/',views.register_view,name='regis'),
    path('login/',views.login_view,name='log'),
    path('logout/',views.logout_view,name='sso'),
]