class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        """
        Rather than using a stack, which complicates things, we will just rely on depth.
        Time: O(n)
        Space: O(1)
        """
        depth = -1
        total = 0
        for index, element in enumerate(s):
            if element == '(':
                depth += 1
            elif element == ')' and s[index - 1] == '(':
                total += 2 ** depth
                depth -= 1
            else:
                depth -= 1
        return total
        