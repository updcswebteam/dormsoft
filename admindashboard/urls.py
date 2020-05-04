from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="admin-dashboard.index"),
    path('users', views.users, name="admin-dashboard.users"),
    path('logs', views.logs, name="admin-dashboard.logs"),
]
