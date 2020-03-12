from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import serializers, viewsets, routers
from incidente.api import urls
from incidente.api import views
#from users.api import views




# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
#####REST_FRAMEWORK URLS############
router.register('incidentes', views.IncidenteView)
router.register('localizacao', views.LocalizacaoView)

router.register(r'users', views.CustomUserView)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/',admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),




    #url(r'^incidentes/', api_incidente_view),
    #url(r'^api/incidentes', include('incidente.api.urls', namespace='detail')),


]


#
# # Serializers define the API representation.
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'is_staff']
#
#
# # ViewSets define the view behavior.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer