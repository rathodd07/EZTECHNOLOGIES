# Recursive Python function to solve tower of hanoi
'''def TowerOfHanoi(n, source, dest, aux):
	if n == 0:
		return
	TowerOfHanoi(n-1, source, aux, dest)
	print("Move disk from", n, "source to", source, "dest", dest)
	TowerOfHanoi(n-1, aux, dest, source)


# Driver code
N = int(input("enter the number of disk:"))
# A, C, B are the name of rods
TowerOfHanoi(N, 'A', 'C', 'B')'''
# tower of hanoi for counting no of moves
def TowerOfHanoi(n):
    count=(2**n)-1
    return count
n=int(input("enter the number of disks:"))
print("the no of moves are:",TowerOfHanoi(n))

