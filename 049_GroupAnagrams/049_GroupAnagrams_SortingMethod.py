class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        for i in range(len(strs)):
            s = ''.join(sorted(strs[i]))
            if s not in hmap:
                hmap[s] = []
            hmap[s].append(strs[i])
        return list(hmap.values())
