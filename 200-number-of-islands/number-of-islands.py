class Solution(object):
    def numIslands(self, grid):
        rows,cols=len(grid),len(grid[0])
        visited=[[0]*cols for _ in range(rows)]
        def traverse(r,c):
            if r<0 or c<0 or r>=rows or c>=cols or visited[r][c]==1:
                return
            if visited[r][c] == 1 or grid[r][c] == "0":
                return
            visited[r][c]=1
            traverse(r,c-1);traverse(r-1,c);traverse(r,c+1);traverse(r+1,c)
        count=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and visited[r][c]!=1:
                    count+=1
                    traverse(r,c)
        return count