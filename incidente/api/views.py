from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets, permissions

from incidente.models import Incidente, Localizacao
from incidente.api.serializers import IncidenteSerializer, LocalizacaoSerializer
from users.models import CustomUser
from users.api.serializers import CustomUserSerializer


class CustomUserView(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


#
#def api_incidente_view(request):
#    try
#        queryset = Incidente.objects.all()
#    except Incidente.DoesNotExist:
#        return Response(status=status.HTTP_404_NOT_FOUND)
#    if request.method == 'GET':
#        serializer = IncidenteSerializer(incidente_get)
#        return Response(serializer.data)


class IncidenteView(viewsets.ModelViewSet):

        queryset = Incidente.objects.all()
        serializer_class = IncidenteSerializer


class LocalizacaoView(viewsets.ModelViewSet):
        queryset = Localizacao.objects.all()
        serializer_class = LocalizacaoSerializer
    