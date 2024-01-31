Given a number N reverse the number and print it.
Example 1: Input: N = 123 Output: 321 Explanation: The reverse of 123 is 321
Example 2: Input: N = 234 Output: 432 Explanation: The reverse of 234 is 432
Input Format
123
Constraints
N <= 1000
Output Format
321
Sample Input 0
123
Sample Output 0
321 

# Enter your code here. Read input from STDIN. Print output to STDOUT
LOGIC 1

n=int(input())
print(str(n)[::-1])

LOGIC 2

n=int(input())
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n//=10
    
print(rev)
