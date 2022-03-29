


n = 15 
l = []
for i in range(n):
    l.append(list(map(int,input().split())))

for i in range(len(l)-2,-1,-1):
    for j in range(len(l[i])):
        l[i][j] = l[i][j]+max(l[i+1][j],l[i+1][j+1])
print('\n\n')
for i in l:
    print(i)
print(l[0][0])
