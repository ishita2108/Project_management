from django.urls import path, include
from .views import home_view, detail_view, search_view, create_student


urlpatterns = [
    path('',home_view ),
    path('student/<int:id>',detail_view),
    path('search/', search_view),
    path('create-student',create_student)
]
