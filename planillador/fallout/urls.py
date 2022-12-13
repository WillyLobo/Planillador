from django.urls import path
from fallout.views import PlanillaFalloutDetailView

app_name = "fallout"

urlpatterns = [
    path("<pk>/", PlanillaFalloutDetailView.as_view()),
]