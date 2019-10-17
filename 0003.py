class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        alpha_dict={}
        start_index,size =0,0
        for stop_size in range(len(s)):
            if s[stop_size] in alpha_dict:
                start_index = max(alpha_dict[s[stop_size]],start_index)
            size = max(size,stop_size-start_index+1)
            alpha_dict[s[stop_size]]=stop_size+1
        return size
    
