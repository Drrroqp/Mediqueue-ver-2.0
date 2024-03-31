from django.urls import path, include
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('register/', views.register_view, name='register'),
    path('account/', account, name = 'account'), #личный кабинет
]
