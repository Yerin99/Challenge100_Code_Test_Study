from collections import deque


def get_moving_time(root, graph):
    # BFS 사용
    edge_t, vertex_t = 1, 2
    moving_time = {root: 0}

    visited = set()
    queue = deque(root)

    while queue:
        cur_node = queue.popleft()
        if cur_node not in visited:
            visited.add(cur_node)
            queue += graph[cur_node]
            for next_node in graph[cur_node]:
                if moving_time[cur_node] == 0:
                    time = moving_time[cur_node] + edge_t
                else:
                    time = moving_time[cur_node] + edge_t + vertex_t

                moving_time[next_node] = min(time, moving_time.get(next_node, 1e90))

    return moving_time


def main():
    n = int(input())
    friends = input().split()
    graph = {}
    friends_moving_time = []

    party_place = "~"
    arrival_time = 1e90

    for _ in range(n):
        line = input().split()
        graph[line[0]] = line[1:-1]

    # TO DO - 1 :
    # BFS를 이용해 friends가 위치해 있는 세 정점에서
    # 가능한 모든 정점까지의 거리를 구하여 moving_time에 저장하기

    for friend in friends:
        friends_moving_time.append(get_moving_time(friend, graph))

    # TO DO - 2 : 모든 정점에 대해,
    # 세 친구 모두 도달할 수 있는지
    # max 시간이 더 짧은지
    # 만약 시간이 같다면 알파벳 순서가 더 빠른지
    # checking 하여 답 내기

    for node in graph.keys():
        each_moving_time = []
        for moving_time in friends_moving_time:
            each_moving_time.append(moving_time.get(node, -1))
        if min(each_moving_time) != -1:
            max_time = max(each_moving_time)
            if arrival_time > max_time:
                arrival_time = max_time
                party_place = node
            elif arrival_time == max_time:
                party_place = min(party_place, node)

    # TO DO - 3 : 조건에 맞게 답 출력

    if party_place == "~" and arrival_time == 1e90:
        party_place = "@"
        arrival_time = -1

    print(party_place)
    print(arrival_time)


main()
