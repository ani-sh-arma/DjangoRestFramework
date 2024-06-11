from home import views
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'persons', views.PersonViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('index/', views.index),
    path('login/', views.login),
    path('register/', views.register),
    # path('person/', views.person),
    path('personAPIView/', views.PersonView.as_view()),
]
