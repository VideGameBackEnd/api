# -*- coding: utf-8 -*-
"""
Author - Ramiro Gutierrez Alaniz
Project - democracia de un tavo homosexual
Area - IT; B-E Develpment
Date - Tuesday, June 3, 2016
"""

# imports
from gamedata.models import Score

"""
Score helper
"""
class ScoreHelper :
    
    def get_party_score( self, party ) :
        """
        This will return the score of an speciic party
        """
        # total init
        total = 0
        # get all the scores per party
        scores = Score.objects.filter( partido=party )
        # sum all
        for s in scores :
            total += s.score
        # return this total shit
        return total
    # End of get_party score function
    
        
#End of score helper class