class Solution:
    def findMin(self, n):

        coins = [10, 5, 2, 1]
        count = 0

        for coin in coins:
            while n >= coin:
                n -= coin
                count += 1

        return count