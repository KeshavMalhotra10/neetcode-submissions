class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numIslands = 0
        m = len(grid) #max amount of rows
        n = len(grid[0]) #max amount of columns
        visited = set() #to track coordinates
        
        def dfs(r,c):
            addOne = False
            #1. check if the bounds are correct
            if r < 0 or c < 0 or r >= m or c >= n:
                return
            #2. check if this coordinate already visited
            elif (r,c) in visited:
                return
            elif grid[r][c] == '0':
                return
            #3. Add coordinate to visited
            visited.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)


        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i,j) not in visited:
                    dfs(i,j)
                    numIslands += 1

        return numIslands


        

        