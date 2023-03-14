f=open('17_11.txt')
a=[]
c=[]
for s in f.readlines():
    a.append(int(s))
for i in  range(len(a)-1):
    if (a[i]+a[i+1])%2==0 and abs(a[i]+a[i+1])%10!=6:
        c.append((a[i]+a[i+1])//2)
print(len(c),max(c))