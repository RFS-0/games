# django
from django.conf.urls import url

app_name = 'laby'

urlpatterns = [

    url(r'^$', views.HomeTemplateView.as_view(), name='default'),
    url(r'^/home$', views.HomeTemplateView.as_view(), name='default'),

]