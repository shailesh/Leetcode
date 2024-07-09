class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def merge_halfs(first_half, second_half, operator):
            if operator == '+':
                return first_half + second_half
            elif operator == '-':
                return first_half - second_half
            elif operator == '*':
                return first_half * second_half

        def recursive_compute(expr):
            results = []

            if expr.isdigit():
                return [int(expr)]

            for i in range(len(expr)):
                if expr[i] in '+-*':
                    first_half_expr = expr[:i]
                    second_half_expr = expr[i+1:]

                    first_half_results = recursive_compute(first_half_expr)
                    second_half_results = recursive_compute(second_half_expr)

                    for fh in first_half_results:
                        for sh in second_half_results:
                            results.append(merge_halfs(fh, sh, expr[i]))
            return results
        
        return recursive_compute(expression)