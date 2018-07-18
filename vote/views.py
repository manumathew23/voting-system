# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Vote, Option

def index(request):
    vote_list = Vote.objects.all()
    context = {
        'vote_list': vote_list,
    }
    return render(request, 'vote/list.html', context)

def detail(request, question_id):
    question = get_object_or_404(Vote, pk=question_id)
    return render(request, 'vote/cast_vote.html', {'question': question})
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)