from django.urls import path
from .views import GenerateImageView, ImageHistoryView

urlpatterns = [
    path('generate-image/', GenerateImageView.as_view(), name='generate-image'),
    path('history/', ImageHistoryView.as_view(), name='image_history'),
]