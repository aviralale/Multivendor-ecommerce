from django.urls import path
from .views import detail, newItem, delete, editItem, items, category_items

app_name = 'item'
urlpatterns = [
    path('',items,name='items'),
    path('new/',newItem,name='new'),
    path('<int:pk>/',detail,name='detail'),
    path('category/<int:category_id>/',category_items,name='category_items'),
    path('<int:pk>/delete/',delete,name='delete'),
    path('<int:pk>/edit/',editItem,name='edit'),

]
