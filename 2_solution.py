"""
1. start with a random minion ID 'n'
    - non-negative integer (1st arg)
    - length of 'n' is 'k' (len(n))
    - in base 'b' (2nd arg)
2. Define 'x' and 'y' as integers with length of 'k'
    - 'x' is 'n' sorted in descending order
    - 'y' is 'n' sorted in ascending order
3. Define 'z' = 'x' - 'y'
    - add leading zeros to 'z' to maintain length of 'k' if needed
4. Assize 'z' as next minion ID 'n'

**Repeat 2 - 4 until cycle (such as constant ID) occurs

<!-- return the number of times code runs before cycle occurs -->
"""

class solution:
    @staticmethod
    def solution(n, b):
        k = len(n)
        x = sorted(n, reverse=True)
        y = sorted(n)
        return n, b, k

print(solution.solution('243', 5))