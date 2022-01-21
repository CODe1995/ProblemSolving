n = 0
info = []
answer = 0
answerTarget = []

def getScore(target:list):
    global answer, answerTarget
    score = [0,0]
    for i in range(11):
        if info[i] < target[i]:
            score[1]+= 10-i
        elif info[i] == 0 and target[i] == 0:
            pass
        else:
            score[0]+= 10-i
    if answer < score[1] - score[0]:            
        answer = score[1] - score[0]
        answerTarget = [num for num in target]
    return

def dfs(depth:int, target:list, index:int):
    global answer, answerTarget
    if depth==n:
        getScore(target)
        return
    for i in range(index, 11):
        if info[i]<target[i]:
            continue
        target[i]+=1
        dfs(depth+1, target, index)
        target[i]-=1
        dfs(depth, target, index+1)

def solution(_n, _info):
    global n, info, answerTarget, answer
    n, info = _n, _info    
    answer = 0
    answerTarget = [0]*11
    dfs(0,[0]*11,0)
    return answerTarget

print(solution(5,[2,1,1,1,0,0,0,0,0,0,0]))
print(solution(1,[1,0,0,0,0,0,0,0,0,0,0]))
print(solution(9,[0,0,1,2,0,1,1,1,1,1,1]))
print(solution(10,[0,0,0,0,0,0,0,0,3,4,3]))