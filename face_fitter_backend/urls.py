from django.conf.urls import url, include,patterns
#from rest_framework import routers
from face import views

#router = routers.DefaultRouter()
#router.register(r'faces', views.FaceViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = patterns(
    'face.views',
    #url(r'^', include(router.urls)),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/face', 'faceRequest')
)