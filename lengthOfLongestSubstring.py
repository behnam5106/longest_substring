class Solution:
    def lengthOfLongestSubstring(self, s:str) -> int:
        s_unicMember=""
        s_sub=""
        for k in range(0,len(s)):
            n=len(s)-k
          
            for j in range(0,k+1):
                s_sub=s[k:n]
                print(s_sub)
                for i in range(0,len(s_sub)):
                    if s_unicMember.find(s_sub[i])==-1:
                        s_unicMember=s_unicMember+s_sub[i]
                    if len(s_unicMember)==len(s_sub):
                        return len(s_unicMember)



s="abcdabbbbbn"

solution=Solution()

print(solution.lengthOfLongestSubstring(s))



