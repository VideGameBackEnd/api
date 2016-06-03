# -*- coding: utf-8 -*-
"""
Author - Ramiro Gutierrez Alaniz
Project - democracia de un tavo homosexual
Area - IT; B-E Develpment
Date - Tuesday, June 3, 2016
"""

# Imports
from django.conf.urls import patterns, url
from .views import *

# Url patterns
urlpatterns = patterns(
    
    'api.views',
    # scores module
    url(r'^score/$', ScoreList.as_view() , name='scores.list'), # scores List
    url(r'^score/byparty/$', ScoreByPartyList.as_view() , name='scores.party.list'), # scores by party List
    url(r'^score/totalbyparty/$', PartyScore.as_view() , name='scores.party.total'), # scores by party List PartiesScores
    url(r'^score/total/$', PartiesScores.as_view() , name='scores.totals'), # scores by party List
    
) # End of url patterns