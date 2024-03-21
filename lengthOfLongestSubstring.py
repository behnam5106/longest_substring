class Solution:
    def lengthOfLongestSubstring(self, s:str) -> int:
        window_start = 0
        max_length = 0
        char_index_map = {}
        for window_end in range(len(s)):
            end_char = s[window_end]
            print("window_end",window_end)
            if end_char in char_index_map:
                window_start = max(window_start, char_index_map[end_char] + 1)
                char_index_map[end_char] = window_start
            char_index_map[end_char] = window_end
            
            max_length = max(max_length, window_end - window_start +1)
        
        return max_length, print ("ok")
 
s="12345"

solution=Solution()
print(solution.lengthOfLongestSubstring(s))
     

