class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        res=[]
        position={}
        for pos,idx in enumerate(order):
            position[idx]=pos
        for idx in position:
            if idx in friends:
                res.append(idx)
        return res
