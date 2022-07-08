from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter
from core import views

router = DefaultRouter()
router.register(r'categorias', views.CategoairaViewsSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
