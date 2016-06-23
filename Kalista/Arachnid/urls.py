from django.conf.urls import url
from . import views

app_name = 'Arachnid'

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^auth/$',views.loginuser, name='loginuser')
]