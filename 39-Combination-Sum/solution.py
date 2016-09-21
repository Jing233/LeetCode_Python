class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        output = []
        if candidates==[]:
            return []
        
        def recur_find(index=0, current=0, current_path=[]):
            if current == target:
                output.append(current_path)
                return
            for i in range(index,len(candidates)):
                new_number = current+candidates[i]
                if new_number <= target:
                    recur_find(i, new_number, current_path+[candidates[i]])
        recur_find()
        return output