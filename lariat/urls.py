from django.conf.urls import url
from . import  views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'add$',views.add_patient, name = 'add_patient'),
    url(r'about$',views.about, name = 'about'),
    url(r'signup$',views.signup, name = 'signup'),
    url(r'admin$', views.admin ,name = 'admin'),
    
]
