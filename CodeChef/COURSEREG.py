t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    print('Yes' if n<=m-k else 'No')

"""
Course Registration
Problem Code: COURSEREG
Contest Code: START32
Difficulty Rating: 470

Problem: There is a group of N friends who wish to enroll in a course together. The course has a maximum capacity of M students that can register for it. If there are K other students who have already enrolled in the course, determine if it will still be possible for all the N friends to do so or not.

Input Format:
The first line contains a single integer T - the number of test cases. Then the test cases follow.
Each test case consists of a single line containing three integers N, M and K - the size of the friend group, the capacity of the course and the number of students already registered for the course.

Output Format:
For each test case, output Yes if it will be possible for all the N friends to register for the course. Otherwise output No.

Constraints
1 ≤ T ≤ 1000
1 ≤ N ≤ M ≤ 100
0 ≤ K ≤ M

Sample 1:
Input:
3
2 50 27
5 40 38
100 100 0

Output
Yes
No
Yes

Explanation:
Test Case 1: The 2 friends can enroll in the course as it has enough seats to accommodate them and the 27 other students at the same time.
Test Case 2: The course does not have enough seats to accommodate the 5 friends and the 38 other students at the same time.

Time limit: 0.5 secs
Source Limit: 50000 Bytes
"""
