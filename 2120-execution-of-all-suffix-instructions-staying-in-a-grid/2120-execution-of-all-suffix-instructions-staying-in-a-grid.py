class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        max_up_steps = startPos[0] + 1
        max_down_steps = n - startPos[0]
        max_left_steps = startPos[1] + 1
        max_right_steps = n - startPos[1]
        
        dirs = {
            "R": (0, 1),
            "L": (0, -1),
            "U": (-1, 0),
            "D": (1, 0)
        }
        m = len(s)
        row_dict = {0: 0}
        col_dict = {0: 0}
        r = c = 0
        t = 1

        ans = []
        for i in range(m - 1, -1, -1):
            max_steps = m - i
            dr, dc = dirs[s[i]]
            r -= dr
            c -= dc
            
            if r - max_up_steps in row_dict:
                max_steps = min(max_steps, t - row_dict[r - max_up_steps] - 1)
                
            if r + max_down_steps in row_dict:
                max_steps = min(max_steps, t - row_dict[r + max_down_steps] - 1)
                
            if c - max_left_steps in col_dict:
                max_steps = min(max_steps, t - col_dict[c - max_left_steps] - 1)
                
            if c + max_right_steps in col_dict:
                max_steps = min(max_steps, t - col_dict[c + max_right_steps] - 1)
            
            row_dict[r] = t
            col_dict[c] = t
            t += 1
            ans.append(max_steps)
            
        return reversed(ans)