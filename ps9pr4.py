#
# ps9pr4.py (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four  
#

import random  
from ps9pr3 import *


class AIPlayer(Player):
    """ a data type for a cmputer to play Connect Four, a subclass of Player
    """
    def __init__(self, checker, tiebreak, lookahead):
        """ initializes the AI player with two new attributes, 
            tiebreak, which breaks ties, and lookahead, which is used as the AI's method of predicting moves
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead
        
    def __repr__(self):
        """ returns a string representation of the AIPlayer object
        """
        return 'Player' + ' ' + self.checker + ' (' + self.tiebreak +', ' + str(self.lookahead) + ')'
    
    def max_score_column(self, scores):
        """ takes a list scores containing a score for each column of the board, 
            and that returns the index of the column with the maximum score
        """
        max_index = []
        max_score = max(scores)
        for i in range(len(scores)):
            if scores[i] == max_score:
                max_index += [i]
        if self.tiebreak == "LEFT":
            return max_index[0]
        elif self.tiebreak == "RIGHT":
            return max_index[-1]
        elif self.tiebreak == "RANDOM":
            return random.choice(max_index)
        
    def scores_for(self, b):
        """ takes a Board object b and determines the called AIPlayer‘s scores for the columns in b
        """
        scores = [50]*b.width
        for col in range(b.width):
            if b.can_add_to(col) == False:
                scores[col] = -1
            elif b.is_win_for(self.checker) == True:
                scores[col] = 100
            elif b.is_win_for(self.opponent_checker()) == True:
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                b.add_checker(self.checker, col)
                aitwo = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead-1)
                opp_scores = aitwo.scores_for(b)
                scores[col] = 100 - max(opp_scores)
                b.remove_checker(col)
                
        return scores
        
        
    def next_move(self, b):
        """ overrides (i.e., replaces) the next_move method that is inherited from Player.
            Rather than asking the user for the next move, this version of next_move should 
            return the called AIPlayer‘s judgment of its best possible move. 
        """
        self.num_moves += 1
        scores = self.scores_for(b)
        index = self.max_score_column(scores)
        return index
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        