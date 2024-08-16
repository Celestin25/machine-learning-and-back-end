from django.urls import path
from .views import create_menu_item, get_menu_items, update_menu_item, delete_menu_item

urlpatterns = [
    path('menu/', create_menu_item, name='create-menu-item'),
    path('menu/', get_menu_items, name='get-menu-items'),
    path('menu/<uuid:item_id>/', update_menu_item, name='update-menu-item'),
    path('menu/<uuid:item_id>/', delete_menu_item, name='delete-menu-item'),
]