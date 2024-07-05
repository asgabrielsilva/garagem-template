from rest_framework.serializers import ModelSerializer

from core.models import Marca

class MarcaSerializer(ModelSerializer):
    class meta:
        model = Marca
        fields = "__all__"