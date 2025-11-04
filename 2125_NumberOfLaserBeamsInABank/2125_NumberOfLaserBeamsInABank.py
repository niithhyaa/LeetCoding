class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        devices = [0]*len(bank)
        for i in range(len(bank)):
            for j in range(len(bank[i])):
                if (bank[i][j]=="1"):
                    devices[i]+=1
        devices = [x for x in devices if x != 0]
        for i in range(len(devices)-1):
            ans += devices[i]*devices[i+1]
        return ans
