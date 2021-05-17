from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'heroes', views.HeroViewSet)

app_name='myapi'
urlpatterns = [
    path(r'admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
#    path('', include(('tutorial.urls', 'tutorial'), namespace='tutorial')),
]
