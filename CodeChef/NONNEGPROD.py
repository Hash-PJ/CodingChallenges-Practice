def appr1(A:tuple)->int:
    '''Approach1: Checking the count of negative numbers present'''
    if len([1 for i in A if i<0])%2==0:
        return 0
     else:
         return 1


def appr2(A:tuple)->int:
    '''Approach2: Multiplying the numbers'''
    n=1
    for a in A:
        n *= a
    return int(n<0)


t = int(input())
for _ in range(t):
    n = int(input())
    a = tuple(map(int, input().split()))
    if 0 in a:
        print('0 in list, so 0')
    else:
        print("Approach1: Checking the count of negative numbers present, It gives:",appr1(a))
        print("Approach2: Multiplying the numbers, It gives:",appr2(a))

'''
Non-Negative Product

Problem Code:NONNEGPROD
Contest Code:START57
Difficulty Rating:948

Problem: Alice has an array of N integers — A1, A2, ..., AN. She wants the product of all the elements of the array to be a non-negative integer. That is, it can be either 00 or positive. But she doesn't want it to be negative.
To do this, she is willing to remove some elements of the array. Determine the minimum number of elements that she will have to remove to make the product of the array's elements non-negative.

Input Format: 
The first line of input will contain a single integer T, denoting the number of test cases.
The first line of each test case contains a single integer N — the number of elements in the array originally.
The next line contains NN space-separated integers — A1, A2, ..., AN, which are the original array elements.
Output Format:
For each test case, output on a new line the minimum number of elements that she has to remove from the array.

Constraints: 
1 <= T <= 1001≤T≤100
2 <= N <= 100002≤N≤10000
-1000 <= Ai <= 1000

Sample 1: Input:
4
3
1 9 8
4
2 -1 9 100
4
2 -1 0 100
4
2 -1 -1 100

Output
0
1
0
0


Explanation:
Test case 1: The product of the elements of the array is 1×9×8=72, which is already non-negative. Hence no element needs to be removed, and so the answer is 0.

Test case 2: The product of the elements of the array is 2×−1×9×100=−1800, which is negative. Alice can remove the element -1−1, and the product then becomes non-negative. Hence the answer is 1.

Test case 3: The product of the elements of the array is 2×−1×0×100=0, which is already non-negative. Hence no element needs to be removed, and so the answer is 0.

Test case 4: The product of the elements of the array is 2×−1×−1×100=200, which is already non-negative. Hence no element needs to be removed, and so the answer is 0.

Time limit: 1 secs
Source Limit: 50000 Bytes

'''
