import sys
T=int(sys.stdin.readline()) # T:테스트케이스
for _ in range(T):
    dict={}
    cnt=1
    n=int(sys.stdin.readline())
    for _ in range(n):
        name,kind=sys.stdin.readline().split()
        if dict.get(kind)==None:
            dict[kind]=[]
        dict[kind].append(name)
    for k in dict.keys():
        cnt*=len(dict[k])+1
    print(cnt-1) # 알몸인 경우 제외