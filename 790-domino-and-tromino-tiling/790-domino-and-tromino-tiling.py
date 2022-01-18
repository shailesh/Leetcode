class Solution:
    def numTilings(self, n: int) -> int:
        """
        :type N: int
        :rtype: int
        """
        if n <= 2:
            return n
        
        cache_d = [0 for i in range(n+1)]
        cache_t = [0 for i in range(n+1)]
        
        cache_d[1] = 1
        cache_d[2] = 2
        
        cache_t[2] = 1
        
        for i in range(3, n+1):
            cache_d[i] = (cache_d[i-1] + cache_d[i-2] + 2 * cache_t[i-1]) % ((10**9) + 7)
            cache_t[i] = (cache_t[i-1] + cache_d[i-2]) % ((10**9) + 7)
        
        return cache_d[n]

        