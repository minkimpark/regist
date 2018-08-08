from django.urls import path
from django.conf.urls import url

from .djangoapps.index import views as IndexViews
from .djangoapps.login import views as LoginViews
from .djangoapps.regist import views as RegistViews
from .djangoapps.write import views as WriteViews

urlpatterns = [
    url('index$',IndexViews.index, name='index'),
    url('login$',LoginViews.login, name='login'),
    url('regist$',RegistViews.regist, name='regist'),
    url('api_regist_create$',RegistViews.api_regist_create, name='api_regist_create'),
    url('login_check$',LoginViews.login_check,name='login_check'),
    url('logout$',LoginViews.logout,name='logout'),
    url('write$',WriteViews.write,name='write'),
    url('api_write_create$',WriteViews.api_write_create, name='api_write_create'),
    url('^api_write_read',WriteViews.api_write_read,name='api_write_read'),
    url('view$',WriteViews.view,name='view'),
]
