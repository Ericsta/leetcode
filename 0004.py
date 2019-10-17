#not finish
import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        while True:
            if len(nums1)==len(nums2)==1:
                return (nums1[0]+nums2[0])/2
            print(nums1,nums2)
            nums1,nums2=self.compare(nums1,nums2)            
    def compare(self,list1,list2):
        
        mid_index1,mid_index2=int(len(list1)/2),int(len(list2)/2)
        print(mid_index1,mid_index2)
        list1_mid,list2_mid=list1[mid_index1],list2[mid_index2]
        print(list1_mid,list2_mid)
        
        
        if list1_mid>list2_mid:
            list1,list2=list1[-mid_index1:],list2[:mid_index2]
        else:
            list1,list2=list1[:mid_index1],list2[-mid_index2:]
            
            
        print(list1,list2)
        return list1,list2
