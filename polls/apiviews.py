from django.shortcuts import get_object_or_404
from django.core import serializers
from django.http import HttpResponse, JsonResponse, Http404
from django.views import View
from django.forms.models import model_to_dict

from .models import Question, Choice


class IndexView(View):
    def get(self, request):
        queryset = Question.objects.order_by('-pub_date')[:5]
        result = serializers.serialize('json', queryset)
        return HttpResponse(result)

        # qs_json = serializers.serialize('json', latest_question_list)
        # return HttpResponse(qs_json, content_type='application/json')
    
        # data = list(latest_question_list)
        # return JsonResponse({'data': data})


class DetailView(View):
    def get(self, request, question_id):
        question = get_object_or_404(Question, id=question_id)
        result = serializers.serialize('json', [question])
        return HttpResponse(result)
        # return JsonResponse(result, safe=False)

class ResultsView(View):
    def get(self, request, question_id):
        question = get_object_or_404(Question, id=question_id)
        return JsonResponse(model_to_dict(question))

class VoteView(View):
    def post(self, request, question_id):
        question = get_object_or_404(Question, id=question_id)
        try:
            # selected_choice = question.choice_set.get(pk=request.GET['choice'])
            selected_choice = question.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            return Http404("Choice does not exist")
        else:
            selected_choice.votes += 1
            selected_choice.save()
        question = get_object_or_404(Question, id=question_id)
        return JsonResponse(model_to_dict(question))