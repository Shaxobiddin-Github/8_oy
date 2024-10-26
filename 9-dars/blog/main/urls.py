from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FoodTypeViewSet, FoodViewSet, CommentViewSet, RegisterView, LogoutView,ReviewViewset
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView




router = DefaultRouter()
router.register(r'food-types', FoodTypeViewSet)
router.register(r'foods', FoodViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'reviews', ReviewViewset, basename='reviews')
router.register(r'register', RegisterView, basename='register')
router.register(r'logout', LogoutView, basename='logout')

urlpatterns = [
    path('', include(router.urls)),  # Routerni buni o‘zgartirdik
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-auth/', include('rest_framework.urls')),  # Avtomatik autentifikatsiya sahifalari
]
