from django.urls import path
from . import apiviews


urlpatterns = [
    
    path('', apiviews.IndexView.as_view(), name='index'),
    path('<int:question_id>/vote/', apiviews.VoteView.as_view(), name='vote'),
    path('<int:question_id>/', apiviews.DetailView.as_view(), name='detail'),
    path('<int:question_id>/results/', apiviews.ResultsView.as_view(), name='results'),
]
