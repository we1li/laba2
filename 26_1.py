a=[]
z=[]
c=0
k=0
f = open("26_1.txt")
s,n = map(int, f.readline().split())
for i in range(n):
    x = int(f.readline())
    a.append(x)
a=sorted(a)
for i in range(len(a)):
    c=c+a[i]
    if c<=s:
      z.append(a[i])
z.pop(-1)
for i in range(len(a)):
    if sum(z)+a[i]<=s:
        k=a[i]
print(len(z)+1,k)

