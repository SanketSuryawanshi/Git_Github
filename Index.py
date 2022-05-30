# [$] Find maximum equal sum of every three stacks >>>


'''

Input : 

  stack1[] = { 3, 10}
  stack2[] = { 4, 5 }
  stack3[] = { 2, 1 }

Output : 0

Sum can only be equal after removing all elements 
from all stacks.


'''
stack1 = [ 3, 2, 1, 1, 1 ]
stack2 = []
stack3 = [ 1, 1, 4, 1 ]

def GetSum(stack):
    return sum(stack)

def GetMaxSum(stack1,stack2,stack3):

    while(1):
        
        if(GetSum(stack1)> GetSum(stack2) and GetSum(stack1)> GetSum(stack3) ):
            stack1.pop(0)
        
        if(GetSum(stack2)> GetSum(stack1) and GetSum(stack2)> GetSum(stack3) ):
            stack2.pop(0)
        
        if(GetSum(stack3)> GetSum(stack2) and GetSum(stack3)> GetSum(stack1) ):
            stack3.pop(0)

        if(len(stack1)==0 or len(stack2)==0 or len(stack3)==0):
            return 0

        if(GetSum(stack1)==GetSum(stack2)==GetSum(stack3)):
            return GetSum(stack1)


print(GetMaxSum(stack1, stack2, stack3))