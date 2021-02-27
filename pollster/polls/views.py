from django.shortcuts import render
from .models import Question, Choice

# get question and display
def index(request):
    latest_question_list = Question.objects.all
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
        context = {'question': question}
        return render(request, 'polls/detail.html', context)
    except print(0):
        pass

# Create your views here.
