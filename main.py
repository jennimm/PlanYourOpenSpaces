data = open('a_solar.txt','r')
W,H = data.readline().split()
W = int(W)
H = int(H)
plan = []
companies = []
companyDevelopers = []
managersBonus = []

for i in range(H):
    plan.append([])
for i in range(H):
    line = data.readline()
    for j in range(W):
        plan[i].append(line[j])

numDevelopers = int(data.readline())
developers = []
for i in range(numDevelopers):
    developer = []
    line = data.readline().split()
    numSkills = int(line[2])
    developer.append(i)
    developer.append(line[0])
    if line[0] not in companies:
        companies.append(line[0])
        companyDevelopers.append([])
    developer.append(int(line[1]))
    developer.append(line[3:])
    developers.append(developer)
    index = companies.index(line[0])
    companyDevelopers[index].append(developer)
# print(companyDevelopers)
# print(developers)

numManagers = int(data.readline())
managers = []
for i in range(numManagers):
    line = data.readline().split()
    details = []
    details.append(i)
    details.append(line[0])
    details.append(int(line[1]))
    managers.append(details)
    managersBonus.append(line)
managersBonus.sort(key= lambda x:x[1])
managersBonus.reverse()
print(managers)
print(plan)
data.close()

def workPotential(dev1, dev2):
    skills1 = dev1[3]
    skills2 = dev2[3]
    wp = 0
    distinct = 0
    for i in skills1:
        for j in skills2:
            if i == j:
                wp+=1
            else:
                distinct+=1
    return wp*(distinct-wp)

def bonusPotential(dev1,dev2):
    if dev1[1] ==dev2[1]:
        return dev1[2]*dev2[2]
    return 0

def totalPotential(dev1, dev2):
    return workPotential(dev1, dev2) + bonusPotential(dev1, dev2)

def managerScore(managers):
    # probably needs to be redone :/
    scores = []
    for managerProfile in managers:
        managerScores = []
        developerArray = []
        managerArray = []
        for person in developers:
            devScore= [person[0]]
            devScore.append(bonusPotential(managerProfile,person))
            developerArray.append(devScore)
        for person in managers:
            # includes all managers (including itself)
            manScoreArr = [person[0]]
            if person != managerProfile:
                manScoreArr.append(bonusPotential(managerProfile,person))
            else:
                manScoreArr.append(0)
            managerArray.append(manScoreArr)
        managerScores.append(developerArray)
        managerScores.append(managerArray)
        scores.append(managerScores)
    return scores
    # first array = first manager - first part of this array is scores w developers, second part is scores w managers

print(managerScore(managers))

# def finingAdjseats(plan):
#     seatnum=[]
#     for a in range(len(plan)):
#         for b in range(len(plan[a])):
#             if plan [a][b] == '_':
#                 coordval=[]
#                 ajval=0
#                 coordval.append(a)
#                 coordval.append(b)
                # if plan[a-1][b] == '':



