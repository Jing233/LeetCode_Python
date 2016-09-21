class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(candidates)
        L = len(nums)
        # table[i] is a list of all possible solution if the target is i
        table = [[] for i in range(target + 1)]
        for i in range(1, target+1):
            for j in range(L):
                num = nums[j]
                if num > i:
                    break
                if num == i:
                    table[i].append([num])
                # DP substructure is presented here
                elif table[i - num]:
                    # for each sub-solution
                    for sub in table[i - num]:
                        # this if is used for eliminating duplicate elements. This is also why we sort the candidates at first.
                        if num >= sub[-1]:
                            table[i].append(sub + [num])
        return table[target]