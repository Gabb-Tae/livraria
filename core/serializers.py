from dataclasses import fields
from statistics import mode
from rest_framework.serializers import ModelSerializer

from core.models import Categoria

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"
