from django.urls import path, include
from rest_framework import routers
router = routers.DefaultRouter()
from AGCS_importadora_Back import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

router = routers.DefaultRouter()
router.register(r'usuarios', views.UserDataViewSet)
router.register(r'cliente', views.ClienteDataViewSet)
router.register(r'producto', views.ProductoDataViewSet)
router.register(r'venta', views.VentaDataViewSet)
router.register(r'importacion', views.ImporDataViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api/token/',TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', views.UserLoginView.as_view(), name="login"),
]