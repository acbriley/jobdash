from django.urls import path
from dashboard import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path("<int:pk>/", views.job_detail, name="job_detail"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login_page, name="login"),
    path('myjobs', views.my_jobs, name="my_jobs")
]
