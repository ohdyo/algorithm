import sys

input = sys.stdin.readline

N = int(input())
num = list(map(int,input().split()))
plus,minus,multi,divide = map(int,input().split())



def dfs(n,sm,add,sub,mul,div):
    global mn, mx
    
    if sm < int(-1e9) or int(1e9) < sm:
        return
    
    if n==N:
        mn = min(mn,sm)
        mx = max(mx,sm)
        return
    
    
    if add>0:
        dfs(n+1,sm+num[n],add-1,sub,mul,div)
    if sub>0:
        dfs(n+1,sm-num[n],add,sub-1,mul,div)
    if mul>0:
        dfs(n+1,sm*num[n],add,sub,mul-1,div)
    if div>0:
        dfs(n+1,int(sm/num[n]),add,sub,mul,div-1)
    
mn, mx = int(1e9),int(-1e9) 

dfs(1,num[0],plus,minus,multi,divide)

print(mx,mn,sep='\n')
