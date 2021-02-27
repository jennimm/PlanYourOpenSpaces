filename = 'a_solar'
data = open(filename+'.txt','r')
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
    if dev1[1] == dev2[1]:
        return int(dev1[2])*int(dev2[2])
    else:
        return 0

def totalPotential(dev1, dev2):
    return workPotential(dev1, dev2) + bonusPotential(dev1, dev2)

def managerScore(managers, developers):
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


def developerScores(developers, numDevelopers):
    scores = []
    for i in range(numDevelopers):
        scores.append([])
        for j in range(numDevelopers):
            if j == i:
                scores[i].append(0)
            elif j < i:
                scores[i].append(scores[j][i])
            else:
                scores[i].append(totalPotential(developers[i], developers[j]))
    return scores

def greatestDeveloperScores(developerScoresArray, ids):
    greatest = 0
    index=0
    for i in ids:
        if sum(developerScoresArray[i]) > greatest:
            greatest = sum(developerScoresArray[i])
            index = i  
    if index == ids[0]:
        developerScoresArray[ids[1]][ids[0]] = 0
    else:
        developerScoresArray[ids[0]][ids[1]] = 0
    return index, developerScoresArray  

def findingAdjseats(plan, char):
    seatnum=[]
    for a in range(len(plan)):
        for b in range(len(plan[a])):
            if plan [a][b] == char:
                coordval=[]
                ajval=0
                coordval.append(a)
                coordval.append(b)
                if a == (len(plan)-1) and b == (len(plan[a])-1) :
                    if plan[a-1][b] == char :
                        ajval+=1
                    if plan[a][b-1] == char:
                        ajval+=1
                elif a < (len(plan)-1) and b == (len(plan[a])-1) :
                    if plan[a-1][b] == char :
                        ajval+=1
                    if plan[a][b-1] == char:
                        ajval+=1
                    if plan[a+1][b] == char:
                        ajval+=1
                elif a == (len(plan)-1) and b < (len(plan[a])-1) :
                    if plan[a-1][b] == char :
                        ajval+=1
                    if plan[a][b-1] == char:
                        ajval+=1
                    if plan[a][b+1] == char:
                        ajval+=1
                else:
                    if plan[a-1][b] == char :
                        ajval+=1
                    if plan[a][b-1] == char:
                        ajval+=1
                    if plan[a][b+1] == char:
                        ajval+=1
                    if plan[a+1][b] == char:
                        ajval+=1
                coordval.append(ajval)
                seatnum.append(coordval)
    return seatnum

def highestScoringPair(scores):
    highScore = 0
    index =[0,0]
    for x in range(len(scores)):
        for y in range(len(scores[0])):
            if scores[x][y] > highScore:
                highScore = scores[x][y]
                index = [x,y]
    
    return index

def getHighest(developer, scores):
    sortedScores = []
    developerScores = scores[developer].copy()
    while len(developerScores) > len(sortedScores):
        maxScore = max(developerScores)
        index = developerScores.index(maxScore)
        if index != developer:
            sortedScores.append(index)
        developerScores[index] = -1
    return sortedScores

def solutionFinder(plan, scores, W, H):
    seatsArray = findingAdjseats(plan,'_')
    if len(seatsArray) == 0:
        return developers
    else: 
        highestSpacesAv = seatsArray[0]
        for i in range(len(seatsArray)):
            if seatsArray[i][-1] > highestSpacesAv[-1]:
                highestSpacesAv = seatsArray[i]
        
        bestDevelopers = highestScoringPair(scores)
        developerId, scores = greatestDeveloperScores(scores, bestDevelopers)
        plan[highestSpacesAv[0]][highestSpacesAv[1]] = developerId
        developers[developerId] = [highestSpacesAv[0], highestSpacesAv[1]]
        while highestSpacesAv[-1] > 0:  
            sortedScores = getHighest(developerId, scores)
            nextBest = sortedScores[0]
            scores[developerId][nextBest] = 0
            if highestSpacesAv[1]+1 < W and plan[highestSpacesAv[0]][highestSpacesAv[1]+1] == "_":
                plan[highestSpacesAv[0]][highestSpacesAv[1]+1] = nextBest
                developers[nextBest] = [highestSpacesAv[0], highestSpacesAv[1]+1]

            elif W-highestSpacesAv[1]-1 >= 0 and plan[highestSpacesAv[0]][highestSpacesAv[1]-1] == "_":
                plan[highestSpacesAv[0]][highestSpacesAv[1]-1] = nextBest
                developers[nextBest] = [highestSpacesAv[0], highestSpacesAv[1]-1]

            elif highestSpacesAv[0]+1 < H and plan[highestSpacesAv[0]+1][highestSpacesAv[1]] == "_":
                plan[highestSpacesAv[0]+1][highestSpacesAv[1]] = nextBest
                developers[nextBest] = [highestSpacesAv[0]+1, highestSpacesAv[1]]
              
            else:
                if H-highestSpacesAv[0]-1 >=0:
                    plan[highestSpacesAv[0]-1][highestSpacesAv[1]] = nextBest
                    developers[nextBest] = [highestSpacesAv[0]-1, highestSpacesAv[1]]
            
            highestSpacesAv[-1] -= 1
        return solutionFinder(plan, scores, W, H)


    
developerScores = developerScores(developers, numDevelopers)
solutions = solutionFinder(plan, developerScores, W, H)
fileOutput = []
for i in solutions:
    if len(i) > 2:
        fileOutput.append('X\n')
    else:
        fileOutput.append(str(i[0])+" "+str(i[1])+"\n")
outputfile = open(filename+'OUT.txt',"a")
outputfile.writelines(fileOutput)
outputfile.close()