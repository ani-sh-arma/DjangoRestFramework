from home import views
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('person', views.PersonViewSet, basename='person')
urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
    path('index/', views.index),
    # path('person/', views.person),
    # path('login/', views.login),
    # path('personAPIView/', views.PersonView.as_view()),
]
