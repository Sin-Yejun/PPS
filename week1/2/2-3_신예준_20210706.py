class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = list(strs[0])
        for i in range(len(strs)):
            li = []
            if len(output) >= len(strs[i]):
                size = len(strs[i])
            else:
                size = len(output)
            for j in range(size):
                if output[j] == strs[i][j]:
                    li.append(output[j])
                else:
                    break
            output = li
        out = "".join(output)
        return out
