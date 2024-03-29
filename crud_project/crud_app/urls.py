from django.urls import path
from .views import create_api, list_api, update_delete_api

urlpatterns = [
    path('create/', create_api),
    path('retrieve/', list_api),
    path('ud/<int:pk>/', update_delete_api)

]