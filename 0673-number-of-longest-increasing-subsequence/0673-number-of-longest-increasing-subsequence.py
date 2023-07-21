class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        sub,nums_max,nums_dict=[],[],collections.defaultdict(list)
        for num in nums:
            index=bisect.bisect_left(sub,num)
            if index==len(sub):
                sub.append(num)
            else:
                sub[index]=num
            nums_max.append(index)
            nums_dict[index].append((sum([lens if max_<num else 0  for lens,max_ in nums_dict[index-1]]) or 1,num))
        return sum([i for i,_ in nums_dict[len(sub)-1]])
        