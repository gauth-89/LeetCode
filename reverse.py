class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        elif x < 10 and x > 0:
            return x
        elif x < 0:
            num = x * -1
            reverse = 0
            while(num != 0):
                reverse = reverse * 10
                reverse = reverse + num % 10
                num = num / 10
                
            return (reverse * -1)
        else:
            reverse = 0
            while(x != 0):
                reverse = reverse * 10
                reverse = reverse + x % 10
                x = x / 10
            return reverse
