from django.urls import path
from .views import GenericAPIView

urlpatterns = [
	path('records', GenericAPIView.as_view()),
	path('records/<int:pk>', GenericAPIView.as_view()),
]