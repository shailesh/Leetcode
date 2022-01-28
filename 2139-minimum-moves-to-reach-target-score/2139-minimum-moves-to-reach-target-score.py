class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        moves, current = 0, target
        while maxDoubles:
            if current == 1:
                return moves
            if current % 2 == 0:
                current = current//2
                maxDoubles -= 1
            else:
                current -= 1
            moves += 1
        return moves + (current - 1)
        