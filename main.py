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
    developer.append(line[1])
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
    line[-1] = int(line[-1])
    managers.append(line)
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

<<<<<<< Updated upstream
def bonusPotential(dev1,dev2):
    if dev1[1] == dev2[1]:
        return int(dev1[2])*int(dev2[2])

def totalPotential(dev1, dev2):
    return workPotential(dev1, dev2) + bonusPotential(dev1, dev2)

print(totalPotential(developers[0],developers[2]))
=======
def finingAdjseats(plan):
    seatnum=[]
    for a in range(len(plan)):
        for b in range(len(plan[a])):
            if plan [a][b] == '_':
                coordval=[]
                ajval=0
                coordval.append(a)
                coordval.append(b)
                if plan[a-1][b] == '':



>>>>>>> Stashed changes
