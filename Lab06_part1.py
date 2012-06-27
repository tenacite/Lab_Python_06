"""
Lab_Python_06
Part 1
"""

import datetime

"""
Whatever the datastructure you choose,
it should represent the following data:

player		| date		| score
_______________________________________
rooney		| 6/23/2012	| 2
rooney		| 6/25/2012	| 2
ronaldo		| 6/19/2012	| 0
ronaldo		| 6/20/2012	| 3
torres		| 6/21/2012	| 0
torres		| 6/21/2012	| 1
"""

## create the player_stats data structure
player_stats={'rooney':[(datetime.date(2012,06,23),2),
              (datetime.date(2012,06,25),2)],
              'ronaldo':[(datetime.date(2012,06,19),0),
              (datetime.date(2012,06,20),3)],
              'torres':[(datetime.date(2012,06,21),0),
              (datetime.date(2012,06,21),1)]}
"""
keyname=str(raw_input("enter the name of the player: "))
for key,value in player_stats.iteritems():
    if key==keyname:"""
for key,value in player_stats.iteritems():
            print key
            for i in value:
                print i

## implement highest_score

def highest_score(player_stats):
    max_score=0
    score=0
    for key,value in player_stats.iteritems():
            for date,goal in value:
                match_date=date
                score=goal
                if max_score<score:
                    max_score=score
                    
                    
## implement highest_score_for_player



## implement highest_scorer






