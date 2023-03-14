a=[]
b=[]
f = open("26_2.txt")
n = int(f.readline())
for i in range(n):
    a1,a2 = map(int, f.readline().split())
    a.append((a1,a2))
a=sorted(a)[::-1]
for i in range(len(a)-1):
    if a[i][0]==a[i+1][0] and abs(a[i][1]-a[i+1][1])==3:
        b.append((a[i],a[i+1]))
print(sorted(b)[::-1])

