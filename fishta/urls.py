from django.urls import path
from fishta.views import HomeView, AboutView, ContactView, CheckResultView

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('checkresult/<str:task_id>/', CheckResultView.as_view(), name='check_result')
]
