from django.conf.urls.static import static
from django.contrib import admin
from mediqueue import settings
from mq.views import *
from django.urls import path, include

urlpatterns = [path('admin/', admin.site.urls),
    path('mediqueue/', index),
    path('registration/', registration)
]