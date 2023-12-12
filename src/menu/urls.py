from django.urls import path
from .views import menu_view

urlpatterns = [
    # path('menu/<str:menu_name>/', MenuView.as_view(), name='menu_view'),
    path('menu/<str:menu_name>/', menu_view, name='menu_view'),
    path('menu/', menu_view, name='menu'),
]
