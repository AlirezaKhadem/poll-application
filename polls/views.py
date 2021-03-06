from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Question
from django.template import loader
from .config import config


# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:config.num_of_question_per_page]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

    # this is another way :) i think is better than prev method
    # return render(request, template_name='polls/index.html', context=context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')

    context = {'question': question}
    return render(request, 'polls/detail.html', context)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
