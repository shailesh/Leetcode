from collections import Counter
class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        """
        First, create a counter for the digits and get the sum.

Then check if we need to remove any digits to get the sum of all of them to be divisible by 3. If we do, we have two cases. If sum(digits) % 3 == 2, we only need to remove a 2,5, or 8 to get the sum to be divisible by 3. If sum(digits) % 3 == 1, we can remove a 1,4, or 7. In either case, we want to remove the smallest digit possible. There is the case where we may not have any of the desired numbers to remove in the digit list, in which case we have to remove a number from the other group in order to make progress toward a sum divisible by 3. This is why the todel list is just these two groups of numbers concatenated together in alternate order. Each time we remove one, we check to see if the sum is divisible by 3 by going back to the top of the while loop.

Once we have removed digits from the counter, we build up the answer by converting the counter back to a list of digits (actually a string) in descending order to ensure the maximum size number. We account for the edge case of all 0s here as well.
        """
        sumd = sum(digits)
        ctr = Counter(digits)
        while sumd % 3 != 0:
            todel = [2,5,8,1,4,7] if sumd % 3 == 2 else [1,4,7,2,5,8]
            for x in todel:
                if ctr[x]>0:
                    ctr[x]-=1
                    sumd -= x
                    break
        ans = ""
        for d in [9,8,7,6,5,4,3,2,1,0]:
            if d == 0 and ans == "" and ctr[d]:
                return "0"
            ans += str(d)*ctr[d]
        return ans
        