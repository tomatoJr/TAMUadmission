
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name = 'home'),
    path('user/', views.user, name = 'user'),
    # path('', include('misterwu')),
]
