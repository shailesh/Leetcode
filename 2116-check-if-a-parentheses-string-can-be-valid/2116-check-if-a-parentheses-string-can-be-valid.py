class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        '''1. Intuitively, odd-length s cannot be valid.
        2. traverse each parenthesis forward, treat all unlocked Parentheses as'(' and check if there is ')'
        3. that cannot be eliminated by previous '(', if it exists, then the input s can't be valid.
        
        4. traverse each parenthesis backward, treat all unlocked Parentheses as')' and check if there is '('
        5. that cannot be eliminated by previous ')', if it exists, then the input s can't be valid.
        '''
        if len(s) % 2:  
            return False

        balance = 0
        for i in range(len(s)):
            balance += 1 if s[i] == '(' or locked[i] == '0' else -1
            if balance < 0:
                return False

        balance = 0
        for i in range(len(s) - 1, -1, -1):
            balance += 1 if s[i] == ')' or locked[i] == '0' else -1
            if balance < 0:
                return False
        return True
        