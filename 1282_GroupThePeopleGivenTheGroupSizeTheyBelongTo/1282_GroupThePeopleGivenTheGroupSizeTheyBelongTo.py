class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        res = []
        gsize_dict = {}

        for i in range(len(groupSizes)):
            size = groupSizes[i]
            if size not in gsize_dict:
                gsize_dict[size] = []
            gsize_dict[size].append(i)
            if len(gsize_dict[size]) == size :
                res.append(gsize_dict[size])
                gsize_dict[size] = [] 
        return res
