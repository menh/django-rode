from django.shortcuts import render
from .models Question
from django.http import HttpResponse

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    last_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in last_question_list])
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking ar the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
