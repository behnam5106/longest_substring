class Solution:
    def lengthOfLongestSubstring(self, s:str) -> int:
        s_sub=""
        for k in range(0,len(s)):
            #n=len(s)-k 
            print("len(s):",len(s))   
            print("k:",k)     
            for j in range(0,k+1):
                s_sub=s[j:len(s)-k+j]
                print("j:",j)
                print("s_sub:",s_sub, "len(s_sub):",len(s_sub))
                x=0
                for i in s_sub:
                    print("i:",i)
                    if s_sub.count(i)==1:
                        x=x+1
                        print("x:",x)
                if x==len(s_sub):
                    print("OK")
                    return x
 
s="1233456sg//s;js;ojssoustu957ll4-9;gmgslkg1ss5f"

solution=Solution()
print(solution.lengthOfLongestSubstring(s))
     

