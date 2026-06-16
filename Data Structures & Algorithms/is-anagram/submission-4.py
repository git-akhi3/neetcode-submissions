class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS , countT = {} , {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            # r,2 ; a,2 ; c,2 ; e,1 ;
            countT[t[i]] = 1 + countT.get(t[i], 0)
            # r,2 ; a,2 ; c,2 ; e,1 ;
        for c in countS :
            if countS[c] != countT.get(c , 0 ):
                return False

        return True




         