f = open('24_28.txt', 'r')
s=f.read()
k=0
x=0
p=27
for i in range(len(s)):
    if s[i]!='*':
        k+=1
    else:
        x=max(k,x)
        k=0
x=max(x,k)
print(x+2)