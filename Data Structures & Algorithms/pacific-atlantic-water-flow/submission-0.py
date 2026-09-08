'''
Pacific ocean: water flows from top and left side
Atlantic Ocean: water flows from bottom and right side

Water can only flow to neighboring cels of eql or lower height


Goal: return a 2d list of cells where water can flow to both pacific and atlantic ocean, each element [r,c]

Solution:
1. Use BFS recursively, with rules mentioned above to find certain cells and append them, use a hashset to ensure that the same coordinates are not repeated

'''

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights) #for rows
        n = len(heights[0]) # for columns

        pac, atl = set(), set() #keep a set of values for pacific ocean, and a set of valus for atlantic ocean
        res = [] #final result

        def dfs(r,c, visit, prevHeight):
            #check 1: is the coordinate bounded in visit or less than prevHeight --> then return
            if (r < 0 or c < 0 or r>= m or c >= n) or (r,c) in visit or heights[r][c] < prevHeight:
                return
            visit.add((r,c))
            
            #perform bfs for all neighbours
            dfs(r+1,c,visit,heights[r][c]) 
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])
            
            #how to know if a cell is next to the ocean?
            #well either starting row, last row, starting column, last column

        #pacific ocean: starting row and column, perform bfs on each
        for c in range(n):
            dfs(0,c,pac, heights[0][c])
            dfs(m-1,c, atl, heights[m-1][c])
        
        #atlantic ocean: last row and last column
        for r in range(m):
            dfs(r,0,pac, heights[r][0])
            dfs(r,n-1,atl, heights[r][n-1])
        
        for i in range(m):
            for j in range(n):
                if (i,j) in pac and (i,j) in atl:
                    res.append([i,j])
        return res
            


        




    