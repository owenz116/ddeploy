from django.urls import re_path
from . import views

app_name = 'blah'

urlpatterns = [
    re_path(r'^register/',views.register, name='registeration'),
    re_path(r'^login/',views.ulogin, name='log'),
]
