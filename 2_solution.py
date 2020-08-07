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
    # making solution able to be called directly on class instead of on instance of class
    @staticmethod
    def solution(n, b):
        k = len(n)
        minion_list = []

        while n not in minion_list:
            x = ''.join(sorted(n, reverse=True))
            y = ''.join(sorted(n))
            x_int = int(x, b)
            y_int = int(y, b)
            z = str(x_int - y_int).zfill(k)
            minion_list.append(z)
            n = z
            return (n)
        else:
            return len(minion_list)




        print(n, b, k, x, y, z, minion_list)

print(solution.solution('243', 5))