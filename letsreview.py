'''Objective
Today we’re expanding our knowledge of Strings and combining it with what we’ve already learned about loops. Check out the Tutorial tab for learning materials and an instructional video!
Task
Given a string, S, of length N that is indexed from 0 to N-1, print its even-indexed and odd-indexed characters as 2 space-separated strings on a single line (see the Sample below for more detail).
Note: 0 is considered to be an even index.'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())

for i in range(0,T):    
    S = input()
    print(S[0::2] + "" ,S[1::2])
    #[::2]-> to extract the elements having even indexes
