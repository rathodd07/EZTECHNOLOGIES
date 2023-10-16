'''length=int(input())
my_list = [None] * length
# Loop to insert elements into the list
for i in range(length):
    element = input(f"Enter element {i+1}: ")
    my_list[i] = element

# Display the final list
print("The list you entered is:", my_list)'''

''' it takes list as strings ['1', '2', '3', '4']
# Get the length of the list as an integer input from the user
length = int(input("Enter the length of the list: "))
# Get a single string containing elements separated by commas as input from the user
elements_input = input("elements separated by commas: ")
# Split the input string into a list using commas as the delimiter
elements_list = elements_input.split(',')
# Check if the number of elements entered matches the declared length
if len(elements_list) != length:
    print(f"Error: You must enter exactly {length} elements.")
else:
    # Display the final list
    print("The list you entered is:", elements_list)'''

'''# the list with the format of integers as [1,2,3,4,5]
# Get the length of the list as an integer input from the user
length = int(input("Enter the length of the list: "))
# Get a single string containing elements separated by commas as input from the user
elements = input("Enter elements separated by commas: ")
# Split the input string into a list using commas as the delimiter and convert to integers
elements_list = [int(i) for i in elements.split(',')]
# Check if the number of elements entered matches the declared length
if len(elements_list) != length:
    print(f"Error: You must enter exactly {length} elements.")
else:
    # Display the final list
    print("The list you entered is:", elements_list)'''



length = int(input("Enter the length of the list: "))
elements = input("Enter elements separated by commas: ")
arr = [int(i) for i in elements.split(',')]
#arr=list(map(int,input().split(',')))
if len(arr) != length:
    print("the list is full , to exted increase the size ")
else:
    print("The list is:", arr)

