class Solution:
    def numberOfWays(self, corridor: str) -> int:
        """
        We know that we need to have exaclty 2 seats in each room. First of all it means that if number of seats is odd or less than 2, we return 0. Also, imagine the case ???SPPPPS????, where we need to put wall somewhere between two S. How many ways we have? Exactly 5, which is distance between these two seats. So, if we have say seats on places 1, 3, 7, 12, 20, 30, then we have 7 - 3 options to put one wall and 20 - 12 for another wall.

Complexity
It is O(n) for time and space.
        """
        places = [i for i, x in enumerate(corridor) if corridor[i] == "S"]
        m = len(places)
        if m % 2 == 1 or m < 2: return 0
        
        ans = 1
        for i in range(m//2 - 1):
            ans = (ans * (places[2*i+2] - places[2*i+1])) % (10**9 + 7)
        return ans
        