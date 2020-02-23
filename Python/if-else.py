

def wierd(n):
    if(n % 2 == 1 or n >= 6 and n <= 20 ):
        print("Wierd")
    else:
        print("Not wierd")

if __name__ == '__main__':    
    wierd(24)