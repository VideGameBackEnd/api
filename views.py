# -*- coding: utf-8 -*-
"""
Author - Ramiro Gutierrez Alaniz
Project - democracia de un tavo homosexual
Area - IT; B-E Develpment
Date - Tuesday, June 3, 2016
"""

# imports
from django.shortcuts import render
from gamedata.models import Score
# Rest framework imports
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .Permissions import QuietBasicAuthentication #custom permissions shit
# model imports 
from gamedata.models import Score
from gamedata.serializers import ScoreSerializer
from rest_framework.permissions import AllowAny
from .helpers import ScoreHelper

"""
This list all the scores
"""
class ScoreList( generics.ListCreateAPIView ) :
    # authentication classes
    authentication_classes = ( AllowAny, )
    # query set 
    queryset = Score.objects.all()
    # serializer
    serializer_class = ScoreSerializer
    # list function definition
    def list( self, request, *args, **kwargs ) :
        """                                                                                                                                                                  
        list function that list all the objects of the model                                                                                                                 
        returns a serialized json response                                                                                                                                   
        """
        instance = self.filter_queryset( self.get_queryset().order_by( '-score' ) )
        #serialize all
        serializer = self.get_serializer( instance, many=True )
        # return on data encap
        data = {
            'data' : serializer.data
        }
        # Return response
        return Response( data )
    # End of list function
# End of score list api view class


"""
This will list by party
"""
class ScoreByPartyList( generics.ListAPIView ) :
    # authentication classes
    authentication_classes = ( AllowAny, )
    # query set 
    queryset = Score.objects.all()
    # serializer
    serializer_class = ScoreSerializer
    # get query set filter function definition
    def get_queryset(self):
        """
        This returns a list of all the scores by party
        """
        return Score.objects.filter(partido=self.request.GET['partido'])
    # End of get_queryset function
    # list function definition
    def list( self, request, *args, **kwargs ) :
        """                                                                                                                                                                  
        list function that list all the objects of the model                                                                                                                 
        returns a serialized json response                                                                                                                                   
        """
        instance = self.filter_queryset( self.get_queryset() )
        #serialize all
        serializer = self.get_serializer( instance, many=True )
        # return on data encap
        data = {
            'data' : serializer.data
        }
        # Return response
        return Response( data )
    # End of list function
# End of ScoreByPartyList api view class

"""
This will return all the party scores
"""
class PartyScore( APIView ) :
    # get definition
    def get( self, request, format=None ) :
        """
        Get function
        """
        # End of for
        data = {
            'data' : {  
                'total' : ScoreHelper().get_party_score( self.request.GET['partido'] )
            }
        }
        return Response( data )
    # End of list function
# End of party score list apiview list class

"""
This will return all the party scores
"""
class PartiesScores( APIView ) :
    # get definition
    def get( self, request, format=None ) :
        """
        Get function that returns the total scores of each party
        """
        # set sumatory to 0
        sumatory = 0
        # get all the scores ordered by party
        scores = Score.objects.order_by('partido')
        # init lists
        parties = list()
        full_list = list()
        # iterate the scores
        for s in scores :
            # verify if the party is not in the list and if it isn't empty
            if s.partido not in parties and s.partido :
                parties.append(s.partido)
        for p in parties :
            # set the score on a variable to save memory iterating
            score_p = ScoreHelper().get_party_score( p )
            # to sumatory
            sumatory += score_p
            # append to the list
            full_list.append( [ p, score_p ] )
        # sort + to -
        full_list = sorted(full_list, key=lambda score: score[1], reverse=True)
        # add the last element with a summatory
        full_list.append( { 'total', sumatory } )
        # End of for
        data = {
            'data' : full_list
        }
        return Response( data )
    # End of list function
# End of party score list apiview list class