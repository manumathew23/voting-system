from django.conf.urls import url
from . import views

app_name = 'vote'
urlpatterns = [
    # ex: /vote/
    url(r'^$', views.index, name='index'),
    # ex: /vote/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /vote/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /vote/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]