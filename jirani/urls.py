from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^home/',views.home,name = 'home'),
    url(r'^new/hood$', views.new_hood, name='new-hood'),
    url(r'^hoods/$', views.hoods, name='hoods'),



]
