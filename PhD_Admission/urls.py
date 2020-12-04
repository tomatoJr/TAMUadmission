
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.homecard, name='homecard'),
    path('table/', views.hometable, name='hometable'),
    path('user/', views.use, name='user'),
    path('email/', views.send_email, name='send_email'),
    path('review/', views.review, name='review'),




    path('addApplicantInfo/', views.addApplicantInfo),
    # path('<int:app_seq_no>/review/', views.review, name='review'),
    #     path('table/<int:app_seq_no>/review/', views.review, name='review'),
    path('table/<int:app_seq_no>/<int:pointer>/<int:total_num>/review/',
         views.review, name='review'),


    path('<int:app_seq_no>/<int:pointer>/<int:total_num>/review/',
         views.review, name='review'),
    path('search/<int:app_seq_no>/<int:pointer>/<int:total_num>/review/',
         views.review, name='review'),


    path('search/', views.search, name='search'),

    path('addReview/', views.addReview, name='addReview'),
]
