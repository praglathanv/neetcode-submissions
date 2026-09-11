class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        l = 0
        win = 0
        max_w = 0
        satisfied = 0

        for r in range(len(customers)):
            if grumpy[r] == 0:
                satisfied += customers[r]
            else:
                win += customers[r]
            
            if r - l + 1 > minutes:
                if grumpy[l] == 1:
                    win -= customers[l]
                l += 1
            
            max_w = max(win, max_w)
            
        return satisfied + max_w

        