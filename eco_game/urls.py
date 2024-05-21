from django.urls import path
from .views import QuestionListView, QuestionDetailView

urlpatterns = [
    path('questions/',
         QuestionListView.as_view(), name='question-list'),
    path('questions/<int:q_id>/',
         QuestionDetailView.as_view(), name='question-detail'),
]
