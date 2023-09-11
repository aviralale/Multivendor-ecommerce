from django.urls import path
from .views import detail, newItem, delete, editItem, items

app_name = 'item'
urlpatterns = [
    path('',items,name='items'),
    path('new/',newItem,name='new'),
    path('<int:pk>/',detail,name='detail'),
    path('<int:pk>/delete/',delete,name='delete'),
    path('<int:pk>/edit/',editItem,name='edit'),

]
