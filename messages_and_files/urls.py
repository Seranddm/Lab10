from django.conf.urls.static import static
from django.urls import path

from Lab10 import settings
from .views import *

urlpatterns = [
    path('', MessageList.as_view(), name='messages_list'),
    path('add-message/', AddMessage.as_view(), name='add_message'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('download/<int:pk>/', download_file, name='download'),

]
