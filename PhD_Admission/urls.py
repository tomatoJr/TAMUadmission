
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.homecard, name = 'homecard'),
    path('table/', views.hometable, name = 'hometable'),
    path('user/', views.use, name = 'user'),
    path('email/', views.send_email, name='send_email'),
    path('review/', views.review, name='review'),

    path('addApplicantInfo/', views.addApplicantInfo),
    path('<int:app_seq_no>/review/', views.review, name='review'),

    # path('', include('misterwu')),
]
