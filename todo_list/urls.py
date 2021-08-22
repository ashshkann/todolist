from django.urls import path
from .views import todo_views, creat_item, delete_item

urlpatterns = [
    path('todo/', todo_views, name="listViews"),
    path('create_todo/', creat_item, name="create_todo"),
    path('delete/<id>/', delete_item, name="delete_item")
]
