class DisjointSet(object):
    def __init__(self, n, path_compression=False):
        self.parent = [i for i in range(n+1)]
        self.path_compression = path_compression
    
    def find(self, x):
        if self.parent[x] != x:
            x_root = self.find(self.parent[x])
            if self.path_compression:
                self.parent[x] = x_root
            return x_root
        return x

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x > y:
            self.parent[x] = y
        else:
            self.parent[y] = x

    def union_graph(self, graph):
        for g in graph:
            self.union(g[0], g[1])
    
    def __str__(self):
        msg = f'''
        부모 노드: {self.parent[1:]}
        소속 집합: {[self.find(i) for i in self.parent[1:]]}
        '''
        return msg

def check_cycle(graph, n):
    cycle = False
    ds = DisjointSet(n)
    for g in graph:
        x_root = ds.find(g[0])
        y_root = ds.find(g[1])
        if x_root == y_root:
            cycle = True
            break
        else:
            ds.union(x_root, y_root)
    return cycle



def kruskal_algorithm(graph, n):
    "Find minimum spanning tree using Kruskal algorithm"
    graph.sort(key = lambda x : x[2])
    mst = []
    ds = DisjointSet(n)

    while True:
        if len(mst) == n-1: break
        u, v, w = graph.pop(0)
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst.append((u, v, w))
    return mst


def dijkstra_algorithm(_graph, start, n):
    graph = [[] for _ in range(n+1)]
    for u, v, w in _graph:
        graph[u].append((v, w))

    INF =  int(1e9)
    distance = [INF] * (n + 1)
    visited = [False] * (n + 1)

    distance[start] = 0
    visited[start] = True
    for v, w in graph[start]:
        distance[v] = w
    
    for i in range(n-1):
        now = sorted([i for i in range(1, n+1) if not visited[i]], key = lambda x: distance[x])[0]
        visited[now] = True

        for v, w in graph[now]:
            cost = distance[now] + w
            if cost < distance[v]:
                distance[v] = cost
    
    return distance


def dijkstra_algorithm_2(_graph, start, n):
    "Dijkstra algorihtm using heapq"
    import heapq

    graph = [[] for _ in range(n+1)]
    for u, v, w in _graph:
        graph[u].append((v, w))

    INF =  int(1e9)
    distance = [INF] * (n + 1)
    
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for v, w in graph[now]:
            cost = dist + w
            if cost < distance[v]:
                distance[v] = cost
                heapq.heappush(q, (cost, v))
    return distance


def floyd_warshall_algorithm(_graph, n):
    INF =  int(1e9)
    graph = [[INF] * (n+1) for _ in range(n+1)]
    for u in range(1, n+1):
        for v in range(1, n+1):
            if u == v:
                graph[u][v] = 0
    for u, v, w in _graph:
        graph[u][v] = w

    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
    
    return graph

if __name__ == '__main__':
    n = 4
    graph = [[1, 2, 4], [1, 4, 6], [2, 1, 3], [2, 3, 7], [3, 1, 5], [3, 4, 4], [4, 3, 2]]
    distance = floyd_warshall_algorithm(graph, n)
    print(distance)
