from django.http import HttpResponse, Http404
from models import Question, Choice
from django.shortcuts import render, get_object_or_404

# Create your views here.

def index(request):

    my_latest_questions = Question.objects.order_by('-pub_date')[:5]
    context = {
        'my_latest_questions_inside_template': my_latest_questions,
    }
    return render(request, 'polls/index.html', context)

def about_us(request):
    return HttpResponse("I have created this site, My name is Nitin")

def detail(request, question_id):
    question = get_object_or_404 (Question, pk=question_id )
    context = {'question': question,}
    return render(request, 'polls/details.html', context)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)