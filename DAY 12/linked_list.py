class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.start=None
        self.temp=None
    def create_list(self):
        for i in range(10):
            new_node =Node(i)
            if self.start is None:
                self.start=new_node
                self.temp=self.start
            else:
                self.temp.next=new_node
                self.temp=self.temp.next
        return self.start
    def print_list(self):
        self.temp=start
        while self.temp:
            print(self.temp.data,end=" ")
            self.temp=self.temp.next
        print()
obj=LinkedList()
start=obj.create_list()
obj.print_list()
obj.print_list()