from django.urls import path
from dashboard import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path("<int:pk>/", views.job_detail, name="job_detail")
]
