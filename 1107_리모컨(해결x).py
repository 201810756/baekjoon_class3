"""
수빈이는 TV를 보고 있다.
수빈이는 채널을 돌리려고 했지만, 버튼을 너무 세게 누르는 바람에, 일부 숫자 버튼이 고장났다.
리모컨에는 버튼이 0부터 9까지 숫자, +와 -가 있다.
+를 누르면 현재 보고있는 채널에서 +1된 채널로 이동하고, -를 누르면 -1된 채널로 이동한다.
채널 0에서 -를 누른 경우에는 채널이 변하지 않고, 채널은 무한대 만큼 있다.
수빈이가 지금 이동하려고 하는 채널은 N이다.
어떤 버튼이 고장났는지 주어졌을 때, 채널 N으로 이동하기 위해서 버튼을 최소 몇 번 눌러야하는지 구하는 프로그램을 작성하시오.
수빈이가 지금 보고 있는 채널은 100번이다.
"""
"""
import sys
N=int(sys.stdin.readline()) # N:이동하려고 하는 채널
M=int(sys.stdin.readline()) # M:고장난 버튼의 개수
if M!=0: # 고장난 버튼이 있으면
    break_list=list(map(int,sys.stdin.readline().split()))
current_ch=100
min_cnt=abs(N-current_ch)
channel_list=[-1]*10
for i in range(len(channel_list)):
    if i not in break_list:
        channel_list[i]=i
for i in range(1000001):
    for j in str(i):
        if channel_list[int(j)]==-1:
            break
        elif j==str(i)[-1]:
            min_cnt=min(min_cnt,abs(N-i)+len(str(i)))
print(min_cnt)
"""
import sys
target=sys.stdin.readline().rstrip()
cur_ch=100
min_cnt=abs(cur_ch-int(target))
M=int(sys.stdin.readline())
if M!=0:
    error=list(sys.stdin.readline().split())
elif M==0:
    print(min(len(target),min_cnt))
    exit()
if int(target)==cur_ch:
    print(0)
    exit()
cnt=0
click_ch=str()
def updown(ch,k):
    a=str(int(ch)-1)
    b=str(int(ch)+1)
    while a in error:
        if a=='0':
            break
        a=str(int(a)-1)
    while b in error:
        if b=='9':
            break
        b=str(int(b)+1)
    minus=k+a
    plus=k+b
    if abs(cur_ch-int(minus))>abs(cur_ch-int(plus)):
        return b
    else:
        return a
def check(ch):
    global click_ch
    if ch not in error:
        click_ch+=ch
    else:
        if ch=='0':
            check(str(int(ch)+1))
        elif ch=='9':
            check(str(int(ch)-1))
        else:
            check(updown(ch,click_ch))
for ch in target:
    cnt+=1
    check(ch)
cnt+=abs(int(target)-int(click_ch))
print(min(min_cnt,cnt))