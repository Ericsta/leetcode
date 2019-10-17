class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        distance_dict = {}
        for id,num in enumerate(nums):     
            if num in distance_dict:
                return distance_dict[num],id
            else:
                distance_dict[target-num]=id
