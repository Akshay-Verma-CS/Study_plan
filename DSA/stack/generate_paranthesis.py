class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        totalChars = n*2
        l = []
        def Generate_Paranthesis(instance,left,right):
            if len(instance) == totalChars:
                l.append(instance)
                return
            
            if left < n :
                Generate_Paranthesis(instance + "(" , left + 1 , right)
            if right < left:
                Generate_Paranthesis(instance + ")" , left , right + 1)
            
            
        Generate_Paranthesis("",0,0)
        return l