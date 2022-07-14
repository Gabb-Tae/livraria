from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter
from core.views import CategoairaViewsSet, EditoraViewSet, LivroViewSet

router = DefaultRouter()
router.register(r'categorias', CategoairaViewsSet)
router.register(r'editoras', EditoraViewSet)
router.register(r'livros', LivroViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
