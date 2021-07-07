
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include

from front.views import *
from limit.views import setlimit,simdata

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^home/', front),
    # url(r'^getHomepageTempData/', getHomepageTempData),
    url(r'^setlimit/', setlimit),
    url(r'^cleanAlarm/', cleanAlarm),
    url(r'^getHomePageStatus/', getHomePageStatus),
    url(r'^getGpuTemp/', getGpuTemp),
    url(r'^getGpuStatus/', getGpuStatus),
    url(r'^getSwitchTemp/', getSwitchTemp),
    url(r'^getSwitchStatus/', getSwitchStatus),
    url(r'^getPower/', getPower),
    url(r'^simdata/', simdata),

]
