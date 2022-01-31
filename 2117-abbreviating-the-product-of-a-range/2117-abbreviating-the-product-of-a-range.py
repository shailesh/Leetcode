class Solution:
    def abbreviateProduct(self, left: int, right: int) -> str:
        C, maxpre, mod, maxval = 0, 10**25, 10**10, 10**12
        val, pre, suf = 1,1,1
        for i in range(left, right+1):
            pre *= i
            suf *= i
            last = 0
            while pre > maxpre:
                last = pre % 10
                pre = pre // 10
            if last >= 5:       # rounding
                pre += 1
            while suf % 10 == 0:
                suf //= 10
                C += 1
            # suf %= mod
            if val <= maxval:
                val *= i
                while val % 10 == 0:
                    val //= 10
        # val records the numeric length of non-zero items
        if len(str(val)) <= 10:
            return str(val) + 'e' + str(C)
        else:
            p, s = str(pre), str(suf)
            return p[:5] + '...' +  s[-5:] + 'e' + str(C)

        if len(str(val)) <= 10:
            return str(val) + 'e' + str(C)
        else:
            p, s = str(pre), str(suf)
            while len(p) > 5:
                p = p[:-1]
            while len(s) > 5:
                s = s[1:]
            while len(s) < 5:
                s = '0' + s
            return p + '...' + s + 'e' + str(C)