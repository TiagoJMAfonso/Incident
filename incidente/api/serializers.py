from rest_framework import serializers
from incidente.models import Incidente, Localizacao
from users.models import CustomUser

class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username','password']


class IncidenteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Incidente
        fields = ['id', 'estado', 'categoria','created_date','update_date', 'localizacao', 'author']


class LocalizacaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Localizacao
        fields = ['id', 'nome', 'descricao','longitude','latitude']