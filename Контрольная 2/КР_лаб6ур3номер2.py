class teams:
    def __init__(self,name,goals):
        self.name=name
        self.goals=goals
q=[]
team1=teams('team1',2)
team2=teams('team2',1)
team3=teams('team3',3)
team4=teams('team4',5)
team5=teams('team5',1)
team6=teams('team6',2)
team7=teams('team7',3)
team8=teams('team8',1)
team9=teams('team9',2)
team10=teams('team10',4)
team11=teams('team11',1)
team12=teams('team12',2)
team13=teams('team13',4)
team14=teams('team14',2)
team15=teams('team15',2)
team16=teams('team16',5)
team17=teams('team17',3)
team18=teams('team18',2)
team19=teams('team19',6)
team20=teams('team20',2)
team21=teams('team21',1)
team22=teams('team22',2)
team23=teams('team23',1)
team24=teams('team24',2)
q.append(team1)
q.append(team2)
q.append(team3)
q.append(team4)
q.append(team5)
q.append(team6)
q.append(team7)
q.append(team8)
q.append(team9)
q.append(team10)
q.append(team11)
q.append(team12)
q.append(team13)
q.append(team14)
q.append(team15)
q.append(team16)
q.append(team17)
q.append(team18)
q.append(team19)
q.append(team20)
q.append(team21)
q.append(team22)
q.append(team23)
q.append(team24)
x=1
w=[]
for i in range(0,12,2):
    if q[i].goals>q[x].goals:
        w.append(q[i])
    else:
        w.append(q[x])
    x+=2
for i in range(len(w)):
    print('From group 1:',w[i].name,'score:',w[i].goals)
print()
x=13
w=[]
for i in range(12,24,2):
    if q[i].goals>q[x].goals:
        w.append(q[i])
    else:
        w.append(q[x])
    x+=2
for i in range(len(w)):
    print('From group 2:',w[i].name,'score:',w[i].goals)
