# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird


# orignal way of doing it
def wierd(n):
    if(n % 2 == 1 or n >= 6 and n <= 20):
        print("Wierd")
    else:
        print("Not wierd")
# Uses the built in range function and tenerary oper for python for a single line 
def wierdBetter(n):
    n in range (6, 21) or n % 2 != 0 if print("Wierd") else print("Not Weird")


if __name__ == '__main__':    
    wierdBetter(24)