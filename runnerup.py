#Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

#Input Format

#The first line contains . The second line contains an array   of  integers each separated by a space.

#Constraints
#2<=n<=10
#-100<=A[i]<=100

#Output Format

#Print the runner-up score.

#Sample Input 0

#5
#2 3 6 6 5
#Sample Output 0
#5
#------------SOLUTION---------------
if __name__=="__main__":
    n = int(input())    #taking input
    
    arr = map(int, input().split()) #mapping input i.e. text to int
    
    arr = list(set(list(arr)))  #converting array to list, getting its set, then converting it to list      
    
    ar = len(arr)   #assigning length of array to ar variable
    
    arr = sorted(arr)   #sorting the array
    
    print(arr[ar-2])    #printing the 2nd largest array
    
    
    
    
    
