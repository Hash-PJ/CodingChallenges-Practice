print('Yes' if int(input()) + 7 > 170 else 'No')

"""
Increase IQ
Problem Code: INCRIQ
Contest Code: MARCH222
Difficulty Rating:478

Problem: A study has shown that playing a musical instrument helps in increasing one's IQ by 7 points. Chef knows he can't beat Einstein in physics, but he wants to try to beat him in an IQ competition.
You know that Einstein had an IQ of 170, and Chef currently has an IQ of X. Determine if, after learning to play a musical instrument, Chef's IQ will become strictly greater than Einstein's.

Print "Yes" if it is possible for Chef to beat Einstein, else print "No" (without quotes).

Input Format: The first and only line of input will contain a single integer X, the current IQ of Chef.

Output Format:
For each testcase, output in a single line "Yes" or "No".

Constraints:
100 ≤ X ≤ 169

Sample 1:
Input
165

Output
Yes

Explanation:
After learning a musical instrument, Chef's final IQ will be 165+7=172. Since 172>170, Chef can beat Einstein.

Sample 2:
Input
120

Output
No

Explanation:
After learning a musical instrument, Chef's final IQ will be 120+7=127. Since 127<170, Chef cannot beat Einstein.

Time limit: 1 secs
Source Limit: 50000 Bytes

"""