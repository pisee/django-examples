from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import restviews


# router = DefaultRouter()
# router.register('questions', restviews.QuestionViewset)

urlpatterns = [
    
    # path('', include(router.urls)),
    path('', restviews.IndexView.as_view(), name='index'),
    path('<int:question_id>/', restviews.DetailView.as_view(), name='detail'),
    path('<int:question_id>/results/', restviews.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', restviews.vote, name='vote'),

]
