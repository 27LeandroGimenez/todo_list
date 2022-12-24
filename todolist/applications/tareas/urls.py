from django.urls import path
from .views import ListaTareas, TareaUpdate, TareaDelete, TareaCreate

urlpatterns = [
    path('', ListaTareas.as_view(), name='lista-tareas'),
    path('tarea-create', TareaCreate.as_view(), name='create'),
    path('tarea-update/<pk>/', TareaUpdate.as_view(), name='update'),
    path('tarea-delete/<pk>/', TareaDelete.as_view(), name='delete'),
]