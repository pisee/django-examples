from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets

from .models import Question, Choice
from .serializers import QuestionSerializer, ChoiceSerializer

class IndexView(ListAPIView):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        queryset = Question.objects.order_by('-pub_date')[:5]
        return queryset

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)   

class DetailView(APIView):
    def get(self, request, question_id):
        question = get_object_or_404(Question, id=question_id)
        result = QuestionSerializer(instance=question)
        return Response(result.data)

class ResultsView(APIView):
    def get(self, request, question_id):
        question = get_object_or_404(Question, id=question_id)
        return Response(model_to_dict(question))

@api_view(['GET','POST'])
def vote(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    try:
        if request.method == 'GET':
            # selected_choice = question.choice_set.get(pk=request.query_params.get('choice', None))
            selected_choice = question.choice_set.get(pk=request.GET['choice'])
        elif request.method == 'POST':
            # selected_choice = question.choice_set.get(pk=request.data['choice'])
            selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return Http404("Choice does not exist")
    else:
        selected_choice.votes += 1
        selected_choice.save()
    question = get_object_or_404(Question, id=question_id)
    return Response(model_to_dict(question))

class QuestionViewset(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Question.objects.all().order_by('-pub_date')
    serializer_class = QuestionSerializer