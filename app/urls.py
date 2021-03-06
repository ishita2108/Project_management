from django.urls import path, include
from .views import home_view, detail_view, search_view, create_student, delete_student, edit_student


urlpatterns = [
    path('',home_view ),
    path('student/<int:id>',detail_view),
    path('search/', search_view),
    path('create-student',create_student),
    path('delete-student', delete_student),
    path('edit-student', edit_student)
]
