# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Vote(models.Model):
    vote_text = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.vote_text

class Option(models.Model):
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE)
    option_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.option_text