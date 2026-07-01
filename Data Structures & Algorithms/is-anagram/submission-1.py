class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count={}
        if len(s)!=len(t):
            return False
        for c in s:
            count[c]=count.get(c,0)+1
        for p in t :
            if p not in count:
                return False
            count[p]-=1
            if count[p]<0:
                return False
        return True

       

       
