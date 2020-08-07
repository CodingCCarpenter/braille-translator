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
            # adding n to the minion list
            minion_list.append(n)
            x = ''.join(sorted(n, reverse=True))
            y = ''.join(sorted(n))
            pre_z = int(x, b)-int(y, b)
            str_z = str(pre_z)
            base_3_z = int(str_z, b)
            z = str(base_3_z).zfill(k)
            n = z
            # Below was taken out to implement scratchpad ideas
            """x = ''.join(sorted(int(n, b), reverse=True))
            y = ''.join(sorted(int(n, b)))
            # converting to base 10 to subtract
            x_int = int(x, 10)
            y_int = int(y, 10)
            z_str_base_10 = str(x_int - y_int)
            z_int_base_b = int(z_str_base_10, b)
            n = str(z_int_base_b)
            print(n) """
            print(n,x,y,pre_z, z)
            print(minion_list)
        else:
            return len(minion_list)

print(solution.solution('1211', 10))




      

print(solution.solution('210022', 3))