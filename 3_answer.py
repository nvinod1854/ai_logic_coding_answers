import sys
s=sys.stdin.read().strip()
if not s:print(0)
else:
    last=[-1]*26
    l=0
    a=0
    for i,ch in enumerate(s):
        idx=ord(ch)-97
        if last[idx]>=l:l=last[idx]+1
        last[idx]=i
        cur=i-l+1
        if cur>a:a=cur
    print(a)
