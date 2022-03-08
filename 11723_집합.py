
import sys
M=int(sys.stdin.readline())
S=set()
for _ in range(M):
    order=sys.stdin.readline().split()
    if len(order)==1:
        command=order[0]
        if command == 'empty':
            S.clear()
        elif command == 'all':
            S = set([i for i in range(1, 21)])
    else:
        command=order[0]
        value=order[1]
        if command == 'add':
            S.add(int(value))
        elif command == 'remove':
            if int(value) in S:
                S.remove(int(value))
        elif command == 'check':
            if int(value) in S:
                print(1)
            else:
                print(0)
        elif command == 'toggle':
            if int(value) in S:
                S.remove(int(value))
            else:
                S.add(int(value))
        elif command == 'empty':
            S.clear()
        elif command == 'all':
            S = set([i for i in range(1, 21)])

