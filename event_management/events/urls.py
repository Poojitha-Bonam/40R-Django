from . import views
from django.urls import path

urlpatterns = [
    path('',views.home_page),
    path('get_event/',views.get_event),
    path('create_event/',views.create_event),
    path('update_event/<int:input_id>',views.update_event),
    path('delete_event/<int:id>',views.delete_event),

    path('get_feedback/<int:input_id>',views.get_feedback),
    path('create_feedback/',views.create_feedback),
    path('update_feedback/<int:input_id>',views.update_feedback),
    path('delete_feedback/<int:id>',views.delete_feedback)
]