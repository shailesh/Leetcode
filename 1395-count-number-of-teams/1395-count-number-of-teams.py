class Solution:
    def numTeams(self, rating: List[int]) -> int:
        """
        We are going to have a main for loop and we are going to pick one element from the ratings list at a time. Then we are going to have two other loops. One is going to scan all elements before and the other one is going to scan all elements after. Those two loops will count number of elements less and greater than the one we picked. So let's say we have 2 elements less than the selected one to the left and 3 elements greater to the right. That means the number of ascending sequences we can build is 2 * 3 = 6 . Now we just need to extend the same logic to all descending sequences and return the total.
        """
        asc = dsc = 0
        for i,v in enumerate(rating):
            llc = rgc = lgc = rlc =0
            for l in rating[:i]:
                if l < v:
                    llc += 1
                if l > v:
                    lgc += 1
            for r in rating[i+1:]:
                if r > v:
                    rgc += 1
                if r < v:
                    rlc += 1
            asc += llc * rgc
            dsc += lgc * rlc            
        return asc + dsc
        