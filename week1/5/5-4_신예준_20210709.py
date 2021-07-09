class Solution:
    def dayOfYear(self, date: str) -> int:
        days = [31,28,31,30,31,30,31,31,30,31,30,31]
        year = int(date[0:4])
        month = int(date[5:7])
        day = int(date[8:10])
        answer = 0
        for i in range(month-1):
            answer += days[i]
        answer += day
        if ((year % 4 == 0) and (year %100 != 0)) or (year % 400 == 0):
            answer += 1
            if month < 3:
                answer -=1
        return answer
