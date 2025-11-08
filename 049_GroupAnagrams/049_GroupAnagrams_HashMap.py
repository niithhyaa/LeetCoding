class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in range(len(strs)):
            freq_arr = [0]*26
            for c in strs[i]:
                freq_arr[ord(c) - ord('a')] += 1
            if tuple(freq_arr) not in d:
                d[tuple(freq_arr)] = []
            d[tuple(freq_arr)].append(strs[i])
        return list(d.values())
