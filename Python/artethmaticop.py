# The first line contains the first integer, . The second line contains the second integer, .

# Constraints



# Output Format

# Print the three lines as explained above.

# Sample Input 0

# 3
# 2
# Sample Output 0

# 5
# 1
# 6



if __name__ == '__main__':
    a = int(input())
    b = int(input())

print('{0} \n{1} \n{2}'.format((a + b), (a - b), (a * b)))