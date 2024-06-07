from home import views
from django.urls import path

urlpatterns = [
    path('index/', views.index),
    path('person/', views.person),
    path('login/', views.login),
    path('personAPIView/', views.PersonView.as_view()),
]
