from collections import deque
def solution(priorities, location):
    answer = []  # 실행된 프로세스
    queue = deque((i, j) for i, j in enumerate(priorities)) #deque([(0, 2), (1, 1), (2, 3), (3, 2)])
    while queue:
        process = queue.popleft()
        print(process)
        # 우선순위가 더 높은 프로세스가 하나라도 있으면 큐에 다시 추가 / 아니면 해당 프로세스 실행
        if queue and any(process[1] < q[1] for q in queue):
            queue.append(process)
        else:
            answer.append(process)

    # location 실행 순서 찾기
    for i in answer:
        if i[0] == location:
            return answer.index(i) + 1

print(solution([2, 1, 3, 2]	,2))