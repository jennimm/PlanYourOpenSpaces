data = open('a_solar.txt','r')
W,H = data.readline().split()
W = int(W)
H = int(H)
plan = []
width = [0]*W
companies = []
companyDevelopers = []
managersBonus = []

for i in range(H):
    plan.append(width)
for i in range(H):
    line = data.readline()
    for j in range(W):
        plan[i][j] = line[j]

numDevelopers = int(data.readline())
developers = []
for i in range(numDevelopers):
    developer = []
    line = data.readline().split()
    numSkills = int(line[2])
    developer.append(line[0])
    if line[0] not in companies:
        companies.append(line[0])
        companyDevelopers.append([])
    developer.append(line[1])
    developer.append(line[3:])
    developers.append(developer)
    index = companies.index(line[0])
    companyDevelopers[index].append(developer)
print(companyDevelopers)
print(developers)

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
data.close()


