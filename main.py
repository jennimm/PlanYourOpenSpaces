data = open('a_solar.txt','r')
W,H = data.readline().split()
W = int(W)
H = int(H)
plan = []
width = [0]*W
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
    skills = line[3:]
    developer.append(line[0])
    developer.append(line[1])
    developer.append(skills)
    developers.append(developer)
print(developers)

numManagers = int(data.readline())
managers = []
for i in range(numManagers):
    line = data.readline().split()
    managers.append(line)

print(managers)
data.close()