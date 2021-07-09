class Solution:
    def checkRecord(self, s: str) -> bool:
        absent = 0
        late = 1
        pv =''
        for i in s:
            if i == 'A':
                absent +=1
            if late == 2 and i!='L':
                late = 1
            if i==pv and i =='L':
                late +=1
            pv = i
        if absent>1 or late >2:
            return False
        else:
            return True
