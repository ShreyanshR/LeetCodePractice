from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        window_sum = 0
        L , count = 0 , 0

        for R in range(len(arr)):
            #print(L,R)
            if R - L + 1 > k:
                window_sum -= arr[L]
                L += 1

            window_sum += arr[R]

            if R - L + 1 == k:
                avg = window_sum/k
                #print(avg)
                if avg >= threshold:
                    print("greater than thres")
                    count += 1

        #print(count)

        return count

    def secondWay(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        curSum = sum(arr[:k-1])

        for L in range(len(arr) - k + 1):
            #okay we are direcly starting the sum at the kth value, so we don't have to iterate thourgh the whole array
            R = L + k - 1
            #print(L,R)
            curSum += arr[R]

            if curSum/k >= threshold:
                res += 1
            
            curSum -= arr[L]
        
        return res


if __name__ == "__main__":
    S = Solution()
    arr = [2,2,2,2,5,5,5,8]
    k = 3
    threshold = 4
    S.numOfSubarrays(arr, k, threshold)