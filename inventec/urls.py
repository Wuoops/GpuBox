
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include

from front.views import *
from limit.views import setlimit

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^home/', front),
    url(r'^getHomepageTempData/', getHomepageTempData),
    url(r'^setlimit/', setlimit),
    url(r'^cleanAlarm/', cleanAlarm),
    url(r'^getHomePageStatus/', getHomePageStatus),

]
