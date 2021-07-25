class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        output = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    output+=4
                    if i>=1 and grid[i-1][j]==1:
                        output -=2
                    if j>=1 and grid[i][j-1]==1:
                        output -=2
        return output
