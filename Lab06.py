class Player:
    def __init__(self,firstname,lastname,team=None):
        self.first_name=firstname
        self.last_name=lastname
        self.scores=[]
        self.team=team

    def add_score(self,score):   
        self.scores.append(score)
        return None

    def total_score(self):
        totalscore=sum(self.scores)
        return totalscore

    def average_score(self):
        
        ave_score=self.total_score()/len(self.scores)
        return ave_score
    def __str__(self):
        return str(self.team)+'\nThe star players are:\n'+self.first_name+' '+self.last_name
            
            
torres= Player('Fernando','Torres','Chelsea')
for i in range(5):
    goals=int(input('enter the goals: '))
    torres.add_score(goals)
print 'The average score:',torres.average_score()
print

 
print '---------------------------------------------------------------------------'

class Team :
    def __init__(self,name,league,manager_name,points=0):
        self.team_name=name
        self.league=league
        self.managerName=manager_name
        self.points=points
        self.players=[]

    def __str__(self):
        return self.team_name+' is in the '+self.league+' managed by '+self.managerName+'.'
        
    def add_player(self,player):
        self.players.append(player)
        return None
    
portugal=Team ('FC Porto','Liga Sagres','Benedictus')
print portugal
spain=Team('Real Madrid','La liga','Jose Morihno')
print spain
print
print '-------------------------------------------------------------------------'
torres= Player('Fernando','Torres',portugal)
ronaldo= Player('Cristiano','Ronaldo',spain)
print torres
print ronaldo

portugal.add_player('Torres')
spain.add_player('Ronaldo')
