from django.urls import path
from .views import ProductViewSet

urlpatterns = [
    path('list-product', ProductViewSet.as_view({
        'get':'list'
    })),
    
    path('product/<str:pk>', ProductViewSet.as_view({
        'get':'retrieve'
    })),
]