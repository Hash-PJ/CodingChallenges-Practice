#User function Template for python3
from math import sqrt
class Solution:
    def perfectSquares(self, N):
        n = int(sqrt(N))
        return n*n==N

    def hasThreePrimeFac(self, N):
        if self.perfectSquares(N):
            factors = [1, N]
            for i in range(2, int(sqrt(N)+1)):
                if N%i==0 and i not in factors:
                    factors.extend([i, N//i])
            #print(factors)
            return 1 if len(set(factors))==3 else 0
        else:
            return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    N=int(input("Enter number: "))
    ob = Solution()
    print(ob.hasThreePrimeFac(N))
# } Driver Code Ends
