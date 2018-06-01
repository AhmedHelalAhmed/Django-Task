from django.conf.urls import url, include
from .models import Patient
from . import views
from rest_framework_swagger.views import get_swagger_view
from rest_framework import routers, serializers, viewsets


schema_view = get_swagger_view(title='Patient API')

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = ('url','patient_name','phone_number' )

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'patients', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.


urlpatterns = [
    url(r'^$', views.addpatient),
    url(r'^swagger-ui$', schema_view),
    url(r'^api/', include(router.urls)),
]






