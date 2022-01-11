class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        """
        idea is to access the smallest value and evict it, since it would not be        useful for any subsequent operation, while evicting multiply it with smaller neighbor and add it to result
        """
        stack = []
        
        n = len(arr)
        result =0
        
        for i in range(n):
            num = arr[i]
            
            #keep popping all small elements as they would be not needed in future
            while stack and stack[-1]<= num:
                prev_small_num= stack.pop()
                
                #calculate the non leaf node
                if stack:
                    result += prev_small_num * (min(stack[-1], num))
                else: result += prev_small_num *num
                    
            stack.append(num)
            
        while stack:
            prev_small_num = stack.pop()
            if stack: result += prev_small_num * stack[-1]
        return result