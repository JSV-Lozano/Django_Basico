from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Question, Choice


""" def index(request):
    lastest_questions_list = Question.objects.all()
    return render(request, "polls/index.html", {
        "lastest_questions_list": lastest_questions_list,
    })


def details(request, question_id):
    question = get_list_or_404(Question, pk=question_id)
    return render(request, "polls/details.html", {
        "question": question[0],
    })


def results(request, question_id):
    question = get_list_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {
        "question": question[0]
    }) """
    


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "lastest_questions_list"
    def get_queryset(self):
        """Return the lastest five published questions"""
        return Question.objects.order_by("-pub_date")[:5]
    
class DetailView(generic.DetailView):
    model = Question
    template_name='polls/details.html'

class ResultView(generic.DetailView):
    model = Question
    template_name='polls/results.html'

def vote(request, question_id):
    question = get_list_or_404(Question, pk=question_id)
    question = question[0]
    try:
        select_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/details.html", {
            "question": question,
            "error_message": "No has seleccionado una opción"
        })
    else:
        select_choice.votes += 1
        select_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
