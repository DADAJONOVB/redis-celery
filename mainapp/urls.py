from django.urls import path
from .views import FeedbackFormView,SuccessView


urlpatterns = [
    path('',FeedbackFormView.as_view()),
    path('success/', SuccessView.as_view(), name='success')
]