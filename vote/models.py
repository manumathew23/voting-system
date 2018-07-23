# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Vote(models.Model):
    vote_text = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Option(models.Model):
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE)
    option_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class UserVote(models.Model):
    ip_address = models.CharField(max_length=15)
    vote = models.ForeignKey(Vote)
    options = models.TextField()