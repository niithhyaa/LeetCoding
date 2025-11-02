class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        n = len(students)
        ans = 0
        for i in range(n):
            while students[i]!=seats[i]:
                if seats[i]<students[i]:
                    students[i]-=1
                    ans+=1
                if seats[i]>students[i]:
                    students[i]+=1
                    ans+=1
        return ans
