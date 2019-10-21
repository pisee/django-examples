from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic, View
from django.utils import timezone
from django.db import transaction

from .models import Question, Choice


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')

    # output = ','.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    
    context = {
        'latest_question_list':latest_question_list,
    }

    # template = loader.get_template('polls/index.html')
    # return HttpResponse(template.render(context, request))
    
    return render(request, 'polls/index.html', context)
    
    

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(id=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question Does Not Exist")
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'polls/detail.html', {'question':question})

# @transaction.atomic
def vote(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        
        # raise ValueError # for transaction rollback test

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


'''
using generic-view
'''
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    # queryset = Question.objects.order_by('-pub_date')
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        # return Question.objects.order_by('-pub_date')[:5]
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    template_name = 'polls/detail.html'
    # model = Question

    # def get_object(self):
    #     pk = self.kwargs['pk']
    #     return get_object_or_404(Question, id=pk)
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

# class ResultsView(generic.DetailView):
#     template_name = 'polls/results.html'
#     model = Question

'''
using normal class-view
'''
class ResultsView(View):
    def get(self, request, pk):
        question = get_object_or_404(Question, pk=pk)
        return render(request, 'polls/results.html', {'question': question})