class Solution:
    def reverse(self, x):
        temp = x
        rev = 0
        if x < 0:
            x = -x
        while(x):
            rem = x % 10
            rev = (rev * 10) + rem
            x = x // 10
        if temp < 0:
            rev = -1 * rev
        if rev > pow(2, 31) or rev < pow(-2,31):
             return 0
        else:
             return rev
             