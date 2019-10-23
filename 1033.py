class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        a,b,c = sorted([a,b,c])
        if c-b==2 or b-a ==2:
            min =1
        else :
            min = self.mintwo(a,b)+self.mintwo(b,c)
        max= b-a+c-b-2

        return min,max
    def mintwo(self,a,b): 
        return 0 if a==b-1 else 1
