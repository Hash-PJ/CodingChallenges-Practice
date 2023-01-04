'''
Tidy Number
Given a number N.Check if it is tidy or not.
A tidy number is a number whose digits are in non-decreasing order.

Example 1:

Input: 
1234
Output:
1
Explanation:
Since 1<2<3<4,therefore the number is tidy.
Example 2:

Input: 
1243
Output:
0
Explanation:
4>3, so the number is not tidy.

Your Task:
You don't need to read input or print anything.Your task is to complete the function isTidy() which takes an Integer N as input parameter and returns 1 if it is tidy.Otherwise, it returns 0.

Expected Time Complexity: O(LogN)
Expected Auxillary Space: O(1)

Constraints:
1<=N<=109
'''
class Solution:
    def isTidy(self,N):
        prev=10
        while(N):
            rem = N % 10
            N //= 10
            if (rem > prev):
                return 0
            prev = rem
        return 1
        
class Solution:
    def isTidy(self,N):
        N = list(map(int, list(str(N))))
        for i in range(1,len(N)):
            if N[i-1]>N[i]:
                return 0
        return 1
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        ob=Solution()
        print(ob.isTidy(N))   
        
# } Driver Code Ends
