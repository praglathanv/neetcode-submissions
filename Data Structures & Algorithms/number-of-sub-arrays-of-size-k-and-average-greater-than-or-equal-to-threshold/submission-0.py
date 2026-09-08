class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        c = 0
        sum = 0

        for r in range(len(arr)):
            sum += arr[r]

            if r - l + 1 == k:
                val = sum / k

                if val >= threshold:
                    c += 1

                sum -= arr[l]
                l += 1

        return c
        