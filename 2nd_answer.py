import sys
d=list(map(int,sys.stdin.read().strip().split()))
if not d:
    print(0)
else:
    n=d[0]
    v=d[1:1+n]
    r=d[1+n:]
    n=min(n,len(v))
    if n==0:
        print(0)
    else:
        k=r[0] if r else 1
        k=max(1,min(k,n))
        c=sum(v[:k])
        m=c
        for i in range(k,n):
            c+=v[i]-v[i-k]
            if c>m: m=c
        print(m)
