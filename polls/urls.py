from django.urls import path

from .views import index, details, results, votes

app_name = 'polls'
urlpatterns = [
    path('', index, name="index"),
    path('<int:question_id>/', details, name="details"),
    path('<int:question_id>/results/', results, name="results"),
    path('<int:question_id>/votes/', votes, name='vote')
]
