class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        """
        First, we need to parse our numbers, just find symbol + inside. For this we can use python functionality with function .index: we can be sure that this index exists. Then we create real and imaginary parts for both of numbers, using found indexes.
        Finally we use definition of complex numbers multiplication and return answer.

        Complexity
        Time and space complexity is O(1), because numbers are restricted to be in range [-100, 100].
        """
        ind1 = num1.index("+")
        ind2 = num2.index("+")
        x1, y1 = int(num1[:ind1]), int(num1[ind1+1:-1])
        x2, y2 = int(num2[:ind2]), int(num2[ind2+1:-1])
        return str(x1*x2-y1*y2) + "+" + str(x1*y2+x2*y1)+"i"