class Node:
    # def __new__(self,data):
    #     print("inside new")
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.start = None
    def append_node(self,data):
        new_node = Node(data)
        current = self.start
        if self.start is None:
            self.start = new_node
        else:
            temp = current
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
        
    def print_list(self):
        current = self.start
        temp = current
        while temp is not None:
            print(temp.data,end=" ")
            temp = temp.next
        print()
    def reverse_list(self):
        current = self.start
        initial = self.start
        arr = []
        while current is not None:
            arr.append(current.data)
            current = current.next
        arr = arr[::-1]
        i=0
        while initial is not None:
            initial.data = arr[i]
            initial = initial.next
            i+=1
    def get_length(self):
        temp = self.start
        count = 0
        while temp is not None:
            count+=1
            temp = temp.next
        return count
    def delete_middle(self):
        length = self.get_length()
        current = self.start
        counter = (length//2 - 1)
        while counter !=0:
            current = current.next
            counter-=1
        if length%2 == 0:
            current.next = current.next.next.next
        else:
            current.next = current.next.next
    def find_median(self):
        length = self.get_length()
        current = self.start
        counter = (length//2 - 1)
        while counter !=0:
            current = current.next
            counter-=1
        if length%2 == 0:
            return (current.data+current.next.data)/2
        else:
            return current.next.data
    
    def delete_after_and_before(self,n):
        current = self.start
        if current.data == n:
            print("before does not exist")
            current.next = current.next.next
        else:
            while current.next.next.data != n:
                current = current.next
            current.next = current.next.next
            current = current.next
            current.next = current.next.next
            
    def insert_after(self,after_value,value_to_be_inserted):
        current = self.start
        while current.data != after_value:
            current = current.next
        if current is None:
            print("after value does not exists")
        else:
            new_node = Node(value_to_be_inserted)
            new_node.next = current.next
            current.next = new_node


my_list = LinkedList()
for i in range(12):
    my_list.append_node(i)
#my_list.print_list()
#my_list.reverse_list()
#my_list.print_list()
#print(my_list.get_length())
#my_list.delete_middle()
my_list.print_list()
#print(my_list.find_median())
my_list.delete_after_and_before(0)
my_list.print_list()
my_list.insert_after(6,100)
my_list.print_list()