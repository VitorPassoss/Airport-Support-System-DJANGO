from django.urls import path

from . import views

urlpatterns = [
    path("", views.MapView.as_view(), name="map"),
    path("type/<str:option>/", views.MapView.as_view(), name="map"),
    path('chat/', views.homepage, name='homepage')
]