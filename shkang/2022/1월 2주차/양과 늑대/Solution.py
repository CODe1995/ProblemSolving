from collections import deque

def isVisited(visited:int, dest:int):
    if visited & 1<<dest == 1:
        return True
    return False

def getSheepWolf(visited:int ,info:list):
    status = [0,0]  # 양, 늑대의 수
    for i in range(len(info)):
        if visited & 1<<i:
            status[info[i]]+=1        
    return status


def deepCopy(src:list):
    ret = []
    for i in src:
        ret.append(i)
    return ret


def bfs(originInfo:list, graph:list):
    # info의 bit화
    answer = 0
    rinfo = [-1]*len(originInfo)
    for i in range(len(originInfo)):        
        rinfo[i] = originInfo[i]
    dqSet = set()
    dq = deque()
    curAdd = [0,1,deepCopy(rinfo)]
    dq.append(curAdd) #다음 방문 index, visited, info
    tupleInfo = tuple(curAdd[2])
    dqSet.add(tuple([curAdd[0],curAdd[1],tupleInfo]))
    while dq:
        index, visited, info = dq.popleft()
        answer = max(answer, getSheepWolf(visited, originInfo)[0])
        for _next in graph[index]:
            if isVisited(visited, _next):
                continue
            # 빈 땅인지 양인지 늑대인지 체크
                # 양 또는 늑대일 때 갯수 체크
                # visited 초기화            
            if info[_next] == 0:    # 양인 경우
                info[_next] = -1
                visited = 1<<_next
            elif info[_next] == 1:  # 늑대인 경우
                info[_next] = -1
                status = getSheepWolf(visited, originInfo)
                visited = 1<<_next
                if status[0]<=status[1]: #늑대가 많음
                    continue
            visited |= 1<<_next
            curAdd = [_next, visited, deepCopy(info)]
            tupleInfo = tuple(curAdd[2])
            if tuple([curAdd[0],curAdd[1],tupleInfo]) in dqSet:
                continue
            dqSet.add(tuple([curAdd[0],curAdd[1],tupleInfo]))
            dq.append(curAdd)
    return answer



def solution(info, edges):
    graph = [list() for _ in info]
    for a,b in edges:        
        graph[a].append(b)
        graph[b].append(a)    
    answer = bfs(info, graph)
    return answer



print(solution([0,0,1,1,1,0,1,0,1,0,1,1],[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))
print(solution([0,1,0,1,1,0,1,0,0,1,0]	,[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]	))
print(solution([0,1]	,[[0,1]]	))