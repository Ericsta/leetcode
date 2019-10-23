class Solution:
    def __init__(self):
        self.flag=1
        self.result=0
    def reverse(self, x: int) -> int:
        if x<0:
            self.flag=-1
        if abs(x)<10:
            self.result = x+self.result*10            
           
            return self.flag*self.result
        else:
            x,y=self.cal_num(abs(x))
            self.result = y+self.result*10
            self.reverse(int(x))
            if self.result > 2147483647 or self.result < -2147483648 :
                return 0
            return self.flag*self.result
    
    def cal_num(self,x):
        return  x/10,x%10
