# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Vote, Option, UserVote
import json

def index(request):
    vote_list = Vote.objects.all()
    context = {
        'vote_list': vote_list,
    }
    return render(request, 'vote/list.html', context)

def detail(request, question_id):
    ip_address = get_ip_address(request)
    try:
        user_vote = UserVote.objects.get(ip_address=ip_address)
        voted = True if user_vote.vote_id == int(question_id) else False
    except:
        voted = False
    if voted:
        vote_trend = {'vote_trend': get_vote_trend(question_id)}
        return render(request, 'vote/trend.html', vote_trend)

    question = get_object_or_404(Vote, pk=question_id)
    return render(request, 'vote/cast_vote.html', {'question': question})

def vote(request, question_id):
    voted_option_list = dict(request.POST.lists()).get('option')
    ip_address = get_ip_address(request)
    if not ip_address in UserVote.objects.values_list('ip_address', flat=True):
        vote = Vote.objects.get(id=question_id)
        user_vote = UserVote(ip_address=ip_address, vote=vote, options=json.dumps(voted_option_list))
        user_vote.save()
        for option in voted_option_list:
            option = int(option)
            option_obj = Option.objects.get(id=option)
            option_obj.votes = option_obj.votes + 1
            option_obj.save()

    # redirect user to trend page
    vote_trend = {'vote_trend': get_vote_trend(question_id)}
    return render(request, 'vote/trend.html', vote_trend)

def get_vote_trend(vote_id):
    vote_obj = Vote.objects.get(id=vote_id)
    all_votes_list = Option.objects.filter(vote=vote_obj)
    all_votes = all_votes_list.values_list('votes', flat=True)
    vote_total = reduce(lambda a, b: a + b, all_votes)
    vote_trend = all_votes_list.values('option_text', 'votes')
    return zip(vote_trend,
             map(lambda x: round(float(x.get('votes'))/37*100, 2), vote_trend))

def get_ip_address(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip