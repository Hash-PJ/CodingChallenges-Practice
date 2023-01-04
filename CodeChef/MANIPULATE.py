t = int(input())
for _ in range(t):
    x,y = map(int, input().split())
    if x>=y:
        print("yes".upper())
    else:
        print('no'.upper())
'''
Ezio and Guards

Problem Code:MANIPULATE
Contest Code:APRIL221
Difficulty Rating:427

Problem: Ezio can manipulate at most X number of guards with the apple of eden.

Given that there are Y number of guards, predict if he can safely manipulate all of them.

Input Format:
First line will contain T, number of test cases. Then the test cases follow.
Each test case contains of a single line of input, two integers X and Y.

Output Format:
For each test case, print YES if it is possible for Ezio to manipulate all the guards. Otherwise, print NO.

1 ≤ X,Y ≤ 100
Sample 1:
Input
3
5 7
6 6
9 1

Output
NO
YES
YES

Explanation:Test Case 11: Ezio can manipulate at most 55 guards. Since there are 77 guards, he cannot manipulate all of them.

Test Case 22: Ezio can manipulate at most 66 guards. Since there are 66 guards, he can manipulate all of them.

Test Case 33: Ezio can manipulate at most 99 guards. Since there is only 11 guard, he can manipulate the guard.
'''
