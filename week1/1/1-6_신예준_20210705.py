class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        li = [[1],[1,1]]
        for i in range(2, numRows):
            newlist = [1]
            j=0
            while len(newlist) != len(li[i-1]):
                newlist.append(li[i-1][j]+li[i-1][j+1])
                j+=1
            newlist.append(1)
            li.append(newlist)
        return li
