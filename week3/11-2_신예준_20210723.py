class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        i, j = sr, sc
        t = [(i,j)]
        origin = image[i][j]
        if origin == newColor:
            return image
        while len(t)!=0:
            if t[0][0] >=1 and image[t[0][0]-1][t[0][1]] == origin:
                t.append((t[0][0]-1,t[0][1]))
                image[t[0][0]-1][t[0][1]] = newColor
            if t[0][0] <len(image)-1 and image[t[0][0]+1][t[0][1]] == origin:
                t.append((t[0][0]+1,t[0][1]))
                image[t[0][0]+1][t[0][1]] = newColor
            if t[0][1] >=1 and image[t[0][0]][t[0][1]-1] == origin:
                t.append((t[0][0],t[0][1]-1))
                image[t[0][0]][t[0][1]-1] = newColor
            if t[0][1] < len(image[0])-1 and image[t[0][0]][t[0][1]+1] == origin:
                t.append((t[0][0],t[0][1]+1))
                image[t[0][0]][t[0][1]+1] = newColor
            image[t[0][0]][t[0][1]] = newColor
            del t[0]
        return image
