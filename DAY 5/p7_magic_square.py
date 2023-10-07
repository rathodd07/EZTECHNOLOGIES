'''import numpy as np

R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))

print("Enter the entries in a single line (separated by space): ")

# User input of entries in a
# single line separated by space
entries = list(map(int, input().split()))

# For printing the matrix
matrix = np.array(entries).reshape(R, C)
print(matrix)
print(type(matrix))
import numpy as np
x =  np.arange(1, 10).reshape(3,3)
print(x)'''


''' How Magic Square works
Magic squares are n*n matrices consisting of n^2 positive integers.
The number of rows or columns of a square matrix is called the order of the matrix.
Typically, magic squares puzzles have odd orders and bear the integers from 1 to n^2. 
The sum of each diagonal, row, and column is the same. 
This number is called magic sum or magic constant. Generally, 
this magic sum depends on the order of the matrix.
The magic squares formula for the magic sum of order n is- n(n**2+1)/2

Magic Square works:
The algorithm you've described is used to generate odd-order magic squares.
A magic square is a square grid of numbers in which the sums of the numbers in each row, column, and diagonal are the same. 
Here's an explanation of each step of the algorithm:

1. **Initialization**: The algorithm starts by placing the number 1 in the middle column of the top row. 
In the notation used, (x, y) represents the row and column positions, respectively. 
So, in this case, (x, y) is initially set to (n/2, n-1), 
where 'n' is the order of the magic square (an odd number).
2. **Filling the Square**: The algorithm proceeds to fill the rest of the magic square by following these rules:
    a. The next number is placed at the position (x-1, y+1). 
    This means moving one row up and one column to the right from the current position.
    b. If the calculated position (x-1, y+1) is not within the bounds of the square:
    - If the row position becomes -1 (above the top row), it is wrapped around to the bottom row (n-1).
    - If the column position becomes 'n' (beyond the rightmost column), 
    it is wrapped around to the leftmost column (0).
    c. If the calculated position (x-1, y+1) already contains a number (i.e., it's already filled), 
    then we need to adjust the position as follows:
    - Increment the row position 'x' by 1 (move one row down).
    - Decrement the column position 'y' by 2 (move two columns to the left).
    d. If the adjusted position (after taking care of wrapping and adjustments) is (-1, n), it is set to (0, n-2).
3. **Repetition**: Steps 2a through 2d are repeated for each number from 2 to n^2, filling in the entire magic square.
The result is a magic square where the numbers from 1 to n^2 are placed in such a way that the sum of each row, column, 
and diagonal is the same.It's important to note that this algorithm is specifically designed for odd-order magic squares 
and might not work correctly for even-order magic squares. Additionally, there can be multiple valid magic squares for the same order 'n' since 
the starting position (1) is arbitrary, and the algorithm will generate different valid solutions 
by varying this starting position.'''

#2 method or approch magic square
def Its_magic_square(n):
    if n%2==0:
        return print("enter only odd values")
    #creating the array with 0 values
    magic_square = [[0] * n for _ in range(n)]
    # Initializing the number 1 and placing at (1,2)
    x= n//2
    y = n-1  
    for num in range(1, n*n+1):
        magic_square[x][y] = num
        x = x-1
        y = y+1
        if x==-1 and y==n:#when row is -1 and col=3  row=n-1 and col=n-2
            x=0
            y=n-2
        else:
            if x==-1:  #when row is -1 follow the row=n-1
                x=n-1
            if y==n:   #when col is 3 follow the col=n-2 or 0
                y=0
            if magic_square[x][y]!= 0: # checking for already filled index position
                x=x+1 #if not equal the row++ and col--
                y=y-2

    return magic_square

def print_magic_square(magic_square):
    for row in magic_square:
        print(" ".join(map(str, row)))

if __name__=="__main__":

    order = int(input("enter the order of matrix:"))
    magic_square = Its_magic_square(order)
    print("Magic Square of Order is:")
    print_magic_square(magic_square)

