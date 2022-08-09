from typing import List


def pacificAtlantic(grid: List[List[int]]) -> List[List[int]]:
    """
    T:
    S:
    """
    def dfs(r0,c0, s):
        stack = [(r0,c0, 0)]  # prev value for comparison
        while stack:
            r,c, prev = stack.pop()
            if (r,c) not in s and 0<=r<len(grid) and 0<=c<len(grid[0]) and grid[r][c] >= prev:
                s.add((r,c))
                stack.append((r+1,c,grid[r][c]))
                stack.append((r-1,c,grid[r][c]))
                stack.append((r,c+1,grid[r][c]))
                stack.append((r,c-1,grid[r][c]))
    pac = set()
    atl = set()
    for R in range(len(grid)):
        dfs(R,0, pac)
        dfs(R,len(grid[0])-1, atl)
    for C in range(len(grid[0])):
        dfs(0, C, pac)
        dfs(len(grid)-1, C, atl)
    print("Pacific:", pac)
    print("Atlantic:", atl)
    
    return list(pac & atl)


inp = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
pacificAtlantic(inp)