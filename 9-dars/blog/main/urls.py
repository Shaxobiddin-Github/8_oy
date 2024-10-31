from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (FoodTypeViewSet, FoodViewSet, CommentViewSet,
                    RegisterView, LogoutView, ReviewViewset,
                    FoodTypeViewSet2, FoodViewSet2, CommentViewSet2,
                    ReviewViewset2)

app_name = 'main'

# Version 1 Router
router_v1 = DefaultRouter()
router_v1.register(r'food-types', FoodTypeViewSet)
router_v1.register(r'foods', FoodViewSet)
router_v1.register(r'comments', CommentViewSet)
router_v1.register(r'reviews', ReviewViewset, basename='reviews')
router_v1.register(r'register', RegisterView, basename='register')
router_v1.register(r'logout', LogoutView, basename='logout')

# Version 2 Router
router_v2 = DefaultRouter()

router_v2.register(r'food-types', FoodTypeViewSet2)  
router_v2.register(r'foods', FoodViewSet2)  
router_v2.register(r'comments', CommentViewSet2)  
router_v2.register(r'reviews', ReviewViewset2, basename='reviews')  

# router_v2.register(r'new-endpoint', NewViewSet, basename='new-endpoint')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v2/', include(router_v2.urls)),
    path('api-auth/', include('rest_framework.urls')),  
]
