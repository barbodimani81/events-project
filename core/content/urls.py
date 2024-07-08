from django.urls import path
from .views import event_create, event_update, event_list, event_detail, event_delete, category_list, category_create, session_list, session_create

urlpatterns = [
    path('event/', event_list, name='event_list'),
    path('event/<int:event_id>/', event_detail, name='event_detail'),
    path('event/create/', event_create, name='event_create'),
    path('event/<int:event_id>/update/', event_update, name='event_update'),
    path('event/<int:event_id>/delete/', event_delete, name='event_delete'),
    path('categories/', category_list, name='category_list'),
    path('categories/create/', category_create, name='category_create'),
    path('sessions/', session_list, name='session_list'),
    path('sessions/create/', session_create, name='session_create'),
]
