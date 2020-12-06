from django.urls import path, include
from .views import home_view, detail_view

urlpatterns = [
    path('',home_view ),
    path('student/<int:id>',detail_view)
]
