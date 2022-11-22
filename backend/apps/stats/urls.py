from django.urls import path
from .views import PersonalStatsView


urlpatterns = [
    path('personal/', PersonalStatsView.as_view())
]
