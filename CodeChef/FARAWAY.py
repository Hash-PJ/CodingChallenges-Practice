def approach1(n:int, A:tuple, m:int)->int:
    b= [0]*n
    for i in range(n):
        b[i] = abs(m-A[i]) if abs(m-A[i])>=abs(A[i]-1) else abs(A[i]-1)
    return sum(b)


t = int(input())
for _ in range(t):
    n, m = map(int,input().split())
    a = tuple(map(int, input().split()))
    print(approach1(n, a, m))

'''
Far Away

Problem Code:FARAWAY
Contest Code:START56
Difficulty Rating:1090

Problem: Chef has an array A of size N and an integer M, such that 1 ≤ Ai ≤ M for every 1 ≤ i ≤ N.
The distance of an array B from array A is defined as:
                                  d(A, B) = \sum_{i=1}^N |Ai - Bi|d(A,B)=i=1∑N ∣Ai−Bi∣
Chef wants an array B of size N, such that 1 ≤ Bi ≤ M and the value d(A,B) is as large as possible, i.e, the distance of B from A is maximum. Find the maximum distance for any valid array BB.

Note: |X| denotes the absolute value of an integer XX. For example, |-4| = 4 and |7| = 7.

Input Format:
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of two lines of input.The first line of each test case contains two space-separated integers N and M — the length of array A and the limit on the elements of A and B.
The second line contains N space-separated integers A1, A2,…,AN.
Output FormatFor each test case, output on a new line the maximum distance of an array from A.

Constraints:
1 ≤ T ≤ 10^5
1 ≤ N ≤ 2⋅10^5
1 ≤ M ≤ 10^9
1 ≤ Ai ≤M
The sum of NN over all test cases won't exceed 3\cdot 10^53⋅105.

Sample 1: Input
4
2 6
3 5
4 1
1 1 1 1
5 7
2 3 4 5 6
7 24
23 7 6 16 12 4 24

Output
7
0
21
127


Explanation:
Test case 1: The array having maximum distance from A is B = [6,1]. Thus the distance is |3-6| + |5-1| = 3 + 4 = 7.
Test case 2: The only array possible is B = [1,1,1,1]. The distance of this array from A is 0.
Test case 3: One of the possible arrays having maximum distance from A is B = [7,7,1,1,1]. Thus the distance is |2-7| + |3-7| + |4-1| + |5-1| + |6-1| = 5 + 4 + 3 + 4 + 5 = 21.

Time limit: 1 secs
Source Limit: 50000 Bytes
'''
