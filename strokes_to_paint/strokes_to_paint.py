class Solution:
    def strokes_to_paint(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        row = len(grid)
        col = len(grid[0])
        visited = set()
        count = 0
        directions=[(-1,0),(0,1),(1,0),(0,-1)]
        def findIsland(x,y):
            color = grid[x][y]
            for dx, dy in directions:
                nx,ny = x+dx, y+dy
                if 0<=nx<row and 0<=ny<col and grid[nx][ny]== color and (nx,ny) not in visited:
                    visited.add((nx,ny))
                    findIsland(nx,ny)
            
        for x in range(row):
            for y in range(col):
                if (x,y) not in visited:
                    count +=1
                    visited.add((x,y))
                    findIsland(x,y)         
        return count
