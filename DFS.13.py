n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
s = []


def DFS(depth, idx, n, m):
    if depth == m:
        print(' '.join(map(str, s)))
        return

    for i in range(idx, n):
        s.append(arr[i])
        DFS(depth+1, i, n, m)
        s.pop()

DFS(0)