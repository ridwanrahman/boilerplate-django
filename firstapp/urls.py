from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from .views import *


urlpatterns = [
    url(r'^$', index),
    # url(r'^home/$', sadmin_index),

]
