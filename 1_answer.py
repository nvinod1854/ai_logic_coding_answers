import sys
d=list(map(int,sys.stdin.read().split()))
if not d:raise SystemExit
n=d[0]
v=d[1:]
m=min(n,len(v)//2)
a=[(v[2*i],v[2*i+1])for i in range(m)]
a.sort()
r=[]
for s,e in a:
    if not r or s>r[-1][1]:r.append([s,e])
    else:
        if e>r[-1][1]:r[-1][1]=e
for s,e in r:print(s,e)
